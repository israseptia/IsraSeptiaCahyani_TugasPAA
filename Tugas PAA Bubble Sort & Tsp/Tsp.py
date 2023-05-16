import math
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def tsp_nearest_neighbor(points):
    n = len(points)
    visited = [False] * n
    route = [0]  # Memulai dari titik awal (indeks 0)
    total_dist = 0

    visited[0] = True

    for _ in range(n - 1):
        curr_point = points[route[-1]]
        min_dist = float('inf')
        nearest_neighbor = None

        for i in range(n):
            if not visited[i]:
                dist = distance(curr_point, points[i])
                if dist < min_dist:
                    min_dist = dist
                    nearest_neighbor = i

        route.append(nearest_neighbor)
        visited[nearest_neighbor] = True
        total_dist += min_dist

    # Kembali ke titik awal
    route.append(0)
    total_dist += distance(points[route[-2]], points[0])

    return route, total_dist

# Menguji fungsi tsp_nearest_neighbor
points = [(1,2), (0,0), (1,1), (3,2), (2,2), (1,3)]
best_route, best_dist = tsp_nearest_neighbor(points)
print("Rute terpendek:", best_route)
print("Jarak terpendek:", best_dist)