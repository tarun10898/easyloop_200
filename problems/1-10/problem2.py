import sys
def solve():
    values = sys.stdin.read().splitlines()

    if len(values) <3:
        return
    
    int_value: int = int(values[0])
    float_value: float = float(values[1])
    string_value: str = values[2].strip()

    print(f"interger value: {int_value}")
    print(f"int to float: {float(int_value)}")
    print(f"float value: {float_value}")
    print(f"float to int: {int(float_value)}")
    print(f"string value: {string_value}")
    print(f"string value to int: {int(string_value)}")


if __name__ == "__main__":
    solve()