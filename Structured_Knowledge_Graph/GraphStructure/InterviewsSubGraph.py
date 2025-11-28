# Created by Marcel Khan on 27.11.25.

from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews import InterviewsNodeData
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import KeepsNodeData


class InterviewsSubGraph:
    interviews_node: NodeKnowledge

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.interviews_node = NodeKnowledge(titel=InterviewsNodeData.TITEL,
                                            description=InterviewsNodeData.CONTENT)

        keeps_node = NodeIllustration(titel=KeepsNodeData.TITLE,
                                      image_name=KeepsNodeData.IMAGE_NAME)

        self.interviews_node.connect(keeps_node)

        graph.add_new_node_to_graph(self.interviews_node)
        graph.add_new_node_to_graph(keeps_node)