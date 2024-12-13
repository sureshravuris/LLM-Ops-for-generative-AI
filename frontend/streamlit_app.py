import streamlit as st
import requests
import json
from typing import Dict, Any

st.set_page_config(
    page_title="Document Summarizer",
    page_icon="📄",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

def summarize_text(text: str) -> Dict[str, Any]:
    """Send text to API for summarization"""
    try:
        headers = {
            "Content-Type": "application/json",
        }
        
        st.info(f"Sending request to {API_URL}/summarize/")
        
        with st.spinner("Processing... This may take a few moments."):
            response = requests.post(
                f"{API_URL}/summarize/",
                json={"text": text},
                headers=headers,
                timeout=180  # Increased timeout to 3 minutes
            )
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = f"API Error: {response.status_code} - {response.text}"
            st.error(error_msg)
            return {"success": False, "error": error_msg}
            
    except requests.exceptions.Timeout:
        error_msg = "Request timed out. The text might be too long or the server is busy."
        st.error(error_msg)
        return {"success": False, "error": error_msg}
    except requests.exceptions.ConnectionError:
        error_msg = f"Could not connect to {API_URL}. Please check if the API server is running."
        st.error(error_msg)
        return {"success": False, "error": error_msg}
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        st.error(error_msg)
        return {"success": False, "error": error_msg}

def main():
    st.title("📄 Document Summarizer")
    st.write("Upload or paste your document to get a concise summary")
    
    # Add API status indicator
    if st.button("Check API Status"):
        try:
            response = requests.get(f"{API_URL}/")
            if response.status_code == 200:
                st.success("API is running! ✅")
            else:
                st.error("API is not responding correctly ❌")
        except:
            st.error("Could not connect to API ❌")
    
    text_input = st.text_area(
        "Enter your text here:",
        height=300,
        placeholder="Paste your document text here..."
    )
    
    if st.button("Summarize", type="primary"):
        if not text_input:
            st.error("Please enter some text to summarize")
            return
            
        with st.spinner("Generating summary..."):
            result = summarize_text(text_input)
            
            if result.get("success", False):
                st.success("Summary generated successfully!")
                st.write("### Summary")
                st.write(result["summary"])
                st.write("---")
                st.write(f"Token count: {result['token_count']}")
            else:
                st.error(f"Error: {result.get('error', 'Unknown error occurred')}")

if __name__ == "__main__":
    main()