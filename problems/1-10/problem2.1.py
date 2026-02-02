import sys
def solve():
    values: list[str] = sys.stin.read().splitlines()
    if len(values) <5:
        return
    int_value: str = values[0].strip()
    float_value:str = values[1].strip()
    bool_value: str = values[2].strip().lower() == "true"
    int_values :int = int(values[3])
    float_values: float = float(values[4])

    print(f"string value: {int(int_value)}")
    print(f"string value to float: {float(float_value)}")
    print(f"boolean value: {bool_value}")
    print(f"int to float: {float(int_values)}")
    print(f"int to string: {str(int_values)}")
    print(f"int to boolean: {int_values != 0}")
    print(f"float to int: {int(float_values)}")
    print(f"float to string: {str(float_values)}")  
    print(f"float to boolean: {float_values != 0.0}")
if __name__ == "__main__":
    solve()