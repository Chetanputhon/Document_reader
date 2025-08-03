# Gemini-Powered Document Extractor App

This Streamlit app reads unstructured documents (PDF, DOCX, Excel, emails, PNG images) and extracts structured JSON data using Google's Gemini AI.

## 🔧 Setup

1. Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
```

2. Set your Gemini API key:

```bash
export GEMINI_API_KEY=your-api-key  # on Linux/macOS
set GEMINI_API_KEY=your-api-key     # on Windows
```

3. Run the app:

```bash
streamlit run app.py
```

## 📁 Supported Formats
- PDF
- DOCX
- Excel (XLSX)
- Email (.msg)
- Image (PNG)

## 🚀 Deployment
Can be deployed to Streamlit Cloud or HuggingFace Spaces.