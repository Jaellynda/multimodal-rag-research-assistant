Multimodal Research Intelligence
A **Local AI Research Assistant** that performs high-fidelity document analysis and cross-paper synthesis using **Retrieval-Augmented Generation (RAG)** and **Llama 3**.

No API billing. 100% Private. Research-ready.

---

## Quick Demo
![Demo](demo.gif) 



Ask complex queries about research papers and receive grounded, deterministic explanations.

**Example Query:**
> "How does predictive forgetting optimize neural generalization according to the SURE framework?"

**Answer:**
> "Predictive forgetting allows the system to shed episodic noise while retaining the conceptual gist, preventing catastrophic interference during consolidation."

---

## Project Motivation
Large Language Models (LLMs) are fluent but prone to hallucination. **New Covenant** explores RAG as a solution to ground AI responses in verified academic data, providing a tool that mimics human cognitive consolidation.

---
## Technical Deep Dive: How the RAG Engine Works

This project implements a sophisticated **Retrieval-Augmented Generation (RAG)** pipeline designed to minimize LLM hallucinations by grounding responses in a local vector database.

### 1. Semantic Chunking & Embedding
Standard text splitting often breaks sentences in half, losing context. This system uses `RecursiveCharacterTextSplitter` to maintain semantic integrity. Each chunk is then transformed into a **384-dimensional vector** using neural embeddings.



### 2. Vector Storage & Retrieval
The high-dimensional vectors are stored in **ChromaDB**. When a query is made:
- The query itself is embedded into a vector.
- We perform a **Cosine Similarity Search** to find the "Nearest Neighbors" in the vector space.
- This allows the system to find relevant information even if the exact keywords don't match.

### 3. The LCEL Synthesis Chain
Using **LangChain Expression Language (LCEL)**, the system follows a strict execution logic:
`Context + Question -> Prompt Template -> Llama 3 -> Parsed Answer`

By enforcing this "Context-Only" rule in the system prompt, we ensure the AI acts as a reliable research assistant rather than a creative writer.

## System Architecture
The system utilizes a decoupled microservices architecture to ensure scalability and local performance.

1. **Ingestion:** Research PDFs are decomposed into semantic chunks.  
2. **Vectorization:** Text is converted to high-dimensional embeddings.  
3. **Retrieval:** Semantic search identifies relevant context via ChromaDB.  
4. **Synthesis:** Meta Llama 3 synthesizes a grounded response via LCEL.  

---

---
## Tech Stack

### Backend & Logic
- **Python / FastAPI:** High-performance asynchronous API layer.  
- **LangChain v1.0:** Advanced orchestration using LCEL (LangChain Expression Language).  
- **Ollama:** Local inference engine for Meta Llama 3.  

### Data & Search
- **ChromaDB:** Vector database for semantic indexing and persistence.  
- **PyPDF:** Robust document parsing and metadata extraction.  

### Frontend
- **Streamlit:** Minimalist, high-end research interface.  

---

<img width="3024" height="1624" alt="image" src="https://github.com/user-attachments/assets/c5e04145-5899-49b3-9d41-9269b7f30039" />


## How it Works: The RAG Pipeline

### 1. Document Processing
Research papers are processed using a `RecursiveCharacterTextSplitter`, ensuring that semantic context is preserved across chunk boundaries.

### 2. Neural Embedding
Each chunk is embedded into a vector space. Unlike keyword search, this allows the AI to understand concepts (e.g., "Memory Consolidation" matches with "Neural Stability").

### 3. LCEL Synthesis
Using the modern Pipe Operator (`|`), the system pipes the retrieved context directly into a constrained Llama 3 prompt, ensuring the model only speaks from the provided data.

---

## What I Learned
- Orchestrating LCEL: Moving beyond legacy chains to custom, pipe-based LLM logic.  
- Vector Database Management: Handling persistence and retrieval efficiency in ChromaDB.  
- Asynchronous API Design: Building non-blocking endpoints for AI inference.  
- Local Inference Optimization: Managing Llama 3 hardware requirements via Ollama.  

---

## Future Roadmap (V2)
- Multimodal Vision: Processing charts and graphs via Llava.  
- Multi-Paper Comparison: Side-by-side reasoning mode.  
- Citation Mapping: Highlighting exactly which page the AI is quoting.  

---
## Project Structure
--

│
├── app/
│   └── new_covenant.py          # Main Streamlit application (UI + RAG pipeline)
│
├── core/
│   ├── rag_pipeline.py          # RAG logic (retrieval + generation)
│   └── embeddings.py            # Embedding + vector store setup
│
├── data/
│   ├── temp/                    # Runtime PDF storage (auto-generated)
│   └── chroma_db/               # Persistent vector database
│
├── legacy/
│   ├── app.py                   # Original UI (deprecated)
│   ├── main.py                  # FastAPI backend (deprecated)
│   └── rag_logic.py             # Initial modular logic
│
├── requirements.txt             # Dependencies (Streamlit Cloud ready)
├── README.md                    # Documentation & portfolio overview
├── Dockerfile                   # Container config (legacy / optional)
└── .gitattributes               # Repository config
--

## License
MIT License  

Copyright (c) 2026 Jaellynda  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
---


