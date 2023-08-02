# Queue

Certainly! Below is a README file template for your Python program implementing a queue data structure:

# Queue Data Structure Python Program

## Introduction
Welcome to the Queue Data Structure Python program! This program demonstrates the implementation of a simple queue using a Python list. A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. It allows elements to be inserted at the rear and removed from the front.

## Requirements
This program requires Python 3.x to run.

## How to Run the Program
1. Clone or download the repository to your local machine.
2. Navigate to the project directory containing the Python script (`queue.py`).
3. Run the `queue.py` script using the following command:
   ```
   python queue.py
   ```
4. The program will execute, demonstrating the basic queue operations.

## Queue Class Description
The `Queue` class provides the following methods for working with the queue:
- `__init__`: Initializes an empty queue.
- `is_empty`: Checks if the queue is empty and returns a Boolean value.
- `enqueue`: Adds an element to the rear of the queue.
- `dequeue`: Removes and returns the element from the front of the queue.
- `size`: Returns the number of elements currently in the queue.

## Customization
Feel free to modify the `main()` function to test different operations on the queue. You can add or remove elements, check the queue's size, and see if it's empty.

## Example Usage
```python
q = Queue()

print("Is the queue empty?", q.is_empty())  # Output: True

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Size of the queue:", q.size())  # Output: 3
print("Dequeue item:", q.dequeue())  # Output: 10
print("Size of the queue after dequeue:", q.size())  # Output: 2
```

