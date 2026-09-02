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

### Q3: Why do we use an isolated virtual environment (`.venv`) for AI projects?
**Answer:**
AI packages (like `google-genai`, `langchain`, `pydantic`, `torch`) evolve rapidly and have strict dependency constraints. If you install everything globally on your computer, library version conflicts will break your other projects. A virtual environment is a self-contained sandbox with its own Python interpreter and `site-packages` directory.

### Q4: Why is `.gitignore` and `.env` separation crucial when working with AI APIs?
**Answer:**
- **The Danger:** LLM API keys have billing attached. If you accidentally commit a key to a public GitHub repository, automated bots scrape it within seconds and exhaust your credits.
- **The Solution:** 
  1. Store secrets locally in a `.env` file.
  2. Add `.env` to `.gitignore` so Git ignores it.
  3. Provide a `.env.example` file that shows the variable names without actual secrets, allowing collaborators to know what environment variables are needed.

### Q5: What happens under the hood during a standard LLM API call?
**Answer:**
When you send a prompt to an LLM provider (like Gemini):
1. **Tokenization:** Your text is converted into numerical tokens (sub-words).
2. **Forward Pass:** The tokens pass through the neural network transformer layers.
3. **Autoregression:** The model predicts the next most probable token one by one until it hits a stop token or reaches the max output token limit.
4. **Decoding & Response:** The output tokens are decoded back into a text response and returned over an HTTP JSON response.

### Q6: What is `temperature` and how does it affect the model's output?
**Answer:**
`temperature` controls how the model samples the probability distribution of possible next tokens:
- **Low temperature (0.0 to 0.3):** The model picks the highest-probability tokens (almost deterministic). Ideal for **analytical research, coding, math, fact-checking, and structured JSON output**.
- **High temperature (0.7 to 1.0+):** Flattens the probabilities, giving less-frequent tokens a chance to be chosen. Ideal for **creative writing, brainstorming, and storytelling**.

### Q7: What is `system_instruction` (System Prompt) and why is it distinct from the user prompt?
**Answer:**
- **System Instruction:** Sets the foundational personality, guidelines, constraints, and output format that persist throughout the interaction (e.g., *"You are an impartial decision analyst. Never make assumptions without evidence."*).
- **User Prompt:** The dynamic, specific question or task provided at runtime (e.g., *"Compare IBPS PO vs Software Engineering"*).
- Separating them gives the system prompt higher priority in steering model behavior.

### Q8: What is Streaming (`generate_content_stream`) and why is it critical for user experience?
**Answer:**
LLMs generate tokens sequentially. If an answer takes 8 seconds to generate 500 words:
- **Without Streaming:** The user stares at a blank screen for 8 seconds before the whole paragraph pops up (feels slow).
- **With Streaming (Server-Sent Events / SSE):** The user sees words appearing immediately (Time To First Token / TTFT is ~200-400ms), giving an instant, responsive experience.

### Q9: How does "Tool Calling" / "Function Calling" actually work?
**Answer:**
1. **Tool Definition:** You write a regular Python function (e.g., `calculate_salary_growth(starting_lpa, rate, years)`).
2. **Schema Extraction:** The SDK automatically inspects your Python function's name, type hints, and docstring, and turns them into a JSON Schema description.
3. **Model Decision:** When given a prompt that requires math or data, the LLM stops text generation and returns a structured `FunctionCall` request asking your app to execute that function with specific arguments.
4. **Local Execution:** Your Python app executes the function locally with the provided arguments.
5. **Final Synthesis:** The output of your function is sent back to the LLM, which uses that ground truth data to formulate its final response.

### Q10: Why are Python type annotations (`float`, `int`, `str`) and docstrings mandatory for tools?
**Answer:**
The LLM cannot see your Python function's internal code; it only sees the function **signature** and **docstring**!
- **Docstring:** Teaches the AI **what** the tool does and **when** it should be chosen.
- **Type Hints:** Ensure the AI sends arguments in the exact format required (e.g. sending `8.0` as a `float` rather than `"eight"` as a string).

### Q11: What is Automatic Function Calling (AFC)?
**Answer:**
In traditional/manual function calling, you had to manually catch the model's tool call response, run your python function, create a `FunctionResponse` object, and send another request to the model.
With **Automatic Function Calling (AFC)**, the modern SDK (like `google-genai`) orchestrates this loop for you: when the model requests a function, the SDK runs your local Python function automatically and feeds the result back to the model in a single seamless call.

---
