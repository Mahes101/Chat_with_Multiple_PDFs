import streamlit as st 
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    vectorstore.save_local("faiss_index_vectorstore")
    


def conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, If the answer
    is not in the provided context, Just say "The answer is not in the provided context", Dont provide the wrong answer\n\n
    Context: \n {context}\n\n
    Question: \n{question}\n\n
    
    Answer:
    """
    
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)
    
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain


def user_question(user_input):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index_vectorstore", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_input)    
    chain = conversational_chain()
    response = chain({"input_documents": docs, "question": user_input}, return_only_outputs=True)
    print(response)
    st.write("Replay: ",  response["output_text"])
    
def main():
    st.set_page_config(
        page_title="Chat with Multiple PDFs",
        page_icon=":books:"
    )    
    
    st.header("Chat with Multiple PDFs")
    user_input=st.text_input("Ask a question about your documents: ")
    
    if user_input:
        user_question(user_input)
    with st.sidebar:
        st.title("Menu")    
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Submit and Process"):   
            with st.spinner("Processing....."):
                raw_text = get_pdf_text(pdf_docs)    
                text_chunks = get_text_chunks(raw_text)
                get_vectorstore(text_chunks)
                st.success("Done processing")

if __name__ == '__main__':
    main()
    