import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key="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"
)

st.set_page_config(page_title="Eleon Protocol Generator", layout="centered")
st.title("Eleon: AI Protocol Generator")
st.markdown("Enter a description of your clinical trial, and Eleon will generate a structured protocol draft using AI.")

user_input = st.text_area("📝 Describe your trial in plain English:", placeholder="E.g., I want to test Drug A vs placebo over 12 months in 100 patients with type 2 diabetes...")

submit = st.button("Generate Protocol")

def create_prompt(description):
    return f"""
You are an AI assistant trained in clinical trial design. Based on the following description, create a protocol draft with these sections:

1. Study Title
2. Study Objectives
3. Study Arms (intervention vs control)
4. Inclusion Criteria
5. Exclusion Criteria
6. Timeline Overview

Trial Description: "{description}"
"""

if submit and user_input:
    with st.spinner("Generating your protocol..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a clinical trials protocol design assistant."},
                    {"role": "user", "content": create_prompt(user_input)}
                ],
                temperature=0.7
            )

            output = response.choices[0].message.content
            st.markdown("### 📄 Generated Protocol")
            st.markdown(output)

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
