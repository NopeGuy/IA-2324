from courier_functions import add_courier, display_couriers
from graph.MonopolyStreetGraphGenerator import MonopolyStreetGraphGenerator
from menu_functions import main_menu, get_nodes, get_user_choice, search_menu
from order_functions import add_order, display_orders
from search_algorithms import compare_search_algorithm_results

generator = MonopolyStreetGraphGenerator()
monopoly_graph = None
couriers = []
orders = []


def main():
    global monopoly_graph, couriers, orders
    while True:
        main_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Exiting the program. Goodbye!")
            break
        elif choice == 1:
            monopoly_graph = generator.generate_graph()
            print("Monopoly Street Graph generated.")
        elif choice == 2:
            if monopoly_graph is not None:
                monopoly_graph.desenha()
            else:
                print("Please generate the graph first (Option 1).")
        elif choice == 3:
            search_menu(monopoly_graph)
        elif choice == 4:
            if monopoly_graph is not None:
                starting_node, finishing_node = get_nodes()
                compare_search_algorithm_results(monopoly_graph, starting_node, finishing_node)
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
