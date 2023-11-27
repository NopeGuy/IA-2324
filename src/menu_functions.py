def main_menu():
    print("===== Health Planet Delivery System =====")
    print("1. Generate Delivery Circuits")
    print("2. Represent Delivery Points as Graph")
    print("3. Use Search Algorithms")
    print("4. Compare Search Algorithm Results")
    print("5. Add Courier")
    print("6. Register Order")
    print("7. Display Registered Orders")
    print("8. Display Registered Couriers")
    print("0. Exit")
    print("===============================")


def get_nodes():
    print("===== Node Selection =====")
    starting_node = input("Insert starting node: ")
    finishing_node = input("Insert finishing node: ")
    return starting_node, finishing_node


def get_user_choice():
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def search_menu(monopoly_graph):
    print("===== Available Search Algorithms =====")
    print("1. A*")
    print("2. Greedy")
    print("3. BFS")
    print("4. DFS")
    print("0. Exit")
    print("===============================")

    sub_choice = get_user_choice()

    if sub_choice == 0:
        return

    if sub_choice in [1, 2, 3, 4]:
        starting_node, finishing_node = get_nodes()

        if sub_choice == 1:
            path, cost = monopoly_graph.procura_aStar(starting_node, finishing_node)
        elif sub_choice == 2:
            path, cost = monopoly_graph.greedy(starting_node, finishing_node)
        elif sub_choice == 3:
            path, cost = monopoly_graph.procura_BFS(starting_node, finishing_node)
        elif sub_choice == 4:
            path, cost = monopoly_graph.procura_DFS(starting_node, finishing_node)

        if path is not None:
            print("Search Algorithm Result:")
            print("Path:", path)
            print("Cost:", cost)
        else:
            print("No path found.")
    else:
        print("Invalid search algorithm choice. Please enter a valid option.")
