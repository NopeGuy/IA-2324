from graph.Graph import Grafo


class MonopolyStreetGraphGenerator:
    def generate_graph(self):
        graph = Grafo(directed=True)

        graph.add_edge("Park Place", "Boardwalk", 1)
        graph.add_edge("Park Place", "Marvin Gardens", 2)
        graph.add_edge("Boardwalk", "Illinois Avenue", 3)
        graph.add_edge("Marvin Gardens", "Illinois Avenue", 1)
        graph.add_edge("Illinois Avenue", "Ventnor Avenue", 2)
        graph.add_edge("Ventnor Avenue", "Connecticut Avenue", 1)
        graph.add_edge("Connecticut Avenue", "St. James Place", 2)
        graph.add_edge("St. James Place", "New York Avenue", 1)
        graph.add_edge("New York Avenue", "Tennessee Avenue", 3)
        graph.add_edge("Tennessee Avenue", "Kentucky Avenue", 2)
        graph.add_edge("Kentucky Avenue", "Indiana Avenue", 1)
        graph.add_edge("Park Place", "St. James Place", 2)
        graph.add_edge("Marvin Gardens", "New York Avenue", 2)
        graph.add_edge("Illinois Avenue", "Tennessee Avenue", 1)
        graph.add_edge("Ventnor Avenue", "Kentucky Avenue", 2)
        return graph


if __name__ == "__main__":
    generator = MonopolyStreetGraphGenerator()
    monopoly_graph = generator.generate_graph()
    print("Monopoly Street Graph:")
    print(monopoly_graph)
    monopoly_graph.desenha()
