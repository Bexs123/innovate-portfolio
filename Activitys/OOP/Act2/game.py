from character import Character

wolfy = Character("James Logan Howlette", "wolverine")
wolfy.set_power('Retractable adamantium claws')
bat = Character('Bruce Wayne', 'Batman')
bat.set_power('Genius-level intellect')

print(f"{wolfy.name} is actually the superhero {wolfy.super} and his power {wolfy.power}")
print(f"{bat.name} is actually the superhero {bat.super} and his power {bat.power}")

wolfy.get_power()
bat.get_power()