# 🤖 AI Personal Research & Decision Assistant

An enterprise-grade, agentic AI system that decomposes complex decision questions, gathers evidence via Web Search, local RAG (PDFs/Notes), and quantitative tools, validates findings with a fact-checker, and generates structured executive decision reports.

---

## 🚀 Learning & Implementation Philosophy
Built progressively from **first principles** to production:
1. **Raw LLM & Tool Calling** (Pure Python, no framework abstraction)
2. **First-Principles RAG** (Custom chunking, embeddings, vector similarity)
3. **LangChain Abstractions** (Loaders, splitters, chains, output parsers)
4. **Multi-Tool Autonomous Agents** (ReAct loop)
5. **Agentic Graphs with LangGraph** (Cyclic state machines, planning, reflection)
6. **Stateful Memory & Checkpointing** (Conversation persistence)
7. **Structured Decision Reporting** (PDF / Markdown reports)
8. **Evaluation & Observability** (RAGAS, benchmark datasets, guardrails)
9. **Full-Stack Application** (FastAPI backend + React frontend)

---

## 📚 Handbook & Documentation
- **Questions & Answers Learning Handbook:** [`questions_and_answers.md`](./questions_and_answers.md)

---

## 🛠️ Quick Start

### 1. Clone & Setup Virtual Environment
```bash
git clone https://github.com/MohitJain2003/ai-research-decision-assistant.git
cd ai-research-decision-assistant

# Create and activate virtual environment (Python 3.12 recommended)
py -3.12 -m venv .venv
# On Windows PowerShell:
.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
Copy `.env.example` to `.env` and insert your API keys:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
