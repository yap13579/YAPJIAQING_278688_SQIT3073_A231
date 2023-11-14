import os
import LoanFunction as L

os.system("cls")
loan_calculations = []
while True:
    os.system("cls")
    print("\nMenu:")
    print("1. Calculate New Loan")
    print("2. Display Previous Loan Calculations")
    print("3. Edit Record")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":

        while True: 
         try:
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

            
      
            print(f"\nMonthly Instalment: RM{round(monthly_payment,2)}")
            print(f"Total Amount Payable: RM{round(total_amount,2)}")
            print(f"Debt Service Ratio (DSR): {round(dsr,2)}%")
            print(f"Eligibility: {eligibility}")

            print() 
            input("Press Enter to continue....")
            break
        
         except:
            print("Please insert again....")
            input()
            os.system("cls")

    elif choice == "2":
        if len(loan_calculations)==0:
               os.system("cls")
               print("Empty list!")
               print() 
               input("Press Enter to continue....")
        else:
               
               L.display_previous_calculations(loan_calculations)
               

    elif choice == "3":
         if len(loan_calculations)==0:
               os.system("cls")
               print("Empty list!")
               print() 
               input("Press Enter to continue....")

         else:
            
             L.edit_record(loan_calculations)
        
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
        
        input()
