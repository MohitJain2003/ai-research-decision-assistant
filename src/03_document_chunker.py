"""
Module 03: Document Ingestion & Chunking (First Principles)
------------------------------------------------------------
Purpose:
  Load a raw document and split it into bite-sized "chunks" with overlap.
  This is the very first step in building a RAG (Retrieval-Augmented Generation) pipeline.
"""

import os
import sys

# Fix Windows console UTF-8 encoding for output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


def load_document(file_path: str) -> str:
    """Read and return the plain text of a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Document not found at: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# ============================================================================
# ✍️ YOUR TASK: Write the chunking function below!
# ============================================================================
def create_chunks(text: str, chunk_size: int = 400, chunk_overlap: int = 80) -> list[dict]:
    """
    Split a long text into smaller overlapping chunks using a sliding window.
    
    Args:
        text (str): The full document text.
        chunk_size (int): Maximum number of characters per chunk.
        chunk_overlap (int): Number of overlapping characters between consecutive chunks.
        
    Returns:
        list[dict]: A list of chunk objects, each having:
                    - 'chunk_id': index (0, 1, 2...)
                    - 'text': the chunk content
                    - 'start_char': start character index in original document
                    - 'end_char': end character index in original document
    """
    chunks=[]
    start=0
    text_length=len(text)
    chunk_id=0

    step=chunk_size-chunk_overlap

    while start < text_length:
        end=min(start + chunk_size, text_length)
        chunk_content=text[start:end].strip()

        if chunk_content:
            chunks.append({
                "chunk_id" : chunk_id,
                "text" : chunk_content,
                "start_char": start,
                "end_char": end
            })
            chunk_id+=1
        start+=step

    return chunks
        


# ============================================================================
# Main Verification & Demonstration
# ============================================================================
def main():
    print("=" * 65)
    print("🚀 Step 2.1: First-Principles Document Chunker")
    print("=" * 65)

    doc_path = os.path.join("data", "sample_career_notes.md")
    raw_text = load_document(doc_path)
    print(f"\n📄 Loaded document: '{doc_path}'")
    print(f"📏 Total Characters in Document: {len(raw_text)}")

    # Test chunking with chunk_size=350 characters and overlap=70 characters
    chunk_size = 350
    chunk_overlap = 70

    chunks = create_chunks(raw_text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    if not chunks:
        print("\n⚠️ `create_chunks()` returned None or empty list.")
        print("👉 Complete the TODO block above, then run this script again!")
        return

    print(f"✂️ Total Chunks Created: {len(chunks)}")
    print("\n" + "-" * 65)
    print("🔍 Inspecting the First 3 Chunks:")
    print("-" * 65)

    for chunk in chunks[:3]:
        print(f"\n📦 [Chunk #{chunk['chunk_id']}] (Chars {chunk['start_char']} to {chunk['end_char']}):")
        print(f"\"{chunk['text']}\"")
        print("~" * 50)

    print("\n✅ Document Chunking Verified Successfully!")


if __name__ == "__main__":
    main()
