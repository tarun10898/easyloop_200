import sys
def solve():
    values: list[str] = sys.stdin.read().splitlines()
    a: int = int(values[0])
    b: int = int(values[1])

    print(f"sum: {a + b}")
    print(f"difference: {a - b}")
    print(f"product: {a * b}")
    if b != 0:
        print(f"quotient: {a / b}")
        print(f"remainder: {a % b}")

if __name__ == "__main__":
    solve()