from package.linkedList import LL

def ll_to_arr(ll:LL):
  arr = [None for i in range(ll.len())]
  curr = ll.head
  i = 0
  while curr is not None:
    arr[i] = curr.info
    i += 1
    curr = curr.next
  return arr

def getUnique(column:list) -> LL:
  unique = LL()
  for i in range(len(column)):
    exist = unique.find(column[i])
    if not exist: unique.append(column[i])
  return unique

def bubble_sort(arr:list) -> list:
  n = len(arr)
  # Traverse through all array elements
  for i in range(n):
    # Last i elements are already in place
    for j in range(0, n-i-1):
      # Traverse the array from 0 to n-i-1
      # Swap if the element found is greater than the next element
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

