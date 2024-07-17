plot = {
    'A': [('B', 4), ('D', 9)],
    'B': [('A', 4), ('C', 7)],
    'C': [('B', 7), ('D', 2)],
    'D': [('A', 9), ('C', 2)]}

def short(graph, post, goal=''):
    road = list(graph)
    dist = {node: 0 if node == post 
            else float('inf')
            for node in graph}
    path = {
        node: list()
        for node in graph
    }
    path[post].append(post)

    while road:
        now = min(road, key=dist.get)
        for point, num in graph[now]:
            if dist[point] > dist[now] + num:
                dist[point] = dist[now] + num
                if path[point] and path[point][-1] == point:
                    path[point] = path[now][:]
                else:
                    path[point].extend(path[now])
                path[point].append(point)
        road.remove(now)
    
    goal_val = [goal] if goal else graph
    print(dist)
    print(path)

    for val in goal_val:
        if val == post:
            continue
        print(f'{post} to {val}\nDistances: {dist[val]}\nPath: {" -> ".join(path[val])}')
    return dist, path

def long(graph, post):
    unit = [val for val in graph]
    dist = {note: float('inf') if note == post
            else 0
            for note in graph}
    path = {node: [] for node in graph}
    path[post].append(post)

    while unit:
        now = max(unit, key=dist.get)
        for point, num in graph[now]: 
            pass
        unit.remove(post)
