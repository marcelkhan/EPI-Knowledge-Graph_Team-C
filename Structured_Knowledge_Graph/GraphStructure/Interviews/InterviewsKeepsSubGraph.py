# Created by Marcel Khan on 14.01.26.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews.Keeps import ExpectationsKeepsNodeData, \
    StudyingSatisfactionKeepsNodeData, SatisfactionWithStudyingKeepsNodeData, OrganisationKeepsNodeData
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import KeepsNodeData


class InterviewsKeepsSubGraph:
    interviews_keeps_node: NodeIllustration

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.interviews_keeps_node = NodeIllustration(titel=KeepsNodeData.TITLE,
                                                        image_name=KeepsNodeData.IMAGE_NAME)

        expectations_keeps_node = NodeKnowledge(titel=ExpectationsKeepsNodeData.TITEL,
                                                description=ExpectationsKeepsNodeData.CONTENT)

        studying_satisfaction_keeps_node = NodeKnowledge(titel=StudyingSatisfactionKeepsNodeData.TITEL,
                                                         description=StudyingSatisfactionKeepsNodeData.CONTENT)

        satisfaction_with_studying_keeps_node = NodeKnowledge(titel=SatisfactionWithStudyingKeepsNodeData.TITEL,
                                                              description=SatisfactionWithStudyingKeepsNodeData.CONTENT)

        organisation_keeps_node = NodeKnowledge(titel=OrganisationKeepsNodeData.TITEL,
                                                description=OrganisationKeepsNodeData.CONTENT)

        self.interviews_keeps_node.connect(expectations_keeps_node)
        self.interviews_keeps_node.connect(studying_satisfaction_keeps_node)
        self.interviews_keeps_node.connect(satisfaction_with_studying_keeps_node)
        self.interviews_keeps_node.connect(organisation_keeps_node)

        graph.add_new_node_to_graph(self.interviews_keeps_node)
        graph.add_new_node_to_graph(expectations_keeps_node)
        graph.add_new_node_to_graph(studying_satisfaction_keeps_node)
        graph.add_new_node_to_graph(satisfaction_with_studying_keeps_node)
        graph.add_new_node_to_graph(organisation_keeps_node)