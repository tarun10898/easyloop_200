
import sys
def solve():
    values: list[str] = sys.stdin.read().splitlines()
    name: str = values[0].strip()
    age: int = int(values[1])
    height: float = float(values[2])
    lang: str = values[3].strip()

    print(f"Hello, my name is {name}, age is {age}, height is {height}m (height*10)cm  loves {lang}")

if __name__ == "__main__":
    solve()