# Created by Marcel Khan on 14.01.26.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews.Drops import ExpectationsDropsNodeData, \
    HandwrittenCodingExamsNodeData, LittleRelevanceModulesNodeData, BWLNodeData
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

        handwritten_coding_exams = NodeKnowledge(titel=HandwrittenCodingExamsNodeData.TITLE,
                                                 description=HandwrittenCodingExamsNodeData.CONTENT)
        little_relevance_node = NodeKnowledge(titel=LittleRelevanceModulesNodeData.TITLE,
                                              description=LittleRelevanceModulesNodeData.CONTENT)

        bwl_node = NodeKnowledge(titel=BWLNodeData.TITLE,
                                 description=BWLNodeData.CONTENT)

        self.interviews_drops_node.connect(expectations_drops_node)
        self.interviews_drops_node.connect(handwritten_coding_exams)
        self.interviews_drops_node.connect(bwl_node)
        self.interviews_drops_node.connect(little_relevance_node)

        graph.add_new_node_to_graph(self.interviews_drops_node)
        graph.add_new_node_to_graph(expectations_drops_node)
        graph.add_new_node_to_graph(handwritten_coding_exams)
        graph.add_new_node_to_graph(bwl_node)
        graph.add_new_node_to_graph(little_relevance_node)