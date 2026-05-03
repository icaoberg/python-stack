# python-stack

> [!WARNING]
> This implementation is inspired by a homework assignment from [15-213](https://www.cs.cmu.edu/~213/) at Carnegie Mellon University. It is intended for educational purposes only and is not suitable for production use.

[![CI](https://github.com/icaoberg/python-stack/actions/workflows/ci.yml/badge.svg)](https://github.com/icaoberg/python-stack/actions/workflows/ci.yml)
[![Release Status](https://img.shields.io/badge/release-v0.1-red.svg)](https://github.com/icaoberg/python-stack)
[![GitHub issues](https://img.shields.io/github/issues/icaoberg/python-stack.svg)](https://github.com/icaoberg/python-stack/issues)
[![GitHub forks](https://img.shields.io/github/forks/icaoberg/python-stack.svg)](https://github.com/icaoberg/python-stack/network)
[![GitHub stars](https://img.shields.io/github/stars/icaoberg/python-stack.svg)](https://github.com/icaoberg/python-stack/stargazers)
[![GitHub license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)

A simple naive implementation of a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) in Python.

The purpose of this repo is to serve as an example of how to set up a GitHub Actions workflow.

## Definition

> A collection of items in which only the most recently added item may be removed. The latest added item is at the top. Basic operations are push and pop. Also known as "last-in, first-out" or LIFO.

— Paul E. Black, *[stack](https://xlinux.nist.gov/dads/HTML/stack.html)*, Dictionary of Algorithms and Data Structures [online], NIST.

## When to Use

A stack is the right structure any time you need to reverse order or track state that must be unwound in reverse:

- **Function call management** — every programming language runtime uses a call stack to track active function calls and local variables.
- **Undo/redo** — text editors and drawing applications push actions onto a stack so they can be popped off in reverse order on undo.
- **Expression parsing** — compilers and calculators use stacks to evaluate arithmetic expressions and match parentheses.
- **Depth-first search (DFS)** — graph traversals use a stack (explicit or via recursion) to explore as deep as possible before backtracking.
- **Browser history** — the back button works by popping the most recently visited page off a stack.

## Requirements

- Python 3.6+

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/icaoberg/python-stack.git
cd python-stack
pip install -r requirements.txt
```

## Usage

```python
from Stack import Stack

s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.size())     # 3
print(s.peek())     # 3
print(s.pop())      # 3
print(s.size())     # 2
print(s.is_empty()) # False
print(s.tolist())   # [1, 2]
```

### Methods

| Method | Description |
|--------|-------------|
| `push(element)` | Add an element to the top of the stack |
| `pop()` | Remove and return the top element |
| `peek()` | Return the top element without removing it |
| `is_empty()` | Return `True` if the stack has no elements |
| `size()` | Return the number of elements in the stack |
| `tolist()` | Return a copy of the stack as a list |

## Testing

```bash
pytest tests.py
```

## Support

If you found this project helpful, consider buying me a coffee!

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/icaoberg)

## Copyright

Copyright © [icaoberg](https://github.com/icaoberg) at [Carnegie Mellon University](https://www.cmu.edu). All rights reserved.
