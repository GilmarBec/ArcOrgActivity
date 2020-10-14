from sample.FloatingPoint.SumBit.Sum import SumBit
from sample.Model.binary import Binary

# a = Binary(input("1 Número Binário para soma(para ponto flutuante utilize . ou ,): "))
# b = Binary(input("2 Número Binário para soma(para ponto flutuante utilize . ou ,): "))

a = Binary("101,1")
b = Binary("0,1")

core = SumBit(a, b)
core.sum()

while core.z.exponent != 0:
    if core.z.exponent > 0:
        core.z.decrement_exponent()
        continue

    if core.z.exponent < 0:
        core.z.increment_exponent()

print("Resultado: ", core.z.list_to_binary(core.z.code))
