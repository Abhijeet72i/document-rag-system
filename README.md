git clone https://github.com/yourusername/document-rag-system.git

cd document-rag-system


Create virtual environment:


python -m venv venv


Activate environment:

Windows:

venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt


---

## 🔑 Configure API Key

Create a Gemini API key from:

https://aistudio.google.com/app/apikey

Then set it as an environment variable:

Windows PowerShell:


$env:GOOGLE_API_KEY="YOUR_API_KEY"


---

## ▶️ Run Backend


cd backend
python -m uvicorn main:app --reload


Backend runs at:


http://127.0.0.1:8000


---

## ▶️ Run Frontend

Open a new terminal:


cd frontend
streamlit run app.py


Open in browser:


http://localhost:8501


---

## 🧪 How to Use

1. Upload a PDF document
2. Click **Upload Document**
3. Enter a question related to the document
4. The system will retrieve relevant chunks and generate an answer

---

## 📌 Example Workflow

Upload PDF → Document Chunking → Embedding Generation → Vector Search → Context Retrieval → LLM Answer

---

## 🎯 Future Improvements

- Chat-style conversational interface
- Multi-document search
- Page number citations
- Hybrid search (BM25 + Vector)
- Deployment using Docker

---

## 👤 Author

**Abhijeet Pathak**

B.Tech Computer Science  
Interested in Data Analytics & AI Systems

---

## 📧 Contact

If you have questions about this project, feel free to reach out.
