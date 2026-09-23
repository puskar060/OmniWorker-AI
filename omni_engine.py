import os
from google import genai

def run_omni_agent(task_description: str, api_key: str) -> str:
    if not api_key:
        return "Error: Gemini API Key is missing."
    try:
        client = genai.Client(api_key=api_key)
        prompt = f"""
        You are OmniWorker AI, an elite autonomous enterprise execution agent.
        Task: {task_description}
        Provide a comprehensive structured output.
        """
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Execution Error: {str(e)}"
