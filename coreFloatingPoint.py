import struct

from sample.FloatingPoint.SumBit.Sum import SumBit
from sample.Model.binary import Binary


def binary_sum():
    a = Binary(input("1 Número Binário para soma(para ponto flutuante utilize . ou ,): "))
    b = Binary(input("2 Número Binário para soma(para ponto flutuante utilize . ou ,): "))

    core = SumBit(a, b)
    core.sum()

    while core.z.exponent != 0:
        if core.z.exponent > 0:
            core.z.decrement_exponent()
            continue

        if core.z.exponent < 0:
            core.z.increment_exponent()

    print("Resultado: ", core.z.list_to_binary(core.z.code))


def bin2float(b):
    h = int(b, 2).to_bytes(8, byteorder="big")
    return struct.unpack('>d', h)[0]


def float2bin(f):
    [d] = struct.unpack(">Q", struct.pack(">d", f))
    return f'{d:032b}'


def eq(b1, b2):
    b1 = Binary(b1)
    b2 = Binary(b2)

    return b1.code == b2.code


def a_less_b(b1, b2):
    b1 = Binary(b1)
    b2 = Binary(b2)

    return b1.code < b2.code


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
