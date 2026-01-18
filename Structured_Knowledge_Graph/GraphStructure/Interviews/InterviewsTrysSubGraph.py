# Created by Marcel Khan on 14.01.26.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews.Trys import ExpectationsTrysNodeData, \
    WorkingInTeamsTrysNodeData, DeficitFrontendDevelopmentNodeData, DeficitHardwareNodeData, DeficitITSecurityNodeData, \
    InteractiveModulesNodeData, MakeModulesInteractiveNodeData, MakeModulesInteresstingNodeData, \
    ModulesCloserToRealityNodeData
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import TrysNodeData
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences.Trys import VisitMoreLecturesNodeData


class InterviewsTrysSubGraph:
    interviews_trys_node: NodeIllustration

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.interviews_trys_node = NodeIllustration(titel=TrysNodeData.TITLE,
                                                      image_name=TrysNodeData.IMAGE_NAME)

        expectations_trys_node = NodeKnowledge(titel=ExpectationsTrysNodeData.TITEL,
                                               description=ExpectationsTrysNodeData.CONTENT)

        working_in_teams_trys_node = NodeKnowledge(titel=WorkingInTeamsTrysNodeData.TITEL,
                                                  description=WorkingInTeamsTrysNodeData.CONTENT)

        deficit_frontend_development_node = NodeKnowledge(titel=DeficitFrontendDevelopmentNodeData.TITLE,
                                                          description=DeficitFrontendDevelopmentNodeData.CONTENT)

        deficit_hardware_node = NodeKnowledge(titel=DeficitHardwareNodeData.TITLE,
                                              description=DeficitHardwareNodeData.CONTENT)

        deficit_it_security_node = NodeKnowledge(titel=DeficitITSecurityNodeData.TITLE,
                                                 description=DeficitITSecurityNodeData.CONTENT)

        interactive_modules_node = NodeKnowledge(titel=InteractiveModulesNodeData.TITLE,
                                                 description=InteractiveModulesNodeData.CONTENT)

        make_modules_interactive_node = NodeKnowledge(titel=MakeModulesInteractiveNodeData.TITLE,
                                                      description=MakeModulesInteractiveNodeData.CONTENT)

        make_modules_interessting_node = NodeKnowledge(titel=MakeModulesInteresstingNodeData.TITLE,
                                                       description=MakeModulesInteresstingNodeData.CONTENT)

        modules_closer_to_reality_node = NodeKnowledge(titel=ModulesCloserToRealityNodeData.TITLE,
                                                       description=ModulesCloserToRealityNodeData.CONTENT)

        self.interviews_trys_node.connect(expectations_trys_node)
        self.interviews_trys_node.connect(working_in_teams_trys_node)
        self.interviews_trys_node.connect(deficit_frontend_development_node)
        self.interviews_trys_node.connect(deficit_hardware_node)
        self.interviews_trys_node.connect(deficit_it_security_node)
        self.interviews_trys_node.connect(interactive_modules_node)
        self.interviews_trys_node.connect(make_modules_interactive_node)
        self.interviews_trys_node.connect(make_modules_interessting_node)
        self.interviews_trys_node.connect(modules_closer_to_reality_node)



        graph.add_new_node_to_graph(self.interviews_trys_node)
        graph.add_new_node_to_graph(expectations_trys_node)
        graph.add_new_node_to_graph(working_in_teams_trys_node)
        graph.add_new_node_to_graph(deficit_frontend_development_node)
        graph.add_new_node_to_graph(deficit_hardware_node)
        graph.add_new_node_to_graph(deficit_it_security_node)
        graph.add_new_node_to_graph(interactive_modules_node)
        graph.add_new_node_to_graph(make_modules_interactive_node)
        graph.add_new_node_to_graph(make_modules_interessting_node)
        graph.add_new_node_to_graph(modules_closer_to_reality_node)
