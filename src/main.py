from Courier import Courier
from Order import Order
from graph.GuimaraesStreetGraphGenerator import GuimaraesStreetGraphGenerator


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


def compare_search_algorithm_results(guimaraes_graph, starting_node, finishing_node):
    print("===== Compare Search Algorithm Results =====")

    path_a_star, cost_a_star = guimaraes_graph.procura_aStar(starting_node, finishing_node)
    # path_greedy, cost_greedy = guimaraes_graph.greedy(starting_node, finishing_node)
    path_bfs, cost_bfs = guimaraes_graph.procura_BFS(starting_node, finishing_node)
    path_dfs, cost_dfs = guimaraes_graph.procura_DFS(starting_node, finishing_node)

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
    client_name = input("Enter client's name: ")
    weight = float(input("Enter product weight (in kg): "))
    volume = float(input("Enter product volume (in cm3): "))
    processing_time = int(input("Enter processing time (in minutes): "))
    starting_node, last_node = get_nodes()

    order = Order(client_name, weight, volume, processing_time, starting_node, last_node)
    return order

def display_orders(orders):
    print("===== Registered Orders =====")
    for order in orders:
        print(f"Client: {order.client_name}, Weight: {order.weight} kg, Volume: {order.volume} cm3,"
              f" Processing Time: {order.processing_time} minutes, "
              f"Start Node: {order.starting_node}, Last Node: {order.last_node}")
    print("===============================")


def display_couriers(couriers):
    print("===== Registered Couriers =====")
    for courier in couriers:
        print(f"Courier: {courier.name}, Transport: {courier.transport}")
    print("===============================")

def main():
    generator = GuimaraesStreetGraphGenerator()
    guimaraes_graph = None
    couriers = []
    orders = []

    while True:
        main_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Exiting the program. Goodbye!")
            break
        elif choice == 1:
            guimaraes_graph = generator.generate_graph()
            print("Monopoly Street Graph generated.")
        elif choice == 2:
            if guimaraes_graph is not None:
                guimaraes_graph.desenha()
            else:
                print("Please generate the graph first (Option 1).")
        elif choice == 3:
            print("===== Available Search Algorithms =====")
            print("1. A*")
            print("2. Greedy")
            print("3. BFS")
            print("4. DFS")
            print("0. Exit")
            print("===============================")

            sub_choice = get_user_choice()

            if sub_choice == 0:
                break

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
        elif choice == 4:
            if guimaraes_graph is not None:
                starting_node, finishing_node = get_nodes()
                compare_search_algorithm_results(guimaraes_graph, starting_node, finishing_node)
            else:
                print("Please generate the graph first (Option 1).")
        elif choice == 5:
            courier = add_courier()
            if courier is not None:
                couriers.append(courier)
                print(f"{courier.name} added as a courier with {courier.transport}.")
        elif choice == 6:
            order = add_order()
            orders.append(order)
            print("Order registered successfully.")
        elif choice == 7:
            display_orders(orders)
        elif choice == 8:
            display_couriers(couriers)
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
