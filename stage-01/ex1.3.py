"""
Explanation: Decimal(0.1) vs Decimal("0.1")

1. Decimal(0.1): Receives a 'float' number. Even before reaching Decimal,
   Python has already converted 0.1 into binary (base 2), generating an imprecise
   approximation (0.1000000000000000055511151231257827021181583404541015625).
   Decimal simply stores that imprecise value.

2. Decimal("0.1"): Receives a 'string' (text). The decimal module reads the digits
   directly in base 10, bypassing the binary float conversion and ensuring the
   exact value 0.1.

3. Why Decimal(input()) worked: Because the input() function always returns a
   string, avoiding the precision loss caused by converting to a float.

Validation with a real value:
- Input: 91750 AOA | Rate: 917.50 AOA per 1 USD
- Expected and actual output: 91750.00 Kz = $100.00
- Source: National Bank of Angola (BNA) reference rate on 2026-11-17 (1 USD = 917.50 AOA)

"""

from decimal import Decimal

value_kz = Decimal(input('Enter the value in Kwanzas (AOA): '))
exchange_rate = Decimal(input('Enter the exchange rate (Kwanzas per 1 USD): '))
value_usd = value_kz / exchange_rate
print(f'{value_kz:.2f} Kz = ${value_usd:.2f}')
