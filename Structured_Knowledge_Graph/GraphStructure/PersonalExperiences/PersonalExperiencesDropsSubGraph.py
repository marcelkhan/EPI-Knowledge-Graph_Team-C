# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences.Keeps import ChatGPTNutzenumLoesungsWegezuerstellenNodeData
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import DropsNodeData
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences.Drops import ExamRequirementsNodeData, \
    RequirementsNodeData,ChatGPTFuersLoesenVonAufgabenNoteData, BolemieLernenVorDerKlausurNodeData,SpaetAbgabenNodeData


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

        chatGpt_node=NodeKnowledge(titel=ChatGPTFuersLoesenVonAufgabenNoteData.TITLE,
                                   description=ChatGPTFuersLoesenVonAufgabenNoteData.CONTENT)

        bulimieLernen_node=NodeKnowledge(titel=BolemieLernenVorDerKlausurNodeData.TITLE,description=BolemieLernenVorDerKlausurNodeData.CONTENT)
        spaet_Abgeben_node=NodeKnowledge(titel=SpaetAbgabenNodeData.TITLE,description=SpaetAbgabenNodeData.CONTENT)


        self.personal_experiences_drops_node.connect(exam_requirements_node)
        self.personal_experiences_drops_node.connect(requirements_node)
        self.personal_experiences_drops_node.connect(bulimieLernen_node)
        self.personal_experiences_drops_node.connect(chatGpt_node)
        self.personal_experiences_drops_node.connect(spaet_Abgeben_node)



        graph.add_new_node_to_graph(self.personal_experiences_drops_node)
        graph.add_new_node_to_graph(exam_requirements_node)
        graph.add_new_node_to_graph(requirements_node)
        graph.add_new_node_to_graph(chatGpt_node)

        graph.add_new_node_to_graph(bulimieLernen_node)
        graph.add_new_node_to_graph(spaet_Abgeben_node)