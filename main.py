import os
import LoanFunction as L

os.system("cls")
loan_calculations = []
while True:
    os.system("cls")
    print("\nMenu:")
    print("1. Calculate New Loan")
    print("2. Display Previous Loan Calculations")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        
        principal = float(input("Enter principal loan amount: "))
        annual_interest_rate = float(input("Enter annual interest rate (in percentage): "))
        loan_term = int(input("Enter loan term (in years): "))
        monthly_income = float(input("Enter applicant's monthly income: "))
        other_commitments = float(input("Enter applicant's other monthly financial commitments: "))

        
        monthly_payment = L.calculate_monthly_instalment(principal, annual_interest_rate, loan_term)
        total_amount = L.calculate_total_amount_payable(monthly_payment, loan_term)
        dsr = L.calculate_dsr(monthly_payment, monthly_income, other_commitments)

        
        if dsr <= 70:
            eligibility = "Eligible" 
        else:
            eligibility ="Not Eligible"

        
        loan_calculations.append({
            "principal": principal,
            "monthly_payment": monthly_payment,
            "total_amount": total_amount,
            "dsr": dsr,
            "eligibility": eligibility
        })

        
        #print("\nMonthly Instalment: RM%.2f" % monthly_payment)
       # print("Total Amount Payable: RM%.2f" % total_amount)
        #print("Debt Service Ratio (DSR): %.2f" %dsr)
       # print("Eligibility: " + eligibility)
        print(f"\nMonthly Instalment: RM{round(monthly_payment,2)}")
        print(f"Total Amount Payable: RM{round(total_amount,2)}")
        print(f"Debt Service Ratio (DSR): {round(dsr,2)}%")
        print(f"Eligibility: {eligibility}")

        print() 
        input("Press Enter to continue....")
        

    elif choice == "2":
        
        L.display_previous_calculations(loan_calculations)
        print() 
        input("Press Enter to continue....")
    elif choice == "3":
        
        print("Exiting the program. Goodbye!")
        print() 
        
        break

    else:
        print("Invalid choice. Please try again.")
        
        input()
