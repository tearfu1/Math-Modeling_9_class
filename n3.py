from const import svobodnoe_padenie as g

def energy(mass, height, speed):
    potential=mass*height*g
    kinetic=(mass*speed**2)/2
    en=kinetic+potential
    print(en)
energy(1, 1, 1)