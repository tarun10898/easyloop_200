if __name__ == "__main__":
    number:int = int(input())
    print(f"Number: {number}")
    if number > 0:
        print("Sign: positive")
    elif number < 0:
        print("Sign: Negative")
    elif number % 2 == 0:
        print("Parity : even")   
    elif number % 2 != 0:
        print("Parity : odd")
               
