import sys
import pygame
from game.kick_text import KickText
from internal.config.game_settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from internal.ui.colors import PRETO


class Game:
    def __init__(self):
        pygame.init()
        self.play_music = True
        self.music_value = 0
        self.game_config()
        self.run()

    def game_config(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("DVD")
        self.clock = pygame.time.Clock()
        self.running = True
        self.text = KickText("DVD", 50, SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.mixer.init()
        self.change_music("internal/assets/ben_10.mp3")

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.key_events(event)

    def key_events(self, event):
        if event.key == pygame.K_ESCAPE:
            self.running = False
        if event.key == pygame.K_s:
            self.on_press_s_key()
        if event.key == pygame.K_SPACE:
            if self.play_music:
                self.play_music = False
                pygame.mixer.music.pause()
            else:
                self.play_music = True
                pygame.mixer.music.unpause()

    def change_music(self, dir):
        pygame.mixer.music.load(dir)
        pygame.mixer.music.play(-1)

    def on_press_s_key(self):
        if self.music_value == 0:
            self.change_music("internal/assets/7k.mp3")
            self.music_value += 1
        elif self.music_value == 1:
            self.change_music("internal/assets/te_esqueci.mp3")
            self.music_value += 1
        elif self.music_value == 2:
            self.change_music("internal/assets/ben_10.mp3")
            self.music_value = 0

    def onKick(self):
        self.text.update()

    def draw(self):
        self.screen.fill(PRETO)
        self.text.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.events()
            self.onKick()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
