from .elements import Element
from random import randrange
from .constants import *
from .snake import Snake

def get_random_element() -> Element:
    return Element(randrange(0, WIDTH), randrange(0, HEIGHT))

def gen_apple(snake:Snake):
    condidate = None
    while condidate is None:
        condidate = get_random_element()
        if snake.is_containers(condidate):
            condidate = None
    return condidate

def gen_center_element() -> Element:
    return Element( WIDTH // 2, HEIGHT // 2)

def is_field_containers(e:Element) -> bool:
    return 0 <= e.x < WIDTH and 0 <= e.y <= HEIGHT

def is_good_head(head:Element, snake:Snake) -> bool:
    return is_field_containers(head) and not snake.is_containers(head)
