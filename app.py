from analyzer import analyze_resume_vs_jd

resume_text = """
Name: Kirnavi Bhavsar
Skills: Python, Networking, Cybersecurity basics, Git
Experience: AI Intern (Beginner)
"""

job_description = """
We are looking for an AI Intern with:
- Strong Python skills
- Basic Machine Learning knowledge
- Experience with APIs
- Understanding of Git and Linux
"""

if __name__ == "__main__":
    print("===== AI RESUME vs JOB DESCRIPTION ANALYSIS =====\n")
    result = analyze_resume_vs_jd(resume_text, job_description)
    print(result)
