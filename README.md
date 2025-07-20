# 🤖 LLM-Based Question Answering System

This project implements an end-to-end healthcare-focused question answering (QA) system by fine-tuning a lightweight Large Language Model (LLM) using the [MedQuAD dataset](https://github.com/abachaa/MedQuAD). It enables users to input medical questions and receive accurate, domain-specific responses.

For full details, refer to [`documentation.md`](./documentation.md)

--- 
## 📂 Dataset

- **Name**: MedQuAD (Medical Question Answering Dataset)
- **Format**: Raw XML → Cleaned JSONL
- **Source**: [GitHub - abachaa/MedQuAD](https://github.com/abachaa/MedQuAD)
- **Preprocessing Steps**:
  - Parse all XML files
  - Extract `<Question>` and `<Answer>` pairs
  - Clean HTML tags and normalize whitespace
  - Filter short/incomplete entries
  - Save in instruction-response format:
    ```json
    {
      "instruction": "What is GERD?",
      "response": "Gastroesophageal reflux disease (GERD) is a..."
    }
    ```
---

## 🧪 Testing

Unit tests are located in the `tests/` folder and ensure:
- Proper extraction of QA pairs
- XML structure handling
- JSONL saving logic

To run all tests:

```bash
python -m unittest discover tests
```
---

## 📁 Project Structure
- `AmirFullLLMProject/`
  - `data/` — Dataset files (raw XMLs, preprocessed JSONL)
    - `MedQuAD_XMLs/` — Original XML dataset
    - `medquad_preprocessed.jsonl` — Final preprocessed QA dataset
  - `src/` — Source code
    - `preprocess_dataset.py` — Main dataset preprocessing pipeline
  - `tests/` — Unit tests
    - `test_preprocessing.py` — Tests for data preprocessing logic
  - `README.md` — Project overview and quick start
  - `documentation.md` — Full project documentation and design notes
  - `requirements.txt` — Python dependencies
  - `.venv/` — Python virtual environment (excluded from version control)

--- 

## ⚙️ Setup
```bash
# Create and activate virtual environment
python -m venv .venv
.venv/Scripts/activate  # Windows

# Install required packages
pip install -r requirements.txt
```