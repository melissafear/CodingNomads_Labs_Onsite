'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''


births_p_yr = (60/6) * 60 * 24 * 365
deaths_p_yr = (60/12) * 60 * 24 * 365
immigrants_p_yr = (60/40) * 60 * 24 * 365

current_pop = 380123456



total_pop_in_3_years = int(current_pop + births_p_yr*3 + immigrants_p_yr*3 - deaths_p_yr*3)
print(f"Total population in 3 years will be {total_pop_in_3_years:,} an increase of {total_pop_in_3_years - current_pop:,}")
