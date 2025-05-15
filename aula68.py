
import csv
from pathlib import Path


DESKTOP = Path.home() / 'Desktop' / 'Aula180.csv'

employees = [
    {'Name': 'Spongebob', 'Age': 32, 'Job': 'Cook', 'Address': 'Bikine tranch'},
    {'Name': 'Patrick', 'Age': 45, 'Job': 'unemployed', 'Address': 'Bikine tranch'},
    {'Name': 'Sandy', 'Age': 27, 'Job': 'Scientist', 'Address': 'Bikine tranch'},
    {'Name': 'Squid Mollusk', 'Age': 56, 'Job': 'manager', 'Address': 'Bikine tranch'},
]

if DESKTOP.exists():
    print(f'The file already exists in {DESKTOP}')

else:
    print('The file needs to be created!')
    with open(DESKTOP, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name','Age','Job','Address'], delimiter=';')
        writer.writeheader()
        writer.writerows(employees)
        print(f'CSV file created: {DESKTOP}')