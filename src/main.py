import pygame

from entities.character.Character import Character
from src.LevelData import LevelData
from tiles.base.Tile import Tile


def main ():
    pygame.init()
    pygame.display.set_caption("2d platform game it")
    screen = pygame.display.set_mode((1600, 900))
    running = True
    tiles = [Tile(500, 500, "Grass")]
    tiles.append(Tile(300, 300, "Grass"))

    DATA = LevelData(98.2)
    lastFrameTicks = 0

    player = Character(200, 200, "character", 10)

    while (running):
        screen.fill((100, 100, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate deltaTime
        t = pygame.time.get_ticks()
        deltaTime = (t - lastFrameTicks) / 1000.0
        lastFrameTicks = t
        player.update(deltaTime, DATA)
        player.draw(screen)
        for tile in tiles:
            tile.draw(screen)
        pygame.display.update()

main()