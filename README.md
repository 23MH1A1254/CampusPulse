# CampusPulse – AI-Based Student Placement Readiness & Skill Gap Analyzer

CampusPulse is an educational machine-learning project that estimates a student's placement-readiness category from academic, technical and experience-related inputs. It also produces a simple improvement plan.

## Features
- Random Forest classification model using scikit-learn
- Interactive Streamlit dashboard
- Student profile inputs: coding, aptitude, communication, CGPA, projects, internships, certifications and hackathons
- Model-estimated probability and evaluation metrics
- Rule-based skill-gap recommendations
- Included sample CSV dataset
- Reproducible training script

## Project structure
```text
CampusPulse/
├── app.py
├── train.py
├── requirements.txt
├── README.md
├── data/
│   └── placement_readiness.csv
├── src/
│   ├── __init__.py
│   ├── model.py
│   └── recommendations.py
└── tests/
    └── test_recommendations.py
```

## Setup (Windows PowerShell)
```powershell
cd CampusPulse
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Train and evaluate
```powershell
python train.py
```

## Run the dashboard
```powershell
streamlit run app.py
```
Open the local URL printed by Streamlit, usually `http://localhost:8501`.

## Dataset and important limitation
The included dataset is **synthetic and generated for demonstration**. Its labels are based on a simulated scoring rule with noise; it is not collected from students, colleges or employers. Therefore, model metrics only measure performance against this artificial dataset. They do not demonstrate real-world hiring accuracy or fairness.

For a serious research project, replace the sample CSV with an ethically collected, consent-based, anonymized dataset; document its source and label definition; check class balance and subgroup performance; and validate on data from a separate institution or time period.

## Responsible use
CampusPulse is a learning and portfolio prototype. It must not be used to reject, rank or make consequential decisions about real students. A placement outcome depends on many factors not represented here, and the model can be wrong.

## Tech stack
Python · Pandas · NumPy · scikit-learn · Streamlit
