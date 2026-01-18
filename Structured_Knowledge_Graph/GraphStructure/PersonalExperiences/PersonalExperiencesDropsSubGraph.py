# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import DropsNodeData
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences.Drops import ExamRequirementsNodeData, \
    RequirementsNodeData, AmountWritenExamsNodeData, KickoffOrgaNodeData, OldProgrammingLanguagesNodeData, \
    ExamMemorizationNodeData, PureLectureNodeData, BulkLearningExamsNodeData, ChatgptToSolveTasksNodeData, LateAssignmentsNodeData


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

        amount_written_exams_node= NodeKnowledge(titel=AmountWritenExamsNodeData.TITLE,
                                                 description=AmountWritenExamsNodeData.CONTENT)

        kickoff_orga_node = NodeKnowledge(titel=KickoffOrgaNodeData.TITLE,
                                          description=KickoffOrgaNodeData.CONTENT)

        old_programming_languages = NodeKnowledge(titel=OldProgrammingLanguagesNodeData.TITLE,
                                                description=OldProgrammingLanguagesNodeData.CONTENT)
        exam_memorization_node = NodeKnowledge(titel=ExamMemorizationNodeData.TITLE,
                                               description=ExamMemorizationNodeData.CONTENT)
        pure_lecture_node = NodeKnowledge(titel=PureLectureNodeData.TITLE,
                                          description=PureLectureNodeData.CONTENT)

        bulk_learning_exams_node = NodeKnowledge(titel=BulkLearningExamsNodeData.TITLE,
                                                 description=BulkLearningExamsNodeData.CONTENT)

        chatgpt_to_solve_tasks_node = NodeKnowledge(titel=ChatgptToSolveTasksNodeData.TITLE,
                                                    description=ChatgptToSolveTasksNodeData.CONTENT)

        late_assignments_node = NodeKnowledge(titel=LateAssignmentsNodeData.TITLE,
                                              description=LateAssignmentsNodeData.CONTENT)

        self.personal_experiences_drops_node.connect(exam_requirements_node)
        self.personal_experiences_drops_node.connect(requirements_node)
        self.personal_experiences_drops_node.connect(amount_written_exams_node)
        self.personal_experiences_drops_node.connect(kickoff_orga_node)
        self.personal_experiences_drops_node.connect(old_programming_languages)
        self.personal_experiences_drops_node.connect(bulk_learning_exams_node)
        self.personal_experiences_drops_node.connect(chatgpt_to_solve_tasks_node)
        self.personal_experiences_drops_node.connect(late_assignments_node)
        self.personal_experiences_drops_node.connect(exam_memorization_node)
        self.personal_experiences_drops_node.connect(pure_lecture_node)

        graph.add_new_node_to_graph(self.personal_experiences_drops_node)
        graph.add_new_node_to_graph(exam_requirements_node)
        graph.add_new_node_to_graph(requirements_node)
        graph.add_new_node_to_graph(amount_written_exams_node)
        graph.add_new_node_to_graph(kickoff_orga_node)
        graph.add_new_node_to_graph(old_programming_languages)
        graph.add_new_node_to_graph(exam_memorization_node)
        graph.add_new_node_to_graph(pure_lecture_node)
        graph.add_new_node_to_graph(bulk_learning_exams_node)
        graph.add_new_node_to_graph(chatgpt_to_solve_tasks_node)
        graph.add_new_node_to_graph(late_assignments_node)