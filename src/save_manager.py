import json
import os

class SaveManager:
    """Handles saving and loading game progress."""
    
    def __init__(self, save_directory="saves"):
        self.save_directory = save_directory
        self.current_save_file = None
        self.ensure_save_directory()
        
    def ensure_save_directory(self):
        """Create save directory if it doesn't exist."""
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)
            
    def save_game(self, save_name, game_data):
        """Save current game state to file."""
        save_path = os.path.join(self.save_directory, f"{save_name}.json")
        try:
            with open(save_path, 'w') as f:
                json.dump(game_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False
            
    def load_game(self, save_name):
        """Load game state from file."""
        save_path = os.path.join(self.save_directory, f"{save_name}.json")
        try:
            with open(save_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading game: {e}")
            return None
            
    def get_save_files(self):
        """Get list of available save files."""
        saves = []
        for file in os.listdir(self.save_directory):
            if file.endswith('.json'):
                saves.append(file[:-5])  # Remove .json extension
        return saves
        
    def delete_save(self, save_name):
        """Delete a save file."""
        save_path = os.path.join(self.save_directory, f"{save_name}.json")
        try:
            os.remove(save_path)
            return True
        except Exception as e:
            print(f"Error deleting save: {e}")
            return False
