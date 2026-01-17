# Created by Timon Kirch on 17.01.26.
from pygame.examples.cursors import image_name

from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews import InterviewsEvaluationsNodeData
from Structured_Knowledge_Graph.GraphContent.Interviews.Evaluations import ExpectationsNodeData, \
    StudyingSatisfactionNodeData, ExamRequirementsNodeData, TheoreticalAndPracticalAspectsNodeData, \
    StudyingSatisfactionResultsNodeData, ExamRequirementsResultsNodeData, TheoreticalAndPracticalAspectsResultsNodeData, \
    LearningMethodsNodeData, LearningMethodsResultsNodeData, OrganisationNodeData, SatisfactionWithStudyingNodeData, \
    WorkingInTeamsNodeData, OrganisationResultsNodeData, RecommendedStudyingPathResultNodeData, \
    SatisfactionWithStudyingResultsNodeData


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

        organisation_node = NodeIllustration(titel=OrganisationNodeData.TITEL,
                                           image_name=OrganisationNodeData.IMAGE_NAME)

        satisfaction_with_studying_node = NodeIllustration(titel=SatisfactionWithStudyingNodeData.TITEL,
                                                         image_name=SatisfactionWithStudyingNodeData.IMAGE_NAME)

        working_in_teams_node = NodeIllustration(titel=WorkingInTeamsNodeData.TITEL,
                                               image_name=WorkingInTeamsNodeData.IMAGE_NAME)

        studying_satisfaction_results_node = NodeKnowledge(titel=StudyingSatisfactionResultsNodeData.TITEL,
                                                           description=StudyingSatisfactionResultsNodeData.CONTENT)

        exam_requirements_results_node = NodeKnowledge(titel=ExamRequirementsResultsNodeData.TITEL,
                                                       description=ExamRequirementsResultsNodeData.CONTENT)

        theoretical_and_practical_aspects_results_node = NodeKnowledge(titel=TheoreticalAndPracticalAspectsResultsNodeData.TITEL,
                                                                       description=TheoreticalAndPracticalAspectsResultsNodeData.CONTENT)

        learning_methods_results_node =NodeKnowledge(titel=LearningMethodsResultsNodeData.TITEL,
                                                     description=LearningMethodsResultsNodeData.CONTENT)

        organisation_results_node =NodeKnowledge(titel=OrganisationResultsNodeData.TITEL,
                                                 description=OrganisationResultsNodeData.CONTENT)

        recommended_studying_path_results_node= NodeKnowledge(titel=RecommendedStudyingPathResultNodeData.TITEL,
                                                              description=RecommendedStudyingPathResultNodeData.CONTENT)

        satisfaction_with_studying_results_node = NodeKnowledge(titel=SatisfactionWithStudyingResultsNodeData.TITEL,
                                                                description=SatisfactionWithStudyingResultsNodeData.CONTENT)

        working_in_teams_results_node = NodeKnowledge(titel=SatisfactionWithStudyingResultsNodeData.TITEL,
                                                      description=SatisfactionWithStudyingResultsNodeData.CONTENT)

        self.interviews_evaluations_node.connect(expectations_node)
        self.interviews_evaluations_node.connect(studying_satisfaction_node)
        self.interviews_evaluations_node.connect(exam_requirements_node)
        self.interviews_evaluations_node.connect(theoretical_and_practical_aspects_node)
        self.interviews_evaluations_node.connect(studying_satisfaction_results_node)
        self.interviews_evaluations_node.connect(exam_requirements_results_node)
        self.interviews_evaluations_node.connect(theoretical_and_practical_aspects_results_node)
        self.interviews_evaluations_node.connect(learning_methods_results_node)
        self.interviews_evaluations_node.connect(learning_methods_node)
        self.interviews_evaluations_node.connect(organisation_node)
        self.interviews_evaluations_node.connect(working_in_teams_node)
        self.interviews_evaluations_node.connect(satisfaction_with_studying_node)
        self.interviews_evaluations_node.connect(organisation_results_node)
        self.interviews_evaluations_node.connect(recommended_studying_path_results_node)
        self.interviews_evaluations_node.connect(satisfaction_with_studying_results_node)
        self.interviews_evaluations_node.connect(working_in_teams_results_node)

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
        graph.add_new_node_to_graph(organisation_node)
        graph.add_new_node_to_graph(working_in_teams_node)
        graph.add_new_node_to_graph(satisfaction_with_studying_node)
        graph.add_new_node_to_graph(organisation_results_node)
        graph.add_new_node_to_graph(recommended_studying_path_results_node)
        graph.add_new_node_to_graph(satisfaction_with_studying_results_node)
        graph.add_new_node_to_graph(working_in_teams_results_node)