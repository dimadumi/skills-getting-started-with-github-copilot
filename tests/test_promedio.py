import pytest
from src.app import promedio


def test_promedio_enteros():
    assert promedio([1, 2, 3]) == pytest.approx(2.0)


def test_promedio_flotantes():
    assert promedio([4.5, 3.0]) == pytest.approx(3.75)


def test_promedio_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        promedio([])
