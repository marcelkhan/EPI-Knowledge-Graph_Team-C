# Created by Timon Kirch on 17.01.26.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews import InterviewsEvaluationsNodeData
from Structured_Knowledge_Graph.GraphContent.Interviews.Evaluations import ExpectationsNodeData


class InterviewsEvaluationsSubGraph:
    interviews_evaluations_node: NodeKnowledge

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.interviews_evaluations_node = NodeKnowledge(titel=InterviewsEvaluationsNodeData.TITEL,
                                                         description=InterviewsEvaluationsNodeData.CONTENT)

        expectations_node = NodeKnowledge(titel=ExpectationsNodeData.TITEL,
                                          description=ExpectationsNodeData.CONTENT)

        self.interviews_evaluations_node.connect(expectations_node)

        graph.add_new_node_to_graph(self.interviews_evaluations_node)
        graph.add_new_node_to_graph(expectations_node)