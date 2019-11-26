def sqrt(x):
    def sqrt_iter(guess):
        if good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))

    def improve(guess):
        return average(guess, (x / guess))

    def average(x, y):
        return (x + y) / 2

    def good_enough(guess):
        return abs(square(guess) - x) < 0.001

    def square(x):
        return x * x

    return sqrt_iter(1.0)

print(sqrt(9))