"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from GraphModel.Graph import Graph
from Structured_Demo_Knowledge_Graph.GraphStructure.HowToSubGraph import HowToSubGraph
from Structured_Demo_Knowledge_Graph.GraphStructure.LiteratureSourceSubGraph import LiteratureSourceSubGraph
from Structured_Demo_Knowledge_Graph.GraphStructure.OnlineSourceSubGraph import OnlineSourceSubGraph
from Structured_Demo_Knowledge_Graph.GraphStructure.PaperSourceSubGraph import PaperSourceSubGraph


class StructuredDemoGraph:
    """
    Diese Klasse hat die Verantwortlichkeit einen Graphen aus Subgraphen aufzubauen
    und Knoten der Subgraphen nach Bedarf zu verbinden.

    Als erstes werden hier Subgraphen als Instanzattribute definiert. Ihnen wird jedoch noch kein Wert zugewiesen.
    Instanzattribute stehen in der gesamten Klasse zur Verfügung so man self.instanzattribut einsetzt.

    Das bedeutet, dass jede Methode in dieser Instanz auf die Subgraphen zugreifen kann.
    Dies ist jedoch nur möglich, wenn dem Instanzattribut etwas zugewiesen wird.
    In der Methode assemble_graph (weiter unten) wird jedem Instanzattribut eine neue Instanz zugewiesen.
    """
    paper_source_subgraph: PaperSourceSubGraph  # wir spezifizieren hier explizit den Typ (PaperSourceSubGraph) damit Python weiß welche Methoden und Attribute genutzt werden können
    online_source_subgraph: OnlineSourceSubGraph
    literature_source_subgraph: LiteratureSourceSubGraph
    how_to_subgraph: HowToSubGraph

    def __init__(self, graph: Graph):
        """
        Dies ist der Konstruktor. Eine spezielle Methode die für das Anlegen einer Instanz verwendet wird.
        Wird eine Klasse instanziiert, wird automatisch der Konstruktor aufgerufen.

        :param graph: Eine Instanz der Klasse Graph. Wenn diese Klasse instanziiert wird,
        enthält der Graph jedoch noch keine Knoten. Diese werden in den Subgraphen angelegt.
        """

        """
        Hier rufen wir die Methode assemble_graph auf. 
        Da der Konstruktor beim instanziieren dieser Klasse ausgeführt wird, 
        wird auch diese Methode ausgeführt sobald eine Instanz von StructuredDemoGraph erzeugt wird.
        Alles in diesem Konstruktor (ebenso wie in allen anderen Methoden) wird von oben nach unten ausgeführt.
        Das bedeutet, es wird erst die Methode assemble_graph aufgerufen in der die Instanzattribute angelegt werden.
        Anschließend wird connect_sub_graphs aufgerufen um ausgewählte Knoten unterschiedlicher Subgraphen
        miteinander zu verbinden.
        
        Wir nutzen hier self. Self ist dabei eine Stellvertreter für "diese Instanz"
        wir sagen quasi die Methode assemble_graph soll in dieser Instanz (self) aufgerufen werden.
        """
        self.assemble_graph(graph)  # Erst werden die Subgraphen angelegt...
        self.connect_sub_graphs()  # ...dann werden sie verbunden.

    def assemble_graph(self, graph):
        """
        Diese Methode dient Ihnen also Demonstration für den Aufbau eines Graphen.
        Er spiegelt die Klasse DemoGraph wieder unterteilt den Code jedoch in kleinere Einheiten
        und nutzt somit direkt die Lösungswerkzeuge Abstraktion und Dekomposition.

        Subgraphen legen dann die eigentlichen Knoten und ihre Verbindungen an und fügen diese der Graph Instanz hinzu.

        In diesem Beispiel legen wir vier Subgraphen an. Dadurch dass wir self verwenden,
        weisen wir die neuen Subgraph Instanzen den oben definierten Instanzattributen zu.
        Dies ermöglicht es uns diese Subgraphen in der Methode unten "connect_sub_graphs" zu referenzieren
        und Verbindungen zwischen Knoten unterschiedlicher Subgraphen herzustellen.
        """
        self.how_to_subgraph = HowToSubGraph(graph)
        self.literature_source_subgraph = LiteratureSourceSubGraph(graph)
        self.online_source_subgraph = OnlineSourceSubGraph(graph)
        self.paper_source_subgraph = PaperSourceSubGraph(graph)

    def connect_sub_graphs(self):
        """
        Wir nutzen hier die Instanzattribute um auf die Subgraphen zuzugreifen. Dies erlaubt es uns Knoten die explizit
        von einem Subgraphen bereitgestellt werden zu referenzieren.
        Das Bereitstellen wird hier wieder über Instanzattribute der Subgraphen ermöglicht.

        Anmerkung:
        Der direkte Zugriff auf andere Instanzen einer Klasse dient in EPI der Vereinfachung.
        Klassen, die Attribute anderer Klassen nutzen sind stark gekoppelt.
        Ändert man etwas an der einen Klasse muss man möglicherweise auch etwas an der anderen Klasse ändern.
        Desto mehr Klassen auf diese Art gekoppelt sind, desto schwieriger werden Änderungen.

        Daher nutzt wir eigentlich Interfaces, um eine lose Kopplung zu erzielen in dem wir die Zugriffe
        auf andere Klassen kapseln (Encapsulation).

        Zur Simplifizierung verzichten wir jedoch darauf im Rahmen von EPI.
        Sie dürfen jedoch auch gerne Interfaces zwischen die Subgraphen schalten.

        """
        self.how_to_subgraph.how_to_node.connect(
            self.literature_source_subgraph.literature_source_example_knowledge_node)
        self.how_to_subgraph.how_to_node.connect(self.online_source_subgraph.online_source_example_knowledge_node)
        self.how_to_subgraph.how_to_node.connect(self.paper_source_subgraph.paper_source_example_knowledge_node)
