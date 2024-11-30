´´´ 
class Atomos:
 
  def __init__(self, símbolo, nombre, electrones, número_atómico):
    self.__símbolo = símbolo
    self.__nombre = nombre
    self.__electrones = electrones
    self.__número_atómico = número_atómico
    print("El átomo se ha creado correctamente")
  
  def __str__(self):
    return "Simbolo: {} \nNombre: {} \nElectrones: {} \nNúmero atómico: {}".format(self.__símbolo, self.__nombre, self.__electrones, self.__número_atómico)

  def perder_electron(self):
    self.__electrones = self.__electrones - 1
      return "Simbolo: {} \nNombre: {} \nElectrones: {} \nNúmero atómico: {}".format(self.__símbolo, self.__nombre, self.__electrones, self.__número_atómico)

  def ganar_electron(self):
    self.__electrones = self.__electrones + 1
      return "Simbolo: {} \nNombre: {} \nElectrones: {} \nNúmero atómico: {}".format(self.__símbolo, self.__nombre, self.__electrones, self.__número_atómico)

  def ver_carga(self):
    self.__ver_carga = int(self.__electrones - self.__número_atómico)
      return "Ver carga: {}".format(self.__ver_carga)
```
