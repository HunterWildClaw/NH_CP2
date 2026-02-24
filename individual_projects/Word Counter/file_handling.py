#NH 2nd file handling for word counter
#Import os, json, and datetime
import os
import json
from datetime import datetime

docs_dir = "documents"
metadata_file = "documents_metadata.json"

def ensure_docs_dir():
    # Make documents folder if it doesn't exist
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

def load_metadata():
    # Read the metadata file if it exists
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r') as f:
            return json.load(f)
    return {}

def save_metadata(metadata):
    # Write metadata to file
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

def count_words(filepath):
    # Count words in a file
    if not os.path.exists(filepath):
        return 0
    with open(filepath, 'r') as f:
        content = f.read()
    return len(content.split())

def create_document():
    # Ask user for document name
    name = input("Enter document name: ").strip()
    
    # Don't let them use empty names
    if not name:
        print("Document name cannot be empty.")
        return
    
    filepath = os.path.join(docs_dir, f"{name}.txt")
    
    # Check if document already exists
    if os.path.exists(filepath):
        print(f"Document '{name}' already exists.")
        return
    
    # Add to metadata and make empty file
    metadata = load_metadata()
    metadata[name] = {"created": datetime.now().isoformat(), "word_count": 0}
    save_metadata(metadata)
    
    with open(filepath, 'w') as f:
        f.write("")
    
    print(f"Document '{name}' created successfully. (0 words)")

def write_document():
    # Ask user which document to write in
    name = input("Enter document name (be exact!): ").strip()
    filepath = os.path.join(docs_dir, f"{name}.txt")
    
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"Document '{name}' does not exist.")
        return
    
    # Get text from user until they type "end"
    print("Enter your text (type 'end' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line == "end":
            break
        lines.append(line)
    
    # Add text to file
    with open(filepath, 'a') as f:
        f.write('\n'.join(lines) + '\n')
    
    # Update metadata with new word count
    word_count = count_words(filepath)
    metadata = load_metadata()
    metadata[name] = {"updated": datetime.now().isoformat(), "word_count": word_count}
    save_metadata(metadata)
    
    print(f"Document '{name}' updated successfully. ({word_count} words)")

def view_document():
    # Ask user which document to read
    name = input("Enter document name: ").strip()
    filepath = os.path.join(docs_dir, f"{name}.txt")
    
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"Document '{name}' does not exist.")
        return
    
    # Get info about the document
    metadata = load_metadata()
    doc_metadata = metadata.get(name, {})
    word_count = count_words(filepath)
    
    # Read and display the file
    with open(filepath, 'r') as f:
        content = f.read()
    
    print(f"\n--- Document: {name} ---")
    print(f"Last updated: {doc_metadata.get('updated', 'Unknown')}")
    print(f"Word count: {word_count}")
    print(f"Content:\n{content}\n")
