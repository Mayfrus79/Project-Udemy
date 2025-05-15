import locale
import string
from datetime import datetime
from pathlib import Path

# Path to the template file (in the same directory as this script)
FILE_PATH = Path(__file__).parent / 'aula69.txt'

# Set locale to system default
locale.setlocale(locale.LC_ALL, '')

def convert_to_brl(number: float) -> str:
    """Convert number to Brazilian Real format"""
    brl = 'R$ ' + locale.currency(number, symbol=False, grouping=True)
    return brl

# Sample data for template
date = datetime(2022, 12, 28)
data = dict(
    name='João',
    value=convert_to_brl(1_234_456),
    date=date.strftime('%d/%m/%Y'),
    company='O. M.',
    phone='+55 (11) 7890-5432'
)

# Custom template class that uses % as delimiter instead of $
class MyTemplate(string.Template):
    delimiter = '%'

# Read template file and substitute values
with open(FILE_PATH, 'r') as file:
    text = file.read()
    template = MyTemplate(text)
    print(template.substitute(data))