# Created by Marcel Khan on 27.11.25.

from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews import InterviewsNodeData
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import KeepsNodeData, DropsNodeData, TrysNodeData


class InterviewsSubGraph:
    interviews_node: NodeKnowledge

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.interviews_node = NodeKnowledge(titel=InterviewsNodeData.TITEL,
                                            description=InterviewsNodeData.CONTENT)

        graph.add_new_node_to_graph(self.interviews_node)