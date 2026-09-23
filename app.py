import streamlit as st
from omni_engine import run_omni_agent

st.set_page_config(page_title="OmniWorker AI", page_icon="⚡", layout="wide")
st.title("⚡ OmniWorker AI: Autonomous Enterprise Operations Engine")

api_key = st.sidebar.text_input("Enter Google Gemini API Key", type="password")
task_input = st.text_area("Describe the task for OmniWorker:")

if st.button("🚀 Execute OmniWorker Agent", type="primary"):
    if not api_key:
        st.warning("Please enter your Gemini API Key.")
    elif not task_input:
        st.warning("Please enter a task.")
    else:
        with st.spinner("Executing workflow..."):
            result = run_omni_agent(task_input, api_key)
            st.success("Completed!")
            st.markdown(result)
