if __name__ == "__main__":
    n:int = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    print(f"array size: {len(arr)}")
    print(f"array elements: {arr}")
    print(f"first_element: {arr[0]}")
    print(f"last_element: {arr[-1]}")
    print(f"sum: {sum(arr)}")
