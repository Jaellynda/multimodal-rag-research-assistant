import streamlit as st
import requests

st.set_page_config(page_title="New Covenant | Research Intelligence", layout="wide")

# Sidebar for Multi-Document Management
with st.sidebar:
    st.header("Research Workspace")
    st.info("Upload multiple papers to enable cross-referential analysis.")
    uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
    
    if st.button("Index Documents"):
        if uploaded_files:
            for file in uploaded_files:
                with st.spinner(f"Indexing {file.name}..."):
                    files = {"file": (file.name, file.getvalue())}
                    requests.post("http://127.0.0.1:8000/upload", files=files)
            st.success("All documents indexed.")
        else:
            st.warning("Please upload files first.")

# Main Interface
st.title("New Covenant Research Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask a cross-document research question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Synthesizing multi-document analysis..."):
            # The logic stays clean: the backend handles the retrieval from all indexed docs
            res = requests.get(f"http://127.0.0.1:8000/query?question={prompt}")
            answer = res.json()["answer"]
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
