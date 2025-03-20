import random


def generate_random_color():
        return (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )