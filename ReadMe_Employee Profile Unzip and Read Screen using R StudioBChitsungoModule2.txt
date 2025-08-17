Employee Profile Unzip and Read Script

This R script automates the process of extracting an employee profile CSV file from a zipped archive and loading it into R for viewing and analysis.

---

What the Script Does

1. Sets the working directory to the folder where the zip file (Employee Profile.zip) is located.
2. Unzips the archive into a subfolder named "unzipped_employee".
3. Lists the files in the unzipped folder to help verify the CSV file name.
4. Reads the specified CSV file (e.g., VICTOR_WYRSCH.csv) into an R data frame.
5. Prints the data frame contents to the console.
6. Opens the data frame viewer in RStudio for easier inspection.

---

How to Use

1. Modify the setwd() path to point to the folder containing your zip file on your computer:

   setwd("C:/Users/Hp/OneDrive/Desktop/Employee Profiles")

2. Ensure your zip file is named exactly "Employee Profile.zip" or update the script accordingly.

3. Confirm the exact CSV file name inside the zip archive (commonly formatted with underscores instead of spaces), and update this line if necessary:

   csv_path <- file.path("unzipped_employee", "VICTOR_WYRSCH.csv")

4. Run the script in R or RStudio. The CSV contents will be printed and opened in a viewer window.

---

Requirements

- R (version 3.5 or higher recommended)
- RStudio (recommended for View() functionality)
- The zipped file Employee Profile.zip should contain at least one CSV file.

---

Troubleshooting

- If you receive an error that the CSV file cannot be found, check the actual file name inside the unzipped folder by examining the printed list from:

  files <- list.files("unzipped_employee")
  print(files)

- Adjust the CSV file name in the script accordingly.

- Ensure your working directory is set correctly with setwd() before running the unzip and read commands.

---

Contact

For questions or further assistance, please contact:

Bezzel Chitsungo
