import pygame

# _sounds = {}

class GameMethods:
    def __init__(self, game):
        self.find_entities = lambda name: game.level.get_entities(name)
        self.restart_level = lambda: game.restart_level()
        self.load_next_level = lambda: game.load_next_level()
        self.get_level_dimensions = lambda: game.level.map_shape[::-1]
        self.load_level_by_index = lambda index: game.load_level(index)
        self.spawn_entity = lambda entity, x, y, *args: game.level.spawn_entity(entity, x, y)
        self.kill_entity = lambda entity: game.level.kill_entity(entity)
        self.get_level = lambda: game.level
        self.get_previous_level_index = lambda: game.previous_level_index
        self.load_level_failed_screen = lambda: self.load_level_by_index(-3)
        self.load_main_menu = lambda: self.load_level_by_index(0)
        self.get_last_level_coins = lambda: game.last_level_coins
        self.load_level_complete = lambda: self.load_level_by_index(-4)
        self.get_player_coins = lambda: game.get_player_coins()
        self.time_left = 0
        self.last_level_time_left = 0

    def play_sound(self, file_name: str):
        if file_name is not None:
            #if not file_name in _sounds:
            sound = pygame.mixer.Sound("../resources/sound/" + file_name)
            sound.play()
            #    _sounds[file_name] = sound
            #_sounds[file_name].play()