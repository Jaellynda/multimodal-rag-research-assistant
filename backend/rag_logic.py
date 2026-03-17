from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class RAGAssistant:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model="llama3")
        self.llm = OllamaLLM(model="llama3")
        self.db_path = "./chroma_db"

    def ingest_pdf(self, file_path):
        loader = PyPDFLoader(file_path)
        splits = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=100
        ).split_documents(loader.load())

        Chroma.from_documents(
            documents=splits, 
            embedding=self.embeddings, 
            persist_directory=self.db_path
        )

    def ask(self, question):
        vectorstore = Chroma(
            persist_directory=self.db_path, 
            embedding_function=self.embeddings
        )
        retriever = vectorstore.as_retriever()

        template = "Answer the question based only on the context:\n{context}\n\nQuestion: {question}"
        prompt = ChatPromptTemplate.from_template(template)

        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        return chain.invoke(question)

    def compare(self, question):
        vectorstore = Chroma(
            persist_directory=self.db_path, 
            embedding_function=self.embeddings
        )
        retriever = vectorstore.as_retriever()
        
        # Specialized Comparison Prompt
        comparison_template = """
        You are a research analyst. Compare and contrast the information found in the retrieved documents 
        to answer the user's research query. Highlight conflicting data points or unique perspectives 
        from different sources.

        Context:
        {context}

        Research Query: {question}
        """
        prompt = ChatPromptTemplate.from_template(comparison_template)
        
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        return chain.invoke(question)
