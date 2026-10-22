# Health_care_analysis
# Healthcare Analytics for Doctor Visits

## Project Overview
Healthcare Analytics for Doctor Visits is a data analysis project that explores patterns in doctor visits using healthcare data. It examines how doctor visits relate to demographic characteristics, health conditions, income, illness, chronic conditions, and healthcare support.

## Problem Statement
Understanding the factors associated with doctor visits can help identify patterns in healthcare utilization and support data-driven analysis.

## Objectives
- Analyze the distribution of doctor visits.
- Explore doctor visits across different age groups and genders.
- Study associations between doctor visits, income, illness, and health conditions.
- Examine the relationship between healthcare support and doctor visits.
- Present findings through an interactive dashboard.

## Dataset
The dataset contains **5,190 records and 13 columns**, including:
- Gender and age
- Income and illness
- Number of doctor visits
- Health status and reduced activity
- Chronic conditions
- Private and public healthcare support indicators

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

## How to Run the Project Locally

1. Clone this repository.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit dashboard:

   ```bash
   streamlit run app.py
   ```

## Dashboard Features
- Interactive gender and age filters
- Summary metrics for doctor visits
- Doctor visit distribution chart
- Comparisons by gender and age group
- Analysis of health and healthcare support indicators
- Dataset preview and filtered CSV download

## Conclusion
This project uses healthcare data visualization and exploratory analysis to understand patterns associated with doctor visits. The results show associations in the dataset and do not establish causation or provide medical diagnoses.
