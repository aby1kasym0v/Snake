from .directions import Direction
from .elements import Element
from typing import Optional
from .constants import *
import pygame



class Infrastructure:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, SCALE)

    def is_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
    def get_pressed_key(self) -> Optional[Direction]:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            return Direction.DOWN
        if key[pygame.K_RIGHT]:
            return Direction.RIGHT
        if key[pygame.K_DOWN]:
            return Direction.UP
        if key[pygame.K_LEFT]:
            return Direction.LEFT

        return None
    
    def fill_screen(self) ->None:
        self.screen.fill(SCREEN_COLOR)

    def draw_element(self, e: Element, color) -> None:
        pygame.draw.rect(
            self.screen,
            pygame.Color(color),
            (e.x * SCALE, e.y * SCALE,ElEMENT_SIZE, ElEMENT_RADIUS), 
            0,
            RADIUS,
        )


    def draw_score(self, score:int) -> None:
        self.screen.blit(
            self.font.render(f'Score: {score}', True, pygame.Color(SCORE_COLOR)),
            (5,5)
        )

    def draw_game_over(self) -> None:
        message = self.font.render("GAME OVER", True, pygame.Color(GAME_OVER_COLOR))
        self.screen.blit(
            message,
            message.get_rect(center = ((WIDTH // 2) * SCALE, (HEIGHT // 2 )* SCALE))
        )

    def update_and_tick(self):
        pygame.display.update()
        self.clock.tick(FPS)

    def quit(self):
        pygame.quit()


