from typing import List

def binarySearchIter(arr: List[int], target: int):
    low = 0
    high = len(arr) - 1


    while (low <= high):
        mid = low + (high - low)//2
        if (arr[mid] == target):
            return mid
        elif (arr[mid] > target):
            high = mid-1
        else:
            low = mid+1
    
    return -1 # skeptical about this cuz python allows negative indexing

def main():
    target = int(input("give me tha darrn target fker: "))
    print("good let's proceed with your castr... [ brainrot NSFW] \n")
    arr = list(map(int, input("Enter the array to search in separated by single space: ").strip().split(" ")))
    result = binarySearchIter(arr, target)
    print("\nTarget is at index: %d" % result)

if __name__ == "__main__":
    main()