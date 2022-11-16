import random, math

from qutip import Bloch3d, basis


def generate_random_bloch():
    b = Bloch3d()
    b.xlabel = ['', '']
    b.ylabel = ['', '']
    b.vector_color = ['g', 'b', 'y']
    x1 = random.uniform(-1.0, 1.0)
    x2 = random.uniform(-math.sqrt(1 - x1 ** 2), math.sqrt(1 - x1 ** 2))
    x3 = random.choice([-math.sqrt(1 - x1 ** 2 - x2 ** 2), math.sqrt(1 - x1 ** 2 - x2 ** 2)])
    b.add_vectors([x1, x2, x3])
    return b