from datetime import datetime
from dateutil.relativedelta import relativedelta  # type: ignore

total_amount = 1_000_000
loan_date = datetime(2025, 3, 14)
loan_duration = relativedelta(years=10)
final_date = loan_date + loan_duration

installment_dates = []
installment_date = loan_date

while installment_date <= final_date:
    installment_dates.append(installment_date)
    installment_date += relativedelta(months=1)

number_of_installments = len(installment_dates)
installment_value = total_amount / number_of_installments

for date in installment_dates:
    print(date.strftime('%Y/%m/%d'), f'${installment_value:,.2f}')

print()
print(
    f'You borrowed ${total_amount:,.2f} to be paid',
    f'in {loan_duration.years} years',
    f'({number_of_installments} months) in installments of '
    f'${installment_value:,.2f}.'
)
