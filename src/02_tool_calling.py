"""
Module 02: Tool / Function Calling (First Principles)
-----------------------------------------------------
Purpose:
  Demonstrate how to give an LLM "tools" (Python functions) to perform
  exact mathematical calculations and fetch structured career facts.
"""

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Fix Windows console UTF-8 encoding for emojis/symbols
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Step 1: Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file! Please check your configuration.")

client = genai.Client(api_key=api_key)

# ============================================================================
# Step 2: Define Python Tool Functions
# Notice: Type hints (e.g. float, int, str) and docstrings are CRITICAL.
# The LLM reads the docstring to understand WHEN and HOW to call the function!
# ============================================================================

def calculate_salary_growth(starting_lpa: float, annual_growth_rate: float, years: int) -> dict:
    """
    Calculate the projected salary after a given number of years using compound annual growth.
    
    Args:
        starting_lpa (float): Starting salary in Lakhs Per Annum (e.g. 8.0 for 8 LPA).
        annual_growth_rate (float): Expected annual growth rate as a decimal (e.g. 0.15 for 15%).
        years (int): Number of years of career progression.
        
    Returns:
        dict: A summary containing final salary (LPA) and total growth.
    """
    print(f"\n⚡ [TOOL EXECUTION] Running calculate_salary_growth(starting_lpa={starting_lpa}, rate={annual_growth_rate}, years={years})...")
    final_salary = starting_lpa * ((1 + annual_growth_rate) ** years)
    total_gain = final_salary - starting_lpa
    return {
        "starting_salary_lpa": starting_lpa,
        "years": years,
        "annual_growth_percentage": f"{annual_growth_rate * 100}%",
        "projected_final_salary_lpa": round(final_salary, 2),
        "total_growth_lpa": round(total_gain, 2)
    }

def get_career_benchmarks(career_name: str) -> dict:
    """
    Retrieve verified benchmark data for a specific career path (e.g. 'ibps_po' or 'software_developer').
    
    Args:
        career_name (str): The career to look up ('ibps_po' or 'software_developer').
        
    Returns:
        dict: Career benchmark details including entry exam, average starting salary, and work-life balance.
    """
    print(f"\n⚡ [TOOL EXECUTION] Running get_career_benchmarks(career_name='{career_name}')...")
    benchmarks = {
        "ibps_po": {
            "title": "IBPS Probationary Officer (Banking)",
            "entry_mode": "National Competitive Exam (Prelims + Mains + Interview)",
            "average_starting_lpa": 6.5,
            "job_security": "Very High (Public Sector)",
            "average_annual_increment_percentage": "7-9% (Bi-partite settlements)",
            "typical_work_hours": "10:00 AM - 6:00 PM (Depends on branch)"
        },
        "software_developer": {
            "title": "Software Development Engineer (IT / Tech)",
            "entry_mode": "Coding Interviews (DSA + System Design + Projects)",
            "average_starting_lpa": 7.5,
            "job_security": "Moderate (Market & Performance Driven)",
            "average_annual_increment_percentage": "12-25% (Performance / Switches)",
            "typical_work_hours": "Flexible / Sprint-based (40-45 hours/week)"
        }
    }
    key = career_name.lower().strip().replace(" ", "_")
    return benchmarks.get(key, {"error": f"No benchmark data found for '{career_name}'. Available: 'ibps_po', 'software_developer'"})

# ============================================================================
# Step 3: Run the AI Assistant with Tool Calling
# ============================================================================

def run_tool_calling_demo():
    print("=" * 65)
    print("🚀 AI Personal Research Assistant - Step 1.3: Tool Calling Demo")
    print("=" * 65)

    # Supply our Python functions directly in the tools list
    tools_list = [calculate_salary_growth, get_career_benchmarks]

    # Create a Chat session with Automatic Function Calling enabled
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are an analytical Career & Decision Advisor. "
                "Always use the provided tools to calculate exact numbers and fetch career benchmarks. "
                "Never invent or guess numbers yourself."
            ),
            temperature=0.1,  # Strict temperature for tool precision
            tools=tools_list,
        )
    )

    # Complex Decision Prompt that requires BOTH tools
    query = (
        "I am deciding between IBPS PO and Software Development. "
        "1. Retrieve the career benchmarks for both. "
        "2. If a Software Engineer starts at 8 LPA and grows at 15% yearly for 5 years, calculate the final salary. "
        "3. Provide a clear, factual comparison based on the tool results."
    )

    print(f"\n📝 User Question:\n{query}\n")
    print("🤖 Agent Reasoning & Tool Interactions:\n" + "-" * 50)

    # Send message to model (Gemini will automatically call tools and continue)
    response = chat.send_message(query)

    print("\n" + "-" * 50)
    print("📊 Final Synthesized Answer from AI:\n")
    print(response.text)
    print("\n" + "=" * 65)
    print("✅ Tool Calling Flow Completed Successfully!")

if __name__ == "__main__":
    run_tool_calling_demo()
