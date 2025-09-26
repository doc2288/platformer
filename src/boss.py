from enemy import Enemy

class Boss(Enemy):
    """Boss enemy class - stronger than regular enemies."""
    
    def __init__(self, x, y, boss_type="default"):
        super().__init__(x, y, health=500)
        self.boss_type = boss_type
        self.speed = 1
        self.attack_power = 50
        self.phase = 1
        self.special_attacks = []
        
    def update(self):
        """Update boss state and behavior."""
        super().update()
        self.check_phase_change()
        
    def check_phase_change(self):
        """Change boss phase based on health."""
        if self.health <= 250 and self.phase == 1:
            self.phase = 2
            self.enter_phase_2()
            
    def enter_phase_2(self):
        """Activate phase 2 abilities."""
        self.speed = 1.5
        self.attack_power = 75
        
    def special_attack(self, player):
        """Perform special boss attack."""
        pass
        
    def summon_minions(self):
        """Summon enemy minions."""
        pass
