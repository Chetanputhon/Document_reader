import streamlit as st
import pdfplumber
from docx import Document
import pandas as pd
import extract_msg
from PIL import Image
import pytesseract
import os
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")

def extract_structured_data_with_gemini(text):
    prompt = f"""
    Extract structured data in JSON format from the text below:

    TEXT:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_text_from_excel(file):
    df = pd.read_excel(file)
    return df.to_string(index=False)

def extract_text_from_msg(file):
    msg = extract_msg.Message(file)
    return msg.body

def extract_text_from_image(file):
    image = Image.open(file)
    return pytesseract.image_to_string(image)

# Streamlit UI
st.title("📄 Unstructured to Structured with Gemini")

uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "xlsx", "msg", "png"])

if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()

    if file_type == "pdf":
        raw_text = extract_text_from_pdf(uploaded_file)
    elif file_type == "docx":
        raw_text = extract_text_from_docx(uploaded_file)
    elif file_type == "xlsx":
        raw_text = extract_text_from_excel(uploaded_file)
    elif file_type == "msg":
        raw_text = extract_text_from_msg(uploaded_file)
    elif file_type == "png":
        raw_text = extract_text_from_image(uploaded_file)
    else:
        st.error("Unsupported file type")
        raw_text = ""

    st.subheader("📜 Raw Extracted Text")
    st.text_area("Extracted", raw_text, height=300)

    if st.button("🔍 Extract Structured Data with Gemini"):
        structured = extract_structured_data_with_gemini(raw_text)
        st.subheader("🗃️ Structured Output")
        st.code(structured, language="json")