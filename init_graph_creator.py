import osmnx as ox

#название места для поиска в OSM
place = "Baku, Azerbaijan"

#загрузка дорожного графа для автомобилей - drive
G = ox.graph_from_place(place, network_type='drive')

#сохранение графа в формате GraphML
ox.save_graphml(G, filepath='baku_drive.graphml')
