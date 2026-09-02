# 🧠 AI Engineer Learning & Project Q&A Handbook
## Project: AI Personal Research & Decision Assistant

> **Purpose**: This living document tracks all theoretical concepts, architecture questions, technical reasoning, and simple explanations as we build the project step-by-step from zero to production.

---

## 🗺️ Roadmap & Curriculum Table of Contents
1. [Milestone 0: AI Engineering Fundamentals](#milestone-0-ai-engineering-fundamentals)
2. [Milestone 1: LLM APIs, Client Calls & Tool Calling Mechanics](#milestone-1-llm-apis-client-calls--tool-calling-mechanics)
3. [Milestone 2: First-Principles RAG (Chunking, Embeddings, Vector DBs)](#milestone-2-first-principles-rag)
4. [Milestone 3: LangChain & Abstraction Layers](#milestone-3-langchain--abstraction-layers)
5. [Milestone 4: Multi-Tool Autonomous ReAct Agents](#milestone-4-multi-tool-autonomous-react-agents)
6. [Milestone 5: Agentic Graphs with LangGraph (Planning, Cycles & Reflection)](#milestone-5-agentic-graphs-with-langgraph)
7. [Milestone 6: Memory, Checkpointing & State Persistence](#milestone-6-memory-checkpointing--state-persistence)
8. [Milestone 7: Structured Executive Reporting & Citation Grounding](#milestone-7-structured-executive-reporting)
9. [Milestone 8: Evaluation, Benchmarking & Observability](#milestone-8-evaluation-benchmarking--observability)
10. [Milestone 9: Full-Stack Production (FastAPI + React)](#milestone-9-full-stack-production)

---

## 📌 Milestone 0: AI Engineering Fundamentals

### Q1: What is the core difference between an ML Engineer and an AI Engineer?
**Answer:**
- **ML Engineer / Researcher:** Focuses on training or fine-tuning machine learning models, loss functions, GPU cluster optimization, and mathematical modeling.
- **AI Engineer:** Focuses on building real-world software powered by foundation models (LLMs/VLMs). They work on orchestration, RAG, tool calling, prompt engineering, agentic workflows, latency/cost optimization, and evaluation.

### Q2: Why build from "First Principles" (Pure Python) before using LangChain/LangGraph?
**Answer:**
Frameworks like LangChain and LangGraph are powerful, but if you start with them without understanding what they do under the hood, you will get stuck whenever things fail (like debugging prompt formatting errors, tool schema mismatches, or vector math bugs). Building with pure Python first ensures you understand:
- How JSON schemas are sent to LLMs for tool calling.
- How text is converted to numbers (embeddings) and matched (cosine similarity).
- Why and where LangChain/LangGraph actually save time.

---

## 📌 Milestone 1: LLM APIs, Client Calls & Tool Calling Mechanics

### Q3: What happens under the hood during a standard LLM API call?
**Answer:**
When you send a prompt to an LLM provider (like Gemini or OpenAI):
1. Your text is broken down into numerical tokens (sub-words).
2. The tokens pass through the neural network transformer layers.
3. The model predicts the next most probable token one by one (autoregression) until it hits a stop token or max length.
4. The output tokens are decoded back into a text response and returned over HTTP.

### Q4: How does "Tool Calling" / "Function Calling" actually work? Does the LLM execute the Python code?
**Answer:**
**No, the LLM does NOT execute code!** 
The process works in 4 steps:
1. **Tool Definition:** You define a function in Python (e.g., `calculate(expression)`) and give the LLM a JSON description (name, purpose, parameter types).
2. **LLM Decision:** You send a user prompt like *"What is 45 * 892?"*. The LLM reads the tool description and decides: *"I shouldn't answer directly; I should call `calculate` with `expression='45 * 892'`"*.
3. **Structured Response:** The LLM returns a structured JSON payload telling your application to run that function with those exact arguments.
4. **Execution & Answer:** **Your Python program** executes the function locally, gets the result (`40140`), sends that result back to the LLM as context, and the LLM produces the final polite response: *"45 multiplied by 892 is 40,140."*

---

*(More questions and answers will be continuously added as we progress through each step!)*
