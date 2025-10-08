from src.calculadora import soma
from src.calculadora import subtrair

def test_soma():
  assert soma(2, 3) == 5

def test_subtracao():
  assert subtrair(10, 5) == 5