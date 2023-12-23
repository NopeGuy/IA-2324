from Courier import Courier
from Order import Order

def main_menu():
    print("===== Health Planet Delivery System =====")
    print("1. Add Courier")
    print("2. Register Order")
    print("3. Display Registered Orders")
    print("4. Display Registered Couriers")
    print("5. Advance a day")
    print("6. Dev Menu")
    print("0. Exit")
    print("===============================")

def dev_menu():
    print("\n===== Dev Menu =====")
    print("1. Represent Delivery Points as Graph")
    print("2. Use Search Algorithms")
    print("3. Compare Search Algorithm Results")
    print("0. Exit to Main Menu")
    print("===============================")
    
def get_node_final():
    print("===== Node Selection =====")
    #starting_node = input("Insert starting node: ")
    finishing_node = input("Delivery Street: ")
    return finishing_node

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


def search_menu(guimaraes_graph):
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
            path, cost = guimaraes_graph.procura_aStar(starting_node, finishing_node)
        elif sub_choice == 2:
            path, cost = guimaraes_graph.greedy(starting_node, finishing_node)
        elif sub_choice == 3:
            path, cost = guimaraes_graph.procura_BFS(starting_node, finishing_node)
        elif sub_choice == 4:
            path, cost = guimaraes_graph.procura_DFS(starting_node, finishing_node)

        if path is not None:
            print("Search Algorithm Result:")
            print("Path:", path)
            print("Cost:", cost)
        else:
            print("No path found.")
    else:
        print("Invalid search algorithm choice. Please enter a valid option.")


def compare_search_algorithm_results(guimaraes_graph, starting_node, finishing_node):
    print("===== Compare Search Algorithm Results =====")
    try:
        path_a_star, cost_a_star = guimaraes_graph.procura_aStar(starting_node, finishing_node)
        print("\nA* Search Result:")
        print("Path:", path_a_star)
        print("Cost:", cost_a_star)
    except:
        print("\nNo path found.")
    
    try:
        path_greedy, cost_greedy = guimaraes_graph.greedy(starting_node, finishing_node)
        print("\nGreedy Search Result:")
        print("Path:", path_greedy)
        print("Cost:", cost_greedy)
    except:
        print("\nNo path found.")
    
    try:
        path_bfs, cost_bfs = guimaraes_graph.procura_BFS(starting_node, finishing_node)
        print("\nBFS Search Result:")
        print("Path:", path_bfs)
        print("Cost:", cost_bfs)
    except:
        print("\nNo path found.")
    
    try:
        path_dfs, cost_dfs = guimaraes_graph.procura_DFS(starting_node, finishing_node)
        print("\nDFS Search Result:")
        print("Path:", path_dfs)
        print("Cost:", cost_dfs)
    except:
        print("\nNo path found.")

def add_courier():
    print("===== Add Courier =====")
    name = input("Enter courier's name: ")
    print("Select transport mode:")
    print("1. Bicycle")
    print("2. Moto")
    print("3. Car")

    transport_choice = get_user_choice()

    if transport_choice in [1, 2, 3]:
        transport_modes = ["Bicycle", "Moto", "Car"]
        transport = transport_modes[transport_choice - 1]
        courier = Courier(name, transport)
        return courier
    else:
        print("Invalid transport mode choice. Courier not added.")
        return None

def add_order():
    print("===== Register Order =====")

    while True:
        client_name = input("Enter client's name: ")
        try:
            weight = float(input("Enter product weight (in kg): "))
            volume = float(input("Enter product volume (in cm3): "))
            time = input("Enter processing time (Days, Hours, Minutes): ")
            days, hours, minutes = map(int, time.split(','))
            processing_time = days * 24 * 60 + hours * 60 + minutes
            starting_node = "Rua de Camoes"
            last_node = get_node_final()

            order = Order(client_name, weight, volume, processing_time, starting_node, last_node)
            return order
        except ValueError:
            print("Invalid input. Please enter numeric values for weight, volume, days, hours, and minutes.")


def display_orders(orders):
    print("===== Registered Orders =====")
    for order in orders:
        if(order.status == "Waiting"):
            print(f"Client: {order.client_name}, Weight: {order.weight} kg, Volume: {order.volume} cm3,"
                f" Processing Time: {order.processing_time} minutes, "
                f"Start Node: {order.starting_node}, Last Node: {order.last_node}")
    print("===============================")


def display_couriers(couriers):
    print("===== Registered Couriers =====")
    for courier in couriers:
        print(f"Courier: {courier.name}, Transport: {courier.transport}")
    print("===============================")
    
def choose_best_algorithm(graph, starting_node, finishing_node):
    guimaraes_graph = graph
    cost = 0
    path = []
    
    try:
        path_a_star, cost_a_star = guimaraes_graph.procura_aStar(starting_node, finishing_node)
        print("\nA* Search Result:")
        print("Path:", path_a_star)
        print("Cost:", cost_a_star)
        cost = cost_a_star
        path = path_a_star
    except:
        print("\nNo A* path found.")
    
    try:
        path_greedy, cost_greedy = guimaraes_graph.greedy(starting_node, finishing_node)
        print("\nGreedy Search Result:")
        print("Path:", path_greedy)
        print("Cost:", cost_greedy)
        if cost_greedy < cost:
            cost = cost_greedy
            path = path_greedy
    except:
        print("\nNo Greedy path found.")
    
    try:
        path_bfs, cost_bfs = guimaraes_graph.procura_BFS(starting_node, finishing_node)
        print("\nBFS Search Result:")
        print("Path:", path_bfs)
        print("Cost:", cost_bfs)
        if cost_bfs < cost:
            cost = cost_bfs
            path = path_bfs
    except:
        print("\nNo BFS path found.")
    
    try:
        path_dfs, cost_dfs = guimaraes_graph.procura_DFS(starting_node, finishing_node)
        print("\nDFS Search Result:")
        print("Path:", path_dfs)
        print("Cost:", cost_dfs)
        if cost_dfs < cost:
            cost = cost_dfs
            path = path_dfs
    except:
        print("\nNo DFS path found.")
        
    return path, cost
        

def process_orders(orders, couriers, guimaraes_graph):
    starting_node = "Rua de Camoes"
    
    for order in orders:
        graph_copy = guimaraes_graph.copy()
        path, cost = choose_best_algorithm(graph_copy, starting_node, order.last_node)

        if path is not None:
            sorted_couriers = sorted(couriers, key=lambda courier: (courier.transport != "Bicycle", courier.transport != "Moto", courier.transport != "Car"))

            selected_courier = None
            for courier in sorted_couriers:
                if courier.verifyWeight(order.weight) and courier.verifyTime(cost, order.processing_time, order.weight):
                    selected_courier = courier
                    break

            if selected_courier is not None:
                selected_courier.add_delivery(order)
                print(f"\nOrder for {order.client_name} added to {selected_courier.name} courier.")
                order.status = "Delivered"
            else:
                print(f"\nNo suitable courier found for order to {order.client_name}.")
