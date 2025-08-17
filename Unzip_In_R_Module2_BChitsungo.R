# Set the working directory to the folder containing the zip file
setwd("C:/Users/Hp/OneDrive/Desktop/Employee Profiles")

# Unzip the archive (e.g., "Employee Profile.zip") into a subfolder named "unzipped_employee"
unzip("Employee Profile.zip", exdir = "unzipped_employee")

# List files in the unzipped folder (optional, to confirm the CSV filename)
files <- list.files("unzipped_employee")
print(files)

# Assuming the CSV file is named "VICTOR_WYRSCH.csv" (check for underscores vs spaces!)
csv_path <- file.path("unzipped_employee", "VICTOR_WYRSCH.csv")

# Read the CSV into a data frame
df <- read.csv(csv_path, header = TRUE, sep = ",")
print(df)           # Print the contents
View(df)            # Open in viewer (works in RStudio)

