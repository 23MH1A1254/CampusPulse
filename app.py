import streamlit as st
import pandas as pd
from src.model import get_trained_model, FEATURES
from src.recommendations import build_recommendations

st.set_page_config(page_title="CampusPulse", page_icon="🎓", layout="wide")
st.title("🎓 CampusPulse")
st.caption("AI-Based Student Placement Readiness & Skill Gap Analyzer")
st.info("This educational demo uses a synthetic sample dataset. Its predictions are not real hiring decisions.")

@st.cache_resource
def load_model():
    return get_trained_model()

model, metrics = load_model()

with st.sidebar:
    st.header("Student Profile")
    coding = st.slider("Coding score", 0, 100, 65)
    aptitude = st.slider("Aptitude score", 0, 100, 60)
    communication = st.slider("Communication score", 0, 100, 65)
    cgpa = st.slider("CGPA", 0.0, 10.0, 7.0, 0.1)
    projects = st.number_input("Completed projects", 0, 20, 2)
    internships = st.number_input("Internships", 0, 10, 0)
    certifications = st.number_input("Certifications", 0, 20, 2)
    hackathons = st.number_input("Hackathons participated", 0, 20, 0)

student = pd.DataFrame([{
    "coding_score": coding,
    "aptitude_score": aptitude,
    "communication_score": communication,
    "cgpa": cgpa,
    "projects": projects,
    "internships": internships,
    "certifications": certifications,
    "hackathons": hackathons
}])[FEATURES]

prediction = int(model.predict(student)[0])
probability = float(model.predict_proba(student)[0][1])

left, middle, right = st.columns(3)
left.metric("Placement readiness", "Ready" if prediction else "Needs improvement")
middle.metric("Model-estimated readiness probability", f"{probability:.1%}")
right.metric("Training accuracy", f"{metrics['accuracy']:.1%}")

st.subheader("Your skill profile")
chart_data = pd.DataFrame({
    "Skill": ["Coding", "Aptitude", "Communication"],
    "Score": [coding, aptitude, communication]
}).set_index("Skill")
st.bar_chart(chart_data, y="Score", y_label="Score out of 100")

st.subheader("Personalized improvement plan")
for item in build_recommendations(coding, aptitude, communication, cgpa,
                                  projects, internships, certifications, hackathons):
    st.write(f"• {item}")

with st.expander("About the ML model"):
    st.write(
        "CampusPulse trains a Random Forest classifier on the included synthetic CSV. "
        "The displayed probability is a model estimate, not a guarantee of placement."
    )
    st.json(metrics)

st.caption("Built for learning and portfolio demonstration. Do not use this tool to make consequential decisions.")
