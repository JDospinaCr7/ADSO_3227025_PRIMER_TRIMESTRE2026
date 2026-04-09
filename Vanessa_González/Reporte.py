from abc import ABC, abstractmethod

# Creamos la clase abstracta
class GenerarRporte(ABC):
      @abstractmethod
      def generar_reporte(self) -> None:
          pass
      
class SistemaPago(ABC):
    def __init__(self, monto: float) -> None:
        self.monto = monto # Atributo comun sin privar
        
    @abstractmethod
    def procesar_pago(self) -> None:
        # Metodo obligatorio definido en la clase abstracta
        pass
    
class PagoBancario(SistemaPago, GenerarRporte):
    def generar_reporte(self) -> None:
        print("REPORTE: Pago realizado mediante sistema bancario")
    def procesar_pago(self) -> None:
        print(f"Procesando la transferencia bancaria por ${self.monto:,.2f}")
        
class PagoCriptomoneda(SistemaPago):
    def procesar_pago(self) -> None:
        print(f"Procesando pago por la cripto moneda, por ${self.monto:,.2f}")
def ejecutar_pago(pago: SistemaPago) -> None:
        pago.procesar_pago()
def main():
    print("****** === SISTEMA DE PAGOS ON INTERFASES ABSTRACTAS === ******")
    pago1 = PagoBancario(30000)
    pago2 = PagoCriptomoneda(50000)
    ejecutar_pago(pago1)
    pago1.generar_reporte()
    print("\nAhora con criptos")
    ejecutar_pago(pago2)
if __name__ == "__main__":
    main()