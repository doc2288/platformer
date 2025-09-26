#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Модуль меню игры
Содержит класс для отображения и обработки главного меню
"""

import pygame
from settings import *


class Menu:
    """Класс главного меню игры"""
    
    def __init__(self):
        """Инициализация меню"""
        # Шрифты
        self.title_font = pygame.font.Font(None, 72)
        self.menu_font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 36)
        
        # Пункты меню
        self.menu_items = [
            {'text': 'Новая игра', 'action': 'new_game'},
            {'text': 'Продолжить', 'action': 'continue'},
            {'text': 'Настройки', 'action': 'settings'},
            {'text': 'Выход', 'action': 'quit'}
        ]
        
        self.selected_item = 0
        self.animation_time = 0
        
        # Флаги для обработки действий
        self.should_start_game = False
        self.should_load_game = False
        self.should_quit = False
        
        # Цвета
        self.normal_color = (255, 255, 255)
        self.selected_color = (255, 255, 0)
        self.title_color = (100, 150, 255)
        
    def handle_event(self, event):
        """Обработка событий меню"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_item = (self.selected_item - 1) % len(self.menu_items)
            elif event.key == pygame.K_DOWN:
                self.selected_item = (self.selected_item + 1) % len(self.menu_items)
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self._execute_action()
                
    def _execute_action(self):
        """Выполнить действие выбранного пункта меню"""
        action = self.menu_items[self.selected_item]['action']
        
        if action == 'new_game':
            self.should_start_game = True
        elif action == 'continue':
            self.should_load_game = True
        elif action == 'settings':
            # TODO: реализовать меню настроек
            pass
        elif action == 'quit':
            self.should_quit = True
            
    def update(self):
        """Обновление анимации меню"""
        self.animation_time += 1
        
    def draw(self, screen):
        """Отрисовка меню"""
        # Отрисовка заголовка
        title_surface = self.title_font.render(GAME_TITLE, True, self.title_color)
        title_rect = title_surface.get_rect()
        title_rect.centerx = SCREEN_WIDTH // 2
        title_rect.y = 100
        screen.blit(title_surface, title_rect)
        
        # Отрисовка пунктов меню
        start_y = 300
        item_spacing = 80
        
        for i, item in enumerate(self.menu_items):
            # Выбор цвета
            if i == self.selected_item:
                color = self.selected_color
                # Эффект мигания для выбранного пункта
                alpha = int(128 + 127 * abs(pygame.math.Vector2(1, 0).rotate(self.animation_time * 5).x))
                color = (*color[:3], alpha) if len(color) == 4 else color
            else:
                color = self.normal_color
                
            # Отрисовка текста
            text_surface = self.menu_font.render(item['text'], True, color)
            text_rect = text_surface.get_rect()
            text_rect.centerx = SCREEN_WIDTH // 2
            text_rect.y = start_y + i * item_spacing
            
            # Отрисовка стрелки для выбранного пункта
            if i == self.selected_item:
                arrow_x = text_rect.left - 40
                arrow_y = text_rect.centery
                # Анимация стрелки
                offset = int(10 * abs(pygame.math.Vector2(1, 0).rotate(self.animation_time * 3).x))
                arrow_surface = self.menu_font.render('>', True, self.selected_color)
                screen.blit(arrow_surface, (arrow_x - offset, arrow_y - arrow_surface.get_height() // 2))
                
            screen.blit(text_surface, text_rect)
            
        # Отрисовка подсказки
        hint_text = 'Используйте стрелки для навигации, Enter для выбора'
        hint_surface = self.small_font.render(hint_text, True, (150, 150, 150))
        hint_rect = hint_surface.get_rect()
        hint_rect.centerx = SCREEN_WIDTH // 2
        hint_rect.y = SCREEN_HEIGHT - 100
        screen.blit(hint_surface, hint_rect)
        
    def reset_flags(self):
        """Сбросить все флаги действий"""
        self.should_start_game = False
        self.should_load_game = False
        self.should_quit = False
