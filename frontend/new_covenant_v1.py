__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="New Covenant | Research Intelligence", layout="wide")
st.title("New Covenant Research Intelligence")

# 1. Access the Secret Key from Hugging Face Settings
if "GROQ_API_KEY" in st.secrets:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
else:
    st.error("Please add GROQ_API_KEY to your Space Secrets!")
    st.stop()

# 2. Initialize Models
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
llm = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="llama-3.1-8b-instant")

# 3. Sidebar for Uploads
with st.sidebar:
    st.header("Document Center")
    uploaded_files = st.file_uploader("Upload Research PDFs", type="pdf", accept_multiple_files=True)
    if st.button("Index Documents"):
        if uploaded_files:
            if not os.path.exists("temp"): os.makedirs("temp")
            all_docs = []
            for f in uploaded_files:
                path = f"temp/{f.name}"
                with open(path, "wb") as file:
                    file.write(f.getvalue())
                loader = PyPDFLoader(path)
                all_docs.extend(loader.load())
            
            splits = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_documents(all_docs)
            Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory="./chroma_db")
            st.success("Indexing Complete!")

# 4. Chat Interface
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("Ask a cross-document query..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
        retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
        
        template = "Answer based ONLY on context:\n{context}\n\nQuestion: {question}"
        prompt_tmpl = ChatPromptTemplate.from_template(template)
        
        chain = ({"context": retriever, "question": RunnablePassthrough()} 
                 | prompt_tmpl | llm | StrOutputParser())
        
        response = chain.invoke(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
