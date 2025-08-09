# Ghost Job Detector (CSV-based)

This Python script identifies potential "ghost job" postings from a local CSV file.  
A ghost job is a listing that may not correspond to an actively hiring position — for example,  
postings that stay online for months, have very low applicant interest, or come from companies  
known to repeatedly post roles without real intent to hire.

> **Note:** This project is a **Proof of Concept (POC)** designed to demonstrate core functionality  
> by processing a single job listing from a CSV file. It is **not production-ready** and serves as a  
> prototype for further development.

---

## Features

- Reads job data from a CSV file (specifically the second row).
- Uses predefined lists of suspicious companies and job titles.
- Scores listings based on multiple criteria including reposting status, description length, applicant count, and posting age.
- Classifies listings as:
  - **Legitimate posting** (score 0–2)
  - **Likely Ghost** (score 3–5)
  - **High Chance** (score 6 or higher)

---

## CSV Format

The script expects the CSV file to have the following columns in order:

