def solve():
    a=input().strip() == "true"

    b=input().strip() == "true"

    print(f"A AND B: {str(a).lower()} and {str(b).lower()} = {str(a and b).lower()}")
    print(f"A OR B: {str(a).lower()} or {str(b).lower()} = {str(a or b).lower()}")
    print(f"Not A: not {str(a).lower()} = {str(not a).lower()}")
    print(f"Not B: not {str(b).lower()} = {str(not b).lower()}") 
if __name__ == "__main__" :
    solve()