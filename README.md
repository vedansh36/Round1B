# 📄 Round 1B – Persona-Driven Document Intelligence

This repository contains our submission for **Round 1B** of the Adobe India Hackathon – *Connecting the Dots*.  
The task is to build an intelligent, offline system that identifies and ranks the most relevant sections across multiple PDFs, based on a **persona** and their **job-to-be-done**, and outputs a structured JSON.

---

## 🧠 Problem Statement

Given:
- A **collection of 3–10 PDFs**
- A **persona definition** (role and domain context)
- A **job-to-be-done** (task based on that persona)

Your task is to:
- Extract relevant sections from each document
- Rank them based on importance to the persona's task
- Provide refined text for each relevant sub-section

---

## ✅ Features

- Ranks relevant content based on persona/job context
- Outputs rich JSON with metadata, ranked sections, and extracted text
- Domain-agnostic and works with any type of document
- Works offline, no network access required
- Fully Dockerized and CPU-only
- Supports `linux/amd64` platform

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:

```txt
PyMuPDF==1.22.3
scikit-learn==1.3.0

```
## 📁 Folder Structure

```plaintext
Round1B/
├── Collection 1/
│   ├── PDFs/                        # Folder with PDFs
│   └── challenge1b_input.json       # Persona and job-to-be-done
│
├── Collection 2/
│   ├── PDFs/
│   └── challenge1b_input.json
│
├── Collection 3/
│   ├── PDFs/
│   └── challenge1b_input.json
│
├── main.py                          # Handles a single collection
├── run_all_collections.py           # Batch runner for all collections
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker config
└── README.md                        # Project documentation (this file)

```
## Installation
```plaintext
docker run --rm -v "${PWD}:/app" --network none round1b:submission123

docker build --platform linux/amd64 -t round1b:submission123 .
