# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import TrysNodeData
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences.Trys import PreparationForThesisNodeData, \
    InsecurityNodeData, ComputerScienceInASocialContextNodeData, SupportNodeData, LearningJourneyNodeData, \
    CourseStructureNodeData, ScientificPapersNodeData, ExamPeriodNodeData, HybridLectureNodeData, \
    MentoringEarlyNodeData, VisitMoreLecturesNodeData


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

        course_structure_node = NodeKnowledge(titel=CourseStructureNodeData.TITLE,
                                              description=CourseStructureNodeData.CONTENT)

        scientific_papers_node = NodeKnowledge(titel=ScientificPapersNodeData.TITLE,
                                               description=ScientificPapersNodeData.CONTENT)

        exam_period_node = NodeKnowledge(titel=ExamPeriodNodeData.TITLE,
                                         description=ExamPeriodNodeData.CONTENT)

        hybrid_lecture_node=NodeKnowledge(titel=HybridLectureNodeData.TITLE,
                                          description=HybridLectureNodeData.CONTENT)

        mentoring_early_node=NodeKnowledge(titel=MentoringEarlyNodeData.TITLE,
                                           description=MentoringEarlyNodeData.CONTENT)

        visit_more_lectures_node = NodeKnowledge(titel=VisitMoreLecturesNodeData.TITLE,
                                                       description=VisitMoreLecturesNodeData.CONTENT)

        self.personal_experiences_trys_node.connect(preparation_for_thesis_node)
        self.personal_experiences_trys_node.connect(insecurity_node)
        self.personal_experiences_trys_node.connect(computer_science_in_a_social_context_node)
        self.personal_experiences_trys_node.connect(support_node)
        self.personal_experiences_trys_node.connect(learning_journey_node)
        self.personal_experiences_trys_node.connect(course_structure_node)
        self.personal_experiences_trys_node.connect(scientific_papers_node)
        self.personal_experiences_trys_node.connect(exam_period_node)
        self.personal_experiences_trys_node.connect(hybrid_lecture_node)
        self.personal_experiences_trys_node.connect(mentoring_early_node)
        self.personal_experiences_trys_node.connect(visit_more_lectures_node)

        graph.add_new_node_to_graph(self.personal_experiences_trys_node)
        graph.add_new_node_to_graph(preparation_for_thesis_node)
        graph.add_new_node_to_graph(insecurity_node)
        graph.add_new_node_to_graph(computer_science_in_a_social_context_node)
        graph.add_new_node_to_graph(support_node)
        graph.add_new_node_to_graph(learning_journey_node)
        graph.add_new_node_to_graph(course_structure_node)
        graph.add_new_node_to_graph(scientific_papers_node)
        graph.add_new_node_to_graph(exam_period_node)
        graph.add_new_node_to_graph(hybrid_lecture_node)
        graph.add_new_node_to_graph(mentoring_early_node)
        graph.add_new_node_to_graph(visit_more_lectures_node)