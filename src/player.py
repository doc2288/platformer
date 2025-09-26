#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Модуль игрока
Содержит класс для управления игроком
"""

import pygame
from settings import *


class Player:
    """Класс игрока"""
    
    def __init__(self):
        """Инициализация игрока"""
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.health = 3
        self.is_dead = False
        
    def handle_event(self, event):
        """Обработка событий"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.on_ground:
                self.jump()
                
    def update(self):
        """Обновление состояния игрока"""
        keys = pygame.key.get_pressed()
        
        # Горизонтальное движение
        if keys[pygame.K_LEFT]:
            self.vel_x = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.vel_x = PLAYER_SPEED
        else:
            self.vel_x = 0
            
        # Применение гравитации
        self.vel_y += GRAVITY
        
        # Ограничение скорости падения
        if self.vel_y > TERMINAL_VELOCITY:
            self.vel_y = TERMINAL_VELOCITY
            
        # Обновление позиции
        self.x += self.vel_x
        self.y += self.vel_y
        
    def jump(self):
        """Прыжок"""
        self.vel_y = PLAYER_JUMP_STRENGTH
        self.on_ground = False
        
    def draw(self, screen):
        """Отрисовка игрока"""
        pygame.draw.rect(screen, PLAYER_COLOR, 
                        (self.x, self.y, self.width, self.height))
                        
    def get_rect(self):
        """Получить прямоугольник столкновений"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
        
    def reset_position(self):
        """Сброс позиции к начальной"""
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.vel_x = 0
        self.vel_y = 0
        
    def respawn(self):
        """Возрождение игрока"""
        self.is_dead = False
        self.health = 3
        self.reset_position()
        
    def get_save_data(self):
        """Получить данные для сохранения"""
        return {
            'x': self.x,
            'y': self.y,
            'health': self.health
        }
        
    def load_from_data(self, data):
        """Загрузить данные из сохранения"""
        player_data = data.get('player_data', {})
        self.x = player_data.get('x', PLAYER_START_X)
        self.y = player_data.get('y', PLAYER_START_Y)
        self.health = player_data.get('health', 3)
