from decimal import Decimal

value_kz = Decimal(input('digit the value in kz(AOA): '))
exchange_rate = Decimal(input('digit the exchange rate: '))
value_usd = value_kz * exchange_rate
print(f'{value_kz:.2f}Kz = ${value_usd:.2f}')
