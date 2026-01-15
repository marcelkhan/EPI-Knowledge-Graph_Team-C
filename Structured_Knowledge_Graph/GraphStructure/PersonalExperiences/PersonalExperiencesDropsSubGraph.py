# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import DropsNodeData
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences.Drops import ExamRequirementsNodeData, \
    RequirementsNodeData


class PersonalExperiencesDropsSubGraph:
    personal_experiences_drops_node: NodeIllustration

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.personal_experiences_drops_node = NodeIllustration(titel=DropsNodeData.TITLE,
                                                                image_name=DropsNodeData.IMAGE_NAME)

        exam_requirements_node = NodeKnowledge(titel=ExamRequirementsNodeData.TITLE,
                                               description=ExamRequirementsNodeData.CONTENT)

        requirements_node = NodeKnowledge(titel=RequirementsNodeData.TITLE,
                                          description=RequirementsNodeData.CONTENT)

        self.personal_experiences_drops_node.connect(exam_requirements_node)
        self.personal_experiences_drops_node.connect(requirements_node)

        graph.add_new_node_to_graph(self.personal_experiences_drops_node)
        graph.add_new_node_to_graph(exam_requirements_node)
        graph.add_new_node_to_graph(requirements_node)