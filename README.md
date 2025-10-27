# 🌍 Backend Automation with Python

This project automates tests for the **RestCountries API** using `pytest`, `requests`, and `jsonschema`.

## 🧠 Scenarios
1. ✅ **Schema Validation** — Ensure API response matches schema  
2. 🌍 **Country Count** — Validate there are 195 countries  
3. 🗣️ **Language Validation** — Ensure SASL is listed under South Africa  

## ⚙️ Setup & Run
```bash
pip install -r requirements.txt
pytest --alluredir=reports/
