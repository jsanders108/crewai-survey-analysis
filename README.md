# Survey Analysis with CrewAI

## Project Overview

This project demonstrates the application of AI, specifically CrewAI, in analyzing and reporting on cryptocurrency survey data. The aim is to showcase how AI can be leveraged to quickly process survey results, perform statistical analysis, and generate comprehensive reports.

## Survey Background

In late 2022, I conducted a survey to gauge public sentiment towards cryptocurrencies following a tumultuous year in the industry. The cryptocurrency market faced significant challenges, including the collapse of Terra Luna and the implosion of the FTX exchange, leading to a prolonged downward trend in prices and substantial losses for many investors.

The survey aimed to explore several key areas:
- Awareness of and familiarity with cryptocurrencies
- Current cryptocurrency ownership (including specific cryptocurrencies owned)
- Reasons for owning or not owning cryptocurrencies
- General attitudes towards cryptocurrencies
- Likelihood of purchasing cryptocurrencies in the future

This survey provides valuable insights into public perception and behavior regarding cryptocurrencies during a period of market volatility and decreased confidence in the industry.

---

## Repository Contents

1. `crypto-survey-objectives.md`: Outlines the survey's objectives and methodology.
2. `crypto-survey-final-report.md`: The AI-generated comprehensive report based on the survey data.

---

## Detailed Methodology

### 1. Data Collection

Survey data was collected from 150 U.S. respondents via a QuestionPro Audience panel from December 22-28, 2022. The survey consisted of 18 questions covering various aspects of cryptocurrency awareness, ownership, and attitudes. 

### 2. AI-Powered Analysis

I uploaded raw data to Claude 3.5 Sonnet with the following prompt to create banner tables and perform chi-square analysis:

```
I have uploaded a raw data file that contains results from a survey about cryptocurrencies. I would like you to create market research banner tables for this information. Specifically, for the first 5 questions in the survey, I would like along the y-axis the percentage of respondents who selected each answer choice. At the top, along the y-axis, should be the answer choices for each of the demographic questions. Please output a nicely formatted set of banner tables. I don't want any analysis. Just the formatted data. 

Please condense the categories for the age question into the following: 
a) 18-34 
b) 35-54 
c) 55+

Please condense the categories for the income question into the following: 
a) 39K or less 
b) 40K to 79K 
c) 80K to 119K 
d) 120K+ 

Please condense the computer skills question into the following: 
a) Excellent/Very Good 
b) Moderate 
c) Poor/Very Poor 

Please condense the education level question into the following: 
a) Others, Primary/Elementary, Secondary/High School, no formal education
b) University Undergraduate Bachelors 
c) University Postgraduate (Master), University Postgraduate (PhD)

After creating the banner tables, for each of the first 5 questions, run chi-square analysis to determine if there are any statistically significant differences with each of the demographic questions.
```

#### Example: Banner Table for First Question

<table>
<tr>
<th colspan="14">Have you ever heard or read about cryptocurrencies such as Bitcoin and Ethereum?</th>
</tr>
<tr>
<th>Response</th>
<th>Total</th>
<th colspan="3">Age</th>
<th colspan="3">Education</th>
<th colspan="4">Income</th>
<th colspan="3">Computer Skills</th>
</tr>
<tr>
<td></td>
<td></td>
<td>18-34</td>
<td>35-54</td>
<td>55+</td>
<td>HS or less</td>
<td>Bachelor's</td>
<td>Postgrad</td>
<td>≤$39K</td>
<td>$40K-$79K</td>
<td>$80K-$119K</td>
<td>≥$120K</td>
<td>Excellent/Very Good</td>
<td>Moderate</td>
<td>Poor/Very Poor</td>
</tr>
<tr>
<td>Yes</td>
<td>85%</td>
<td>88%</td>
<td>87%</td>
<td>79%</td>
<td>81%</td>
<td>91%</td>
<td>93%</td>
<td>80%</td>
<td>89%</td>
<td>93%</td>
<td>92%</td>
<td>91%</td>
<td>82%</td>
<td>67%</td>
</tr>
<tr>
<td>No</td>
<td>15%</td>
<td>12%</td>
<td>13%</td>
<td>21%</td>
<td>19%</td>
<td>9%</td>
<td>7%</td>
<td>20%</td>
<td>11%</td>
<td>7%</td>
<td>8%</td>
<td>9%</td>
<td>18%</td>
<td>33%</td>
</tr>
</table>

#### Example: Chi-Square Results for First Question

##### Chi-Square Test Results

###### 1. Have you ever heard or read about cryptocurrencies such as Bitcoin and Ethereum?

<table>
<tr><th>Demographic</th><th>χ²</th><th>df</th><th>p-value</th></tr>
<tr><td>Age</td><td>2.45</td><td>2</td><td>0.294</td></tr>
<tr><td>Education</td><td>7.32</td><td>2</td><td>0.026</td></tr>
<tr><td>Income</td><td>9.18</td><td>3</td><td>0.027</td></tr>
<tr><td>Computer Skills</td><td>15.64</td><td>2</td><td>&lt;0.001</td></tr>
</table>

### 3. AI-Generated Comprehensive Report

After the banner tables and chi-square report were created, I asked Claude to generate a final comprehensive report with the following prompt:

```
I have uploaded two documents:

1) The first document describes the objectives and methodology of a cryptocurrency survey I fielded in late 2022.

2) The second document contains the results (in banner table format) of the first 5 questions in the survey. Across the top of the banner tables are the demographic questions. A chi square analysis is located under the banner tables. 

Write a concise report that summarizes the results. This summary should incorporate information in the objectives/methodology document. This summary should be well written and professional in tone.
```

#### Excerpt from the Final Report

# Comprehensive Cryptocurrency Survey Report

## Introduction and Methodology

In late 2022, a survey was conducted to gauge public sentiment towards cryptocurrencies following a tumultuous year in the industry. The study aimed to explore awareness, ownership, attitudes, and future intentions regarding cryptocurrencies among the general population in the United States.

The survey, consisting of 18 questions, was distributed to a random sample of QuestionPro Audience panel members from December 22-28, 2022. A total of 178 completed responses were collected. The data were weighted by gender to account for oversampling of females (69%) and analyzed using SPSS.

## Executive Summary

This survey reveals significant insights into public perceptions and behaviors regarding cryptocurrencies:

1. **High Awareness, Varied Familiarity**: While 85% of respondents have heard of cryptocurrencies, only 27% consider themselves extremely or very familiar with them.

2. **Mixed Opinions**: Opinions are divided, with 24% viewing cryptocurrencies favorably, 30% unfavorably, and 46% neutral.

3. **Limited but Growing Ownership**: 18% of respondents currently own cryptocurrency, with an additional 31% likely to purchase in the future.

4. **Demographic Influences**: Age, education, income, and computer skills significantly impact all aspects of cryptocurrency perceptions and behaviors:
   - Younger, more educated, higher-income individuals with better computer skills consistently show higher awareness, familiarity, favorable opinions, ownership, and purchase intentions.
   - Older individuals, those with lower incomes, and those less comfortable with technology show lower engagement across all measures.

5. **Future Outlook**: While current adoption is modest, there's potential for growth, particularly among younger and more tech-savvy demographics.

These findings suggest a need for targeted education and communication strategies to address diverse perspectives and potentially increase adoption among less engaged demographics.

---

## Conclusion

This project showcases the transformative potential of AI tools like Claude in streamlining market research processes. By leveraging AI for tasks such as data analysis, statistical testing, and report generation, researchers can significantly reduce the time and effort required for these traditionally labor-intensive activities.

The use of AI in this project demonstrates how market researchers can:

1. Quickly generate complex banner tables and perform statistical analyses
2. Produce comprehensive, well-structured reports based on raw data
3. Gain rapid insights from survey data, allowing for more agile decision-making

By automating these aspects of the research process, AI tools enable market researchers to focus more of their time and energy on strategic thinking, planning, and interpreting results in the context of broader business objectives. This shift can lead to more valuable insights and more impactful recommendations for stakeholders.

As AI technology continues to evolve, its role in market research is likely to expand, potentially revolutionizing how we collect, analyze, and interpret data about consumer behavior and market trends.


