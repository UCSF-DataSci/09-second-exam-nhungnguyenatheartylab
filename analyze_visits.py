import pandas as pd
import random
from datetime import datetime

# Load the data
column_names = ['patient_id', 'visit_date', 'age', 'education_level', 'walking_speed']
data = pd.read_csv("ms_data.csv", names=column_names)

# Convert 'visit_date' to datetime format
data['visit_date'] = pd.to_datetime(data['visit_date'])
data['patient_id'] = data['patient_id'].astype(str)
data['education_level'] = data['education_level'].astype('category')

# Sort the data by patient_id and visit_date
data = data.sort_values(by=['patient_id', 'visit_date'])
print(data.dtypes)

# Check for missing values
print("missing value:")
print(data.isnull().sum())

# Read insurance types from 'insurance.lst'
insurance_types = pd.read_csv('insurance.lst', header=None)[0].tolist()

# Assign insurance type consistently per patient_id
patient_insurance_map = {patient_id: random.choice(insurance_types) for patient_id in data['patient_id'].unique()}
data['insurance_type'] = data['patient_id'].map(patient_insurance_map)

# Define base costs for each insurance type
base_costs = {'Basic': 100, 'Premium': 200, 'Platinum': 300}

# Function to calculate visit cost based on insurance type with random variation
def calculate_visit_cost(insurance_type):
    base_cost = base_costs.get(insurance_type, 100)  # Default to 100 if not in base_costs
    variation = random.uniform(-20, 20)  # Random variation between -20 and 20
    return base_cost + variation

# Generate visit costs based on insurance type
data['visit_cost'] = data['insurance_type'].apply(calculate_visit_cost)

# Summary statistics
print("Mean walking speed by education level:")
print(data.groupby('education_level')['walking_speed'].mean())

print("Mean costs by insurance type:")
print(data.groupby('insurance_type')['visit_cost'].mean())

data['age_group'] = pd.cut(data['age'], bins=range(20, 90, 10), right=False)
mean_speed_by_age_group = data.groupby('age_group')['walking_speed'].mean()
print("Mean walking speed by age group:")
print(mean_speed_by_age_group)

# Save processed data for future use
data.to_csv('ms_data_analyzed.csv', index=False)