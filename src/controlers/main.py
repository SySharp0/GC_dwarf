import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.galaxy import Galaxy

class GalaxyControler:
    galaxies = []

    @classmethod
    def save_galaxy(cls, galaxies: Galaxy):
        cls.galaxies.append(Galaxy)

    @classmethod
    def list_galaxy(cls, galaxies:Galaxy):
        cls.galaxies

    