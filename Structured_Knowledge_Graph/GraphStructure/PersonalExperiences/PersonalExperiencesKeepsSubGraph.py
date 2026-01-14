# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import KeepsNodeData
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences.Keeps import ProjectorientedModulesNodeData, \
    TeamworkNodeData, ModernSoftwareDevelopmentConceptsNodeData, PersonalResponsibilityNodeData


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

        modern_software_development_concepts_node = NodeKnowledge(titel=ModernSoftwareDevelopmentConceptsNodeData.TITLE,
                                                                  description=ModernSoftwareDevelopmentConceptsNodeData.CONTENT)

        personal_responsibility_node = NodeKnowledge(titel=PersonalResponsibilityNodeData.TITLE,
                                                     description=PersonalResponsibilityNodeData.CONTENT)


        self.personal_experiences_keeps_node.connect(projectoriented_modules_node)
        self.personal_experiences_keeps_node.connect(teamwork_node)
        self.personal_experiences_keeps_node.connect(modern_software_development_concepts_node)
        self.personal_experiences_keeps_node.connect(personal_responsibility_node)

        graph.add_new_node_to_graph(self.personal_experiences_keeps_node)
        graph.add_new_node_to_graph(projectoriented_modules_node)
        graph.add_new_node_to_graph(teamwork_node)
        graph.add_new_node_to_graph(modern_software_development_concepts_node)
        graph.add_new_node_to_graph(personal_responsibility_node)