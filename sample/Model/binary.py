class Binary:
    RIGHT_SHIFT = "right"
    LEFT_SHIFT = "left"

    def __init__(self, code: str, exponent: int = 0):
        self.whole = '0'
        self.fractional = '0'
        self.code = code
        self.exponent = exponent

    @staticmethod
    def list_to_binary(binary):
        return ''.join(map(str, binary))

    def binary_to_decimal(self, binary):
        return int(str("0b"+self.list_to_binary(binary)), 2)

    @staticmethod
    def decimal_to_binary(decimal):
        return bin(decimal)[2:]

    @property
    def code(self):
        return self.whole + ['.'] + self.fractional

    @property
    def whole(self):
        return self.__whole

    @property
    def fractional(self):
        return self.__fractional

    @code.setter
    def code(self, code: str or float or int, separator: str = ''):
        if isinstance(code, (str, float, int)):
            self.whole, self.fractional = self.float_separate(code)

            code = self.handle_float_code(code)

            if separator == '':
                self.__code = list(str(code))
                return

            self.__code = str(code).split(separator)

    @whole.setter
    def whole(self, whole):
        self.__whole = self.mixed_to_list(whole)

    @fractional.setter
    def fractional(self, fractional):
        self.__fractional = self.mixed_to_list(fractional)

    def process_exponent(self):
        whole = self.whole
        last_digit = int(self.list_to_binary(self.whole))

        if len(whole) == 1 and last_digit == 1:
            return

        if last_digit > 1:
            self.increment_exponent()

            self.process_exponent()
            return

        if last_digit < 1:
            self.decrement_exponent()

            self.process_exponent()
            return

    def increment_exponent(self):
        self.exponent += 1

        tmp, self.whole = self.shift(self.whole, self.RIGHT_SHIFT)
        self.fractional = list(tmp) + self.fractional

    def decrement_exponent(self):
        self.exponent -= 1

        tmp, self.fractional = self.shift(self.fractional)
        self.whole += tmp

    def shift_chain(self, array, side: str = LEFT_SHIFT):
        if side == self.LEFT_SHIFT:
            tmp = array[0]
            code = array[1:]
            return code + list(tmp)

        if side == self.RIGHT_SHIFT:
            tmp = array[-1]
            code = array[:-1]
            return list(tmp) + code

        raise Exception("Shift not allowed: side pass[" + str(side) + "]")

    def shift(self, array, side: str = LEFT_SHIFT):
        if not len(array):
            return [0, 0]

        if side == self.LEFT_SHIFT:
            tmp = array[0]

            if len(array) > 1:
                return [tmp, array[1:]]

            return [tmp, [0]]

        if side == self.RIGHT_SHIFT:
            tmp = array[-1]

            if len(array) > 1:
                return [tmp, array[:-1]]

            return [tmp, [0]]

        raise Exception("Shift not allowed: side pass[" + str(side) + "]")

    @staticmethod
    def float_separate(number: str or float):
        number = str(number)

        if "," in number:
            return number.split(",")

        if "." in number:
            return number.split(".")

        return [number, 0]

    @staticmethod
    def handle_float_code(number: str or float):
        # number = str(number)
        #
        # # if number.count(',') == 1:
        # #     number.lstrip(',')
        # #     return number
        # #
        # # if number.count('.') == 1:
        # #     number.lstrip('.')
        # #     return number
        #
        return number

    @staticmethod
    def mixed_to_list(obj):
        if not isinstance(obj, list):
            return list(str(obj))

        return obj
