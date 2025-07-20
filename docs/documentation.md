# 🚀 Project Title: Context-Aware Multilingual Translator (or QA System)

## 📌 Table of Contents
1. [Project Overview](#project-overview)
2. [Environment Setup](#environment-setup)
3. [Dataset Preparation](#dataset-preparation)
4. [Model Selection](#model-selection)
5. [Training Configuration](#training-configuration)
6. [Evaluation Metrics](#evaluation-metrics)
7. [Inference & API](#inference--api)
8. [Deployment](#deployment)
9. [Monitoring & Feedback Loop](#monitoring--feedback-loop)
10. [Future Work](#future-work)

---

## 📖 Project Overview
Briefly describe the project:
This project develops an **end-to-end question answering (QA) system** tailored for the healthcare domain by fine-tuning a lightweight **large language model (LLM)** using the **QLoRA* method. The system enables users to input medical or health-related questions and receive accurate, context-aware answers via a deployed API interface.

Reliable access to structured medical knowledge through natural language interfaces can support both healthcare professionals and patients by improving decision-making, reducing research time, and minimizing reliance on generic search engines.

The project uses the Phi-1.5 model, chosen for its balance of performance and efficiency, and fine-tunes it specifically for healthcare QA tasks to ensure relevance and domain-specific understanding.

---

## ⚙️ Environment Setup

### 🐍 Python Version
- Python 3.10

### 🖥️ Hardware
- OS: Windows 11 Pro
- GPU: NVIDIA GeForce RTX 3060 (12 GB VRAM)
- RAM: 16 GB

### 🧪 Virtual Environment
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
# or
source .venv/bin/activate      # macOS/Linux
```

### 📦 Key Libraries and Versions
| Library         | Version       |
|-----------------|---------------|
| torch           | 2.2.2+cu118   |
| torchvision     | 0.17.2+cu118  |
| torchaudio      | 2.2.2+cu118   |
| transformers    | 4.40.0        |
| datasets        | 2.19.0        |
| peft            | 0.10.0        |
| accelerate      | 0.27.2        |
| bitsandbytes    | 0.43.0        |
| sentencepiece   | latest        |
| evaluate        | latest        |
| scikit-learn    | latest        |
| scipy           | latest        |

### 📥 Installation Instructions
```bash
pip install --upgrade pip
pip install torch==2.2.2+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers==4.40.0 datasets==2.19.0 peft==0.10.0 accelerate==0.27.2
pip install bitsandbytes==0.43.0 sentencepiece evaluate scikit-learn
```

### 🧪 GPU Check
``` python
import torch
print(torch.cuda.is_available())        # Should return True
print(torch.cuda.get_device_name(0))    # Should return your GPU name
```
---

## 📂 Dataset Preparation

The dataset used in this project is **MedQuAD**, a real-world, expert-annotated collection of medical question-answer (QA) pairs gathered from trusted sources such as the NIH and MedlinePlus. The data was originally stored in XML format across multiple topic-specific folders.

The dataset used for this project is the **MedQuAD** (Medical Question Answering Dataset), which contains thousands of question–answer pairs derived from trusted health sources such as NIH and MedlinePlus.

🔗 **Source**: [MedQuAD GitHub Repository](https://github.com/abachaa/MedQuAD)


### Steps Followed:

1. **XML Collection & Parsing**  
   All `.xml` files were recursively gathered from the MedQuAD directory structure. Each file contains one or more `<QAPair>` tags, holding a `<Question>` and an `<Answer>`.

2. **Extraction of QA Pairs**  
   Each QA pair was parsed and validated to ensure both the question and answer fields were present. Files with multiple QAPairs were fully extracted.

3. **Cleaning**  
   - HTML tags were removed from the text content.  
   - Extra whitespaces and formatting inconsistencies were normalized.

4. **Filtering**  
   QA pairs with very short questions (less than 10 characters) or answers (less than 20 characters) were discarded to ensure data quality and relevance.

5. **Formatting**  
   Each pair was converted into an instruction-based format, with keys:
   ```json
   {
     "instruction": "question text",
     "response": "answer text"
   }```

6. **Saving**
The final preprocessed dataset was saved in a .jsonl format named medquad_preprocessed.jsonl inside the data/ directory, with each line representing a single QA pair.

---

### 🧠 Model Selection

--- 

### ⚙️ Training Configuration

---

### 📊 Evaluation Metrics

---

### 🧪 Inference & API

---

### 🚀 Deployment

---

### 📈 Monitoring & Feedback Loop

---

### 🔮 Future Work