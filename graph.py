import osmnx as ox
import random

G = ox.load_graphml("baku_drive.graphml")

#по всем дорогам идем
for u, v, key, data in G.edges(keys=True, data=True):

    #смотрим колво полос
    lanes = data.get('lanes', 1)  #по умолчанию 1 полоса
    if isinstance(lanes, list):
        lanes = int(lanes[0])
    elif isinstance(lanes, str):
        lanes = int(lanes)

    #симуляция пробки
    traffic_load = random.uniform(0.0, 1.0)

    #добавляем к дате полосы и пробки
    data['lanes_count'] = lanes
    data['traffic_load'] = traffic_load

    length_m = data.get('length', 100)  #длина участка в метрах,по умолчанию 100

    #чем длиннее дорога и больше пробка тем тяжелее ребро
    #большее количество полос немного смягчает вес
    #коэффициент 10 здесь означает что глухая пробка увеличивает штраф в 10 раз
    weight = (length_m / lanes) * (1 + traffic_load * 10)

    #сохраняем
    data['total_weight'] = weight


ox.save_graphml(G, "baku_weighted.graphml")
fig, ax = ox.plot_graph(
    G,
    node_size=5,          # Размер точек (перекрестков)
    edge_color="#999999", # Цвет дорог
    edge_linewidth=0.8,   # Толщина линий
    bgcolor="white"       # Фон
)