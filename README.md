# Chat_with_Multiple_PDFs

Project Overview
The project involves creating a chat application that allows users to interact with multiple PDF documents using the Google Gemini Pro LLM model, LangChain, and Streamlit. The goal is to enable users to upload PDF files, ask questions related to the content of these PDFs, and receive answers based on the information extracted from the documents1.

Key Features
PDF Upload: Users can upload multiple PDF files containing the information they want to query.

Text Extraction: The application extracts text from the uploaded PDF files using PyPDF2.

Text Chunking: The extracted text is divided into smaller chunks to facilitate efficient processing.

Vector Embeddings: LangChain is used to create vector embeddings of the text chunks, enabling efficient similarity search.

Question Answering: Users can ask questions related to the content of the PDF files. The Gemini Pro model processes these questions and generates answers based on the relevant text chunks1.

Streamlit Interface: The application features a user-friendly web interface built with Streamlit, allowing users to interact with the chatbot seamlessly.

Technologies Used
Streamlit: Used for building the web application interface.

PyPDF2: Used for reading text from PDF files.

LangChain: A library for natural language processing tasks, including text splitting, vector embeddings, and question answering.

Google Gemini Pro: The generative AI model used for generating answers to user questions.

FAISS: A library for similarity search, used for creating a vector store of text chunks from the PDF files.

How It Works
Upload PDF Files: Users upload multiple PDF files containing the information they want to query.

Process PDF Files: The application extracts the text from the PDFs and splits it into chunks.

Create Vector Store: The text chunks are used to create a vector store, which is used for similarity search during question answering.

Ask Questions: Users can ask questions related to the content of the PDF files.

Generate Answers: The Gemini model finds the most relevant chunks from the PDFs and generates an answer based on the context provided in the question.

Demo
A demo of the application can be accessed through a Streamlit web interface, where users can upload PDF files, ask questions, and receive answers based on the content of the PDFs.

Getting Started
To use this tool, simply navigate to the Streamlit web interface, input your PDF topic, choose the style and word count, and click 'Generate'. The tool will take care of the rest, providing you with a customized blog post.

This project showcases the powerful combination of LangChain, Google Gemini Pro, and Streamlit to create an interactive and intelligent chat application for processing multiple PDF documents1.
