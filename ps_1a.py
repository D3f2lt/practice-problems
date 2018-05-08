# Author: d3f2lt
# Time: 05:16 PM

def cal_credit_balance():
    outstanding_balance = float(raw_input('Enter the outstanding balance on your credit card:'))
    annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as decimal:'))
    min_monthly_payment_rate = float(raw_input('Enter the minimum monthly payment rate as decimal:'))
    monthly_interest_rate = annual_interest_rate / 12.0 
    months = 0
    total_amount = 0
    balance = outstanding_balance

    while(months < 12):
        min_monthly_payment = min_monthly_payment_rate * balance
        interest_paid = monthly_interest_rate * balance
        principal_paid = min_monthly_payment - interest_paid
        remaining_balance = balance - principal_paid
        months += 1
        print 'Month:', months
        print 'Minimum monthly payment: $' + str(round(min_monthly_payment, 2))
        print 'Principal paid: $' + str(round(principal_paid, 2))
        print 'Remaining balance: $' + str(round(remaining_balance, 2))
        total_amount += min_monthly_payment
        balance = remaining_balance

    print 'RESULT'
    print 'Total amount paid: $' + str(round(total_amount, 2))
    print 'Remaining balance: $' + str(round(remaining_balance, 2))


## testing...
if __name__ == '__main__':
    cal_credit_balance()
    input('Press Enter to Exit!!')
