
from funciones import sumar


def test_sumar_positivos():
    assert sumar(2, 3) == 5


def test_sumar_negativos():
    assert sumar(-2, -3) == -5


def test_sumar_positivo_y_negativo():
    assert sumar(5, -3) == 2


def test_sumar_cero():
    assert sumar(5, 0) == 5


def test_sumar_decimales():
    assert sumar(2.5, 1.5) == 4.0

