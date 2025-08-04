from stack_queue import push, pop, enqueue, dequeue

# Stack Test
print("Stack Test:")
push(10)
push(20)
print(pop())  # 20

# Queue Test
print("\nQueue Test:")
enqueue(1)
enqueue(2)
print(dequeue())  # 1

# LinkedList Test
from linked_list import LinkedList
print("\nLinked List Test:")
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.traverse()  # 30 -> 20 -> 10 -> None
ll.delete(20)
ll.traverse()  # 30 -> 10 -> None

# Array Test
import array_operations as ao
print("\nArray Test:")
ao.insert(2, 99)
print(ao.arr)
ao.delete(1)
print(ao.arr)
print(ao.access(2))

# Matrix Test
import matrix_operations as mo
print("\nMatrix Test:")
print(mo.matrix)
print(mo.access(2, 2))