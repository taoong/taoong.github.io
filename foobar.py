import math

def nearest_power_of_2(x):
    prev = 2 ** int(math.log(x, 2))
    next = 2 ** (int(math.log(x, 2)) + 1)
    return (x - prev, next - x)

def is_odd(x):
    return x & 1

def answer(n):
    n = int(n)
    mem = {}

    def helper(n, start, curr):
        # Check mem
        if start in mem:
            return mem[start]

        # Base case
        if n == 1 or n == 0:
            mem[start] = curr
            return 0

        # If odd
        if is_odd(n):
            nearest = nearest_power_of_2(n)
            # Go up
            if nearest[1] < helper(nearest[0], nearest[0], 0):
                return helper(n + 1, start, curr + 1) + 1
            # Go down
            else:
                return helper(n - 1, start, curr + 1) + 1

        # If even
        else:
            nearest = nearest_power_of_2(n)
            # Landed on a power of 2
            if nearest[0] == 0:
                return helper(n / 2, start, curr + 1) + 1
            # Go up
            if nearest[1] < helper(nearest[0], nearest[0], 0):
                return helper(n + 1, start, curr + 1) + 1
            # Go down
            else:
                return helper(n / 2, start, curr + 1) + 1
    
    return helper(n, n, 0)

print(answer(1243))