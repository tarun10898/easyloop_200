
# class Solution:
#     arr: list[int]
#     k : int
#     direction: str

#     def __init__(self, arr: list[int], k: int, direction: str) -> None:
#         self.arr = arr
#         self.k = k
#         self.direction = direction

#     def left_rotate(self) -> list[int]:
#         if self.direction != "left":
#             raise ValueError("direction should be left")
#         k : int = self.k % len(self.arr)
#         return self.arr[k:] + self.arr[:k]
    
#     def right_rotate(self)-> list[int]:
#         if self.direction != "right":
#             raise ValueError("direction should be right: ")
#         k: int = self.k % len(self.arr)
#         return self.arr[-k:] + self.arr[:-k]

# if __name__ == "__main__":
#     n:int = int(input("enter the number of elements in the array: "))
#     arr:list[int] = list(map(int,input("enter the eleements in the array: ").strip().split()))[:n]
#     k:int = int(input("enter the number of places it should move: "))
#     direction: str = input("enter the direction to move (left or right): ").strip().lower()

#     values: Solution = Solution(arr, k, direction)
#     if direction == "left":
#         left_roated_array: list[int] = values.left_rotate()
#         print(f"array after left rotation: {left_roated_array}" )
#     elif direction == "right":
#         right_roated_array: list[int] = values.right_rotate()
#         print(f"array after right rotation: {right_roated_array}")
#     else:
#         print("Invalid direction. Please enter 'left' or 'right'.")


# time complexity : O(n) as we are traversing the array once to perform the left or right rotation.
# space complexity : O(n) as we are creating a new array to store the rotated values


# class Solution:
#     arr: list[int]
#     k: int
#     direction: str

#     def __init__ (self, arr: list[int], k: int, direction: str) -> None:
#         self.arr  = arr
#         self.k = k % len(arr)
#         self.direction = direction


#     def reverse_array(self, start:int, end:int) -> None:
#         while start < end:
#             self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
#             start += 1
#             end -= 1

#     def left_rotate(self) ->  list[int]:
#         if self.direction != "left":
#             raise ValueError("direction should be left")
#         n: int = len(self.arr)
#         self.reverse_array(0, self.k-1)
#         self.reverse_array(self.k, n-1)
#         self.reverse_array(0, n-1)
#         return self.arr

    
#     def right_rotate(self) -> list[int]:
#         if self.direction != "right":
#             raise ValueError("direction should be right")
#         n: int = len(self.arr)
#         self.reverse_array(n-self.k, n-1)
#         self.reverse_array(0, n-self.k-1)
#         self.reverse_array(0,n-1)
#         return self.arr
        



# if __name__ == "__main__":
#     n:int = int(input("enter the number of elements in the array: "))
#     arr: list[int] = list(map(int,input(("enter the elements in the array: ")).strip().split()))[:n]
#     k:int = int(input("enter the number of places to rotate: "))
#     direction: str = input("enter the direction to rotate (left or right): ").strip().lower()

#     values: Solution = Solution(arr,k,direction)
#     if direction == "left":
#         left_rotated_array: list[int] = values.left_rotate()
#         print(f"arrary after the left rotation is: {left_rotated_array}")
#     elif direction == "right":
#         right_rotated_array: list[int] = values.right_rotate()
#         print(f"array after the right rotation is: {right_rotated_array}")
#     else:
#         print("invalid direction. please enter 'left' or 'right'.")



# time complexity : O(n) as we are traversing the array a few times to perform the left or right rotation.
# space complexity : O(1) as we are not using any extra space except for a few variables to store the results.  
