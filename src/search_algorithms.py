def compare_search_algorithm_results(monopoly_graph, starting_node, finishing_node):
    print("===== Compare Search Algorithm Results =====")

    path_a_star, cost_a_star = monopoly_graph.procura_aStar(starting_node, finishing_node)
    # path_greedy, cost_greedy = monopoly_graph.greedy(starting_node, finishing_node)
    path_bfs, cost_bfs = monopoly_graph.procura_BFS(starting_node, finishing_node)
    path_dfs, cost_dfs = monopoly_graph.procura_DFS(starting_node, finishing_node)

    print("A* Search Result:")
    print("Path:", path_a_star)
    print("Cost:", cost_a_star)

    print("\nGreedy Search Result:")
    # print("Path:", path_greedy)
    # print("Cost:", cost_greedy)

    print("\nBFS Search Result:")
    print("Path:", path_bfs)
    print("Cost:", cost_bfs)

    print("\nDFS Search Result:")
    print("Path:", path_dfs)
    print("Cost:", cost_dfs)
