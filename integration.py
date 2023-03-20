import numpy as np


# pi times the integral from 1 to 3 of f(x)^2 dx == 42.5944535653 (from desmos)


def f(x: float):
    numerator: float = np.sqrt(x) + np.cos(7 * x)
    original = pow(numerator, x) / 2
    squared = original**2
    return squared


def main():
    a: float = 1  # lower bound of integral
    b: float = 3  # upper bound of integral
    n: int = int(7.83e6)  # number of subintervals

    delta = (b - a) / n

    mid = sum([f(a + (i - 0.5) * delta) for i in range(1, n + 1)]) * delta * np.pi

    trap = (
        (0.5 * f(a) + sum([f(a + i * delta) for i in range(1, n)]) + 0.5 * f(b))
        * delta
        * np.pi
    )

    print("The estimated value of this definite integral using midpoint rule is", mid)
    print("The estimated value of this definite integral using trapezoid rule is", trap)


main()
