class CuentaBancaria:
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
        self.tipoInteres = 1.5

    def getTitular(self):
        return self.titular

    def setTitular(self, titular):
        self.titular = titular
    
    def getNumeroCuenta(self):
        return self.numeroCuenta

    def getSaldo(self):
        return self.saldo
    
    def ingresar(self, cantidad):
        if(cantidad <= 0):
            print("El valor para ingresar es invalido.")
        else:
            self.saldo += cantidad

    def retirar(self, cantidad):
        if(cantidad <= 0 or cantidad > self.getSaldo()):
            print("El saldo es menor a la cantidad solicitada, o el valor a retirar es invalido")
        else:
            self.saldo -= cantidad
    
    def calcularInteres(self):
        return self.saldo + (self.saldo*self.tipoInteres/100)

    def setTipoInteres(self, tipoInteres):
        if(tipoInteres < 0 or tipoInteres > 10):
            print("Cantidad de interes ingresada es invalida")
        else:
            self.tipoInteres = tipoInteres


