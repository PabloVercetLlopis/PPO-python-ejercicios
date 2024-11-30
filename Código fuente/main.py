# Clase Producto
p1 = Producto(codigo = "TH43K", nombre = "Televisión", precio = 799, tipo = "Plasma")
print(p1)
print("="*40)
precio_final = p1.calcular_total(5)
print("El precio total para 5 unidades de {} es de:{}".format(p1.nombre, precio_final))

# Clase Atomos
a1 = Atomos(símbolo = "Mg", nombre = "Magnesio", electrones = 12, número_atómico = 12)
print(a1)
print("="*40)
print(a1.perder_electron())
print("="*40)
print(a1.ganar_electron())
print("="*40)
print(a1.ver_carga())

# Clase Semimetales
s1 = Semimetales(símbolo = "Pb", nombre = "Plomo", electrones = 82, número_atómico = 82, energia = 715.6, conductor = False)
print(s1)
print("="*40)
s1.encender_radiacion(790)
print("="*40)
s1.apagar_radiacion()
print("="*40)
s1.ver_carga()

# Clase Metales
m1 = Metales(símbolo = "Al", nombre = "Aluminio", electrones = 13, número_atómico = 13, ultima_capa = "p", conductor = True)
print(m1)
print("="*40)
m1.magnetismo()

# Clase Radioactivos
r1 = Radioactivos(símbolo = "U", nombre = "Uranio", electrones = 92, número_atómico = 92, ultima_capa = "f", conductor = False, radioactividad = True)
print(r1)
print("="*40)
r1.ver_radioactividad()

# Clase NoRadioactivos
r1 = NoRadioactivos(símbolo = "C", nombre = "Carbono", electrones = 6, número_atómico = 6, ultima_capa = "p", conductor = True, no_radioactividad = False)
print(r1)
print("="*40)
r1.ver_radioactividad()
