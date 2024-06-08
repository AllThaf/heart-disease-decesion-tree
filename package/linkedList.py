class Node:
  def __init__(self, info):
    self.info = info
    self.next = None

class LL:
  def __init__(self):
    self.head = None
  
  def append(self, info):
    newNode = Node(info)

    if self.head is None:
      self.head = newNode
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.next = newNode

  def display(self):
    curr = self.head
    while curr is not None:  
      print(curr.info)
      curr = curr.next

  def len(self):
    curr = self.head
    count = 0
    while curr is not None:
      count += 1
      curr = curr.next
    return count

  def find(self, data):
    curr = self.head
    while curr is not None:
      if curr.info == data: return True
      curr = curr.next
    return False
