import time

from sample.Mulbit.MulBit import MulBit
from sample.Mulbit.test.DataProvider import DATA_PROVIDER


class TestCase:
    def __init__(self):
        self.mul_bit = None
        self.tests = 0

    def setup(self, m, q):
        self.mul_bit = MulBit(m, q)

    def base(self, data):
        start = time.time()

        self.setup(data["m"], data["q"])
        self.mul_bit.run()

        end = time.time()
        final_time = (end-start)

        print("Time: "+str(final_time)+"s")

        self.tests += 1

        if self.mul_bit.result == data["result"]:
            print(str(self.tests) + " Tests passed!")
            return

        print("\n===========================================================")
        print("====> Data <====")
        print(data)
        print("====> Result <====")
        print(self.mul_bit.result)
        print("====> Expected <====")
        print(data["result"])
        raise Exception("Test [" + str(self.tests) + "] Failed!")

    def test_8_bits(self):
        print("\nStarting 8 Bit Tests!")

        self.tests = 0
        for data in DATA_PROVIDER[8]:
            self.base(data)

    def test_16_bits(self):
        print("\nStarting 16 Bit Tests!")

        self.tests = 0
        for data in DATA_PROVIDER[16]:
            self.base(data)

    def test_32_bits(self):
        print("\nStarting 32 Bit Tests!")

        self.tests = 0
        for data in DATA_PROVIDER[32]:
            self.base(data)

    def test_64_bits(self):
        print("\nStarting 64 Bit Tests!")

        self.tests = 0
        for data in DATA_PROVIDER[64]:
            self.base(data)
