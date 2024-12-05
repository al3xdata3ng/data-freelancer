from utils import *

annual_income_before_tax = 37000
annual_working_weeks = 40
weekly_working_hours = 20
monthly_gross_employer_salary = 2776

net_annual_income = income_calculator(annual_income_before_tax)

gross_hourly_rate = hourly_rate(net_annual_income
            ,annual_working_weeks
            ,weekly_working_hours)

annual_employer_cost = employer_cost(monthly_gross_employer_salary)


print(f"net_annual_income: {net_annual_income} \n gross_hourly_rate: {gross_hourly_rate} \n annual_employer_cost: {annual_employer_cost}")
