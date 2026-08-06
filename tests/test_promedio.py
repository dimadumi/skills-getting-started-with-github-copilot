import pytest
from src.app import promedio


def test_promedio_enteros():
    assert promedio([1, 2, 3]) == pytest.approx(2.0)


def test_promedio_flotantes():
    assert promedio([4.5, 3.0]) == pytest.approx(3.75)


def test_promedio_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        promedio([])


@pytest.mark.parametrize("nums, expected", [
    ([-1, -2, -3], -2.0),
    ([1, 2.5, 3], (1 + 2.5 + 3) / 3),
    ([42], 42),
    (list(range(1000)), sum(range(1000)) / 1000),
])
def test_promedio_varios(nums, expected):
    assert promedio(nums) == pytest.approx(expected)


def test_promedio_valor_no_numerico_lanza_typeerror():
    with pytest.raises(TypeError):
        promedio([1, 'a', 3])
