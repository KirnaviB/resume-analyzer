import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_resume_vs_jd(resume_text, job_description):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are an AI Resume Screening Agent.

Compare the RESUME with the JOB DESCRIPTION and provide output in this format:

Match Percentage: XX%

Matching Skills:
- skill1
- skill2

Missing Skills:
- skill1
- skill2

Strengths:
- point1
- point2

Suggestions:
- suggestion1
- suggestion2

Final Verdict:
(Fit / Needs Improvement / Not Suitable)

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
