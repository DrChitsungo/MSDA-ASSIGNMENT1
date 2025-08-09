#Hihgridge Construction Company Payment Slips.
#As the Software Engineer, I have been given a task to develop payslips to facilitate weekly payments.
#The company has 400 employees whose earnings range from $7500 to $30000.Here is the code:

# Initialize an empty list to store employee details
employee_list = []

def store_employee_details():
    # Ask the user how many employees they want to enter
    try:
        num_employees = int(input("How many employee details do you want to enter? "))
    except ValueError:
        print("Invalid number. Exiting program.")
        exit()

    # Loop through the number of employees
    for i in range(num_employees):
        print(f"\nPlease enter Employee {i + 1} details in format: id name gender salary")
        data = input().strip().split()

        # Validate if all 4 fields are provided
        if len(data) != 4:
            print("Invalid input format. Please provide exactly 4 fields: id name gender salary")
            continue

        emp_id, name, gender, salary = data

        # Optional: Convert salary to a number if needed
        try:
            salary = float(salary)
        except ValueError:
            print("Invalid salary value. It must be a number.")
            continue

        # Store employee details in a dictionary
        employee = {
            "id": emp_id,
            "name": name,
            "gender": gender,
            "salary": salary,
            "employee_level": "Unassigned",
        }

        # Add the employee to the list
        employee_list.append(employee)

        # Output confirmation
        print(f"ID: {emp_id}, name: {name}, gender: {gender}, salary: {salary}")

    # Print all employee records at the end
    print("\nAll Employee Records:")
    for emp in employee_list:
        print(emp)


def assign_employee_levels_with_conditional():
    """
    Function to assign employee levels using conditional statement in for loop
    If salary > $10,000 and < $20,000, assign Employee level as "A1"
    """

    #print("Processing workers with conditional statement...")
    #print("Condition: If salary > $10,000 and < $20,000, assign Employee level as 'A1'")
    #print("=" * 80)
    #print('conditional:if salary >$7,500 and <$30,000 and gender =female, assign Employee level as "A5-F"')
    # Counter for tracking assignments
    a1_assignments = 0
    total_processed = 0


    # For loop with conditional statement
    for worker in employee_list:
        try:
            # Get worker's current salary
            salary = worker['salary']
            worker_id = worker['id']
            worker_name = worker['name']
            worker_gender = worker['gender']
            print(f"Processing {worker_name} ({worker_id}) - Salary: ${salary:,.2f}")

            # CONDITIONAL STATEMENT: If salary > $10,000 and < $20,000, assign "A5-F"
            if (salary >= 7500 and salary <= 30000):
                if worker_gender == 'female':
                    worker['employee_level'] = 'A5-F'
                    a1_assignments += 1
                    print(f"  ✓ ASSIGNED: Employee level 'A5-F' (Salary: ${salary:,.2f})")
                    total_processed += 1
                else:
                    print('')

            # CONDITIONAL STATEMENT: If salary > $10,000 and < $20,000, assign "A1"
            elif (salary >= 10000 and salary <= 30000):
                worker['employee_level'] = 'A1'
                a1_assignments += 1
                print(f"  ✓ ASSIGNED: Employee level 'A5-F' (Salary: ${salary:,.2f})")
                total_processed += 1
        except Exception as e:
            print(f"Error processing worker {worker.get('id', 'Unknown')}: {str(e)}")

    # Summary report

    print("=" * 80)
    print("CONDITIONAL ASSIGNMENT SUMMARY")
    print("=" * 80)
    print(f"Total workers processed: {total_processed}")
    print(f"Workers assigned 'A1' level: {a1_assignments}")
    print(f"Condition applied: Salary > $10,000 AND Salary < $20,000")
    print()
    return worker

#Code to extract a single employees details and generate payslip
def generate_payslip():
    try:
        employee_id = str(input("Please enter employee id? "))

        for employee in employee_list:
            if employee_id == employee_id:
                    print("Employee ID:", employee_id)
                    print("Employee Name:", employee['name'])
                    print("Employee Gender:", employee['gender'])
                    print("Employee Salary:", employee['salary'])
                    print("Employee Level:", employee['employee_level'])
                    print("*********** AUGUST 2025 ***********")
                    print("****HIGHRIDGE CONSTRUCTION COMPANY****")
                    print("****PAYMENT ADVICE SlIP****")
                    print("")
                    print("-" * 80)
                    print(f"{'Employee ID':<12} {'Name':<20} {'Gender':<12} {'Salary':<12} {'Level':<10}")
                    print(f"{employee_id :<12} {employee['name']:<20} {employee['gender']:<12} {employee['salary']:<12} {employee['employee_level']:<10}")
                    print("-" * 80)

    except ValueError:
        print("Invalid number. Exiting program.")
        exit()


def display_results():
    """Display the results after conditional assignment"""
    print("FINAL WORKER STATUS:")
    print("-" * 60)
    print(f"{'Employee ID':<12} {'Name':<20} {'Salary':<12} {'Level':<10}")
    print("-" * 60)

    for worker in employee_list:
        print(f"{worker['id']:<12} {worker['name']:<20} ${worker['salary']:<11,.2f} {worker['employee_level']:<10}")


# Execute the functions
if __name__ == "__main__":
    # Run the basic conditional assignment
    print("BASIC CONDITIONAL STATEMENT EXAMPLE")
    print("=" * 80)
    store_employee_details()

    updated_workers = assign_employee_levels_with_conditional()
    generate_payslip()