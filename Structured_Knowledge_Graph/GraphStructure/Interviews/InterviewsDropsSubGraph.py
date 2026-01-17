# Created by Marcel Khan on 14.01.26.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews.Drops import ExpectationsDropsNodeData
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import DropsNodeData


class InterviewsDropsSubGraph:
    interviews_drops_node: NodeIllustration

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.interviews_drops_node = NodeIllustration(titel=DropsNodeData.TITLE,
                                                        image_name=DropsNodeData.IMAGE_NAME)

        expectations_drops_node = NodeKnowledge(titel=ExpectationsDropsNodeData.TITEL,
                                                description=ExpectationsDropsNodeData.CONTENT)

        self.interviews_drops_node.connect(expectations_drops_node)

        graph.add_new_node_to_graph(self.interviews_drops_node)
        graph.add_new_node_to_graph(expectations_drops_node)