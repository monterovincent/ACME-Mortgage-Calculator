'''''
Authors : Ebube Vincent Okutalukwe  
Course: CPRG 216A  Object-Oriented Programming 1
Date: 10/09/2025
Project : ACME Bank Mortgage Calculator
Description:  This program calculates the monthly mortgage payments and,
if requested, produces an amortization schedule for a mortgage.
It includes input validation, down payment rules, insurance rates,
and monthly payment formulas according to ACME Bank Ltd. guidelines
'''''



print("Welcome to ACME Bank Ltd. Mortgage Calculator\n")

#  INPUT SECTION 
client_name = input("Enter client name: ")
property_address = input("Enter address of property: ")
purchase_price = float(input("Enter purchase price: "))

#  MINIMUM DOWN PAYMENT (Table 1) 
if purchase_price <= 500000:
    min_down_payment = purchase_price * 0.05
elif purchase_price <= 1000000:
    min_down_payment = (500000 * 0.05) + ((purchase_price - 500000) * 0.10)
else:
    min_down_payment = purchase_price * 0.20

min_down_percent = round((min_down_payment / purchase_price) * 100, 3)

#  VALIDATE DOWN PAYMENT INPUT
down_payment_percent = 0.0
while down_payment_percent < min_down_percent or down_payment_percent > 100:
    down_payment_percent = float(
        input(f"Enter down payment percentage (minimum {min_down_percent:.3f}): ")
    )
    if down_payment_percent < min_down_percent or down_payment_percent > 100:
        print("Please enter a value between the minimum and 100.\n")

#  DETERMINE INSURANCE RATE (Table 2) 
if down_payment_percent < 10:
    insurance_rate = 4.0
elif down_payment_percent < 15:
    insurance_rate = 3.1
elif down_payment_percent < 20:
    insurance_rate = 2.8
else:
    insurance_rate = 0.0

#  CALCULATE AMOUNTS 
down_payment_amount = purchase_price * (down_payment_percent / 100)
insurance_cost = (purchase_price - down_payment_amount) * (insurance_rate / 100)
principal_amount = purchase_price - down_payment_amount + insurance_cost

print(f"Down payment amount is ${down_payment_amount:,.0f}")
print(f"Mortgage insurance price is ${insurance_cost:,.0f}")
print(f"Total mortgage amount is ${principal_amount:,.0f}")

#  VALIDATE TERM & AMORTIZATION 
term = 0
while term != 1 and term != 2 and term != 3 and term != 5 and term != 10:
    term = int(input("Enter mortgage term (1, 2, 3, 5, 10): "))
    if term != 1 and term != 2 and term != 3 and term != 5 and term != 10:
        print("Please enter a valid choice")

amortization = 0
while amortization != 5 and amortization != 10 and amortization != 15 \
    and amortization != 20 and amortization != 25:
    amortization = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
    if amortization != 5 and amortization != 10 and amortization != 15 \
    and amortization != 20 and amortization != 25:
        print("Please enter a valid choice")

#  DETERMINE INTEREST RATE (Table 3)
RATE_TABLE = {1: 0.0595, 2: 0.059, 3: 0.056, 5: 0.0529, 10: 0.06}
annual_rate = RATE_TABLE[term]
print(f"Interest rate for the term will be {annual_rate * 100:.2f}%")

#  EFFECTIVE MONTHLY RATE 
emr = ((1 + (annual_rate / 2)) ** 2) ** (1 / 12) - 1

#  MONTHLY PAYMENT 
n = amortization * 12
monthly_payment = principal_amount * (emr * (1 + emr) ** n) / ((1 + emr) ** n - 1)

print(f"Monthly payment amount is: ${monthly_payment:,.0f}")
