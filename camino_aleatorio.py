from borracho import BorrachoTradicional, BorrachoMuyModerado, BorrachoDerecha
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, output_file, show

def saber_tipo_borracho(tipo_de_borracho):
    if tipo_de_borracho.__name__ == "BorrachoMuyModerado":
        return "Borracho Muy Moderado"
    elif tipo_de_borracho.__name__ == "BorrachoDerecha":
        return "Borracho Derecha"
    else:
        return "Borracho Tradicional"
        
def caminata(borracho, pasos, tipo_de_borracho):
    
    inicio = [borracho.posicion()]
    x_graph = [0]
    y_graph = [0]
    for _ in range(pasos-1):
        borracho.camina()
        x, y = borracho.posicion()
        x_graph.append(x)
        y_graph.append(y)
    tipo = saber_tipo_borracho(tipo_de_borracho)
    graficar_pasos(x_graph, y_graph, tipo, pasos)
    return borracho.distancia_origen()

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    
    borracho = []
    distancias = []
    
    for i in range(numero_de_intentos):
        borracho.append(tipo_de_borracho(nombre=f'Kike {i}'))
        simulacion_caminata = caminata(borracho[i], pasos, tipo_de_borracho)
        print(simulacion_caminata)
        distancias.append(round(simulacion_caminata, 1))
    print("diatancias",distancias)
    return distancias
    
def graficar_pasos(x_graph, y_graph, tipo, pasos):
    
    grafica = figure(title=tipo, x_axis_label='x axis', y_axis_label='y axis')
    grafica.line(x_graph, y_graph, legend_label=str(pasos)+' pasos')
    final_x = x_graph[-1]
    final_y = y_graph[-1]
    grafica.diamond_cross(0, 0, fill_color ="green", line_color ="green", size = 18)
    grafica.diamond_cross(final_x, final_y, fill_color ="red", line_color ="green", size = 18)
    recta_final_x = [0, final_x]
    recta_final_y = [0, final_y]
    grafica.line(recta_final_x, recta_final_y, line_width = 2, color="red")
    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
    
if __name__ == '__main__':
    distancias_de_caminata = [100000]
    numero_de_intentos = 1
    
    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
    main(distancias_de_caminata, numero_de_intentos, BorrachoMuyModerado)
    main(distancias_de_caminata, numero_de_intentos, BorrachoDerecha)