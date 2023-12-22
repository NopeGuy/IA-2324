from graph.Graph import Grafo

class GuimaraesStreetGraphGenerator:
    def generate_graph(self):
        graph = Grafo(directed=True)

        graph.add_edge("Alameda D Afonso Henriques", "Avenida Conde Margaride", 2)
        graph.add_edge("Alameda D Afonso Henriques", "Rua de Santo Antonio", 3)
        graph.add_edge("Avenida Conde Margaride", "Largo Republica do Brasil", 4)
        graph.add_edge("Rua de Santo Antonio", "Avenida D Joao IV", 1)
        graph.add_edge("Largo Republica do Brasil", "Rua Egas Moniz", 2)
        graph.add_edge("Rua de Santo Antonio", "Rua da Rainha D Maria II", 5)
        graph.add_edge("Avenida D Joao IV", "Largo do Toural", 3)
        graph.add_edge("Rua da Rainha D Maria II", "Rua de Camoes", 2)
        graph.add_edge("Largo do Toural", "Rua da Liberdade", 2)
        graph.add_edge("Rua de Camoes", "Rua de Sao Francisco", 3)
        graph.add_edge("Rua de Camoes", "Largo do Trovador", 4)
        graph.add_edge("Rua da Liberdade", "Praca da Oliveira", 10)
        graph.add_edge("Rua da Liberdade", "Largo da Mumadona", 4)
        graph.add_edge("Rua de Sao Francisco", "Largo da Mumadona", 1)
        graph.add_edge("Praca da Oliveira", "Largo do Trovador", 4)
        graph.add_edge("Largo da Mumadona", "Rua de Santa Maria", 3)
        graph.add_edge("Largo do Trovador", "Avenida D Afonso Henriques", 10)
        graph.add_edge("Rua de Santa Maria", "Avenida D Afonso Henriques", 2)
        graph.add_edge("Rua de Santa Maria", "Largo do Trovador", 1)
        graph.add_edge("Rua Egas Moniz", "Largo do Trovador", 2)

        return graph


if __name__ == "__main__":
    generator = GuimaraesStreetGraphGenerator()
    guimaraes_graph = generator.generate_graph()
    print("Guimarães Street Graph:")
    print(guimaraes_graph)
    guimaraes_graph.desenha()
