# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import TrysNodeData
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences.Trys import PreparationForThesisNodeData, \
    InsecurityNodeData, ComputerScienceInASocialContextNodeData, SupportNodeData, LearningJourneyNodeData


class PersonalExperiencesTrysSubGraph:
    personal_experiences_trys_node: NodeIllustration

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.personal_experiences_trys_node = NodeIllustration(titel=TrysNodeData.TITLE,
                                                                image_name=TrysNodeData.IMAGE_NAME)

        preparation_for_thesis_node = NodeKnowledge(titel=PreparationForThesisNodeData.TITLE,
                                                    description=PreparationForThesisNodeData.CONTENT)

        insecurity_node = NodeKnowledge(titel=InsecurityNodeData.TITLE,
                                        description=InsecurityNodeData.CONTENT)

        computer_science_in_a_social_context_node = NodeKnowledge(titel=ComputerScienceInASocialContextNodeData.TITLE,
                                                                  description=ComputerScienceInASocialContextNodeData.CONTENT)

        support_node = NodeKnowledge(titel=SupportNodeData.TITLE,
                                     description=SupportNodeData.CONTENT)

        learning_journey_node = NodeKnowledge(titel=LearningJourneyNodeData.TITLE,
                                              description=LearningJourneyNodeData.CONTENT)

        self.personal_experiences_trys_node.connect(preparation_for_thesis_node)
        self.personal_experiences_trys_node.connect(insecurity_node)
        self.personal_experiences_trys_node.connect(computer_science_in_a_social_context_node)
        self.personal_experiences_trys_node.connect(support_node)
        self.personal_experiences_trys_node.connect(learning_journey_node)

        graph.add_new_node_to_graph(self.personal_experiences_trys_node)
        graph.add_new_node_to_graph(preparation_for_thesis_node)
        graph.add_new_node_to_graph(insecurity_node)
        graph.add_new_node_to_graph(computer_science_in_a_social_context_node)
        graph.add_new_node_to_graph(support_node)
        graph.add_new_node_to_graph(learning_journey_node)