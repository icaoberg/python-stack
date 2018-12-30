from Stack import Stack

def test_empty():
	s = Stack()
	assert s.isEmpty()
	assert s.size() == 0

def test_it():
	s = Stack()
	for i in range(100):
		s.push(i)
		assert s.size() == i+1
