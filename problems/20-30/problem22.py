def solve():
    string1: str = input("enter the first string").strip()
    string2: str = input("enter the second string").strip()
    
    if string2 in string1:
        print(f"{string2} is a substring of {string1}")
    else:
        print(f"{string2} is not a substring of {string1}")

    if string1 == string2:
        print(f"{string1} and {string2} are equal")
    else:
        print(f"{string1} and {string2} are not equal")

             

if __name__ == "__main__":
    solve()