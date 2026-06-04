# src/comisiones.py


def calcular_comision(monto_orden: float, tipo_negocio: str) -> float:
    """
    Calcula la comisión que cobra la plataforma Barrio por cada orden.
    - Los 'restaurantes' pagan 10% de comisión.
    - Los 'food_trucks' pagan 5% de comisión.
    - Cualquier otro tipo paga 15% por defecto.
    - Si la orden es de más de $500, se le hace un descuento de $10 a la comisión final.
    """
    if monto_orden <= 0:
        raise ValueError("El monto de la orden debe ser mayor a cero")

    # Calcular comisión base
    if tipo_negocio == "restaurante":
        comision = monto_orden * 0.10
    elif tipo_negocio == "food_truck":
        comision = monto_orden * 0.05
    else:
        comision = monto_orden * 0.15

    # Aplicar beneficio por orden grande
    if monto_orden > 500:
        comision = comision - 10

    # Evitar que la comisión sea negativa por el descuento
    if comision < 0:
        comision = 0.0

    return round(comision, 2)
