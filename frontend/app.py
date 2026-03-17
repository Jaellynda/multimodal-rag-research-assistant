import streamlit as st
import requests

# FAANG Style: Clean, minimalist layout
st.set_page_config(
    page_title="New Covenant | Research Intelligence", 
    page_icon="🔬", 
    layout="wide"
)

# Professional Header
st.markdown("""
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #1E1E1E;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }
    </style>
    <div class="main-title">New Covenant Research Intelligence</div>
    <div class="sub-title">Multimodal Retrieval-Augmented Generation (RAG) System</div>
    """, unsafe_allow_html=True)

# Sidebar Design
with st.sidebar:
    st.header("Document Management")
    st.info("Upload technical PDFs for cross-referential analysis.")
    uploaded_file = st.file_uploader("Select PDF", type="pdf", help="Max size: 50MB")
    
    if uploaded_file:
        if st.button("Initialize Indexing"):
            with st.spinner("Analyzing document structure..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                try:
                    response = requests.post("http://127.0.0.1:8000/upload", files=files)
                    st.success("Document successfully vectorized.")
                except:
                    st.error("Connection to backend failed.")

# Chat System with Streaming-style Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Query Input
if prompt := st.chat_input("Enter research query..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Synthesizing answer..."):
            try:
                res = requests.get(f"http://127.0.0.1:8000/query?question={prompt}")
                answer = res.json()["answer"]
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error("Synthesis error. Ensure the backend is running.")

