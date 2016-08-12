# The prime factors of 13195 are 5, 7, 13 and 29.
import sys

class Finder():
    def __init__(self, bignum):
        self.bignum = bignum
        self.primes = [2, 3]
        self.factors = list()

    def _smallest_prime_factor(self, n):
        # Return the smallest prime factor of n.
        # If n is prime, its smallest prime factor is n.

        # Try known primes first
        for p in self.primes:
            if n % p == 0:
                return p

        # Seek another prime up to root(n)
        for i in range(self.primes[-1] + 2, int(n**0.5) + 1, 2):  # use step 2 since no even primes exist

            if self._smallest_prime_factor(i) == i:
                # print("Discovered new prime:", i)
                self.primes.append(i)

                # Does our number n divide by i?  If so, we've found its smallest prime factor
                if n % i == 0:
                    return i
        
        return n

    def results(self):
        j = self.bignum

        # Instead of seeking largest prime factor, start with the smallest, because that
        # makes the problem successively easier and easier.
        while True:
            f = self._smallest_prime_factor(j)
            if j == f:
                # We've found the last (largest) prime factor of self.bignum.
                self.factors.append(j)
                self.primes.append(j)
                return self.factors

            # We've found a prime factor of self.bignum, but it has a larger one.
            self.factors.append(f)

            # Here's where the problem gets easier.  We can now continue the search 
            # on a much smaller number.
            j = j/f


def main():
    bignum = int(sys.argv[1])
    f = Finder(bignum)
    print("Prime factors of %d are: %s" % (bignum, f.results()))
    print("Primes discovered: %s" % f.primes)

if __name__ == '__main__':
    main()

# >$ python problem_03.py 13195
# Prime factors of 13195 are: [5, 7, 13, 29]
# Primes discovered: [2, 3, 5, 7, 11, 13, 29]

# >$ python problem_03.py 1044
# Prime factors of 1044 are: [2, 2, 3, 3, 29]
# Primes discovered: [2, 3, 5, 29]

# >$ python problem_03.py 600851475143
# Prime factors of 600851475143 are: [71, 839, 1471, 6857]
# Primes discovered: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, ...6857]

# Answer: the largest prime factor of 600851475143 is 6857.