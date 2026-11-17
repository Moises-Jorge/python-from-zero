"""
Explicação: Decimal(0.1) vs Decimal("0.1")

1. Decimal(0.1): Recebe um número do tipo 'float'. Antes mesmo de chegar ao Decimal,
   o Python já converteu 0.1 para binário (base 2), gerando uma aproximação imprecisa
   (0.1000000000000000055511151231257827021181583404541015625). O Decimal limita-se
   a guardar esse valor impreciso.

2. Decimal("0.1"): Recebe uma 'string' (texto). O módulo decimal lê os dígitos
   diretamente em base 10, sem passar pelo float binário, garantindo o valor exato 0.1.

3. Por que Decimal(input()) funcionou: Porque a função input() devolve sempre uma string,
   evitando a perda de precisão da conversão para float.

Validação com valor real:
- Input: 91750 AOA | Taxa: 917.50 AOA por 1 USD
- Output esperado e obtido: 91750.00 Kz = $100.00
"""

from decimal import Decimal

value_kz = Decimal(input('Enter the value in Kwanzas (AOA): '))
exchange_rate = Decimal(input('Enter the exchange rate (Kwanzas per 1 USD): '))
value_usd = value_kz / exchange_rate
print(f'{value_kz:.2f} Kz = ${value_usd:.2f}')
