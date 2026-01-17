# Created by Marcel Khan on 14.01.26.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import KeepsNodeData


class InterviewsKeepsSubGraph:
    interviews_keeps_node: NodeIllustration

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.interviews_keeps_node = NodeIllustration(titel=KeepsNodeData.TITLE,
                                                        image_name=KeepsNodeData.IMAGE_NAME)

        graph.add_new_node_to_graph(self.interviews_keeps_node)