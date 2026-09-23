import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

def initialize_gemini():
    """Initializes the Google Gemini LLM."""
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2
    )

def run_support_agent(customer_inquiry: str):
    """Agent 1: Handles customer support and generates professional replies."""
    llm = initialize_gemini()
    
    prompt = PromptTemplate(
        input_variables=["inquiry"],
        template=(
            "You are an expert AI Customer Support Agent for a global tech company. "
            "Analyze the following customer message and provide a polite, professional, "
            "and resolution-focused response:\n\nCustomer Inquiry: {inquiry}\n\n"
            "AI Support Response:"
        )
    )
    
    # Modern LangChain Expression Language (LCEL) pipe operator (|)
    chain = prompt | llm
    response = chain.invoke({"inquiry": customer_inquiry})
    return response.content

def run_finance_agent(invoice_data: str):
    """Agent 2: Parses financial data and extracts actionable audit items."""
    llm = initialize_gemini()
    
    prompt = PromptTemplate(
        input_variables=["data"],
        template=(
            "You are an AI Finance & Operations Agent. "
            "Review the following text, extract key financial figures, verify compliance, "
            "and output a clean operational summary:\n\nRaw Data: {data}\n\n"
            "Finance Audit Summary:"
        )
    )
    
    chain = prompt | llm
    response = chain.invoke({"data": invoice_data})
    return response.content

# --- Testing the Multi-Agent Engine ---
if __name__ == "__main__":
    print("🚀 Initializing OmniWorker AI Engine...\n")
    
    # Test 1: Customer Support Task
    sample_inquiry = "Hi, my subscription payment failed twice today, but money was debited from my bank account. Please help!"
    print(f"--- Running Support Agent ---")
    support_output = run_support_agent(sample_inquiry)
    print(support_output)
    print("\n" + "="*50 + "\n")
    
    # Test 2: Finance Task
    sample_invoice = "Invoice #1092 from AWS Cloud Services. Amount: $450.50. Due Date: Oct 15, 2026. Status: Pending approval."
    print(f"--- Running Finance Agent ---")
    finance_output = run_finance_agent(sample_invoice)
    print(finance_output)