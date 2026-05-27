import pandas as pd

def create_sample_dataset():

    raw_data = {
        'EmpID': [101, 102, 103, 104],
        'EmployeeName': ['Narasimha', 'Teja', 'Nikhil', 'Balu'],
        'Salary': [45000, 52000, 61000, 48000],
        'Department': ['HR', 'IT', 'Finance', 'Marketing'],
        'Experience': [2, 5, 7, 3],
        'PermanentEmployee': [True, True, False, True]
    }

    df = pd.DataFrame(raw_data)

    df['EmpID'] = df['EmpID'].astype('int64')
    df['EmployeeName'] = df['EmployeeName'].astype('object')
    df['Salary'] = df['Salary'].astype('int64')
    df['Department'] = df['Department'].astype('object')
    df['Experience'] = df['Experience'].astype('int64')
    df['PermanentEmployee'] = df['PermanentEmployee'].astype('bool')

    return df


def RES():

    print("-" * 80)
    print("PANDAS ASSIGNMENT: DataFrame.select_dtypes() Demonstration".center(80))
    print("-" * 80)

    df = create_sample_dataset()

    print("\n--- [Step 1: Original DataFrame] ---")
    print(df)

    print("\n--- DataFrame Column Information (Data Types) ---")
    print(df.dtypes)
    print("-" * 80)

    print("\n--- [Example 1: Selecting Numeric Columns Only] ---")
    print("Method Call: df.select_dtypes(include='number')")

    numeric_df = df.select_dtypes(include='number')

    print("\nResulting DataFrame:")
    print(numeric_df)

    print("\nSelected Columns Dtypes:")
    print(numeric_df.dtypes)

    print("-" * 80)

    print("\n--- [Example 2: Selecting String / Object Columns Only] ---")
    print("Method Call: df.select_dtypes(include='object')")

    object_df = df.select_dtypes(include='object')

    print("\nResulting DataFrame:")
    print(object_df)

    print("\nSelected Columns Dtypes:")
    print(object_df.dtypes)

    print("-" * 80)

    print("\n--- [Example 3: Selecting Boolean Columns Only] ---")
    print("Method Call: df.select_dtypes(include='bool')")

    boolean_df = df.select_dtypes(include='bool')

    print("\nResulting DataFrame:")
    print(boolean_df)

    print("\nSelected Columns Dtypes:")
    print(boolean_df.dtypes)

    print("-" * 80)

    print("\n--- [Example 4: Excluding Numeric Columns] ---")
    print("Method Call: df.select_dtypes(exclude='number')")

    non_numeric_df = df.select_dtypes(exclude='number')

    print("\nResulting DataFrame:")
    print(non_numeric_df)

    print("\nSelected Columns Dtypes:")
    print(non_numeric_df.dtypes)

    print("-" * 80)



RES()