from .elements import Element
from collections import deque
from .directions import Direction

class Snake:
    def __init__(self, head:Element) -> None:
        self.deque = deque()
        self.deque.appendleft(head)
        self.direction = Direction.RIGHT

    def set_directions(self, new_direction:Direction) -> None:
        if len(self.deque) == 1 or new_direction.value % 2 != self.direction.value % 2:
            self.direction = new_direction


    def enqueue(self, head:Element) -> None:
        self.deque.appendleft(head)

    def dequeue(self) -> None:
        self.deque.pop()

    def get_new_head(self) -> Element:
        head = self.deque[0]
        if self.direction == Direction.UP:
            return Element(head.x , head.y +1)
        if self.direction == Direction.RIGHT:
            return Element(head.x + 1 , head.y)
        if self.direction == Direction.LEFT:
            return Element(head.x - 1, head.y)
        if self.direction == Direction.DOWN:
            return Element(head.x , head.y -1)
        

    def is_containers(self, e:Element) -> Element:
        try:
            self.deque.index(e)
            return True
        except ValueError:
            return False





