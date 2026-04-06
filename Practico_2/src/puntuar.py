# src/puntuar.py

def obtener_ganador_ronda(scores_ronda):
   
    max_puntos = -1
    ganador = ""
    
    for nombre, jueces in scores_ronda.items():
        total_jugador = sum(jueces.values()) 
        if total_jugador > max_puntos:
            max_puntos = total_jugador
            ganador = nombre
            
    return ganador, max_puntos

def procesar_competencia(lista_rounds):
    # Guarda estadísticas de cada cocinero
    stats = {}

    for ronda in lista_rounds:
        tema = ronda['theme']
        scores = ronda['scores']
        
        ganador, puntos = obtener_ganador_ronda(scores)
        print(f"Ronda {tema} - Ganador: {ganador} ({puntos} pts)")

        # Estadísticas generales
        for nombre, jueces in scores.items():
            puntos_ronda = sum(jueces.values())
            
            # Si no existe
            if nombre not in stats:
                stats[nombre] = {"total": 0, "ganadas": 0, "mejor": 0, "rondas_contadas": 0}
            
            stats[nombre]["total"] += puntos_ronda
            stats[nombre]["rondas_contadas"] += 1
            
            if puntos_ronda > stats[nombre]["mejor"]:
                stats[nombre]["mejor"] = puntos_ronda

            if nombre == ganador:
                stats[nombre]["ganadas"] += 1

    return stats

  

def obtener_total(item):
    stats_del_cocinero = item[1]
    return stats_del_cocinero['total']