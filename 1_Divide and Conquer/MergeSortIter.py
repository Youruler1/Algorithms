from typing import List

def Merge(A: List[int], start: int, mid: int, end: int) -> None:
    p = start
    q = mid + 1

    # to record size of resultant concatenated list
    k = 0
    # ancillary list that is later used to update original list A
    Arr = []

    for i in range(start, end+1):
        if (p > mid):
            Arr.append(A[q])
            # k += 1
            q += 1
        elif (q > end):
            Arr.append(A[p])
            # k += 1
            p += 1
        elif (A[p] <= A[q]):
            Arr.append(A[p])
            # k += 1
            p += 1
        else:
            Arr.append(A[q])
            # k += 1
            q += 1
    
    # now copying Arr into relevant section of A
    for i in range(len(Arr)):
        A[start] = Arr[i]
        start += 1


def MergeSortIter(A: List[int], start: int, end: int):
    if (start >= end): return
    mid = (start + end)//2
    MergeSortIter(A, start, mid)
    MergeSortIter(A, mid+1, end)
    Merge(A, start, mid, end)

def main():
    A = list(map(int, input("Enter the elements in the array: ").strip().split(" ")))
    start = 0
    end = len(A)-1
    MergeSortIter(A, start, end)
    print(A)
    

if __name__ == "__main__":
    main()
