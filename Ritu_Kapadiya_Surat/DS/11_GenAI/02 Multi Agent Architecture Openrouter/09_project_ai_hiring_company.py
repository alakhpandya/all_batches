# Project: AI Hiring Company

"""
Create an AI recruitment company.

Create agents:
- Resume Analyser
- Skill Evaluator
- HR Reviewer

Workflow:
- Resume Analyzer => Skill Evaluator => HR Reviewer

User will provide:
- Text of the resume of the candidate

AI System will do:
- Evaluate skills
- Evaluate candidate also
- Identify strengths and weaknesses
- Generate hiring recommendation

**Concepts to be implimented**
1. Multi-stage AI evaluation pipeline
	- Flow: Raw Resume => Analysis => Skill Evaluation => HR Decision

2. "Division of Labor" / Specialized Agents
Make each agent:
	- having responsiblity as narrow as possible
	- focussed deeply
	- improves workflow quality

3. Sequential Context Sharing
	- Use CrewAI to automatically pass extracted information, evaluation context and previous outputs between agents

4. Business AI Systems/AI workflow automation
**Testing of your workflow**

Observe the final output (Rejection/Acceptance) by the system by providing:
- weak resume with fewer skills and no projects
- resumes for different job roles like Data Scientist, Frontend Developer, AI Engineer, Data Analysts etc


**Future Upgrade**
- Add ATS scoring agent that checks ATS Compatibility
- Add an Interview Question Generator agent for technical round based on the resume


**Importance of AI Supervision**
- Figure out and make a note of the limitations of your AI System.
"""