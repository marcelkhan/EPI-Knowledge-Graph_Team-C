# Created by Timon Kirch on 17.01.26.
from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews import InterviewsEvaluationsNodeData
from Structured_Knowledge_Graph.GraphContent.Interviews.Evaluations import ExpectationsNodeData, \
    StudyingSatisfactionNodeData, ExamRequirementsNodeData, TheoreticalAndPracticalAspectsNodeData, \
    StudyingSatisfactionResultsNodeData, ExamRequirementsResultsNodeData, TheoreticalAndPracticalAspectsResultsNodeData, \
    LearningMethodsNodeData, LearningMethodsResultsNodeData, ExamTypeDislikesResultsNoteData, ExamTypeDislikesNodeData, \
    AgedExamTypesNodeData, AmountOfTopicsNodeData, AmountOfTopicsResultsNodeData, QualityOfTopicsNodeData, \
    QualityOfTopicsResultsNodeData, IncreaseOfLectureTypeResultsNodeData, IncreaseOfLectureTypeNodeData


class InterviewsEvaluationsSubGraph:
    interviews_evaluations_node: NodeKnowledge

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.interviews_evaluations_node = NodeKnowledge(titel=InterviewsEvaluationsNodeData.TITEL,
                                                         description=InterviewsEvaluationsNodeData.CONTENT)

        expectations_node = NodeKnowledge(titel=ExpectationsNodeData.TITEL,
                                          description=ExpectationsNodeData.CONTENT)

        studying_satisfaction_node = NodeIllustration(titel=StudyingSatisfactionNodeData.TITEL,
                                                      image_name=StudyingSatisfactionNodeData.IMAGE_NAME)

        exam_requirements_node = NodeIllustration(titel=ExamRequirementsNodeData.TITEL,
                                                  image_name=ExamRequirementsNodeData.IMAGE_NAME)

        theoretical_and_practical_aspects_node = NodeIllustration(titel=TheoreticalAndPracticalAspectsNodeData.TITEL,
                                                                  image_name=TheoreticalAndPracticalAspectsNodeData.IMAGE_NAME)

        learning_methods_node = NodeIllustration(titel=LearningMethodsNodeData.TITEL,
                                                 image_name=LearningMethodsNodeData.IMAGE_NAME)

        exam_type_dislikes_node = NodeIllustration(titel=ExamTypeDislikesNodeData.TITEL,
                                                  image_name=ExamTypeDislikesNodeData.IMAGE_NAME)

        amount_of_topics_node = NodeIllustration(titel=AmountOfTopicsNodeData.TITEL,
                                                 image_name=AmountOfTopicsNodeData.IMAGE_NAME)

        quality_of_topics_node = NodeIllustration(titel=QualityOfTopicsNodeData.TITEL,
                                                  image_name=QualityOfTopicsNodeData.IMAGE_NAME)

        increase_of_lecture_type_node = NodeIllustration(titel=IncreaseOfLectureTypeNodeData.TITEL,
                                                         image_name=IncreaseOfLectureTypeNodeData.IMAGE_NAME)

        studying_satisfaction_results_node = NodeKnowledge(titel=StudyingSatisfactionResultsNodeData.TITEL,
                                                           description=StudyingSatisfactionResultsNodeData.CONTENT)

        exam_requirements_results_node = NodeKnowledge(titel=ExamRequirementsResultsNodeData.TITEL,
                                                       description=ExamRequirementsResultsNodeData.CONTENT)

        theoretical_and_practical_aspects_results_node = NodeKnowledge(titel=TheoreticalAndPracticalAspectsResultsNodeData.TITEL,
                                                                       description=TheoreticalAndPracticalAspectsResultsNodeData.CONTENT)

        learning_methods_results_node = NodeKnowledge(titel=LearningMethodsResultsNodeData.TITEL,
                                                     description=LearningMethodsResultsNodeData.CONTENT)

        exam_type_dislikes_results_node = NodeKnowledge(titel=ExamTypeDislikesResultsNoteData.TITEL,
                                                        description=ExamTypeDislikesResultsNoteData.CONTENT)

        aged_exam_types_node = NodeKnowledge(titel=AgedExamTypesNodeData.TITEL,
                                             description=AgedExamTypesNodeData.CONTENT)

        amount_of_topics_results_node = NodeKnowledge(titel=AmountOfTopicsResultsNodeData.TITEL,
                                                      description=AmountOfTopicsResultsNodeData.CONTENT)

        quality_of_topics_results_node = NodeKnowledge(titel=QualityOfTopicsResultsNodeData.TITEL,
                                                       description=QualityOfTopicsResultsNodeData.CONTENT)

        increase_of_lecture_type_results_node = NodeKnowledge(titel=IncreaseOfLectureTypeResultsNodeData.TITEL,
                                                              description=IncreaseOfLectureTypeResultsNodeData.CONTENT)

        self.interviews_evaluations_node.connect(expectations_node)
        self.interviews_evaluations_node.connect(studying_satisfaction_node)
        self.interviews_evaluations_node.connect(exam_requirements_node)
        self.interviews_evaluations_node.connect(theoretical_and_practical_aspects_node)
        self.interviews_evaluations_node.connect(studying_satisfaction_results_node)
        self.interviews_evaluations_node.connect(exam_requirements_results_node)
        self.interviews_evaluations_node.connect(theoretical_and_practical_aspects_results_node)
        self.interviews_evaluations_node.connect(learning_methods_results_node)
        self.interviews_evaluations_node.connect(learning_methods_node)
        self.interviews_evaluations_node.connect(exam_type_dislikes_results_node)
        self.interviews_evaluations_node.connect(exam_type_dislikes_node)
        self.interviews_evaluations_node.connect(aged_exam_types_node)
        self.interviews_evaluations_node.connect(amount_of_topics_results_node)
        self.interviews_evaluations_node.connect(amount_of_topics_node)
        self.interviews_evaluations_node.connect(quality_of_topics_node)
        self.interviews_evaluations_node.connect(quality_of_topics_results_node)
        self.interviews_evaluations_node.connect(increase_of_lecture_type_results_node)
        self.interviews_evaluations_node.connect(increase_of_lecture_type_node)

        graph.add_new_node_to_graph(self.interviews_evaluations_node)
        graph.add_new_node_to_graph(expectations_node)
        graph.add_new_node_to_graph(studying_satisfaction_node)
        graph.add_new_node_to_graph(exam_requirements_node)
        graph.add_new_node_to_graph(theoretical_and_practical_aspects_node)
        graph.add_new_node_to_graph(studying_satisfaction_results_node)
        graph.add_new_node_to_graph(exam_requirements_results_node)
        graph.add_new_node_to_graph(theoretical_and_practical_aspects_results_node)
        graph.add_new_node_to_graph(learning_methods_results_node)
        graph.add_new_node_to_graph(learning_methods_node)
        graph.add_new_node_to_graph(exam_type_dislikes_results_node)
        graph.add_new_node_to_graph(exam_type_dislikes_node)
        graph.add_new_node_to_graph(aged_exam_types_node)
        graph.add_new_node_to_graph(amount_of_topics_results_node)
        graph.add_new_node_to_graph(amount_of_topics_node)
        graph.add_new_node_to_graph(quality_of_topics_node)
        graph.add_new_node_to_graph(quality_of_topics_results_node)
        graph.add_new_node_to_graph(increase_of_lecture_type_results_node)
        graph.add_new_node_to_graph(increase_of_lecture_type_node)