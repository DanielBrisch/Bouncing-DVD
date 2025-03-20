from game.dvd import DVD
from utils.utils import generate_random_color


class DvdColors(DVD):
    def change_color(self):
        self.color = generate_random_color()
        self.text_surf = self.font.render(self.text, True, self.color)
    
    def draw(self, screen):
        screen.blit(self.text_surf, self.rect)