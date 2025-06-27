from typing import List

def BinarySearchRecur(arr: List[int], low: int, high: int, target: int):
    mid = low + (high-low)//2
    if high < low:
        return -1 # taaargeeet not found sed lyf
    if (arr[mid] == target):
        # print(mid)
        return mid
    elif (arr[mid] > target):
        # print(mid)
        return BinarySearchRecur(arr, low, mid-1, target)
    else:
        # print(mid)
        return BinarySearchRecur(arr, mid+1, high, target)
    

def main():
    target = int(input("Gimme the target fker: "))
    print("thnx loser\n")
    arr = list(map(int, input("Enter the array elements separated by one space: ").strip().split(" ")))
    print("good jooob maybe ur not so retarded after all\n")
    result = BinarySearchRecur(arr, 0, len(arr)-1, target)
    print("target is at index: %d" % result)

if __name__ == "__main__":
    main()
