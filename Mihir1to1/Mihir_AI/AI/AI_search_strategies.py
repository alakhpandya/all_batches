def A_star(window, grid, width, rows, start, end):
    open = PriorityQueue()
    order = 1
    h_start = h(start, end)
    open.put((h_start, h_start, order, start))
    f_values = {}
    g_values = {}
    backtrack = {}
    simplified_queue = {start}
    for row in grid:
        for node in row:
            f_values[node] = float("inf")
            g_values[node] = float("inf")

    f_values[start] = h_start
    g_values[start] = 0

    while not open.empty():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        node = open.get()[3]

        
        for current in node.neighbors:
            # print("for started")
            temp_g = g_values[node] + 1

            if node == end:
                create_path(backtrack, end, window, grid, rows, width)
                start.make_start()
                return True


            if temp_g < g_values[current]:
                g_values[current] = temp_g
                h_value = h(current, end)
                f_values[current] = g_values[current] + h_value
                backtrack[current] = node

                if current not in simplified_queue:
                    order += 1
                    open.put((f_values[current], h_value, order, current))
                    simplified_queue.add(current)
                    node.make_open()

        draw(window, grid, rows, width)
