class Radioactivos(Metales):
  def __init__(self, símbolo, nombre, electrones, número_atómico, ultima_capa, conductor, radioactividad):
    super().__init__(símbolo, nombre, electrones, número_atómico, ultima_capa, conductor)
    self.__radioactividad = radioactividad
    print("Se ha creado correctamente el radioactivo")

  @property
    def radioactividad(self):
      return self.__radioactividad

  @radioactividad.setter
    def radioactividad(self, radioactividadNuevo):
      self.__radioactividad = radioactividadNuevo

  def __str__(self):
    if self.__radioactividad == True:
      return super().__str__() + "\nRadioactividad: True"
    else:
      return super().__str__() + "\nRadioactividad: False"

  def ver_radioactividad(self):
    if self.__radioactividad == True:
      print("El átomo tiene radioactividad")
    else:
      print("El átomo NO tiene radioactividad")
