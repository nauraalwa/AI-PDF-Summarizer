# AI-Text-Summarizer

An app to summarize long paragraphs utilizing the Gemini AI API and Streamlit

# 1. Load the PDF from the user
Through streamlit file uploader, we get the PDF. 
Then, the PDF is converted into bytes. 

# 2. Configure Gemini AI
Get the API Keys from Google AI Studio, and see the documentation for Gemini AI Document Reading.

# 3. Generate summary from Gemini AI
Feed the PDF bytes to the Gemini AI.
Use instruction prompting to tell Gemini AI to summarize the PDF into only 1 paragraph.
