Healthcare Data Analysis Project: Comprehensive Summary

Project Overview

The goal of this project was to explore, analyze, and extract meaningful insights from real-world healthcare datasets using various machine learning and data science techniques. We focused on three datasets:
1.	Diabetes Dataset : Electronic health records of diabetic patients.
2.	Health Insurance Dataset : Information about insurance charges and patient demographics.
3.	Heart Disease Dataset : Cardiology-focused patient data including diagnosis and risk factors.

Objectives

•	Predictive Modeling: Classify whether a patient would be readmitted to the hospital.
•	Unsupervised Learning: Group patients into clusters based on similarity in health or financial profiles.
•	Time Series Analysis: Identify trends in hospital visits and medications over time.
•	Natural Language Processing (NLP): Analyze textual data like diagnosis codes or medical specialties to uncover patterns or dominant topics.

1. Diabetes Dataset :Classification
   
 Purpose:
 
To predict patient readmission using structured health record features (e.g., number of medications, diagnoses, procedures).

Steps:

•	Preprocessed and cleaned the data (handled missing values, encoded categorical features).
•	Created two targets:
o	Multiclass target: <30, >30, NO for readmission.
o	Binary target: 1 = readmitted (<30 or >30), 0 = not readmitted (NO).
•	Addressed class imbalance using SMOTE (Synthetic Minority Oversampling).
•	Trained a Random Forest Classifier.
•	Evaluated with accuracy, precision, recall, F1-score, and ROC-AUC.

Findings:

•	The model achieved 67% accuracy.
•	Readmissions are challenging to predict, but features like number of inpatient visits, medications, and length of hospital stay were strong indicators.

 3. Health Insurance Dataset : Clustering

Purpose:

To identify patient groups based on demographics, lifestyle, and healthcare costs.

Steps:

•	Encoded categorical variables (e.g., sex, smoking status, region).
•	Removed the target column (charges) for unsupervised learning.
•	Standardized features and applied KMeans Clustering.
•	Visualized using PCA (Principal Component Analysis) to reduce dimensionality to 2D.

Findings:

•	Formed 3 distinct clusters:
o	Cluster 1: Generally healthier, non-smokers, lower costs.
o	Cluster 2: Smokers with higher insurance charges.
o	Cluster 3: Possibly older patients or those with more children and moderate costs.
•	Useful for insurance pricing strategies or targeted health programs.

 5. Time Series Trends : Diabetes Dataset
    
Purpose:

To analyze longitudinal behavior of patients—how medication usage, hospital time, and readmissions change over multiple visits.

Steps:
•	Created a visit count per patient using patient_nbr.
•	Binned patients into cohorts (Low, Medium) based on number of visits.
•	Aggregated average num_medications, time_in_hospital, and readmitted_flag.

Findings:

•	Patients with more visits tended to have slightly higher medication usage and higher readmission rates.
•	Time in hospital remained fairly consistent, implying treatment plans are standardized.

7. Natural Language Processing (NLP) : Diabetes Dataset
   
 Purpose:
 
To extract meaning from diagnosis codes and medical specialties, especially where structured data may miss nuances.

Steps:

•	Combined medical_specialty, diag_1, diag_2, diag_3 into one text column.
•	Cleaned text: removed punctuation, lowercased, removed stopwords.
•	Vectorized text using TF-IDF.
•	Applied Latent Dirichlet Allocation (LDA) for topic modeling.

 Findings:
 
•	LDA uncovered 3 major topics from diagnosis patterns, likely representing:
o	Endocrinology-related codes (diabetes, glucose disorders).
o	Cardiovascular-related codes (hypertension, heart failure).
o	General medicine or emergency care (injuries, infections).
•	These topics can help in clinical triage or patient routing.

 Final Learnings & Insights
 
Technique	Key Takeaway
Classification:	Predictive models can estimate readmission, but class imbalance matters.
Clustering:	Patient segmentation uncovers hidden groups for personalized care.
Time Series:	Visit trends reveal behavioral and treatment patterns.
Natural Language Processing (NLP):	Even numeric codes, when treated as text, reveal rich thematic clusters.

 Conclusion
 
This project showcases the power of end-to-end data science in healthcare, combining:

•	Structured machine learning
•	Unsupervised learning
•	Time-based cohort analysis
•	Natural language processing

Such work can help hospitals reduce readmission rates, insurers optimize pricing, and doctors better understand patient populations.

