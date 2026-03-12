from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

# Put your Gemini API key here
API_KEY = "AIzaSyD2zYE6a7DIOz0dXvr0qAaEGp9Z-cch5_I"


def ask_question(question):

    # Local embedding model (free)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load vector database
    vectordb = Chroma(
        persist_directory="../db",
        embedding_function=embeddings
    )

    # Create retriever
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    # Retrieve relevant chunks
    docs = retriever.invoke(question)

    # Combine retrieved chunks
    context = "\n\n".join([doc.page_content for doc in docs])

    # Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=API_KEY,
        temperature=0.2
    )

    prompt = f"""
You are a helpful assistant.

Answer the question using the context below.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    sources = [doc.page_content[:200] for doc in docs]

    return {
        "answer": response.content,
        "sources": sources
    }