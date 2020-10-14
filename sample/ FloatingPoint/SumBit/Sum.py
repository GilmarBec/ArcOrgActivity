from sample.Model.binary import Binary


class SumBit:
    def __init__(
            self,
            x: Binary,
            y: Binary,
            overflow_base: int = 8,
            underflow_base: int = 8,
            z: Binary = None
    ):
        self.x = x
        self.y = y
        self.z = z
        self.overflow_base = overflow_base
        self.underflow_base = underflow_base

    def sum(self):
        res = self.validate_simple()

        if res:
            return res

        self.handle_exponent()

        block = self.block_sum(self.x.fractional, self.y.fractional)
        fractional = block[0]
        block = self.block_sum(self.x.whole, self.y.whole, block[1])
        whole = [block[1]] + block[0]

        z_data = self.x.list_to_binary(self.x.mixed_to_list(whole) + ['.'] + self.x.mixed_to_list(fractional))

        self.z = Binary(z_data, self.x.exponent)

        if len(self.z.whole) + 1 > self.overflow_base:
            raise Exception("Overflow was occurred, z ["+str(self.z.list_to_binary(self.z))+"]")

        if len(self.z.fractional) + 1 > self.underflow_base:
            raise Exception("Overflow was occurred, z ["+str(self.z.list_to_binary(self.z))+"]")

        print(self.z.whole)
        self.normalize(self.z)

    def normalize(self, x: Binary):
        if x.exponent > 0:
            x.decrement_exponent()
            self.normalize(x)

        if x.exponent < 0:
            x.increment_exponent()
            self.normalize(x)

        return x

    def block_sum(self, x_number, y_number, tmp: int = 0):
        x_bin = int(self.x.list_to_binary(x_number))
        y_bin = int(self.y.list_to_binary(y_number))

        if x_bin == 0 and y_bin == 0:
            return [tmp, 0]

        if x_bin == 0:
            return [y_number, 0]

        if y_bin == 0:
            return [x_number, 0]

        x_number.reverse()
        y_number.reverse()

        max_size = x_number

        if self.x.binary_to_decimal(x_number) < self.y.binary_to_decimal(y_number):
            max_size = y_number

        z = []
        tmp = tmp

        for i in range(len(max_size)):
            x = 0
            y = 0

            if len(x_number) >= i:
                x = int(x_number[i])

            if len(y_number) >= i:
                y = int(y_number[i])

            bin_z = self.binary_sum(x + tmp, y)
            z += [bin_z[0]]
            tmp = bin_z[1]

        z.reverse()
        return [z, tmp]

    @staticmethod
    def mixed_to_list(obj):
        if not isinstance(obj, list):
            return list(str(obj))

        return obj

    @staticmethod
    def binary_sum(x: int = 0, y: int = 0):
        z = x + y

        if z > 1:
            z -= 2
            return [z, 1]

        return [z, 0]

    def handle_exponent(self):
        self.x.process_exponent()
        self.y.process_exponent()

        self.eq_exponents()

    def eq_exponents(self):
        if self.x.exponent > self.y.exponent:
            self.y.increment_exponent()
            self.eq_exponents()

        if self.x.exponent < self.y.exponent:
            self.x.increment_exponent()
            self.eq_exponents()

        return

    def validate_simple(self):
        if not self.x:
            return self.y

        if not self.y:
            return self.x

        return False


a = Binary("100")
b = Binary("100")

c = SumBit(a, b)
c.sum()
print(c.z.list_to_binary(c.z.code))
