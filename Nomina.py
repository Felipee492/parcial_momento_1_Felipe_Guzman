empleados = []

while True:
    print("\n--- SISTEMA DE NÓMINA - STARTUP ---")
    print("1. Registrar Empleado")
    print("2. Calcular Nómina Completa")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del empleado: ")
        salario = float(input("Salario Base Mensual: "))
        dias = int(input("Días trabajados (1-30): "))
        empleados.append({"nombre": nombre, "salario": salario, "dias": dias})
        print(f"Empleado {nombre} registrado con éxito.")

    elif opcion == "2":
        if not empleados:
            print("No hay empleados registrados en el sistema.")
        else:
            print("\n" + "="*40)
            print("DETALLE DE NÓMINA")
            print("="*40)
            for emp in empleados:
                # 1. Sueldo básico proporcional a los días trabajados
                sueldo_devengado = (emp["salario"] / 30) * emp["dias"]
                
                # 2. Auxilio de transporte (Regla: < 2 SMMLV aprox. $2.600.000)
                # Se paga proporcional a los días laborados
                val_transporte = 162000 if emp["salario"] <= 2600000 else 0
                aux_transporte = (val_transporte / 30) * emp["dias"]
                
                # 3. Deducciones de Ley (Salud 4% y Pensión 4% = 8%)
                # Se calculan sobre el sueldo devengado (sin incluir transporte)
                salud = sueldo_devengado * 0.04
                pension = sueldo_devengado * 0.04
                total_deducciones = salud + pension
                
                # 4. Neto a pagar
                neto_pagar = sueldo_devengado + aux_transporte - total_deducciones
                
                print(f"Empleado: {emp['nombre']}")
                print(f"  > Días Lab: {emp['dias']}")
                print(f"  > Sueldo Devengado: ${sueldo_devengado:,.0f}")
                print(f"  > Aux. Transporte:  ${aux_transporte:,.0f}")
                print(f"  > Salud y Pensión: -${total_deducciones:,.0f}")
                print(f"  > NETO A RECIBIR:   ${neto_pagar:,.0f}")
                print("-" * 20)

    elif opcion == "3":
        print("Saliendo del sistema...")
        break