# 5. Unión con prioridades (Intermedio). Dados dos diccionarios de precios (mismo universo de
# productos), crea un nuevo diccionario fusionado donde tengan prioridad los valores del
# segundo. Además, devuelve la lista de claves cuyo valor cambió respecto al primero.

mercadona_prices = {"Queso": 2.20, "Hamburguesas": 4.35, "Aceite": 7.50}
carrefour_prices = {"Queso": 2.00, "Aceite": 4.30, "Leche": 1.10}

# Directamente???
cheapest_groceries = mercadona_prices.copy()

changed_keys = [k for k, v in carrefour_prices.items()
                if k not in cheapest_groceries or cheapest_groceries[k] != v]

cheapest_groceries.update(carrefour_prices)

print(cheapest_groceries)
print(changed_keys)