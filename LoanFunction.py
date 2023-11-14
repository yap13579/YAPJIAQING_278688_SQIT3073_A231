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
    
     #for i , record in enumerate(loan_calculations,start=1):
     #   print(str(i) + ". Principal: RM " + str(round(record['principal'],2)) 
     #   + ",\n   Monthly Instalment: RM " + str(round(record['monthly_payment'],2))
     #   + ",\n   Total Amount Payable: RM " + str(round(record['total_amount'],2))
     #   + ",\n   DSR: " + str(round(record['dsr'],2)) + "%" 
     #   + ",\n   Eligibility :" + str(record['eligibility']))
    i=0
    for each in loan_calculations:
        i+=1
        print(str(i) + ". Principal: RM " + str(round(each['principal'],2) )
        + ",\n   Monthly Instalment: RM " + str(round(each['monthly_payment'],2))
        + ",\n   Total Amount Payable: RM " + str(round(each['total_amount'],2))
        + ",\n   DSR: " + str(round(each['dsr'],2)) + "%" 
        + ",\n   Eligibility :" + str(each['eligibility']))
    print() 
    input("Press Enter to continue....")

def edit_record(loan_calculations):
    while True:
        try:
           print("\nPrevious Loan Calculations:")
           
           i=0
           for each in loan_calculations:
                i+=1
                print(str(i) + ". Principal: RM " + str(round(each['principal'],2) )
                + ",\n   Monthly Instalment: RM " + str(round(each['monthly_payment'],2))
                + ",\n   Total Amount Payable: RM " + str(round(each['total_amount'],2))
                + ",\n   DSR: " + str(round(each['dsr'],2)) + "%" 
                + ",\n   Eligibility :" + str(each['eligibility']))

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

    


    