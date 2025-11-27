# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences import PersonalExperiencesNodeData


class PersonalExperiencesSubGraph:
    personal_experiences_node : NodeKnowledge

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):

        self.personal_experiences_node = NodeKnowledge(titel=PersonalExperiencesNodeData.TITEL,
                                                      description=PersonalExperiencesNodeData.CONTENT)

        graph.add_new_node_to_graph(self.personal_experiences_node)