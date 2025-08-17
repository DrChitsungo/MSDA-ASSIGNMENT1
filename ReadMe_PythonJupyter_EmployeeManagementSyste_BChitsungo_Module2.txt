==================================================
Employee Salary Management System - README
==================================================

Author: Bezzel Chitsungo

Description:
-------------
This project is a Jupyter Notebook-based application written in Python. It processes an employee salary dataset, converts it into a searchable dictionary, allows retrieval of individual employee records by name, and provides functionality to export selected employee data as a CSV file, which is then zipped for secure storage or sharing.

--------------------------------------------------
Features:
-------------
1. Load and display salary data from a CSV file.
2. Convert the dataset into a dictionary format for fast lookups.
3. Retrieve and display salary details for a specific employee.
4. Export employee details to a `.csv` file and compress it into a `.zip` archive.

--------------------------------------------------
File Requirements:
-------------
- CSV File: A file named `Salary2.csv` must exist in:
  `C:/Users/Hp/OneDrive/Desktop/`
- Columns expected in the CSV include:
  `EmployeeName`, `JobTitle`, `BasePay`, `OvertimePay`, `OtherPay`, `Benefits`, `TotalPay`, `TotalPayBenefits`, and `Year`.

--------------------------------------------------
How to Use:
-------------
1. **Setup Environment**:
   - Run the notebook in a Python 3 Jupyter environment.
   - Ensure required packages are installed: `pandas`, `zipfile`, and `os`.

2. **Step-by-step Flow**:

   - **Load CSV**:
     The CSV is loaded into a DataFrame using pandas:
     file_path = "C:/Users/Hp/OneDrive/Desktop/Salary2.csv"
     salary_data = pd.read_csv(file_path)

   - **Convert to Dictionary**:
     Each employee's data is indexed by their name in a dictionary:
     employee_dict = {
         "EMPLOYEE_NAME": {
             "JobTitle": ...,
             "BasePay": ...,
             ...
         }
     }

   - **Search Employee**:
     The function `get_employee_details(name)` retrieves an employee's record by name.

   - **Export & Zip**:
     Using the `write_employee_to_csv()` function, the selected employee's data is exported as:
     - A CSV file named after the employee (`First_Last.csv`)
     - A zip file named `Employee Profile.zip`, stored at:
       `C:/Users/Hp/OneDrive/Desktop/Employee Profiles/`

   - **Interactive Prompt**:
     At the end, the script prompts you to enter an employee name:
     Please enter employee name: VICTOR WYRSCH

--------------------------------------------------
Error Handling:
-------------
- A `DtypeWarning` may appear when reading the CSV due to mixed data types.
- If an employee name is not found, the system displays:
  No employee found with the name: ...
- Exceptions during export are caught and displayed.

--------------------------------------------------
Output Example:
-------------
After entering the name "VICTOR WYRSCH", the output includes:
- Printed salary details in the console
- Exported CSV: `VICTOR_WYRSCH.csv`
- Zipped file: `Employee Profile.zip`

--------------------------------------------------
Customization:
-------------
- To use a different CSV file, change the `file_path` variable.
- To store output files in a different directory, update:
  folder_path = "C:/Users/Hp/OneDrive/Desktop/Employee Profiles"

--------------------------------------------------
License:
-------------
This project is for educational and personal use only.

--------------------------------------------------
Contact:
-------------
Bezzel Chitsungo eng.chitsungo@gmail.com
