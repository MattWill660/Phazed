from enum import Enum
import numpy as np


class Element(Enum):
    H = 1
    He = 3
    C = 13
    P = 31
    Xe = 129


class Nuclei:
    """Class to contain information on nuclei"""

    def __init__(self, element='Xe'):
        self.element = element
        self.gamma = 33.5
        self.spin = 0.5


class Env:
    """Class to contain information on local environment"""

    def __init__(self):
        self.isoInts = []
        self.anisoInts = []
        self.T1 = 100
        self.T2 = 50
        self.T2star = 10
        self.dist = np.zeros((64, 64))

    def add_iso_int(self, strength=1000):
        self.isoInts.append(strength)

    def add_aniso_int(self, strength=1000):
        self.anisoInts.append(strength)


class Sample(Nuclei, Env):
    """Class for the sample being studied"""

    def __init__(self, name):
        Nuclei.__init__(self)
        Env.__init__(self)
        self.name = name
