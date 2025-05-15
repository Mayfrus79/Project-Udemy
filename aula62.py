import calendar
 
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
print(list(enumerate(calendar.day_name)))
print(calendar.day_name[numero_primeiro_dia])
print(calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)])

