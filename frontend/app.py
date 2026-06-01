import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Explain Like I'm 5",
    layout="centered"
)

# ---- HEADER ----
st.title("Explain Like I'm 5")
st.subheader("Paste any text or upload a PDF — get 3 explanations!")

# ---- INPUT MODE TOGGLE ----
mode = st.radio("Choose input type:", ["Paste Text", "Upload PDF"])

result = None

# ---- TEXT MODE ----
if mode == "Paste Text":
    text = st.text_area(
        "Paste your text here:",
        height=200,
        placeholder="e.g. Quantum entanglement is..."
    )
    
    if st.button("Explain it"):
        if not text.strip():
            st.warning("Please enter some text first!")
        else:
            with st.spinner("Generating 3 explanations..."):
                response = requests.post(
                    f"{API_URL}/explain/text",
                    json={"text": text}
                )
                if response.status_code == 200:
                    result = response.json()
                else:
                    st.error("Something went wrong. Is the backend running?")

# ---- PDF MODE ----
elif mode == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    
    if st.button("Explain it"):
        if uploaded_file is None:
            st.warning("Please upload a PDF first!")
        else:
            with st.spinner("Reading PDF and generating explanations..."):
                response = requests.post(
                    f"{API_URL}/explain/pdf",
                    files={"file": (uploaded_file.name,
                                   uploaded_file.getvalue(),
                                   "application/pdf")}
                )
                if response.status_code == 200:
                    result = response.json()
                else:
                    st.error("Something went wrong. Is the backend running?")

# ---- DISPLAY RESULTS ----
if result:
    st.divider()
    st.success("Here are your 3 explanations!")
    
    kid_tab, student_tab, expert_tab = st.tabs(["Kid", "Student", "Expert"])
    
    with kid_tab:
        st.markdown(result["kid"])
    
    with student_tab:
        st.markdown(result["student"])
    
    with expert_tab:
        st.markdown(result["expert"])