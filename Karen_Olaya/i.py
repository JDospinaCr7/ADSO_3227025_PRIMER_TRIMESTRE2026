from ast import Pass
from typing import Self
from abc  import ABC, abstractmethod

class Empleado(abc):
  self._nombre = None
  self.nombre = nombre

  @property
  def nombre(self) -> str:
    return self._nombre
  @nombre.setter
  def nombre(self, nombre: str) -> None:

    if isinstance(valor, str) and valor.strip():
      self._nombre = valor.strip()
    else:
      raise ValueError("error")

  @abstractmethod
  def trabajar(Self) -> None:
    pass

  class Gerente(empleado):
    def trabajar(self) -> None:
      print(f"{self.nombre} abstraccion")

  class Desarrollador(empleado: Empleado) -> None:
  empleado.trabajar()
  def ejecutar_tarea()

  def main():

    gerente1 = Gerente("Laura")
    Desarrollador1 = Desarrollador("Kevin Jean")
    ejecutar_tarea(gerente1)
    ejecutar_tarea(Desarrollador1)
    print("\n******************")
    print("Actulizando el nombre del desarrollador")
    Desarrollador1.nombre = "Pedrito perez"
    print(f"El nuevo desarrollador es {Desarrollador1.nombre}")

  if __name__ == "__main__"
      main()
