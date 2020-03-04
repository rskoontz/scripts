#!/usr/bin/env python3
import math

principle = int(input("Enter the starting principle, no commas: "))
r = float(input("What is the interest rate in decimals, example, .0175 : "))
t = int(input("How many of years to compound? : "))
n = int(input("What is the number of times the interest is compounded per year? : "))
pmt = int(input("What is the monthly contribution per month? : "))
interest_period = n * t

def compound_interest(principle, r, t): 
    CI = principle * (pow((1 + r / n), interest_period)) 
    return CI

def compound_interest_monthly():
   m_cmpd_rate = pmt - (pmt * (pow((1 + r / n), interest_period)))
   total_balance_after_cmpd_mnth = (m_cmpd_rate / (1 - (1 + (r / n))))
   return total_balance_after_cmpd_mnth

def total_all(CI, total_balance_after_cmpd_mnth):
    total = CI + total_balance_after_cmpd_mnth
    print("After {0} years, the total balance will be ${1}".format(t,total))

def main():
    compound_interest(principle,r,t)
    compound_interest_monthly()
    CI = compound_interest(principle,r,t)
    total_balance_after_cmpd_mnth = compound_interest_monthly()
    total_all(CI, total_balance_after_cmpd_mnth)

if __name__ == "__main__":
    main()