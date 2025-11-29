import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.549876
current_temp = 0.5

print(f"Ideal temperature is ", Decimal(ideal_temp), "°C")
print(f"Current temperature is ", Fraction(current_temp), "°C")
print(f"Temperature difference: {ideal_temp - current_temp}°C")
print(sys.float_info)

