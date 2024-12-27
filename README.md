# Predicting-Employee-Attrition-Using-HR-Analytics

# Predicting-Employee-Attrition-Using-HR-Analytics

## Overview
This project leverages machine learning and HR analytics to predict employee attrition, enabling organizations to identify key risk factors and take proactive measures to retain valuable talent. Using advanced data preprocessing and modeling techniques, the project demonstrates how predictive analytics can drive better workforce management decisions.

## Features
- **Data Preprocessing:** Handled missing values, scaled features, and applied one-hot encoding for categorical variables.
- **Feature Selection:** Employed Recursive Feature Elimination (RFE), Lasso regression, and PCA to identify the most impactful predictors of attrition.
- **Machine Learning Models:** Developed and fine-tuned models including Random Forest Classifier and XGBoost to achieve high prediction accuracy.
- **Evaluation Metrics:** Assessed models using ROC-AUC, F1-score, and accuracy to ensure robust performance.
- **Actionable Insights:** Provided insights into key factors influencing employee attrition, aiding in strategic HR decision-making.

## Dataset
The dataset includes employee demographics, job roles, satisfaction levels, performance ratings, and other HR-related attributes. It is structured with the following key columns:
- **EmployeeID**: Unique identifier for each employee.
- **JobRole**: Current role of the employee.
- **MonthlyIncome**: Salary details.
- **JobSatisfaction**: Employee's satisfaction level with the job.
- **Attrition**: Target variable indicating whether the employee left the organization.

## Tools and Technologies
- **Programming Languages:** Python
- **Libraries and Frameworks:** Pandas, NumPy, Scikit-learn, XGBoost
- **Visualization:** Matplotlib, Seaborn
- **Development Environment:** Jupyter Notebook

## Key Steps
1. **Data Preprocessing:**
   - Checked for missing values and handled them appropriately.
   - Standardized numerical features and encoded categorical variables.
2. **Exploratory Data Analysis (EDA):**
   - Identified patterns and relationships using correlation heatmaps and visualizations.
   - Highlighted key predictors of employee attrition.
3. **Feature Engineering:**
   - Applied feature selection methods like RFE and Lasso regression to reduce dimensionality.
   - Used PCA to further enhance model performance.
4. **Model Development:**
   - Trained multiple classification models, including Random Forest and XGBoost.
   - Optimized hyperparameters using GridSearchCV.
5. **Model Evaluation:**
   - Evaluated models on test data using ROC-AUC, F1-score, precision, and recall.
6. **Insights and Recommendations:**
   - Identified top factors contributing to attrition, such as job satisfaction and income.
   - Provided actionable recommendations to reduce attrition rates.

## Results
- Achieved **88% accuracy** using the Random Forest Classifier.
- The XGBoost model demonstrated high precision with an F1-score of **0.84**.
- Highlighted actionable insights for HR teams, focusing on improving job satisfaction and addressing salary disparities.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Predicting-Employee-Attrition-Using-HR-Analytics.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Predicting-Employee-Attrition-Using-HR-Analytics
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Jupyter Notebook to explore the analysis and models.

## Future Work
- Incorporate additional data sources for improved prediction accuracy.
- Explore deep learning models for enhanced performance.
- Develop an interactive dashboard for real-time attrition monitoring.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any queries or suggestions, feel free to reach out:
- **Email:** DivyaKodanganti@my.unt.edu
- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)
- **GitHub:** [Your GitHub Profile](https://github.com/yourusername)
