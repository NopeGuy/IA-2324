from datetime import datetime, timedelta
from menu_functions import *
from graph.GuimaraesStreetGraphGenerator import GuimaraesStreetGraphGenerator

def main():
    generator = GuimaraesStreetGraphGenerator()
    guimaraes_graph = None
    couriers = []
    orders = []
    guimaraes_graph = generator.generate_graph()
    print("Guimarães Street Graph generated.")
    current_date = datetime.now().date()
    formatted_date = current_date.strftime("%d-%m-%Y")
    
    courier1 = Courier("Joao", "Bicycle")
    courier2 = Courier("Maria", "Car")
    couriers.append(courier1)
    couriers.append(courier2)
    orders.append(Order("Boda", 1, 1, 3000, "Rua de Camoes", "Rua da Saudade"))
    orders.append(Order("Boda2", 1, 1, 3000, "Rua de Camoes", "Avenida Conde Margaride"))
    orders.append(Order("Batata", 4, 1, 1000, "Rua de Camoes", "Rua da Abadia"))

    while True:
        print("\n      Welcome, today is " + formatted_date + ".")
        main_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Exiting the program. Goodbye!")
            break
        elif choice == 1:
            courier = add_courier()
            if courier is not None:
                couriers.append(courier)
                print(f"{courier.name} added as a courier with {courier.transport}.")
                
        elif choice == 2:
            order = add_order(guimaraes_graph)
            orders.append(order)
            print("Order registered successfully.")
            
        elif choice == 3:
            display_pending_orders(orders)
        elif choice == 4:
            display_sent_orders(orders)
        elif choice == 5:
            display_couriers(couriers)
        elif choice == 6:
            current_date = current_date + timedelta(days=1)
            formatted_date = current_date.strftime("%d-%m-%Y")
            for courier in couriers:
                courier.weight = 0
                courier._deliveries = []
            process_orders(orders, couriers, guimaraes_graph)
        
        elif choice == 7:

            while True:
                dev_menu()
                choice = get_user_choice()
                
                if(choice == 0):
                    break
                elif(choice == 1):
                    if guimaraes_graph is not None:
                        guimaraes_graph.desenha()
                        
                elif(choice == 2):
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
                        
                elif(choice == 3):
                    if guimaraes_graph is not None:
                        starting_node, finishing_node = get_nodes()
                        compare_search_algorithm_results(guimaraes_graph, starting_node, finishing_node)
                    else:
                        print("\nNot a valid option.")
        else:
            print("\nInvalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
