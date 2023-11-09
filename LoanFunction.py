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
    
    for i , calculation in enumerate(loan_calculations,start=1):
        print(str(i) + ". Principal: RM " + str(round(calculation['principal'],2)) 
        + ",\n   Monthly Instalment: RM " + str(round(calculation['principal'],2))
        + ",\n   Total Amount Payable: RM " + str(round(calculation['total_amount'],2))
        + ",\n   DSR: " + str(round(calculation['dsr'],2)) + "%")
