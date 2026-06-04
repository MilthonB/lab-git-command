# import pytest

from comisiones import calcular_comision  # type: ignore


def test_calcular_comision_restaurante() -> None:

    # AAA

    # Arrange ( rrancar, preparar los datos para el test)
    monto: float = 100.0
    tipo: str = "restaurante"

    # Act ( Ejecutar la fucnion que se va a testear  )
    resultado: float = calcular_comision(monto, tipo)  # type: ignore

    # Assert ( Verifciar el resultado de la ejecionc de la funcion con el resultado esperado)
    assert (
        resultado == 10.0
    ), f"Se esperaba una comisión de 10.0 pero se obtuvo {resultado}"
