def build_recommendations(coding, aptitude, communication, cgpa,
                          projects, internships, certifications, hackathons):
    tips = []
    if coding < 70:
        tips.append("Practice one coding problem daily and revise data structures and algorithms.")
    if aptitude < 70:
        tips.append("Spend 20–30 minutes daily on quantitative aptitude, logical reasoning and verbal practice.")
    if communication < 70:
        tips.append("Practice explaining one technical topic aloud and participate in mock interviews.")
    if cgpa < 7.0:
        tips.append("Create a semester study plan and focus on improving core-subject fundamentals.")
    if projects < 2:
        tips.append("Build at least two complete projects and publish clear READMEs with screenshots.")
    if internships < 1:
        tips.append("Look for internships, virtual work experience or supervised real-world projects.")
    if certifications < 2:
        tips.append("Choose one relevant certification and complete a hands-on portfolio project alongside it.")
    if hackathons < 1:
        tips.append("Try a college hackathon or team coding event to gain collaboration experience.")
    if not tips:
        tips.append("Good profile balance. Keep practicing interviews and update your portfolio regularly.")
    return tips
