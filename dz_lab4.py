import numpy as np
import matplotlib.pyplot as plt 

def logarifmic_spir(b):
    phi = np.arange(0, 8*np.pi, 0.01)
    r = np.exp(b * phi)

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y)
    plt.savefig('logarifmic_spir.png')

logarifmic_spir(0.3)
plt.close()



def arhimed_spir(k):
    phi = np.arange(0, 8*np.pi, 0.01)
    r = k * phi

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y)
    plt.savefig('arhimed_spir.png')

arhimed_spir(0.5)
plt.close()



def spiral_wand(k):
    phi = np.arange(0.25, 8*np.pi, 0.01)
    r = k / phi**0.5

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('spiral_wand.png')

spiral_wand(0.9)
plt.close()


def rose(k):
    phi = np.arange(0.01, 8*np.pi, 0.09)
    r = np.sin(k*phi)

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y)
    plt.savefig('rose')

rose(9)