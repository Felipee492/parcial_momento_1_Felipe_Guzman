empleados = []

while True:
    print("\n--- SISTEMA DE NÓMINA ---")
    print("1. Registrar Empleado")
    print("2. Calcular Nómina")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        salario = float(input("Salario Base: "))
        dias = int(input("Días trabajados: "))
        empleados.append({"nombre": nombre, "salario": salario, "dias": dias})
        print("Empleado registrado.")

    elif opcion == "2":
        if not empleados:
            print("No hay empleados.")
        else:
            for emp in empleados:
                sueldo_base = (emp["salario"] / 30) * emp["dias"]
                # Regla de negocio
                transporte = 160000 if emp["salario"] < 2600000 else 0
                proporcional_transporte = (transporte / 30) * emp["dias"]
                
                descuento = sueldo_base * 0.08 # 8% salud y pension
                total = sueldo_base - descuento + proporcional_transporte
                
                print(f"\nEmpleado: {emp['nombre']}")
                print(f"Total a pagar: ${total:,.0f}")

    elif opcion == "3":
        break