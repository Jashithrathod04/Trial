import streamlit as st
import google.generativeai as genai
import pandas as pd

# -------------------------------
# Page Setup
# -------------------------------
st.set_page_config(page_title="CoachBot AI", page_icon="🏋️‍♂️")
st.title("🏋️‍♂️ CoachBot AI - Smart Fitness Assistant")
st.markdown("AI-powered personalized training for young athletes.")

# -------------------------------
# API Configuration
# -------------------------------
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("API Key not found. Add GOOGLE_API_KEY in Streamlit Secrets.")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("models/gemini-1.5-pro")

# -------------------------------
# User Input Section
# -------------------------------
st.header("📝 Athlete Profile")

sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics"])
position = st.text_input("Player Position")
injury = st.text_area("Injury History / Risk Areas", placeholder="None if healthy")
intensity = st.selectbox("Training Intensity", ["Low", "Moderate", "High"])
diet = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan"])
goal = st.text_input("Desired Goal")

# -------------------------------
# Prompt Builder
# -------------------------------
def base_prompt(task):
    return f"""
    You are a certified youth sports coach.

    Athlete Details:
    Sport: {sport}
    Position: {position}
    Injury History: {injury}
    Intensity Level: {intensity}
    Diet Preference: {diet}
    Goal: {goal}

    Guidelines:
    - Prioritize safety.
    - Avoid exercises that worsen injury.
    - Suggest low-resource and home-based alternatives.
    - Keep tone motivating and youth-friendly.
    - Be clear and structured.

    Task:
    {task}
    """

# -------------------------------
# Feature Buttons (10 Required)
# -------------------------------

features = {
    "🏋️ Full Workout Plan": "Generate a full-body workout plan.",
    "🩹 Injury Recovery Plan": "Create a safe recovery training schedule.",
    "🔥 Warm-Up & Cooldown": "Generate personalized warm-up and cooldown routine.",
    "🎯 Tactical Coaching Tips": "Provide tactical skill improvement tips.",
    "🥗 Weekly Nutrition Plan": "Create a 7-day nutrition guide.",
    "💧 Hydration Strategy": "Provide hydration and electrolyte guidance.",
    "🧠 Mental Focus Routine": "Provide tournament mental preparation tips.",
    "📅 Match-Day Plan": "Create match-day preparation checklist.",
    "🧘 Mobility Routine": "Generate mobility and flexibility exercises.",
    "🏠 Low-Resource Training": "Create a no-equipment home workout plan."
}

selected_feature = st.selectbox("Select Coaching Feature", list(features.keys()))

# -------------------------------
# Generate Button
# -------------------------------

if st.button("🚀 Generate Plan"):
    if not position or not goal:
        st.warning("Please complete all required fields.")
    else:
        with st.spinner("Generating personalized coaching advice..."):
            try:
                temperature = 0.3 if "Workout" in selected_feature or "Recovery" in selected_feature else 0.8
                
                response = model.generate_content(
                    base_prompt(features[selected_feature]),
                    generation_config=genai.types.GenerationConfig(
                        temperature=temperature
                    )
                )

                st.success("✅ AI Coaching Output")
                st.markdown(response.text)

            except Exception as e:
                st.error("Error generating response.")
                st.write(e)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("⚠️ For educational purposes. Consult professional coach or doctor for medical advice.")
















streamlit
google-generativeai
pandas
