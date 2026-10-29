loan_amount = float(input("Loan amount ($): "))
annual_rate = float(input("Annual interest rate (%): "))
years = int(input("Loan term (years): "))

monthly_rate = annual_rate / 100 / 12
number_of_payments = years * 12

if monthly_rate == 0:
    payment = loan_amount / number_of_payments
else:
    payment = (
        loan_amount
        * monthly_rate
        / (1 - (1 + monthly_rate) ** -number_of_payments)
    )

print(f"Monthly payment: ${payment:,.2f}")