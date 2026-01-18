# Created by Marcel Khan on 14.01.26.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews.Trys import ExpectationsTrysNodeData, \
    WorkingInTeamsTrysNodeData, DeficitFrontendDevelopmentNodeData, DeficitHardwareNodeData, DeficitITSecurityNodeData, \
    InteractiveModulesNodeData, ElectiveSubjectNodeData, ModernAgileCurriculumNodeData, ProjectNodeData
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import TrysNodeData


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
        elective_subject_node = NodeKnowledge(titel=ElectiveSubjectNodeData.TITLE,
                                              description=ElectiveSubjectNodeData.CONTENT)
        modern_agile_node = NodeKnowledge(titel=ModernAgileCurriculumNodeData.TITLE,
                                          description=ModernAgileCurriculumNodeData.CONTENT)
        projects_node = NodeKnowledge(titel=ProjectNodeData.TITLE,
                                      description=ProjectNodeData.CONTENT)

        self.interviews_trys_node.connect(expectations_trys_node)
        self.interviews_trys_node.connect(working_in_teams_trys_node)
        self.interviews_trys_node.connect(deficit_frontend_development_node)
        self.interviews_trys_node.connect(deficit_hardware_node)
        self.interviews_trys_node.connect(deficit_it_security_node)
        self.interviews_trys_node.connect(interactive_modules_node)
        self.interviews_trys_node.connect(elective_subject_node)
        self.interviews_trys_node.connect(modern_agile_node)
        self.interviews_trys_node.connect(projects_node)


        graph.add_new_node_to_graph(self.interviews_trys_node)
        graph.add_new_node_to_graph(expectations_trys_node)
        graph.add_new_node_to_graph(working_in_teams_trys_node)
        graph.add_new_node_to_graph(deficit_frontend_development_node)
        graph.add_new_node_to_graph(deficit_hardware_node)
        graph.add_new_node_to_graph(deficit_it_security_node)
        graph.add_new_node_to_graph(interactive_modules_node)
        graph.add_new_node_to_graph(elective_subject_node)
        graph.add_new_node_to_graph(modern_agile_node)
        graph.add_new_node_to_graph(projects_node)