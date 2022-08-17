import pygame as pg
import sys
from assets.button import Button
from settings import *
from world import World
from hud import HUD
from database import Database


class Atlys:
    def __init__(self):
        # Pygame Functionality
        pg.init()
        pg.font.init()
        pg.display.set_caption("Atlys - A Pirate Survival Adventure")
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN, pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.is_paused = False

        SCREEN_WIDTH = self.screen.get_width()
        SCREEN_HEIGHT = self.screen.get_height()

        # Database
        self.db = Database()

        # World Variables
        self.world = World()

        # HUD Variables
        self.hud = HUD(self.world.display_surface)

    def main_menu(self):
        """
        Main game menu with options for new game, load game, options, and quit
        """
        while True:

            menu_image = pg.image.load("assets/images/main_menu.jpg").convert()
            self.screen.blit(menu_image, (0, 0))

            mouse_pos = pg.mouse.get_pos()

            menu_font = pg.font.Font('assets/fonts/Cinzel-Regular.ttf', 200)
            menu_text = menu_font.render('Atlys', True, 'white')
            menu_rect = menu_text.get_rect(center=((SCREEN_WIDTH // 2) + menu_text.get_width() // 2, 100))

            play_button = Button(image=pg.image.load('assets/images/rect.png'), pos=(200, self.screen.get_height() / 2),
                                 text_input='Play Atlys', font=pg.font.Font('assets/fonts/Cinzel-Regular.ttf', 55),
                                 base_color="#d7fcd4", hovering_color="White")

            load_button = Button(image=pg.image.load('assets/images/rect.png'), pos=(200, self.screen.get_height() / 2 + 125),
                                 text_input='Load Saved', font=pg.font.Font('assets/fonts/Cinzel-Regular.ttf', 55),
                                 base_color="#d7fcd4", hovering_color="White")

            options_button = Button(image=pg.image.load('assets/images/rect.png'), pos=(200, self.screen.get_height() / 2 + 250),
                                 text_input='Options', font=pg.font.Font('assets/fonts/Cinzel-Regular.ttf', 55),
                                 base_color="#d7fcd4", hovering_color="White")

            quit_button = Button(image=pg.image.load('assets/images/rect.png'), pos=(200, self.screen.get_height() / 2 + 375),
                                 text_input='Quit', font=pg.font.Font('assets/fonts/Cinzel-Regular.ttf', 55),
                                 base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(menu_text, menu_rect)

            for btn in [play_button, load_button, options_button, quit_button]:
                btn.change_color(mouse_pos)
                btn.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if play_button.check_for_input(mouse_pos):
                        self.run()
                    elif options_button.check_for_input(mouse_pos):
                        self.run()
                    elif quit_button.check_for_input(mouse_pos):
                        pg.quit()
                        sys.exit()

            pg.display.update()

    def load_menu(self):
        pass

    def options_menu(self):
        pass

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.is_paused = not self.is_paused # Toggle pause game
                    elif event.key == pg.K_BACKSPACE:
                        pg.quit()
                        sys.exit()

            dt = self.clock.tick() / 1000
            if not self.is_paused:
                self.world.run(dt)
                self.hud.update(dt)
            pg.display.update()


if __name__ == '__main__':
    atlys = Atlys()
    atlys.run()
