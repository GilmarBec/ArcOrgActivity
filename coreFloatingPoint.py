from FloatingPoint import *

select_operation = input(
    "Selecione entre \n"
    "b2f: binário para decimal com ponto flutuante\n"
    "f2b: decimal com ponto flutuante para binário\n"
    "eq: comparar igualdade entre 2 binários\n"
    "alb: compara a menor que b (binário)\n"
    "sum: soma de valores binários\n\n"
    ": "
)

if select_operation == "b2f":
    print(bin2float(input("Número binário no padrão IEE 754 32bits: ")))
elif select_operation == "f2b":
    print(float2bin(float(input("Número decimal(com ponto flutuante ou não): "))))
elif select_operation == "eq":
    print(eq(input("Número binário comum (ex: 10110.101): "), input("Número binário comum (ex: 10110.101): ")))
elif select_operation == "alb":
    print(a_less_b(input("Número binário comum (ex: 10110.101): "), input("Número binário comum (ex: 10110.101): ")))
elif select_operation == "sum":
    binary_sum()
else:
    print("Operation selected not accepted")
