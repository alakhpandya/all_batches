from random import choice

tsp = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0]
]

def createRandomRoute(tsp):
    noOfCities = len(tsp)
    cities = [i for i in range(noOfCities)]
    route = []
    while cities:
        newCity = choice(cities)
        route.append(newCity)
        cities.remove(newCity)
    return route

def findBestNeighbour(neighbours):
    min = findRouteLength(neighbours[0])
    min_route=neighbours[0]
    for neighbour in neighbours:
        current_length=findRouteLength(neighbour)
        if current_length<min :
            min=current_length
            min_route=neighbour

    return min_route,min

def findRouteLength(route):
    dist=0
    for i in range(len(route)-1):
        dist=dist+tsp[route[i]][route[i+1]]
    dist+=tsp[route[0]][route[-1]]
    return dist

def createNeighbour(route):
    neighbours=[]
    for i in range(len(route)):
        for j in range(i+1,len(route)):
            n1=route.copy()
            n1[i],n1[j]=n1[j],n1[i]
            neighbours.append(n1)
    return neighbours

def main():
    route = createRandomRoute(tsp)
    # print(route)
    while True:
        neighbors = createNeighbour(route)
        length1 = findRouteLength(route)
        tempRoute, length2 = findBestNeighbour(neighbors)
        if length1 <= length2:
                return route
        route = tempRoute

print(main())