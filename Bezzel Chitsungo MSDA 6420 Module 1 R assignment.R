# Highridge Construction Company Payment Slips
# As the Software Engineer, I have been given a task to develop payslips to facilitate weekly payments.
# The company has 400 employees whose earnings range from $7500 to $30000. Here is the code:

# Initialize an empty data frame to store employee details
employee_list <- data.frame(
  id = character(),
  name = character(),
  gender = character(),
  salary = numeric(),
  employee_level = character(),
  stringsAsFactors = FALSE
)

store_employee_details <- function() {
  # Ask the user how many employees they want to enter
  num_employees <- tryCatch({
    as.integer(readline("How many employee details do you want to enter? "))
  }, warning = function(w) {
    cat("Invalid number. Exiting program.\n")
    return(NULL)
  }, error = function(e) {
    cat("Invalid number. Exiting program.\n")
    return(NULL)
  })
  
  if (is.null(num_employees) || is.na(num_employees)) {
    return(NULL)
  }
  
  # Loop through the number of employees
  for (i in 1:num_employees) {
    cat(sprintf("\nPlease enter Employee %d details in format: id name gender salary\n", i))
    data_input <- trimws(readline())
    data_parts <- strsplit(data_input, "\\s+")[[1]]
    
    # Validate if all 4 fields are provided
    if (length(data_parts) != 4) {
      cat("Invalid input format. Please provide exactly 4 fields: id name gender salary\n")
      next
    }
    
    emp_id <- data_parts[1]
    name <- data_parts[2]
    gender <- data_parts[3]
    salary_input <- data_parts[4]
    
    # Convert salary to a number
    salary <- tryCatch({
      as.numeric(salary_input)
    }, warning = function(w) {
      cat("Invalid salary value. It must be a number.\n")
      return(NA)
    }, error = function(e) {
      cat("Invalid salary value. It must be a number.\n")
      return(NA)
    })
    
    if (is.na(salary)) {
      next
    }
    
    # Create employee record
    new_employee <- data.frame(
      id = emp_id,
      name = name,
      gender = gender,
      salary = salary,
      employee_level = "Unassigned",
      stringsAsFactors = FALSE
    )
    
    # Add the employee to the list
    employee_list <<- rbind(employee_list, new_employee)
    
    # Output confirmation
    cat(sprintf("ID: %s, name: %s, gender: %s, salary: %s\n", emp_id, name, gender, salary))
  }
  
  # Print all employee records at the end
  cat("\nAll Employee Records:\n")
  for (i in 1:nrow(employee_list)) {
    cat(sprintf("ID: %s, Name: %s, Gender: %s, Salary: %.2f, Level: %s\n",
                employee_list$id[i], employee_list$name[i], employee_list$gender[i],
                employee_list$salary[i], employee_list$employee_level[i]))
  }
}

assign_employee_levels_with_conditional <- function() {
  # Function to assign employee levels using conditional statement in for loop
  # If salary > $10,000 and < $20,000, assign Employee level as "A1"
  
  # Counter for tracking assignments
  a1_assignments <- 0
  total_processed <- 0
  
  # For loop with conditional statement
  for (i in 1:nrow(employee_list)) {
    tryCatch({
      # Get worker's current details
      salary <- employee_list$salary[i]
      worker_id <- employee_list$id[i]
      worker_name <- employee_list$name[i]
      worker_gender <- employee_list$gender[i]
      
      cat(sprintf("Processing %s (%s) - Salary: $%.2f\n", worker_name, worker_id, salary))
      
      # CONDITIONAL STATEMENT: If salary >= $7500 and <= $30000 and gender = female, assign "A5-F"
      if (salary >= 7500 && salary <= 30000) {
        if (worker_gender == 'female') {
          employee_list$employee_level[i] <<- 'A5-F'
          a1_assignments <- a1_assignments + 1
          cat(sprintf("  ✓ ASSIGNED: Employee level 'A5-F' (Salary: $%.2f)\n", salary))
          total_processed <- total_processed + 1
        } else {
          cat("\n")
        }
      }
      # CONDITIONAL STATEMENT: If salary >= $10,000 and <= $30,000, assign "A1"
      else if (salary >= 10000 && salary <= 30000) {
        employee_list$employee_level[i] <<- 'A1'
        a1_assignments <- a1_assignments + 1
        cat(sprintf("  ✓ ASSIGNED: Employee level 'A1' (Salary: $%.2f)\n", salary))
        total_processed <- total_processed + 1
      }
    }, error = function(e) {
      cat(sprintf("Error processing worker %s: %s\n", worker_id, e$message))
    })
  }
  
  # Summary report
  cat(paste(rep("=", 80), collapse = ""), "\n")
  cat("CONDITIONAL ASSIGNMENT SUMMARY\n")
  cat(paste(rep("=", 80), collapse = ""), "\n")
  cat(sprintf("Total workers processed: %d\n", total_processed))
  cat(sprintf("Workers assigned levels: %d\n", a1_assignments))
  cat("Condition applied: Salary > $10,000 AND Salary < $20,000\n")
  cat("\n")
}

# Code to extract a single employee's details and generate payslip
generate_payslip <- function() {
  tryCatch({
    employee_id <- readline("Please enter employee id? ")
    
    # Find the employee (Note: original Python code had a bug - comparing employee_id to itself)
    employee_found <- FALSE
    for (i in 1:nrow(employee_list)) {
      if (employee_list$id[i] == employee_id) {
        employee_found <- TRUE
        cat("Employee ID:", employee_id, "\n")
        cat("Employee Name:", employee_list$name[i], "\n")
        cat("Employee Gender:", employee_list$gender[i], "\n")
        cat("Employee Salary:", employee_list$salary[i], "\n")
        cat("Employee Level:", employee_list$employee_level[i], "\n")
        cat("*********** AUGUST 2025 ***********\n")
        cat("****HIGHRIDGE CONSTRUCTION COMPANY****\n")
        cat("****PAYMENT ADVICE SLIP****\n")
        cat("\n")
        cat(paste(rep("-", 80), collapse = ""), "\n")
        cat(sprintf("%-12s %-20s %-12s %-12s %-10s\n", 
                    "Employee ID", "Name", "Gender", "Salary", "Level"))
        cat(sprintf("%-12s %-20s %-12s %-12.2f %-10s\n", 
                    employee_id, employee_list$name[i], employee_list$gender[i], 
                    employee_list$salary[i], employee_list$employee_level[i]))
        cat(paste(rep("-", 80), collapse = ""), "\n")
        break
      }
    }
    
    if (!employee_found) {
      cat("Employee with ID", employee_id, "not found.\n")
    }
    
  }, error = function(e) {
    cat("Invalid input. Exiting program.\n")
  })
}

display_results <- function() {
  # Display the results after conditional assignment
  cat("FINAL WORKER STATUS:\n")
  cat(paste(rep("-", 60), collapse = ""), "\n")
  cat(sprintf("%-12s %-20s %-12s %-10s\n", "Employee ID", "Name", "Salary", "Level"))
  cat(paste(rep("-", 60), collapse = ""), "\n")
  
  for (i in 1:nrow(employee_list)) {
    cat(sprintf("%-12s %-20s $%-11.2f %-10s\n", 
                employee_list$id[i], employee_list$name[i], 
                employee_list$salary[i], employee_list$employee_level[i]))
  }
}

# Execute the functions
main <- function() {
  # Run the basic conditional assignment
  cat("BASIC CONDITIONAL STATEMENT EXAMPLE\n")
  cat(paste(rep("=", 80), collapse = ""), "\n")
  
  store_employee_details()
  assign_employee_levels_with_conditional()
  generate_payslip()
  display_results()
}

# Run the main function
main()