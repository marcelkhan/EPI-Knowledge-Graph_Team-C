# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from Structured_Knowledge_Graph.GraphStructure.EvaluationSubGraph import EvaluationSubGraph


class StructuredKnowledgeGraph:

    evaluation_subgraph: EvaluationSubGraph

    def __init__(self, graph: Graph):
        self.assemble_graph(graph)
        self.connect_sub_graphs()

    def assemble_graph(self, graph):
        self.evaluation_subgraph = EvaluationSubGraph(graph)

    def connect_sub_graphs(self):
        pass