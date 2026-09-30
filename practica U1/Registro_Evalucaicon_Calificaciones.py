
def mostrar_encabezado_escuela():
    """
    Instituto mega chido de México
        -- REGISTRO DE CALIFICACIONES --
    """
def obtener_nota_minima_aprobatoria():
    return(6.0)

def evaluar_rendimiento(nota_final):
    if nota_final > 7:
        return("Reprobado")
    elif nota_final >= 7 and nota_final <= 9.4:
        return("Aprobado")
    elif nota_final >= 9.5 and nota_final <= 10:
        return("Exelente")

def calcular_promedio_ponderado(nota_examen,nota_tareas):
    calificacion_examen = float(nota_examen) * 0.7
    calificacion_tareas = float(nota_tareas) * 0.3
    return round(calificacion_examen + calificacion_tareas,1)

def generar_boleta(nombre_alumno,nota_examenes,nota_tareas):
    enExtraordinario = "No"
    calificacion_final = calcular_promedio_ponderado(nota_examenes,nota_tareas)

    if calificacion_final < obtener_nota_minima_aprobatoria():
        enExtraordinario = "Si"

    estado_academico = evaluar_rendimiento(calificacion_final)
    print(f"""
        {mostrar_encabezado_escuela()}
Alumno: {nombre_alumno}
Nota final: {calificacion_final}
Estado: {estado_academico}
Requiere Extraordinario: {enExtraordinario}
""")


nombre_alumno = input("Ingrese el nombre del alumno: ")
nota_examenes = input("Ingrese la nota del examen: ")
nota_tareas = input("Ingrese la nota de las tareas: ")



generar_boleta(nombre_alumno,nota_examenes,nota_tareas)