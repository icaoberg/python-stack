import pytest
from Stack import Stack

def test_empty():
    s = Stack()
    assert s.is_empty()
    assert s.size() == 0
    assert len(s) == 0

def test_push():
    s = Stack()
    for i in range(10):
        s.push(i)
        assert s.size() == i + 1
        assert s.peek() == i

def test_pop_order():
    s = Stack()
    for i in range(10):
        s.push(i)
    for i in reversed(range(10)):
        assert s.size() == i + 1
        assert s.peek() == i
        assert s.pop() == i
        assert s.size() == i

def test_pop_empty():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()

def test_peek_empty():
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()

def test_tolist():
    s = Stack()
    s.push(1)
    s.push(2)
    result = s.tolist()
    result.append(99)
    assert s.size() == 2

def test_repr():
    s = Stack()
    s.push(1)
    s.push(2)
    assert repr(s) == "Stack([1, 2])"
