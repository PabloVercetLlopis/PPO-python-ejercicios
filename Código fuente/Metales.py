```
class Metales(Atomos):  
  def __init__(self, símbolo, nombre, electrones, número_atómico, ultima_capa, conductor):
    super().__init__(símbolo, nombre, electrones, número_atómico)
    self.__ultima_capa = ultima_capa
    self.__conductor = conductor
    print("Se ha creado correctamente el Metal")
  
  @property
    def ultima_capa(self):
      return self.__ultima_capa

  @ultima_capa.setter
    def ultima_capa(self, ultmia_capa_Nuevo):
      self.__ultima_capa = ultima_capa_Nuevo

  @property
    def conductor(self):
      return self.__conductor

  @conductor.setter
    def conductor(self, conductorNuevo):
      self.__conductor = conductorNuevo

  def __str__(self):
    if self.__conductor == True:
      return super().__str__() + "\nUltima capa: {} \nConductor: TRUE".format(self.__ultima_capa)
    else:
      return super().__str__() + "\nUltima capa: {} \nConductor: FALSE".format(self.__ultima_capa)

  def magnetismo(self):
    if "d" or "f" in ultima_capa:
      print("Este metal tiene propiedades magnéticas")
    else:
      print("Este metal NO tiene propiedades magnéticas")
```
