#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Основной модуль игры - Платформер
Содержит инициализацию игры и основной игровой цикл
"""

import pygame
import sys
from settings import *
from menu import Menu
from player import Player
from level_loader import LevelLoader
from sound_manager import SoundManager
from save_manager import SaveManager


class Game:
    """Основной класс игры"""
    
    def __init__(self):
        """Инициализация игры"""
        pygame.init()
        
        # Настройка экрана
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        
        # Игровые объекты
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GAME_STATE_MENU
        
        # Менеджеры
        self.sound_manager = SoundManager()
        self.save_manager = SaveManager()
        self.level_loader = LevelLoader()
        
        # Игровые объекты
        self.menu = Menu()
        self.player = None
        self.current_level = None
        
        # Игровые переменные
        self.game_data = self.save_manager.load_game()
        
    def handle_events(self):
        """Обработка событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if self.state == GAME_STATE_MENU:
                self.menu.handle_event(event)
                if self.menu.should_start_game:
                    self.start_new_game()
                elif self.menu.should_load_game:
                    self.load_game()
                elif self.menu.should_quit:
                    self.running = False
                    
            elif self.state == GAME_STATE_PLAYING:
                if self.player:
                    self.player.handle_event(event)
                    
    def start_new_game(self):
        """Начать новую игру"""
        self.player = Player()
        self.current_level = self.level_loader.load_level(1)
        self.state = GAME_STATE_PLAYING
        
    def load_game(self):
        """Загрузить сохранённую игру"""
        if self.game_data:
            self.player = Player()
            self.player.load_from_data(self.game_data)
            level_num = self.game_data.get('current_level', 1)
            self.current_level = self.level_loader.load_level(level_num)
            self.state = GAME_STATE_PLAYING
            
    def update(self):
        """Обновление игровой логики"""
        if self.state == GAME_STATE_MENU:
            self.menu.update()
            
        elif self.state == GAME_STATE_PLAYING:
            if self.player and self.current_level:
                self.player.update()
                self.current_level.update(self.player)
                
                # Проверка завершения уровня
                if self.current_level.is_completed:
                    self.next_level()
                    
                # Проверка смерти игрока
                if self.player.is_dead:
                    self.player.respawn()
                    
    def next_level(self):
        """Переход на следующий уровень"""
        next_level_num = self.current_level.level_number + 1
        self.current_level = self.level_loader.load_level(next_level_num)
        if self.current_level:
            self.player.reset_position()
            self.save_manager.save_game({
                'current_level': next_level_num,
                'player_data': self.player.get_save_data()
            })
        else:
            # Игра пройдена
            self.state = GAME_STATE_MENU
            
    def render(self):
        """Отрисовка"""
        self.screen.fill(BACKGROUND_COLOR)
        
        if self.state == GAME_STATE_MENU:
            self.menu.draw(self.screen)
            
        elif self.state == GAME_STATE_PLAYING:
            if self.current_level:
                self.current_level.draw(self.screen)
            if self.player:
                self.player.draw(self.screen)
                
        pygame.display.flip()
        
    def run(self):
        """Основной игровой цикл"""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
