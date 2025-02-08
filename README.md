# Survey Analysis with CrewAI

## Project Overview

This project demonstrates how CrewAI can be used to automate the analysis of cryptocurrency survey data and generate a comprehensive market research report. By leveraging a multi-agent framework, the system processes raw survey responses, performs statistical analyses, and delivers actionable insights.

## Survey Background

In late 2022, a survey was conducted to understand public sentiment towards cryptocurrencies in the wake of industry challenges such as the Terra Luna collapse and the FTX implosion. Key survey areas included:

- **Awareness & Familiarity:** How well respondents know about cryptocurrencies.
- **Ownership Trends:** Current and past ownership of digital assets.
- **Opinions & Future Intentions:** Attitudes and likelihood of purchasing cryptocurrencies.
- **Demographics:** Age, education, gender, income, and computer skills.

A total of 150 U.S. respondents were surveyed via a QuestionPro Audience panel.

## Methodology & AI Workflow

### **Data Processing**
The survey data was processed using Python scripts, which generated:
- Data tables summarizing response distributions.
- Frequency tables for categorical variables.
- Chi-square statistical tests to identify significant relationships.

These processed results were then passed to AI agents for analysis.

### **CrewAI Analysis Workflow**
This project utilized a structured **two-agent review process** to ensure high-quality insights:

1. **Expert Market Research Analyst**  
   - Analyzed the processed survey data, identified key findings, and drafted a structured market research report.  
   
2. **Expert Market Research Reviewer**  
   - Reviewed the report to ensure clarity, logical flow, and accuracy.
   - Verified statistical interpretations and improved actionable insights.

### **Language Model**
The analysis and report generation were powered by **GPT-o3-mini**, which enabled the AI agents to efficiently interpret data, generate meaningful insights, and refine findings.

## Repository Structure

- **Documentation:**
  - `crypto-survey-objectives.md`: Survey objectives and methodology.
  - `crypto-survey-final-report.md`: The final AI-generated report.

- **Configuration Files:**
  - `config/agents.yaml`: Defines the two AI agents and their roles.
  - `config/tasks.yaml`: Outlines tasks such as data analysis and report review.

- **Source Code:**
  - `crew.py`: Assembles the CrewAI agents and tasks into a sequential workflow.
  - `main.py`: The entry point that loads survey data, processes it, and generates the final report.

## Implementation Summary

CrewAI’s modular "flows" framework drove this project through several steps:

1. **Agent & Task Configuration:**
   - **Agents** were defined with clear roles in `agents.yaml`.
   - **Tasks** in `tasks.yaml` guided the agents to:
     - Analyze processed survey results (frequency tables, cross-tabulations, chi-square tests).
     - Generate a structured report covering an executive summary, methodology, findings, and recommendations.

2. **Crew Assembly and Execution:**
   - The agents and tasks were integrated in `crew.py` to form a crew that operated sequentially.
   - The process was initiated in `main.py`, which read the CSV survey data, processed it, and kicked off the CrewAI workflow.

## Report Highlights

### **High Awareness but Limited Familiarity**
Over 83% of respondents are aware of cryptocurrencies, yet nearly 59% report being "Not at all" or "Slightly familiar."

### **Digital Literacy’s Impact**
Significant statistical associations (e.g., awareness vs. computer skills, χ² = 44.48, p < 0.001) underline the role of digital competence in understanding cryptocurrencies.

### **Demographic Influences**
Variations in familiarity and ownership trends are linked to education, income, and gender.

### **Actionable Recommendations**
Suggested initiatives include:

- Targeted educational campaigns to increase familiarity.
- Segmented marketing strategies tailored to different demographic groups.
- Enhanced digital literacy programs to improve understanding and adoption of cryptocurrencies.

For complete details, see the full report in `crypto-survey-final-report.md`.

## Conclusion

This project illustrates how CrewAI can automate and enhance qualitative data analysis, turning raw survey responses into insightful, actionable reports. The structured two-agent review process ensures high-quality outputs, making this approach ideal for research applications requiring accuracy and professional presentation.

By combining:

- **Python-based statistical analysis**,  
- **CrewAI multi-agent workflows**, and  
- **GPT-o3-mini for report generation**,  

this system delivers a scalable, efficient solution for transforming raw survey data into strategic business intelligence.



