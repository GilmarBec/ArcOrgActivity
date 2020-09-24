from sample.test.DataProvider import DATA_PROVIDER

changes = 0


def bit_format(bit, n_bit: int):
    response = [0] * n_bit

    for i in range(len(bit)):
        response[-i-1] = bit[-i-1]

    return response


while True:
    bits = int(input("Bits in this test [8, 16, 32, 64]: "))
    m = int(input("First Value: "))
    q = int(input("Second Value: "))

    data = {
        "m": bit_format(bin(m)[2:], bits),
        "q": bit_format(bin(q)[2:], bits),
        "result": bit_format(bin(m * q)[2:], bits*2+1),
    }

    print(data)

    DATA_PROVIDER[bits].append(data)

    changes += 1

    cancel = input("More data (Y/n)? ")

    if cancel in ["n", "N", "NO", "No", "no", "Não", "não", "NÃO"]:
        break

if changes > 0:
    file = open("DataProvider.py", "w")
    file.write("DATA_PROVIDER = "+str(DATA_PROVIDER))
    file.close()
