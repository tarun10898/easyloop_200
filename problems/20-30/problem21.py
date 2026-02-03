def reversed_string(string_given: str) -> str:
    chars:list[str] = list(string_given)
    low:int =0
    high:int = len(chars)-1
    while low<high:
        chars[low],chars[high] = chars[high],chars[low]
        low+=1
        high-=1
    return ''.join(chars)


def solve():
    string_given: str = input("enter the string: ").strip()
    reversed_value: str = reversed_string(string_given)
    print(f"reversed string of {string_given} is {reversed_value}")
    vowel_count: int = 0
    for char in string_given:
        if char.lower() in 'aeiou':
            vowel_count += 1
    print(f"number of vowels in {string_given} is {vowel_count}")
    upper:str = string_given.upper()
    print(f"uppercase of {string_given} is {upper}")

if __name__ == "__main__":
    solve()