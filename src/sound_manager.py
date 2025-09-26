import pygame

class SoundManager:
    """Manages all game sounds and music."""
    
    def __init__(self):
        self.sounds = {}
        self.music_volume = 0.7
        self.sfx_volume = 0.8
        self.current_music = None
        
        # Initialize pygame mixer if not already done
        if not pygame.mixer.get_init():
            pygame.mixer.init()
            
    def load_sound(self, name, file_path):
        """Load a sound effect."""
        try:
            sound = pygame.mixer.Sound(file_path)
            self.sounds[name] = sound
            return True
        except Exception as e:
            print(f"Error loading sound {name}: {e}")
            return False
            
    def play_sound(self, name, volume=None):
        """Play a sound effect."""
        if name in self.sounds:
            sound = self.sounds[name]
            if volume is None:
                volume = self.sfx_volume
            sound.set_volume(volume)
            sound.play()
            
    def load_music(self, file_path):
        """Load background music."""
        try:
            pygame.mixer.music.load(file_path)
            return True
        except Exception as e:
            print(f"Error loading music: {e}")
            return False
            
    def play_music(self, loops=-1, fade_in=0):
        """Play background music."""
        pygame.mixer.music.set_volume(self.music_volume)
        if fade_in > 0:
            pygame.mixer.music.fadeout(fade_in)
        pygame.mixer.music.play(loops)
        
    def stop_music(self, fade_out=0):
        """Stop background music."""
        if fade_out > 0:
            pygame.mixer.music.fadeout(fade_out)
        else:
            pygame.mixer.music.stop()
            
    def set_music_volume(self, volume):
        """Set music volume (0.0 to 1.0)."""
        self.music_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.music_volume)
        
    def set_sfx_volume(self, volume):
        """Set sound effects volume (0.0 to 1.0)."""
        self.sfx_volume = max(0.0, min(1.0, volume))
        
    def pause_music(self):
        """Pause background music."""
        pygame.mixer.music.pause()
        
    def unpause_music(self):
        """Unpause background music."""
        pygame.mixer.music.unpause()
