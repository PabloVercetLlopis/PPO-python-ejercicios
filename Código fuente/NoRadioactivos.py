class NoRadioactivos(Metales):
  def __init__(self, símbolo, nombre, electrones, número_atómico, ultima_capa, conductor, no_radioactividad):
    super().__init__(símbolo, nombre, electrones, número_atómico, ultima_capa, conductor)
    self.__no_radioactividad = no_radioactividad
    print("Se ha creado correctamente el NO radioactivo")
   
  @property
    def no_radioactividad(self):
      return self.__no_radioactividad
  
  @no_radioactividad.setter
    def no_radioactividad(self, NOradioactividadNuevo):
      self.__no_radioactividad = NOradioactividadNuevo
  
  def __str__(self):
    if self.__no_radioactividad == False:
      return super().__str__() + "\nNO Radioactividad: False"
    else:
      return super().__str__() + "\nNO Radioactividad: True"
  
  def ver_radioactividad(self):
    if self.__no_radioactividad == True:
      print("El átomo tiene radioactividad")
    else:
      print("El átomo NO tiene radioactividad")
