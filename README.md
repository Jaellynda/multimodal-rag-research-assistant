<img width="3024" height="1626" alt="image" src="https://github.com/user-attachments/assets/4729cdec-27f2-4e08-80ef-a491487a6480" /># New Covenant: Multimodal Research Intelligence
A **Local AI Research Assistant** that performs high-fidelity document analysis and cross-paper synthesis using **Retrieval-Augmented Generation (RAG)** and **Llama 3**.

No API billing. 100% Private. Research-ready.

---

## Quick Demo
![Demo](demo.gif) 
<img width="3024" height="1626" alt="image" src="https://github.com/user-attachments/assets/43d6c699-7809-4201-a3b2-5d053dac51a2" />




Ask complex queries about research papers and receive grounded, deterministic explanations.

**Example Query:**
> "How does predictive forgetting optimize neural generalization according to the SURE framework?"

**Answer:**
> "Predictive forgetting allows the system to shed episodic noise while retaining the conceptual gist, preventing catastrophic interference during consolidation."

---

## Project Motivation
Large Language Models (LLMs) are fluent but prone to hallucination. **New Covenant** explores RAG as a solution to ground AI responses in verified academic data, providing a tool that mimics human cognitive consolidation.

---

## System Architecture
The system utilizes a decoupled microservices architecture to ensure scalability and local performance.

1. **Ingestion:** Research PDFs are decomposed into semantic chunks.  
2. **Vectorization:** Text is converted to high-dimensional embeddings.  
3. **Retrieval:** Semantic search identifies relevant context via ChromaDB.  
4. **Synthesis:** Meta Llama 3 synthesizes a grounded response via LCEL.  

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

## Project Structure
```text
multimodal-rag/
├── backend/
│   ├── main.py          # FastAPI server & LCEL Pipeline logic
│   └── data/            # Local PDF document repository
├── frontend/
│   └── app.py           # Streamlit Research Interface
├── chroma_db/           # Persistent Vector Database (Binary)
├── venv/                # Isolated Virtual Environment
├── .gitignore           # Git exclusion rules
├── requirements.txt     # Dependency manifest
└── README.md            # System Documentation
---


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
#Screenshots
<img width="3022" height="1546" alt="image" src="https://github.com/user-attachments/assets/0a4e866d-821d-4af9-afb5-8a28286eab88" />



## License
MIT License  

Copyright (c) 2026 Jaellynda  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
---

