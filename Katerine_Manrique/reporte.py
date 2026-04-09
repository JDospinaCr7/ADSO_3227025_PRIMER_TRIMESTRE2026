from abc import ABC,abstractmethod
class GenerarReporte(ABC):
    @abstractmethod
    def generar_reporte(self) -> None:
        pass
class Sistemapago(ABC):
    def __init__(self,monto:float) -> None:
        self.monto = monto #Atributo comun sin privar
    @abstractmethod
    def procesar_pago(self)-> None:
        #Metodo obligatorio definido en la clase abstracta
        pass
class Pagobancario(Sistemapago,GenerarReporte):
    def generar_reporte(self)-> None:
        print("REPORTE: pago realizado mediante sistema bancario")
    def procesar_pago(self)-> None:
        print(f"procesando la transferencia bancaria por ${self.monto:,.2f}")
class Pagocriptomoneda(Sistemapago):
        def procesar_pago(self)-> None:
            print(f"procesando pago CRIPTO MONEDAS, por ${self.monto:,.2f}")

def ejecutar_pago(pago: Sistemapago)->None:
    pago.procesar_pago() 

def main():
     print("*******==SISTEMA DE PAGOS CON INTERFASES ABSTRACTAS==********")
     pago1 = Pagobancario(30000)
     pago2 = Pagocriptomoneda(50000)
     ejecutar_pago(pago1)
     pago1.generar_reporte()
     print("\nAhora con CRIPTOS")
     ejecutar_pago(pago2)

if __name__=="__main__":
    main()

        
    
    