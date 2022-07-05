from character import Character

spidey = Character("Peter Parker", "Spiderman")
spidey.set_power("Web-slinging")
hulk = Character("Bruse Banner", "Hulk")
hulk.set_power("smashing")

print(f"{spidey.name} is actually the superhero {spidey.super} and his power {spidey.power}")
print(f"{hulk.name} is actually the superhero {hulk.super} and his power {hulk.power}")

spidey.get_power()
hulk.get_power()