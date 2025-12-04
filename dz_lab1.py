def mechanical_energy_1(V, m, h):
    g = 10
    Ek = (m * V**2)/2
    En = m * g * h 
    return Ek + En


def mechanical_energy_2(m, V=0, h=0):
    g  = 10
    Ek = (m * V**2)/2
    En = m * g * h 
    return Ek + En


def mechanical_energy_3(**kwargs):
    m = kwargs['m']
    V = kwargs['V']
    h = kwargs['h']
    g = 10 
    Ek = (m * V**2)/2
    En = m * g * h 
    return Ek + En

print(mechanical_energy_3(m = 5, V = 10, h = 3))