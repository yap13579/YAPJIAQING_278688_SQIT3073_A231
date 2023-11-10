import os
def calculate_monthly_instalment(principal, interest, year):
    monthly_interest = interest / 100 / 12
    num = year * 12
    monthly_payment = principal * (monthly_interest / (1 - (1 + monthly_interest) ** -num))
    return monthly_payment

def calculate_total_amount_payable(monthly_payment, year):
    total = monthly_payment * year * 12
    return total


def calculate_dsr(housing_loan, monthly_income, commitments):
    total_commitments = housing_loan + commitments
    dsr = (total_commitments / monthly_income) * 100
    return dsr

def display_previous_calculations(loan_calculations):
    print("\nPrevious Loan Calculations:")
    i=1
    for record in loan_calculations:
        
        print(str(i) + ". Principal: RM " + str(round(record.principal,2)) 
        + ",\n   Monthly Instalment: RM " + str(round(record.monthly_payment,2))
        + ",\n   Total Amount Payable: RM " + str(round(record.total_amount,2))
        + ",\n   DSR: " + str(round(record.dsr,2)) + "%" 
        + ",\n   Eligibility :" + str(record.eligibility))
        i+=1

    print() 
    input("Press Enter to continue....")

def edit_record(loan_calculations):
    while True:
        try:
           print("\nPrevious Loan Calculations:")
           i=1
           for record in loan_calculations:
               
               print(str(i) + ". Principal: RM " + str(round(record.principal,2)) 
               + ",\n   Monthly Instalment: RM " + str(round(record.monthly_payment,2))
               + ",\n   Total Amount Payable: RM " + str(round(record.total_amount,2))
               + ",\n   DSR: " + str(round(record.dsr,2)) + "%" 
               + ",\n   Eligibility :" + str(record.eligibility))
               i+=1

           print()
           
                    
           a=int(input("\nwhich record you want to delete :"))
           del loan_calculations[a-1]
           print("delete done!")
           print() 
           input("Press Enter to continue....")
           break
        except:
            print("Please insert again....")
            input()
            os.system("cls")

class loan_record:
    def __init__(self,principal,monthly_payment,total_amount,dsr,eligibility):
        self.principal=principal
        self.monthly_payment=monthly_payment
        self.total_amount=total_amount
        self.dsr=dsr
        self.eligibility=eligibility