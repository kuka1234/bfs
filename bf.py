import matplotlib.pyplot as plt

starting_point = [0, 0]
ending_point = [3, 2]
max_rows = 20
block_points = [[1, 2], [4, 4]]

queue = []
visited = set()
plotted_points = []



def create_blocks(block_points, max_rows):
    temp_list = []
    for i in block_points:
        for j in range(0, max_rows):
            temp_list.append([i[0], i[1] - j])

    block_points = temp_list
    return block_points


block_points = create_blocks(block_points, max_rows)


def init_graph(starting_point, ending_point, block_points):
    x, y = starting_point
    plt.scatter(x, y, c='red', marker='h', s=70)
    x, y = ending_point
    plt.scatter(x, y, c='green', marker='*', s=70)

    for i in block_points:
        x, y = i
        plt.scatter(x, y, c='black', marker='s', s=100)


init_graph(starting_point, ending_point, block_points)


def show_graph(current_point):
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    if current_point not in plotted_points:
        plotted_points.append(current_point)
        x, y = current_point
        plt.scatter(x, y)
        plt.pause(0.000000000001)

def bfs(starting_point, ending_point, block_points, graph: bool):
    main_dict = {}
    queue.append(starting_point)
    iterate_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    temp_start = 0
    temp_end = 0
    diff = 1
    counter = 0
    time = 0
    while queue:
        current_point = queue.pop(0)
        visited.add(tuple(current_point))

        if counter == diff:
            time += 1
            counter = 0
            diff = temp_end - temp_start
            temp_start = temp_end
        counter += 1

        if current_point == ending_point:
            route = []
            target = ending_point
            while any(tuple(target) in x for x in main_dict.values()):
                for key, value in main_dict.items():
                    for j in value:
                        if j == tuple(target):
                            route.append(target)
                            target = key
            return time, main_dict, route

        for i in iterate_list:
            p = zip(current_point, i)
            my_sum = [x + y for (x, y) in p]
            if tuple(my_sum) in visited or my_sum in block_points or my_sum in queue:
                continue
            else:
                if tuple(current_point) in main_dict:
                    main_dict[tuple(current_point)].append(tuple(my_sum))
                else:
                    main_dict[tuple(current_point)] = [tuple(my_sum)]
                    if graph:
                        show_graph(current_point)

                queue.append(my_sum)
                temp_end += 1




time, main_dict, route = bfs(starting_point, ending_point, block_points, True)
print(time)
print(route)

