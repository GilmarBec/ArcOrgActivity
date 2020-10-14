from sample.Mulbit.MulBit import MulBit

m = input("First number in bits, separated by comma(','): ")
q = input("Second number in bits, separated by comma(','): ")

m = m.split(',')
q = q.split(',')

mul_bit = MulBit(m, q)
mul_bit.run()

print(mul_bit.result)
