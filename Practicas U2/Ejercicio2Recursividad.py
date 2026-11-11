def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    if not depositos:
        return 0.0
    
    saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)
    deposito_actual = depositos[-1]
    
    return (saldo_anterior + deposito_actual) * (1 + tasa_interes)


print(calcular_saldo_final([1000, 2000, 1500], 0.05))