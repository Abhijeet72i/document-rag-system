nfvjknfjkeimport streamlit as st
import requests

st.title("📄 Document QA System")

backend = "http://127.0.0.1:8000"

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:

    files = {"file": uploaded_file}

    if st.button("Upload Document"):

        r = requests.post(f"{backend}/upload", files=files)

        if r.status_code == 200:
            st.success("Document indexed successfully!")
        else:
            st.error(r.text)


st.subheader("Ask a question")

question = st.text_input("Enter question")

if st.button("Ask"):

    r = requests.get(
        f"{backend}/ask",
        params={"q": question}
    )

    if r.status_code == 200:

        data = r.json()

        st.subheader("Answer")
        st.write(data["answer"])

        st.subheader("Sources")

        for s in data["sources"]:
            st.info(s)

    else:
        st.error(r.text)
