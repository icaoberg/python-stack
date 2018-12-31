from Stack import Stack

def test_empty():
	s = Stack()
	assert s.isEmpty()
	assert s.size() == 0

def test_it():
	s = Stack()
	for i in range(10):
		s.push(i)
		assert s.size() == i+1
		assert s.peek() == i

	for i in reversed(range(10)):
		assert s.size() == i+1
		assert s.peek() == i
		assert s.pop() == i
		assert s.size() == i
