'''''
Author: Ebube Vincent Okutalukwe 
Course: CPRG 216A  Object-Oriented Programming 1
Date: 10/09/2025
Project : ACME Bank Mortgage Calculator
Description:  PART 2  AMORTIZATION SCHEDULE
This file imports the Part 1 program, then adds the loop
that displays the full amortization schedule month by month
'''



from mortgage_calculator_part1 import *

choice = input("Would you like to see the amortization schedule? (Y/N): ").lower()

if choice == "y":
    print("\n           Monthly Amortization Schedule\n")
    print(f"{'Month':<8}{'Opening Bal':>15}{'Payment':>12}"
        f"{'Principal':>12}{'Interest':>12}{'Closing Bal':>15}")

    opening_balance = principal_amount
    total_principal = 0
    total_interest = 0

    for month in range(1, term * 12 + 1):
        monthly_interest = opening_balance * emr
        monthly_principal = monthly_payment - monthly_interest
        closing_balance = opening_balance - monthly_principal

        total_principal += monthly_principal
        total_interest += monthly_interest

        print(f"{month:<8}{opening_balance:>15.2f}{monthly_payment:>12.2f}"
            f"{monthly_principal:>12.2f}{monthly_interest:>12.2f}{closing_balance:>15.2f}")

        opening_balance = closing_balance

    print("=" * 70)
    print(f"{'Total':<50}{total_principal:>12.2f}{total_interest:>12.2f}")
    print("\nEnd of Amortization Schedule")
