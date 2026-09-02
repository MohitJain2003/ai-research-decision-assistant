"""
Module 01: Direct LLM Interaction (First Principles)
-----------------------------------------------------
Purpose:
  Demonstrate raw LLM API communication without framework abstractions.
  Learn core parameters: system instructions, temperature, and streaming.
"""

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Fix Windows console UTF-8 encoding for emojis/symbols
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Step 1: Load environment variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file! Please check your configuration.")

# Step 2: Initialize the official Gemini Client
client = genai.Client(api_key=api_key)

def run_direct_llm():
    print("=" * 60)
    print("🚀 AI Personal Research Assistant - Step 1.2: Direct LLM Call")
    print("=" * 60)

    # Step 3: Define System Instruction (Persona & Behavior)
    system_instruction = (
        "You are an expert AI Career & Research Advisor. "
        "Provide objective, concise, and structured comparisons to help users make informed decisions."
    )

    # Step 4: Configure Generation Parameters
    # - temperature: 0.0 (most deterministic) to 2.0 (creative)
    # - system_instruction: defines persona/role
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.3,
        max_output_tokens=800,
    )

    # Step 5: Define User Query
    user_query = "Compare preparing for IBPS PO vs focusing on a Software Development career in 3 concise bullet points."
    print(f"\n📝 User Query: {user_query}\n")
    print("🤖 Model Response (Streaming in real-time):\n" + "-" * 50)

    # Step 6: Call the Model with Streaming Output
    response_stream = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=user_query,
        config=config,
    )

    full_text = ""
    for chunk in response_stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_text += chunk.text

    print("\n" + "-" * 50)
    print("✅ LLM Call Completed Successfully!")

if __name__ == "__main__":
    run_direct_llm()
