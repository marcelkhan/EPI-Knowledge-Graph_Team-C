# Created by Timon Kirch on 17.01.26.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews import InterviewsEvaluationsNodeData


class InterviewsEvaluationsSubGraph:
    interviews_evaluations_node: NodeKnowledge

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.interviews_evaluations_node = NodeKnowledge(titel=InterviewsEvaluationsNodeData.TITEL,
                                                         description=InterviewsEvaluationsNodeData.CONTENT)

        graph.add_new_node_to_graph(self.interviews_evaluations_node)