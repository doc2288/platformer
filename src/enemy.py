class Enemy:
    """Base enemy class for all game enemies."""
    
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.speed = 2
        self.direction = 1
        
    def update(self):
        """Update enemy state and movement."""
        pass
        
    def move(self):
        """Handle enemy movement AI."""
        pass
        
    def attack(self, player):
        """Attack the player if in range."""
        pass
        
    def take_damage(self, damage):
        """Take damage and handle death."""
        self.health -= damage
        if self.health <= 0:
            self.die()
            
    def die(self):
        """Handle enemy death."""
        pass
