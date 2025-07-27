import os
import json
import argparse
from datetime import datetime

import fitz  # PyMuPDF

import re

def extract_section_info(pdf_dir, filename):
    path = os.path.join(pdf_dir, filename)
    doc = fitz.open(path)

    best_page_number = 0
    best_score = 0
    best_text = ""

    for i, page in enumerate(doc):
        text = page.get_text().strip()
        score = len(text.split())  # crude scoring: longest page = most content
        if score > best_score:
            best_score = score
            best_text = text
            best_page_number = i + 1  # page numbers are 1-indexed

    # Remove newlines and collapse multiple spaces
    cleaned_text = re.sub(r'\s+', ' ', best_text).strip()

    # Use first line as section title (before cleaning, to preserve real heading formatting)
    first_line = best_text.split("\n")[0].strip()

    return {
        "section_title": first_line if first_line else "Untitled Section",
        "importance_rank": 0,  # This will be added during loop in main logic
        "page_number": best_page_number,
        "refined_text": cleaned_text
    }


def process_documents(pdf_dir, input_json_path):
    with open(input_json_path, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    # Construct metadata from your current JSON format
    input_documents = input_data["documents"]  # list of dicts with filename + title

    metadata = {
        "input_documents": input_documents,
        "persona": input_data["persona"]["role"],
        "job_to_be_done": input_data["job_to_be_done"]["task"],
        "processing_timestamp": datetime.now().isoformat()
    }

    # Extract sections and subsection analysis from documents
    extracted_sections = []
    subsection_analysis = []

    for rank, doc in enumerate(input_documents, start=1):
        info = extract_section_info(pdf_dir, doc["filename"])
        extracted_sections.append({
            "document": doc["filename"],
            "section_title": info["section_title"],
            "importance_rank": rank,
            "page_number": info["page_number"]
        })
        subsection_analysis.append({
            "document": doc["filename"],
            "refined_text": info["refined_text"],
            "page_number": info["page_number"]
        })

    return {
        "metadata": metadata,
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_json", required=True, help="Path to input JSON")
    parser.add_argument("--pdf_dir", required=True, help="Directory containing PDFs")
    parser.add_argument("--output_json", required=True, help="Path to output JSON")
    args = parser.parse_args()

    results = process_documents(args.pdf_dir, args.input_json)

    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
