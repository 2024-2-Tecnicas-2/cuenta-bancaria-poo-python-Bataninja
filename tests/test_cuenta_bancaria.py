import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from cuenta_bancaria import CuentaBancaria


class TestCuentaBancaria(unittest.TestCase):
    
    def setUp(self):
        self.cuenta1 = CuentaBancaria("Jhon Doe", "505051", 0)
        self.cuenta2 = CuentaBancaria("Mark Doe", "500001",50000)
    
    def test_getTitular1(self):
        self.assertEqual(self.cuenta1.getTitular(), "Jhon Doe")

    def test_getTitular2(self):
        self.assertEqual(self.cuenta2.getTitular(), "Mark Doe")

    def test_setTitular1(self):
        self.cuenta1.setTitular("N N")
        self.assertEqual(self.cuenta1.getTitular(), "N N")

    def test_setTitular2(self):
        self.cuenta2.setTitular("")
        self.assertEqual(self.cuenta2.getTitular(), "")

    def test_getNumeroCuenta1(self):
        self.assertEqual(self.cuenta1.getNumeroCuenta(), "505051")

    def test_getNumeroCuenta2(self):
        self.assertEqual(self.cuenta2.getNumeroCuenta(), "500001")

    def test_getSaldoCuenta1(self):
        self.assertEqual(self.cuenta1.getSaldo(), 0)

    def test_getSaldoCuenta2(self):
        self.assertEqual(self.cuenta2.getSaldo(), 50000)

    def test_getIngresarCuenta1_Negativo(self):
        self.cuenta1.ingresar(-1)
        self.assertEqual(self.cuenta1.getSaldo(), 0)

    def test_getIngresarCuenta2_Positivo(self):
        self.cuenta2.ingresar(10000)
        self.assertEqual(self.cuenta2.getSaldo(), 60000)

    def test_getRetirarCuenta1_NoSaldo(self):
        self.cuenta1.retirar(1)
        self.assertEqual(self.cuenta1.getSaldo(), 0)

    def test_getRetirarCuenta2_Positivo(self):
        self.cuenta2.retirar(10000)
        self.assertEqual(self.cuenta2.getSaldo(), 40000)

    def test_getCalcularInteresCuenta1(self):
        self.assertEqual(self.cuenta1.calcularInteres(), 0)

    def test_getCalcularInteresCuenta2(self):
        self.assertEqual(self.cuenta2.calcularInteres(), 50000+(50000*1.5/100))

    def test_getSetTipoInteresCuenta1_MayorQue10(self):
        self.cuenta1.setTipoInteres(11)
        self.assertEqual(self.cuenta1.tipoInteres, 1.5)

    def test_getSetTipoInteresCuenta2_IgualA10(self):
        self.cuenta2.setTipoInteres(10)
        self.assertEqual(self.cuenta2.calcularInteres(), 50000+(50000*10/100))

if __name__ == '__main__':
    unittest.main()