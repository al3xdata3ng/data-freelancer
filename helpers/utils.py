def income_calculator(annual_payment: float):

    
    vat: float = 0.24
    tax_bins: dict = {'0-10': 0.09,
                        '10-20': 0.22,
                        '20-30': 0.28,
                        '30-40': 0.36,
                         '40-': 0.44 }
    ater_vat_annual_payment = annual_payment * (1 - vat)
    
    if ater_vat_annual_payment > 0 and ater_vat_annual_payment <= 10000:
        net_annual_payment = (1 - tax_bins['0-10']) * ater_vat_annual_payment
    elif ater_vat_annual_payment > 10000 and ater_vat_annual_payment <= 20000:
        net_annual_payment = (1 - tax_bins['0-10']) * 10000 \
                        + (1 - tax_bins['10-20']) * (ater_vat_annual_payment - 10000)
    elif ater_vat_annual_payment > 20000 and ater_vat_annual_payment <= 30000:
        net_annual_payment = (1 - tax_bins['0-10']) * 10000 \
                        + (1 - tax_bins['10-20']) * 10000 \
                        + (1 - tax_bins['20-30']) * (ater_vat_annual_payment - 20000)
    elif ater_vat_annual_payment > 30000 and ater_vat_annual_payment <= 40000:
        net_annual_payment = (1 - tax_bins['0-10']) * 10000 \
                        + (1 - tax_bins['10-20']) * 10000 \
                        + (1 - tax_bins['20-30']) * 10000 \
                        + (1 - tax_bins['30-40']) * (ater_vat_annual_payment - 30000)
    elif ater_vat_annual_payment > 40000:
        net_annual_payment = (1 - tax_bins['0-10']) * 10000 \
                        + (1 - tax_bins['10-20']) * 10000 \
                        + (1 - tax_bins['20-30']) * 10000 \
                        + (1 - tax_bins['30-40']) * 10000 \
                        + (1 - tax_bins['40-']) * (ater_vat_annual_payment - 40000)
        
    return net_annual_payment


def employer_cost(gross_salary: float):
    tax = 0.2229
    employer_cost = (gross_salary * (1 + tax)) * 14

    return employer_cost


def hourly_rate(annual_income_before_taxes: float, annual_working_weeks: int, weekly_working_hours: int):
    annual_billable_hours = annual_working_weeks * weekly_working_hours
    hourly_rate = annual_income_before_taxes / annual_billable_hours

    return hourly_rate 








