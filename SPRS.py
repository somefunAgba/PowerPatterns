# Number Theory Computing
# Recursive Patterns in Powers

# Integer Powers of any real number
# param n: base number, n
# param r: exponent number, r
# return: power, the result of the operation
import time
import sys

sys.setrecursionlimit(1500)


class SPRS:

    def __init__(self, n, r=2):

        # Memory Map
        self.n = n
        self.r = r
        # self.mem_list = []
        self.memo = {0: 1, 1: n}

        # Somefun's Square Method
        # The square of any positive or negative real number value can be generalized
        # into these returned formula expression below, where n is that number
        self.a = self.n - 1
        self.c = 3 + (self.n - 2)
        self.memo[2] = (self.a * self.c) + 1

    # returns the power, the result of the recursive power series pattern
    def valr(self):
        memo = self.memo
        r = self.r
        if r not in memo:

            def pp_series(k):
                if k in memo:
                    return memo[k]
                p = k - 1
                memo[k] = pp_series(p) * memo[1]

                # print('Memory Map:\n')
                # for k in memo:
                #     print(k, '->', memo[k], end=' || ')
                # print('\n')

                return memo[k]

            return pp_series(r)
        else:
            return memo[r]

    # returns the power, the result of the recursive power series pattern
    def valr2(self):
        memo = self.memo
        r = self.r
        if r not in memo:
            if r % 2 != 0:
                p = int((r - 1) * 0.5)
                memo[r] = memo[1]
                for i in range(p):
                    memo[r] = memo[r] * memo[2]
            if r % 2 == 0:
                p = int(r * 0.5)
                memo[r] = memo[2]
                for i in range(p):
                    memo[r] = memo[r] * memo[2]

        return memo[r]

    # returns the power, the result of the sum of power series pattern
    def vals(self):
        memo = self.memo
        r = self.r
        a = self.a
        if r not in memo:
            p = r - 3 + 1
            sums = 0
            for j in range(p):
                if j not in memo:
                    isums = 0
                    k = j - 3 + 1
                    for o in range(k):
                        isums += memo[o]
                        memo[j] = memo[2] * (1 + (a * isums))
                sums += memo[j]
            memo[r] = memo[2] * (1 + (a * sums))

        return memo[r]

    @property
    # returns a map of the recursive power series, r of a number, n
    def map_mem(self):
        # print('Memory Map:\n')
        # for k in self.memo:
        #     self.mem_list.append(self.memo[k])
        return self.memo


if __name__ == '__main__':
    #
    ts = time.clock()
    for index in range(64):
        psr = SPRS(2, 7)
    tf = time.clock()
    tfs0 = (tf - ts) / 64
    print('Time: ', tfs0, 'secs')
    #
    t = 100
    ##
    psr1 = SPRS(2, 7)
    print(psr1.valr())

    print('algo1')
    ts = time.clock()
    for index in range(t):
        SPRS(2, t).valr()
    tf = time.clock()
    tfs1 = (tf - ts) / t
    print('Time: ', tfs1, 'secs')
    print(psr1.memo)


    ##
    psr2 = SPRS(2, 7)
    print(psr2.valr2())

    print('algo2')
    ts = time.clock()
    for index in range(t):
        SPRS(2, t).valr2()
    tf = time.clock()
    tfs2 = (tf - ts) / t
    print('Time: ', tfs2, 'secs')
    print(psr2.memo)

    ##
    psr3 = SPRS(2, 7)
    print(psr3.vals())

    print('algo3')
    ts = time.clock()
    for index in range(t):
        SPRS(2, t).vals()
    tf = time.clock()
    tfs3 = (tf - ts) / t
    print('Time: ', tfs3, 'secs')
    print(psr3.memo)
    #

    print('inbuilt')
    ts = time.clock()
    for index in range(t):
        psi = 2 ** t
    tf = time.clock()
    tfs4 = (tf - ts) / t
    print('Time: ', tfs4, 'secs')

    #
    mintfs = min(tfs1, tfs2, tfs3)
    print('Min:', mintfs)
    relspeed = [tfs0/mintfs, tfs1/mintfs, tfs2/mintfs, tfs3/mintfs, mintfs/tfs4]
    print(relspeed)


