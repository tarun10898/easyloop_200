import sys

def solve():
    values = sys.stdin.read().splitlines()

    # Ensure enough input lines
    if len(values) < 8:
       
        return

    int_value: int = int(values[0])
    str_value: str = values[1].strip()
    bool_value: bool = values[2].strip().lower() == "true"
    float_value: float = float(values[4])
    char_value: str = values[5].strip()[0]  # single character

    print(f'integer value: {int_value}')
    print(f'string value: {str_value}')
    print(f'boolean value: {bool_value}')
    print(f'float value: {float_value}')
    print(f'character value: {char_value}')

    new_int_value: int = int(values[6])
    int_value = new_int_value
    print(f'updated integer value: {int_value}')

    init_value: str = values[7].strip()
    print(f'initialized string value: {init_value}')

if __name__ == "__main__":
    solve()
