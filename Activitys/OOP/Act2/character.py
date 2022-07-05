
class Character():
    def __init__(self, real_name, super_name):
    
        self.name = real_name
        self.super = super_name

# setter
    def set_power(self, hero_power):
            self.power = hero_power
            
# getter
    def get_power(self):
        print(self.power)