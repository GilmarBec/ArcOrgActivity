from FloatingPoint import *
from sample.FloatingPoint.SumBit.test.DataProvider import *
from sample.FloatingPoint.SumBit.test.TestCase import TestCase

test = TestCase()

for data in SUM_DATA_PROVIDER:
    test.base(data)

for data in CONVERSION_DATA_PROVIDER:
    if float2bin(data['f']) == data['b']:
        continue
    raise Exception("Test float2bin [" + str(data) + "] Failed!")

for data in CONVERSION_DATA_PROVIDER:
    if bin2float(data['b']) == data['f']:
        continue
    raise Exception("Test bin2float [" + str(data) + "] Failed!")

for data in COMPARISON_DATA_PROVIDER:
    if a_less_b(data['b1'], data['b2']) == data['result']:
        continue
    raise Exception("Test a_less_b [" + str(data) + "] Failed!")

for data in COMPARISON_DATA_PROVIDER:
    if eq(data['b1'], data['b2']) == data['eq']:
        continue
    raise Exception("Test eq [" + str(data) + "] Failed!")
