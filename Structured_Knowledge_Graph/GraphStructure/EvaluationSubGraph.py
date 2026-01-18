# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Evaluation import EvaluationNodeData
from Structured_Knowledge_Graph.GraphContent.Evaluation import ModuleambestebundgefallenNodeData


class EvaluationSubGraph:
    evaluation_node: NodeKnowledge

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        # Knoten anlegen
        self.evaluation_node = NodeKnowledge(titel=EvaluationNodeData.TITEL,
                                             description=EvaluationNodeData.CONTENT)

        Modulgood_node=NodeKnowledge(titel=ModuleambestebundgefallenNodeData.TITLE,description=ModuleambestebundgefallenNodeData.CONTENT)
        # Knoten verbinden
        # self.evaluation_node.connect()

        # Knoten im Graphen einfügen
        graph.add_new_node_to_graph(self.evaluation_node)
        graph.add_new_node_to_graph(Modulgood_node)
        self.evaluation_node.connect(Modulgood_node)