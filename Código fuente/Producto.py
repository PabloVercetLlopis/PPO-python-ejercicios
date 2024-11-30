class Producto:
   def __init__(self, codigo, nombre, precio, tipo):
         self.codigo = codigo
         self.nombre = nombre
         self.precio = precio
         self.tipo = tipo
         print(f"Producto creado correctamente.")
         
  @property
    def codigo(self):
      return self.__codigo
      
  @codigo.setter
    def codigo(self, codigoNuevo):
      self.__codigo = codigoNuevo

  @property
    def nombre(self):
      return self.__nombre

  @nombre.setter
    def nombre(self, nombreNuevo):
      self.__nombre = nombreNuevo

  @property
    def precio(self):
      return self.__precio

  @precio.setter
    def precio(self, precioNuevo):
      self.__precio = precioNuevo

  @property
    def tipo(self):
      return self.__tipo

  @tipo.setter
    def tipo(self, tipoNuevo):
      self.__tipo = tipoNuevo
        
    def __str__(self):
      return "Codigo: {} \nNombre: {} \nPrecio: {}$ \nTipo: {}".format(self.__codigo, self.__nombre, self.__precio, self.__tipo)

    def calcular_total(self, unidades):
      return self.__precio*unidades
