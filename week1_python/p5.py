''' Taxation Problem:
Lab 6: Tax Calculator Problem
GlobalNext Solutions, a rapidly growing IT company, employs a diverse workforce ranging from entry-
level developers to senior executives. The HR department wants to streamline the tax calculation
process for employees under the New Tax Regime (2023). They’ve decided to build a tax calculation
program that computes salaries, taxes, and net incomes while ensuring compliance with the latest tax
laws.
As a software developer in GlobalNext’s HR-Tech team, you are tasked with developing this program.
The system should process employee salary details, validate inputs, calculate taxes, and generate
detailed reports.
The program should:
1. Accept employee details, including monthly salary components.
2. Calculate gross and taxable income according to the New Tax Regime (2023).
3. Compute the tax payable using the appropriate tax slabs.
4. Apply any applicable standard deductions and rebates.
5. Generate reports detailing gross salary, taxable income, tax payable, and net salary.

Level 1: Basic Input and Salary Calculation
Objective: Capture employee details and calculate the gross salary.
Tasks:
• Accept the following inputs for an employee:
o Name
o EmpID
o Basic Monthly Salary
o Special Allowances (Monthly)
o Bonus Percentage (Annual Bonus as % of Gross Salary)
• Calculate:
o Gross Monthly Salary = Basic Salary + Special Allowances
o Annual Gross Salary = (Gross Monthly Salary × 12) + Bonus
• Output:
o Display the employee details, gross monthly salary, and annual gross salary.

Level 2: Taxable Income Calculation
Objective: Calculate taxable income after standard deductions.
Tasks:
• Deduct a Standard Deduction of ₹50,000 from the annual gross salary.
• Compute the Taxable Income and display all intermediate calculations.
Output: Display gross salary, standard deduction and taxable income.

Level 3: Tax and Rebate Calculation
Objective: Compute tax payable using the New Tax Regime (2023) slabs.
Tasks:
1. Calculate tax based on the following slabs:
o ₹0 - ₹3,00,000: 0%
o ₹3,00,001 - ₹6,00,000: 5%
o ₹6,00,001 - ₹9,00,000: 10%
o ₹9,00,001 - ₹12,00,000: 15%
o ₹12,00,001 - ₹15,00,000: 20%
o Above ₹15,00,000: 30%
2. Apply Section 87A Rebate:
o Taxable income ≤ ₹7,00,000 → 100% rebate (tax payable = ₹0).
3. Add a 4% Health and Education Cess to the calculated tax.

TalenciaGlobal HandsOn Framework - THLF
Level 4: Net Salary Calculation
Objective: Calculate annual net salary after tax deductions.
Tasks:
1. Compute Net Salary = Annual Gross Salary - Total Tax Payable.
2. Display:
o Annual Gross Salary
o Total Tax Payable (including cess)
o Annual Net Salary

Level 5: Report Generation
Objective: Generate a detailed report for employees.
Tasks:
1. Summarize all computed details:
o Employee Details (Name, EmpID)
o Gross Monthly Salary
o Annual Gross Salary
o Taxable Income
o Tax Payable (with breakdown)
o Annual Net Salary
2. Format the output as a report for better readability.

Level 6: Input Validation Rules
Objective: Validate all inputs to ensure accuracy and correctness.
Validation Rules:
1. Employee Details:
o Name: Non-empty, alphabets only, max 50 characters.
o EmpID: Alphanumeric, 5–10 characters.
2. Salary Inputs:
o Basic Salary: Positive number, max ₹1,00,00,000.
o Special Allowances: Non-negative, max ₹1,00,00,000.
o Bonus Percentage: Numeric value, 0–100.
3. Derived Calculations:
o Gross Monthly Salary must be greater than zero.
o Annual Gross Salary should not exceed realistic values.
4. General:
o Reject invalid inputs with a clear error message.
o Provide re-entry prompts for invalid data.
'''




# Input details
name = input("Enter employee's name: ")
emp_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic monthly salary: "))
special_allowances = float(input("Enter monthly special allowances: "))
bonus_percentage = float(input("Enter annual bonus percentage (as a % of gross salary): "))

# Calculations
gross_monthly_salary = basic_salary + special_allowances
annual_gross_salary = (gross_monthly_salary * 12) + (gross_monthly_salary * bonus_percentage / 100)

# Display Employee Details
print("\nEmployee Details:")
print(f"Name: {name}")
print(f"Employee ID: {emp_id}")
print(f"Gross Monthly Salary: ₹{gross_monthly_salary:,.2f}")
print(f"Annual Gross Salary: ₹{annual_gross_salary:,.2f}")

# Taxable Income Calculation
standard_deduction = 50000
taxable_income = annual_gross_salary - standard_deduction

print("\nTaxable Income Calculation:")
print(f"Annual Gross Salary: ₹{annual_gross_salary:,.2f}")
print(f"Standard Deduction: ₹{standard_deduction:,.2f}")
print(f"Taxable Income: ₹{taxable_income:,.2f}")

# Tax Calculation
tax = 0

if taxable_income > 1500000:
    tax += (taxable_income - 1500000) * 0.30
    taxable_income = 1500000
if taxable_income > 1200000:
    tax += (taxable_income - 1200000) * 0.20
    taxable_income = 1200000
if taxable_income > 900000:
    tax += (taxable_income - 900000) * 0.15
    taxable_income = 900000
if taxable_income > 600000:
    tax += (taxable_income - 600000) * 0.10
    taxable_income = 600000
if taxable_income > 300000:
    tax += (taxable_income - 300000) * 0.05
    taxable_income = 300000
if annual_gross_salary <= 700000:
    tax = 0  # Rebate under section 87A

# Cess Calculation
cess = tax * 0.04
total_tax_payable = tax + cess

# Display Tax Breakdown
print("\n-- Tax Breakdown --")
print(f"Base Tax: ₹{tax:.2f}")
print(f"Health and Education Cess (4%): ₹{cess:.2f}")
print(f"Total Tax Payable: ₹{total_tax_payable:.2f}")
