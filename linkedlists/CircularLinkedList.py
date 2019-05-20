class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class CircularList:
  def __ini__(self, data=None):
    self.head = None
    self.tail = None
    self.size = 0

  def clear(self):
    self.tail = None
    self.head = None

  def append(self, data):
    node = Node(data)
    if self.head:
      self.head.next = node
      self.head = node
    else:
      self.head = node
      self.tail = node
    self.head.next = self.tail
    self.size += 1

  def delete(self, data):
    current = self.tail
    prev = self.tail
    while prev == current or prev != self.head:
      if current.data == data:
        self.tail = current.next
        self.head.next = self.tail
      else:
        prev.next = current.next
        self.size -= 1
    return 
    prev = current
    current = current.next

  def iter(self):
    current = self.tail
    while current:
      val = current.data
      current = current.next
      yield val
