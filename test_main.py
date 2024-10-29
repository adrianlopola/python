import unittest
from main import verificar_edad_para_licencia

class TestVerificarEdadParaLicencia(unittest.TestCase):
    def test_edad_mayor_o_igual_a_18(self):
        # Prueba que debe pasar
        self.assertEqual(verificar_edad_para_licencia(18), "Puedes sacar el carnet de conducir.")
        self.assertEqual(verificar_edad_para_licencia(20), "Puedes sacar el carnet de conducir.")

    def test_edad_menor_a_18(self):
        # Prueba que debe pasar
        self.assertEqual(verificar_edad_para_licencia(16), "No puedes sacar el carnet de conducir.")

    def test_edad_negativa(self):
        # Prueba que debe fallar
        self.assertEqual(verificar_edad_para_licencia(-1), "Puedes sacar el carnet de conducir.")

if __name__ == "__main__":
    unittest.main()