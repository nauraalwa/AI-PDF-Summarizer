import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

def configure_gemini(file_bytes):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = "Summarize this document into only 1 paragraph"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Part.from_bytes(
                data=file_bytes,
                mime_type='application/pdf',
            ),
            prompt])
    return response.text

def main():
    st.set_page_config("AI PDF Summarizer")
    st.title("AI PDF Summarizer")

    pdf_doc = st.file_uploader("Upload your PDF here:", type="pdf")
    if st.button("Process"):
        file_bytes = pdf_doc.read() # gives the bytes alr, so httpx.get() no need since it expects a string then will turn into bytes too
        summary = configure_gemini(file_bytes)
        try:
            st.success("Summary generated")
            st.markdown(f"{summary}")
        except Exception as e:
            st.error(f"error occurred: {e}")

if __name__ == "__main__":
    main()