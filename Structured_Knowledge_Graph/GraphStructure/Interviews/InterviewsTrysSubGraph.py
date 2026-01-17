# Created by Marcel Khan on 14.01.26.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import TrysNodeData


class InterviewsTrysSubGraph:
    interviews_trys_node: NodeIllustration

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.interviews_trys_node = NodeIllustration(titel=TrysNodeData.TITLE,
                                                      image_name=TrysNodeData.IMAGE_NAME)

        graph.add_new_node_to_graph(self.interviews_trys_node)