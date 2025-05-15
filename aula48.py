class car:
    def __init__(self, name):
        self.name = name 
        self._engine = None
        self._manufacturer = None
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value):
        self._engine = value
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value

class engine:
    def __init__(self, name):
        self.name = name
    
class manufacturer:
    def __init__(self, name):
        self.name = name
    
beetle = car('Bettle')
volkswagen = manufacturer('volkswagen')
engine_1_0 = engine('1.0')

beetle.manufacturer = volkswagen
beetle.engine = engine_1_0

print(beetle.name, beetle.manufacturer.name, beetle.engine.name)

gol = car('Gol')
gol.manufacturer = volkswagen
gol.engine = engine_1_0

print(gol.name, gol.manufacturer.name, gol.engine.name)

