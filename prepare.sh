#!/bin/bash

# Step 1: Run the data generation script
python3 generate_dirty_data.py

# Step 2: Clean the data
grep -v '^#' ms_data_dirty.csv | sed '/^$/d' | sed 's/,,/,/g' | \
cut -d',' -f1,2,4,5,6 | awk -F',' '$5 >= 2.0 && $5 <= 8.0' > ms_data.csv

# Step 3: Create insurance type list
echo -e "insurance_type\nBasic\nPremium\nPlatinum" > insurance.lst

# Step 4: Summarize data
total_visits=$(tail -n +2 ms_data.csv | wc -l)
echo "Total number of visits (excluding header): $total_visits"
echo "First few records of the processed data:"
head -n 5 ms_data.csv
