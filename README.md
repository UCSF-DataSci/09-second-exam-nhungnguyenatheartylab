# EXAM 2

## QUESTION 1: Data Preparation with Command-Line Tools 

### 1. Check the generated data:
     'cat ms_data_dirty.csv'

# The order of columns: patient_id,visit_date,time,age,education_level,walking_speed,site,room,staff_id,form_version
    'cut -d',' -f1,2,4,5,6'

# 2. Make prepare.sh executable and run the script:
    'chmod +x prepare.sh'
    './prepare.sh'

### 3. Create a list of insurance type
    'cat insurance.lst'
insurance_type
Basic
Premium
Platinum
### 4. Generate a summary of the processed data:
   'wc -l ms_data.csv | awk '{print $1-1}'  # a total of  15502rows
   'head -n 5 ms_data.csv'

patient_id,visit_date,age,education_level,walking_speed,insurance_type,visit_cost
P0001,2020-03-10,72.45,Some College,3.53,Premium,204.46700179329434
P0001,2020-05-24,72.65,Some College,2.91,Premium,198.81889907387216
P0001,2020-08-07,72.86,Some College,3.25,Premium,181.78565574135166
P0001,2020-11-06,73.11,Some College,3.01,Premium,212.14182918510895


## QUESTION 2: Data Analysis with Python
### 1. Load the data
    'column_names = ['patient_id', 'visit_date', 'age', 'education_level', 'walking_speed']'
    'data = pd.read_csv("ms_data.csv", names=column_names)'

#### Convert 'visit_date' to datetime format and sort the data
    'data['visit_date'] = pd.to_datetime(data['visit_date'])'
    'data = data.sort_values(by=['patient_id', 'visit_date'])'

#### Check the sorted dataset:
    'print(data.head())'

patient_id visit_date    age education_level  walking_speed
0      P0001 2020-03-10  72.45    Some College           3.53
1      P0001 2020-05-24  72.65    Some College           2.91
2      P0001 2020-08-07  72.86    Some College           3.25
3      P0001 2020-11-06  73.11    Some College           3.01
4      P0001 2021-01-23  73.32    Some College           3.06

### 2. Calculate basic costs for insurance types:
 patient_id visit_date    age education_level  walking_speed insurance_type  visit_cost
0      P0001 2020-03-10  72.45    Some College           3.53        Premium  204.467002
1      P0001 2020-05-24  72.65    Some College           2.91        Premium  198.818899
2      P0001 2020-08-07  72.86    Some College           3.25        Premium  181.785656
3      P0001 2020-11-06  73.11    Some College           3.01        Premium  212.141829
4      P0001 2021-01-23  73.32    Some College           3.06        Premium  185.775141

### 3. Calculate summary statistics:
   Mean walking speed by education level:
Bachelors       4.079708
Graduate        4.486748
High School     3.267000
Some College    3.696761

Mean costs by insurance type:
Basic             100.202799
Platinum          299.862845
Premium           199.704661
insurance_type    100.040694

Mean walking speed by age group:
[20, 30)    4.702142
[30, 40)    4.305305
[40, 50)    4.024156
[50, 60)    3.740355
[60, 70)    3.468374
[70, 80)    3.169570

## QUESTION 3: Statistical Analysis
# Model walking speed by age and education 
   Mixed Linear Model Regression Results
============================================================================
Model:                   MixedLM      Dependent Variable:      walking_speed
No. Observations:        15414        Method:                  REML         
No. Groups:              1000         Scale:                   0.1149       
Min. group size:         11           Log-Likelihood:          -5327.7021   
Max. group size:         18           Converged:               No           
Mean group size:         15.4                                               
----------------------------------------------------------------------------
                                Coef.  Std.Err.    z     P>|z| [0.025 0.975]
----------------------------------------------------------------------------
Intercept                        5.611    0.011  511.992 0.000  5.589  5.632
education_level[T.Graduate]      0.406    0.009   46.253 0.000  0.388  0.423
education_level[T.High School]  -0.798    0.009  -90.735 0.000 -0.815 -0.780
education_level[T.Some College] -0.402    0.009  -47.023 0.000 -0.418 -0.385
age                             -0.030    0.000 -173.349 0.000 -0.031 -0.030
Group Var                        0.002    0.002                             

# Model visit cost by insurance
============================================================================

                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:             visit_cost   R-squared (uncentered):                   0.918
Model:                            OLS   Adj. R-squared (uncentered):              0.918
Method:                 Least Squares   F-statistic:                          8.682e+04
Date:                Wed, 20 Nov 2024   Prob (F-statistic):                        0.00
Time:                        16:39:59   Log-Likelihood:                         -85029.
No. Observations:               15414   AIC:                                  1.701e+05
Df Residuals:                   15412   BIC:                                  1.701e+05
Df Model:                           2                                                  
Covariance Type:            nonrobust                                                  
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Platinum     299.9332      0.892    336.111      0.000     298.184     301.682
Premium      200.1428      0.813    246.325      0.000     198.550     201.735
==============================================================================
Omnibus:                   120581.821   Durbin-Watson:                   0.156
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             2187.926
Skew:                           0.583   Prob(JB):                         0.00
Kurtosis:                       1.569   Cond. No.                         1.10
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.

## QUESTION 4: Data Visualization
# Graphs are shown in visualize.ipynb