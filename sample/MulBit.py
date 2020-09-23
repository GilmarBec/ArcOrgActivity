

class MulBit:
    def __init__(self, m, q):
        self.m = m
        self.q = q
        self.result = [0] * (len(q) + 1) + q
        self.result_len = len(self.result)
        self.m_len = len(m)

    def run(self):
        for i in range(1, self.m_len + 1):
            if self.q[-i]:
                self.sum(self.result[0:(self.m_len+1)])

            self.shift()

    def sum(self, ca):
        m = [0] + self.m
        tmp = 0

        for i in range(len(ca) - 1, -1, -1):
            if ca[i] and m[i]:
                ca[i] = tmp
                tmp = 1
            else:
                ca_or_m = ca[i] or m[i]

                if tmp:
                    if ca_or_m:
                        ca[i] = 0
                    else:
                        ca[i] = 1
                        tmp = 0
                else:
                    ca[i] = ca_or_m

        self.setSumResult(ca)

    def setSumResult(self, sum_array):
        self.result = sum_array + self.result[(self.m_len+1):self.result_len]

    def shift(self):
        for i in range(len(self.result) - 1, 0, -1):
            self.result[i] = self.result[i - 1]

        self.result[0] = 0
