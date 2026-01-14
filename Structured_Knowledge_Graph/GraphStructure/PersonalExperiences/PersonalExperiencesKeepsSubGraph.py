# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import KeepsNodeData
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences.Keeps import ProjectorientedModulesNodeData, \
    TeamworkNodeData


class PersonalExperiencesKeepsSubGraph:
    personal_experiences_keeps_node: NodeIllustration

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.personal_experiences_keeps_node = NodeIllustration(titel=KeepsNodeData.TITLE,
                                                                image_name=KeepsNodeData.IMAGE_NAME)

        projectoriented_modules_node = NodeKnowledge(titel=ProjectorientedModulesNodeData.TITLE,
                                                description=ProjectorientedModulesNodeData.CONTENT)
        teamwork_node = NodeKnowledge(titel=TeamworkNodeData.TITLE,
                                      description=TeamworkNodeData.CONTENT)

        self.personal_experiences_keeps_node.connect(projectoriented_modules_node)
        self.personal_experiences_keeps_node.connect(teamwork_node)

        graph.add_new_node_to_graph(self.personal_experiences_keeps_node)
        graph.add_new_node_to_graph(projectoriented_modules_node)
        graph.add_new_node_to_graph(teamwork_node)