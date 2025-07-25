import streamlit as st
import requests
import json
import re

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Tech Relevance AI", layout="wide")
st.title(" Tech Relevance AI")

# Resume Upload
st.header("📄 Upload Your Resume")
uploaded_file = st.file_uploader("Choose your resume file", type=["pdf", "txt", "docx"])
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{BACKEND_URL}/upload-resume", files={"file": uploaded_file})
    if response.status_code == 200:
        st.success(" Resume uploaded successfully!")
    else:
        st.error(" Resume upload failed.")

# Detect Domains
if st.button(" Detect Relevant Domains from Resume"):
    response = requests.get(f"{BACKEND_URL}/detect-domain")
    if response.status_code == 200:
        domains = response.json().get("domains", [])
        st.subheader(" Detected Domains:")
        for domain in domains:
            st.markdown(f"- **{domain}**")
    else:
        st.error("Failed to detect domains.")

# Fetch & Score News
if st.button("📰 Fetch Personalized Tech News"):
    response = requests.get(f"{BACKEND_URL}/relevant-news")
    if response.status_code == 200:
        raw_items = response.json().get("articles", [])
        st.subheader(" Tech News Relevance")

        for item in raw_items:
            st.markdown(f"""
            #### 📰 [{item['title']}]({item['url']})
            - **Source:** {item['source']}
            - **Published At:** {item['publishedAt']}
            - **Description:** {item['description']}
            """)