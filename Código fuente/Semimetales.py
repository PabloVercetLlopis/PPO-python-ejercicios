class Semimetales(Atomos):
  def __init__(self, símbolo, nombre, electrones, número_atómico, energia, conductor):
    super().__init__(símbolo, nombre, electrones, número_atómico)
    self.__energia = int(energia)
    self.__conductor = conductor
    print("Se ha creado con éxito el Semimetal")
  
  @property
    def energia(self):
      return self.__energia

  @energia.setter
    def energia(self, energiaNueva):
      self.__energia = energiaNueva

  @property
    def conductor(self):
      conductor = False
      return self.__conductor

  @conductor.setter
    def conductor(self, conductorNuevo):
      self.__conductor = conductorNuevo

  def __str__(self):
    if self.__conductor == False:
      return super().__str__() + "\nEnergia de ionización: {} \nConductor: FALSE".format(self.__energia)
    else:
      return super().__str__() + "\nEnergia de ionización: {} \nConductor: TRUE".format(self.__energia)

  def encender_radiacion(self, energia_radiacion):
    if energia_radiacion >= self.energia:
      print("La radiación se ha encendido porque la energia de radiacion es mayor")
      self.__conductor = True
    else:
      self.__conductor = False

  def apagar_radiacion(self):
    self.__conductor = False
    print("El conductor se ha apagado y es: {}".format(self.__conductor))

  def ver_carga(self):
    ver_carga = super().ver_carga
    print("La carga es: {}".format(ver_carga))
