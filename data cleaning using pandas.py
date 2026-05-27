# =========================================
# DATA CLEANING USING PANDAS
# =========================================

# Import required libraries
import pandas as pd
import numpy as np


# =========================================
# STEP 1: CREATE A MESSY DATASET
# =========================================

# Creating a deliberately dirty dataset
# Includes:
# - Missing values
# - Duplicate rows
# - Incorrect data types
# - Invalid entries

data = {
    'House_ID': [101, 102, 103, 104, 105, 102, 106, 107],
    'Price': [250000, 300000, np.nan, '400000', 350000, 300000, 500000, 'error'],
    'Bedrooms': [3, 4, 3, 5, np.nan, 4, 3, 2],
    'Area_SqFt': ['1500', '2000', 'Unknown', '2500', '2200', '2000', '3000', '1800'],
    'Location': ['Urban', 'Suburban', 'Urban', 'Rural', 'Urban', 'Suburban', None, 'Rural']
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display raw data
print("--- RAW DATA ---")
print(df)


# =========================================
# STEP 2: CHECK BASIC INFORMATION
# =========================================

print("\n--- DATAFRAME INFO ---")
print(df.info())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated())


# =========================================
# STEP 3: REMOVE DUPLICATES
# =========================================

# Remove duplicate rows
# Keep the first occurrence

df = df.drop_duplicates(subset=['House_ID'], keep='first')

print("\n--- AFTER REMOVING DUPLICATES ---")
print(df)


# =========================================
# STEP 4: HANDLE MISSING VALUES
# =========================================

# Fill missing values in Bedrooms column with median
median_bedrooms = df['Bedrooms'].median()
df['Bedrooms'] = df['Bedrooms'].fillna(median_bedrooms)

# Fill missing values in Location column with mode
mode_location = df['Location'].mode()[0]
df['Location'] = df['Location'].fillna(mode_location)

print("\n--- AFTER HANDLING MISSING VALUES ---")
print(df)


# =========================================
# STEP 5: FIX DATA TYPES
# =========================================

# Convert Price column to numeric
# Invalid entries become NaN

df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Convert Area_SqFt column to numeric
# Invalid values like 'Unknown' become NaN

df['Area_SqFt'] = pd.to_numeric(df['Area_SqFt'], errors='coerce')

print("\n--- AFTER DATA TYPE CONVERSION ---")
print(df)


# =========================================
# STEP 6: HANDLE NEW MISSING VALUES
# =========================================

# Fill missing values created during conversion

price_mean = df['Price'].mean()
df['Price'] = df['Price'].fillna(price_mean)

area_mean = df['Area_SqFt'].mean()
df['Area_SqFt'] = df['Area_SqFt'].fillna(area_mean)

print("\n--- AFTER FILLING NUMERIC MISSING VALUES ---")
print(df)


# =========================================
# STEP 7: FINAL CLEANED DATASET
# =========================================

print("\n--- FINAL CLEANED DATASET ---")
print(df)


# =========================================
# STEP 8: SAVE CLEANED DATA
# =========================================

# Save cleaned dataset to CSV file

df.to_csv('cleaned_housing_data.csv', index=False)

print("\nCleaned dataset saved successfully!")