import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

# Load the analyzed data
data = pd.read_csv('ms_data_analyzed.csv')

# Convert data types
data['visit_date'] = pd.to_datetime(data['visit_date'])
data['patient_id'] = data['patient_id'].astype(str)
data['education_level'] = data['education_level'].astype('category')
print(data.dtypes)

# Check for missing values
print("missing value:")
print(data.isnull().sum())


# Ensure 'walking_speed' is numeric
print(data['walking_speed'].head())

# If necessary, convert 'walking_speed' to numeric
data['walking_speed'] = pd.to_numeric(data['walking_speed'], errors='coerce')


# Multiple regression for walking speed
model = smf.ols('walking_speed ~ age + education_level', data=data).fit()
print(model.summary())

model = smf.ols('walking_speed ~ age + education_level + insurance_type', data=data).fit()
print(model.summary())

# T-test for cost by insurance type
insurance_types = data['insurance_type'].unique()
group1 = data[data['insurance_type'] == insurance_types[0]]['visit_cost']
group2 = data[data['insurance_type'] == insurance_types[1]]['visit_cost']
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"T-statistic: {t_stat}, P-value: {p_value}")

import seaborn as sns
import matplotlib.pyplot as plt

# Box plot of visit costs by insurance type
plt.figure(figsize=(10, 6))
sns.boxplot(x='insurance_type', y='visit_cost', data=data)
plt.title('Visit Costs by Insurance Type')
plt.xlabel('Insurance Type')
plt.ylabel('Visit Cost ($)')
plt.show()
