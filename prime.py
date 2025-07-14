import math


def is_prime(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def main():
    """tiene toda la lógica principal"""

    for i in range(100):
        if is_prime(i):
            print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
