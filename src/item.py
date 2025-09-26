class Item:
    """Base class for all collectible items in the game."""
    
    def __init__(self, x, y, item_type="generic"):
        self.x = x
        self.y = y
        self.item_type = item_type
        self.collected = False
        self.value = 10
        
    def collect(self, player):
        """Handle item collection by player."""
        if not self.collected:
            self.collected = True
            self.apply_effect(player)
            return True
        return False
        
    def apply_effect(self, player):
        """Apply item effect to player."""
        pass
        
class HealthPotion(Item):
    """Health restoration item."""
    
    def __init__(self, x, y):
        super().__init__(x, y, "health_potion")
        self.heal_amount = 50
        
    def apply_effect(self, player):
        """Restore player health."""
        pass
        
class Coin(Item):
    """Currency item for scoring."""
    
    def __init__(self, x, y, value=10):
        super().__init__(x, y, "coin")
        self.value = value
        
    def apply_effect(self, player):
        """Add score to player."""
        pass
