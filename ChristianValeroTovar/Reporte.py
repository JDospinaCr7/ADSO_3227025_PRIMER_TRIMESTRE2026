from abc import ABC, abstractmethod
class GenerarReporte(ABC):
    @abstractmethod
    def generar_reporte(self) -> None:
        pass

class SistemaPago(ABC):
    def __init__(self, monto: float) -> None:
        self.monto = monto # atributo comun sin privar

    @abstractmethod
    def procesar_pago(self) -> None:
    # Metodo obligatorio definido en la clase abstracta
        pass

class PagoBancario(SistemaPago, GenerarReporte):
    def generar_reporte(self) -> None:
        print(f"Reporte: pago realizado mediante sistema bancario")
    
    def procesar_pago(self) -> None:
        print(f"Procesando la transferencia bancaria por ${self.monto:,.2f}")


class PagoCriptomonedas(SistemaPago):
    def procesar_pago(self) -> None:
        print(f"Procesando pago Criptomonedas, por ${self.monto:,.2f}")


def ejecutar_pago(pago: SistemaPago) -> None:
    pago.procesar_pago()

def main():
    print("******   ===   Sistema de pagos On interfases Abiertas   ===   ******")

    pago1 = PagoBancario(30000)
    pago2 = PagoCriptomonedas(50000)
    ejecutar_pago(pago1)
    pago1.generar_reporte() 
    print("Ahora con cryptos")
    ejecutar_pago(pago2)



if __name__ == "__main__":
    main()