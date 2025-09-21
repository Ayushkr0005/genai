import streamlit as st
import google.generativeai as genai

# -------------------------------
# CONFIGURE GEN AI (Direct Key)
# -------------------------------
genai.configure(api_key="AIza...YOUR_API_KEY_HERE...")

# Use Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# -------------------------------
# STREAMLIT UI
# -------------------------------
st.set_page_config(page_title="AI Career & Skills Advisor", layout="centered")

st.title("🎯 AI-Powered Career & Skills Advisor")
st.write("Get a personalized roadmap, skill gap analysis, and interview prep powered by Google Gemini AI.")

# Input fields
career_goal = st.text_input("Enter your desired career (e.g., Data Scientist, Cloud Engineer):")
skills = st.text_area("Enter your current skills (comma separated):", "Python, SQL")

if st.button("Generate Guidance"):
    with st.spinner("AI is generating your personalized roadmap..."):
        prompt = f"""
        I want to become a {career_goal}.
        My current skills are: {skills}.
        
        Please do the following:
        1. Suggest missing skills (gap analysis).
        2. Create a 3-step learning roadmap with recommended resources.
        3. Generate 2 sample interview questions with short answers.
        """

        try:
            response = model.generate_content(prompt)
            st.subheader("📌 Personalized Career Guidance")
            st.write(response.text)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

st.markdown("---")
st.caption("Prototype built for GenAI Hackathon ✨")
