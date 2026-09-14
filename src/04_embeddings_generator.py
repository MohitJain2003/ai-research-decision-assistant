"""
Module 04: Vector Embeddings & Similarity (First Principles)
------------------------------------------------------------
Purpose:
  1. Convert text chunks into numerical vectors (Embeddings) using Gemini.
  2. Implement Cosine Similarity from scratch in pure Python to measure
     semantic closeness between questions and document chunks.
"""

import os
import sys
import math
from dotenv import load_dotenv
from google import genai

# Fix Windows console UTF-8 encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Step 1: Load API Key and initialize Gemini Client
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file! Please check your configuration.")

client = genai.Client(api_key=api_key)


def get_embedding(text: str) -> list[float]:
    """
    Call Gemini's embedding model to convert a text string into a list of floats.
    Model: text-embedding-004 produces a 768-dimensional vector.
    """
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
    )
    # Extract the numerical vector from response
    return response.embeddings[0].values


# ============================================================================
# ✍️ YOUR TASK: Write the Cosine Similarity math function below!
# ============================================================================
def calculate_cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """
    Calculate the cosine similarity between two numerical vectors.
    Formula:
        CosineSimilarity = (A · B) / (||A|| * ||B||)
        where:
        - (A · B) is the dot product: sum(a * b for a, b in zip(vec_a, vec_b))
        - ||A|| is the Euclidean norm: sqrt(sum(a * a for a in vec_a))
        - ||B|| is the Euclidean norm: sqrt(sum(b * b for b in vec_b))

    Returns:
        float: A score between -1.0 and 1.0 (1.0 means identical direction/meaning).
    """
    # 1. Calculate the dot product: multiply matching elements and sum them up
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))

    # 2. Calculate the Euclidean norm (magnitude) of vector A: sqrt(sum(a^2))
    norm_a = math.sqrt(sum(a * a for a in vec_a))

    # 3. Calculate the Euclidean norm (magnitude) of vector B: sqrt(sum(b^2))
    norm_b = math.sqrt(sum(b * b for b in vec_b))

    # Guard against division by zero
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0

    # 4. Return cosine similarity: dot product divided by the product of norms
    return dot_product / (norm_a * norm_b)


# ============================================================================
# Main Verification & Semantic Similarity Test
# ============================================================================
def main():
    print("=" * 65)
    print("🚀 Step 2.2: First-Principles Vector Embeddings & Similarity")
    print("=" * 65)

    # 1. Define three test phrases
    text_1 = "Software Engineer coding in Python and building backend systems."
    text_2 = "Full stack web developer programming web applications."
    text_3 = "Banking PO exam syllabus, speed math shortcuts, and reasoning."

    print("\n📝 Generating Embeddings using 'text-embedding-004'...")
    vec_1 = get_embedding(text_1)
    vec_2 = get_embedding(text_2)
    vec_3 = get_embedding(text_3)

    print(f"✅ Embedding 1 generated: Vector with {len(vec_1)} dimensions")
    print(f"👀 First 5 numbers of Vector 1: {[round(x, 4) for x in vec_1[:5]]}")

    # 2. Check similarity
    sim_1_2 = calculate_cosine_similarity(vec_1, vec_2)
    sim_1_3 = calculate_cosine_similarity(vec_1, vec_3)

    if sim_1_2 is None or sim_1_3 is None:
        print("\n⚠️ `calculate_cosine_similarity()` returned None.")
        print("👉 Complete the TODO block above, then run this script again!")
        return

    print("\n" + "-" * 65)
    print("🎯 Semantic Similarity Results (Scale: 0.0 to 1.0):")
    print("-" * 65)
    print(f"Phrase 1: \"{text_1}\"")
    print(f"Phrase 2: \"{text_2}\"")
    print(f"👉 Similarity (Tech vs Tech): {sim_1_2:.4f} (High match expected!)")
    print("-" * 65)
    print(f"Phrase 1: \"{text_1}\"")
    print(f"Phrase 3: \"{text_3}\"")
    print(f"👉 Similarity (Tech vs Banking): {sim_1_3:.4f} (Lower match expected!)")
    print("-" * 65)

    if sim_1_2 > sim_1_3:
        print("\n🎉 SUCCESS! Vector embeddings correctly recognized that Tech & Web Dev")
        print("   are much closer in meaning than Tech & Banking!")


if __name__ == "__main__":
    main()
