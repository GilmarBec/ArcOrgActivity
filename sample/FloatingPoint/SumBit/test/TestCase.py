import time

from sample.FloatingPoint.SumBit.Sum import SumBit
from sample.Model.binary import Binary


class TestCase:
    def __init__(self):
        self.sum_bit = None
        self.tests = 0

    def setup(self, a, b):
        self.sum_bit = SumBit(a, b)

    def base(self, data):
        start = time.time()

        for i in range(1000):
            self.setup(Binary(data["a"]), Binary(data["b"]))
            self.sum_bit.sum()

            while self.sum_bit.z.exponent != 0:
                if self.sum_bit.z.exponent > 0:
                    self.sum_bit.z.decrement_exponent()
                    continue

                if self.sum_bit.z.exponent < 0:
                    self.sum_bit.z.increment_exponent()

        end = time.time()
        final_time = (end-start)

        print("Time: "+str(final_time)+"s")

        self.tests += 1

        if self.sum_bit.z.list_to_binary(self.sum_bit.z.code) == data["result"]:
            print(str(self.tests) + " Tests passed!")
            return

        print("\n===========================================================")
        print("====> Data <====")
        print(data)
        print("====> Result <====")
        print(self.sum_bit.z.list_to_binary(self.sum_bit.z.code))
        print("====> Expected <====")
        print(data["result"])
        raise Exception("Test [" + str(self.tests) + "] Failed!")