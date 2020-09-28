class Node:
	next = None
	prev = None
	def __init__(self, data):
		self.data = data 


	def display(self):
		print(f"{self.data}",end="")

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def push_head(self,data):
		new = Node(data)
		if self.isEmpty():
			self.tail = new
		else:
			self.head.prev = new
		new.next = self.head
		self.head = new

	def pull_head(self):
		temp = self.head
		self.head = self.head.next
		self.head.prev = None
		if self.head is None:
			self.tail = None
		return temp

	def push_tail(self, data):
		new = Node(data)
		new.next = None
		self.tail.next = new
		new.prev = self.tail 
		self.tail = new

	def pull_tail(self):
		temp = self.tail
		self.tail = self.tail.prev
		self.tail.next = None
		return temp

	def delete(self, value):
		if self.head.data == value:
			self.head = self.head.next
			self.head.prev = None
		elif self.tail.data == value:
			self.tail = self.tail.prev
			self.tail.next = None
		else:
			current = self.head.next
			while current.data != value:
				current = current.next
			current.prev.next = current.next
			current.next.prev = current.prev

	def isEmpty(self):
		return self.head is None

	def display(self):
		value = self.head
		while value is not None:
			value.display()
			value = value.next
		print()

dList = DoublyLinkedList()
dList.push_head(20)
dList.push_head(30)
dList.push_head(40)
dList.delete(40)
dList.delete(20)
dList.delete(30)
dList.display()

