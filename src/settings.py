#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Модуль настроек игры
Содержит все константы и конфигурацию игры
"""

# === Основные настройки ===
GAME_TITLE = "Платформер"
FPS = 60

# === Настройки экрана ===
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BACKGROUND_COLOR = (135, 206, 235)  # Небесно-голубой

# === Состояния игры ===
GAME_STATE_MENU = "menu"
GAME_STATE_PLAYING = "playing"
GAME_STATE_PAUSED = "paused"
GAME_STATE_GAME_OVER = "game_over"

# === Настройки игрока ===
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 48
PLAYER_SPEED = 5
PLAYER_JUMP_STRENGTH = -15
PLAYER_COLOR = (255, 100, 100)
PLAYER_START_X = 100
PLAYER_START_Y = 500

# === Настройки физики ===
GRAVITY = 0.8
TERMINAL_VELOCITY = 15
FRICTION = 0.8

# === Настройки платформ ===
PLATFORM_COLOR = (101, 67, 33)  # Коричневый
PLATFORM_WIDTH = 128
PLATFORM_HEIGHT = 32

# === Настройки врагов ===
ENEMY_WIDTH = 32
ENEMY_HEIGHT = 32
ENEMY_SPEED = 2
ENEMY_COLOR = (255, 0, 0)

# === Настройки боссов ===
BOSS_WIDTH = 64
BOSS_HEIGHT = 64
BOSS_SPEED = 1.5
BOSS_COLOR = (128, 0, 128)
BOSS_HEALTH = 5

# === Настройки предметов ===
ITEM_WIDTH = 24
ITEM_HEIGHT = 24

# Типы предметов
ITEM_COIN = "coin"
ITEM_HEALTH = "health"
ITEM_KEY = "key"
ITEM_POWERUP = "powerup"

# Цвета предметов
ITEM_COLORS = {
    ITEM_COIN: (255, 215, 0),      # Золотой
    ITEM_HEALTH: (0, 255, 0),      # Зелёный
    ITEM_KEY: (255, 255, 0),       # Жёлтый
    ITEM_POWERUP: (255, 0, 255)    # Маджента
}

# === Настройки уровней ===
LEVEL_WIDTH = 2048
LEVEL_HEIGHT = 768
TILE_SIZE = 32

# === Настройки камеры ===
CAMERA_SMOOTH = 0.1
CAMERA_DEADZONE_WIDTH = 200
CAMERA_DEADZONE_HEIGHT = 100

# === Настройки аудио ===
SOUND_VOLUME = 0.7
MUSIC_VOLUME = 0.5

# === Клавиши управления ===
# Используются константы pygame
KEY_LEFT = 'left'
KEY_RIGHT = 'right'
KEY_JUMP = 'space'
KEY_ATTACK = 'x'
KEY_PAUSE = 'escape'

# === Пути к файлам ===
ASSETS_DIR = "assets"
IMAGES_DIR = f"{ASSETS_DIR}/images"
SOUNDS_DIR = f"{ASSETS_DIR}/sounds"
MUSIC_DIR = f"{ASSETS_DIR}/music"
LEVELS_DIR = f"{ASSETS_DIR}/levels"
SAVES_DIR = "saves"

# === Настройки сохранений ===
SAVE_FILE = f"{SAVES_DIR}/save_game.json"
MAX_SAVE_SLOTS = 3

# === Настройки интерфейса ===
UI_FONT_SIZE = 24
UI_COLOR = (255, 255, 255)
UI_BACKGROUND_COLOR = (0, 0, 0, 128)

# === Настройки отладки ===
DEBUG_MODE = False
SHOW_FPS = True
SHOW_HITBOXES = False

# === Настройки сложности ===
DIFFICULTY_EASY = "easy"
DIFFICULTY_NORMAL = "normal"
DIFFICULTY_HARD = "hard"

DIFFICULTY_SETTINGS = {
    DIFFICULTY_EASY: {
        'enemy_speed_multiplier': 0.7,
        'player_health_multiplier': 1.5,
        'respawn_time': 1.0
    },
    DIFFICULTY_NORMAL: {
        'enemy_speed_multiplier': 1.0,
        'player_health_multiplier': 1.0,
        'respawn_time': 2.0
    },
    DIFFICULTY_HARD: {
        'enemy_speed_multiplier': 1.3,
        'player_health_multiplier': 0.7,
        'respawn_time': 3.0
    }
}

DEFAULT_DIFFICULTY = DIFFICULTY_NORMAL
