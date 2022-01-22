import numpy_financial as npf
import numpy as np
import matplotlib.pyplot as plt

# Future Value - (fv)
print('==============================================================================================================')
print('# Future Value - (fv)')
res = npf.fv(rate=0.08, nper=5, pmt=0, pv=-1000)
print("Res", res)

print('==============================================================================================================')

# Numpy Refresh
print('# Numpy Refresh')
prices = [42.8, 102.03, 240.38, 80.9]

print("Prices: ", prices)

print("np.mean(prices): ", np.mean(prices))

print("np.std(prices): ", np.std(prices))

print("np.sum(prices): ", np.sum(prices))

print("np.max(prices): ", np.max(prices))

print('==============================================================================================================')
# Numpy-Financial

# Future Value - (fv)
print('# Future Value - (fv)')
print("Future Value - (fv): ", npf.fv(rate=1, nper=1, pmt=0, pv=-100))
print('==============================================================================================================')
# Present Value - (pv)
print('# Present Value - (pv)')
print("Present Value - (pv)", npf.pv(rate=0.10, nper=8, pmt=0, fv=1000))
print('==============================================================================================================')
print('# Monthly payment (Loan)')
# Monthly payment against loan principal plus interest
# The pmt() function is used to compute the payment against loan principal plus interest.

# Let's say we want to calculate how much we have to pay monthly to pay back
# a loan of 100,000 in 5 years. The yearly interest rate is 7%, and is calculated monthly.
print("Loan Payments: ", npf.pmt(rate=0.07 / 12, nper=5 * 12, pv=100000, fv=0))

print('==============================================================================================================')
print('# Monthly payment (Investment)')
# Note that aside from computing a monthly mortgage payment,
# the pmt() function can be used to return the periodic deposit one must make to achieve
# a specified future balance with a given interest rate.

# The code will return the monthly deposits needed to achieve 50000 in 5 years with 10% annual interest.
print("Monthly Payment for future goal: ", npf.pmt(rate=0.07/12, nper=5*12, pv=0, fv=50000))
print('==============================================================================================================')
print('# Internal Rate of Return')
# Numpy Financial has an irr() function, used to calculate the IRR (Internal Rate of Return).

# Let's assume we invested 5000 and got the following payments back: 500, 700, 1000, 3000.
# To calculate the IRR, we first need to declare an array with the values, with the
# first value being our initial investment:

cashflow = [-5000, 500, 700, 1000, 3000]

print("IRR: ", npf.irr(cashflow))
print('==============================================================================================================')
print('# Comparing IRR')
# Comparing IRR
# Let's use the irr() function to compare two investment opportunities and decide which one is better.

# Option 1:
# Requires 50K in investment
# Will pay 10K, 25K, 25K, 35K, 42K each year for the next 5 years.
#
# Option 2:
# Requires 30K in investment
# Will pay 10K, 13K, 18K, 25K, 20K each year for the next 5 years.
#
# Let's calculate the IRR for each investment and compare:

cf1 = [-50000, 10000, 25000, 25000, 35000, 42000]
cf2 = [-30000, 10000, 13000, 18000, 25000, 20000]
print(f"For Cash Flow {cf1} Irr")
print("Option 1: ", npf.irr(cf1))
print('==============================================================================================================')
print(f"For Cash Flow {cf2} Irr")
print("Option 2: ", npf.irr(cf2))
print('==============================================================================================================')
# Plotting Data
print('# Plotting Data')
rev = [18000, 25000, 20000, 45000, 19500]
plt.plot(rev)
plt.savefig('Plotting_Data_1.png')
plt.clf()
print('==============================================================================================================')
# Plotting Data 2
print('# Plotting Data 2')
rev = [18000, 25000, 20000, 45000, 32000]
months = ['June', 'July', 'August', 'September', 'October']
plt.plot(months, rev)
plt.savefig('Plotting_Data_2.png')
plt.clf()
print('==============================================================================================================')
# Accessing Data

# Web Scraping
print('# Web Scraping')

