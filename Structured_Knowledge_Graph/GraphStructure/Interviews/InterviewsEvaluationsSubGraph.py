# Created by Timon Kirch on 17.01.26.
from pygame.examples.cursors import image_name

from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.Interviews.Trys import TRYModulsMoreInteraktivNodeData
from Structured_Knowledge_Graph.GraphContent.Interviews import InterviewsEvaluationsNodeData
from Structured_Knowledge_Graph.GraphContent.Interviews.Evaluations import ExpectationsNodeData, \
    StudyingSatisfactionNodeData, ExamRequirementsNodeData, TheoreticalAndPracticalAspectsNodeData, \
    StudyingSatisfactionResultsNodeData, ExamRequirementsResultsNodeData, TheoreticalAndPracticalAspectsResultsNodeData, \
    LearningMethodsNodeData, LearningMethodsResultsNodeData, ExamTypeDislikesResultsNoteData, ExamTypeDislikesNodeData, \
    AgedExamTypesNodeData, AmountOfTopicsNodeData, AmountOfTopicsResultsNodeData, QualityOfTopicsNodeData, \
    QualityOfTopicsResultsNodeData, IncreaseOfLectureTypeResultsNodeData, IncreaseOfLectureTypeNodeData, \
    WorkingInTeamsNodeData, SatisfactionWithStudyingNodeData, OrganisationNodeData, OrganisationResultsNodeData, \
    RecommendedStudyingPathResultNodeData, SatisfactionWithStudyingResultsNodeData, WorkingInTeamsResultsNodeData,\
    WhichModulDidYouLikeTheMostAndWhyNodeData,WhichModulWhichWereIrrelevantOldOrBadTransmittedNodeData,\
    WhichModulsWhereNotPraxisNearEnoughNodeData,WhichThemesWereEspeciallyWorthNodeData,WhichSubjektsYouWantToKnowMoredNodeData


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

        organisation_results_node = NodeKnowledge(titel=OrganisationResultsNodeData.TITEL,
                                                  description=OrganisationResultsNodeData.CONTENT)

        recommended_studying_path_results_node = NodeKnowledge(titel=RecommendedStudyingPathResultNodeData.TITEL,
                                                               description=RecommendedStudyingPathResultNodeData.CONTENT)

        satisfaction_with_studying_results_node = NodeKnowledge(titel=SatisfactionWithStudyingResultsNodeData.TITEL,
                                                                description=SatisfactionWithStudyingResultsNodeData.CONTENT)

        working_in_teams_results_node = NodeKnowledge(titel=WorkingInTeamsResultsNodeData.TITEL,
                                                      description=WorkingInTeamsResultsNodeData.CONTENT)
        which_Module_did_you_like_the_most_node=NodeKnowledge(titel=WhichModulDidYouLikeTheMostAndWhyNodeData.TITEL,
                                                              description=WhichModulDidYouLikeTheMostAndWhyNodeData.CONTENT)
        more_interaktive_node=NodeKnowledge(titel=TRYModulsMoreInteraktivNodeData,
                                                       description=TRYModulsMoreInteraktivNodeData.CONTENT)
        which_Module_Were_Irrelevant_Old_Or_Baad_Transmitted_node=NodeKnowledge(titel=WhichModulWhichWereIrrelevantOldOrBadTransmittedNodeData.TITLE,
                                                                                description=WhichModulWhichWereIrrelevantOldOrBadTransmittedNodeData.CONTENT)
        which_Module_Were_Not_Praxis_Near_Enough_node=NodeKnowledge(titel=WhichModulsWhereNotPraxisNearEnoughNodeData.TITLE,
                                                                    description=WhichModulsWhereNotPraxisNearEnoughNodeData.CONTENT)

        which_Themes_Were_Especially_Worht_node=NodeKnowledge(titel=WhichThemesWereEspeciallyWorthNodeData.TITLE,
                                                              description=WhichThemesWereEspeciallyWorthNodeData.CONTENT)
        which_Subjekts_You_Want_To_Know_More_node=NodeIllustration(titel=WhichSubjektsYouWantToKnowMoredNodeData.TITEL,
                                                                image_name=WhichSubjektsYouWantToKnowMoredNodeData.IMAGE_NAME)

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
        self.interviews_evaluations_node.connect(organisation_node)
        self.interviews_evaluations_node.connect(working_in_teams_node)
        self.interviews_evaluations_node.connect(satisfaction_with_studying_node)
        self.interviews_evaluations_node.connect(organisation_results_node)
        self.interviews_evaluations_node.connect(recommended_studying_path_results_node)
        self.interviews_evaluations_node.connect(satisfaction_with_studying_results_node)
        self.interviews_evaluations_node.connect(working_in_teams_results_node)
        self.interviews_evaluations_node.connect(which_Module_did_you_like_the_most_node)
        self.interviews_evaluations_node.connect(which_Module_Were_Irrelevant_Old_Or_Baad_Transmitted_node)
        self.interviews_evaluations_node.connect(which_Module_Were_Not_Praxis_Near_Enough_node)
        self.interviews_evaluations_node.connect(which_Themes_Were_Especially_Worht_node)
        self.interviews_evaluations_node.connect(which_Subjekts_You_Want_To_Know_More_node)
        ##self.interviews_evaluations_node.connect(more_interaktive_node)

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
        graph.add_new_node_to_graph(organisation_node)
        graph.add_new_node_to_graph(working_in_teams_node)
        graph.add_new_node_to_graph(satisfaction_with_studying_node)
        graph.add_new_node_to_graph(organisation_results_node)
        graph.add_new_node_to_graph(recommended_studying_path_results_node)
        graph.add_new_node_to_graph(satisfaction_with_studying_results_node)
        graph.add_new_node_to_graph(working_in_teams_results_node)
        graph.add_new_node_to_graph(which_Module_did_you_like_the_most_node)
        graph.add_new_node_to_graph(which_Module_Were_Irrelevant_Old_Or_Baad_Transmitted_node)
        graph.add_new_node_to_graph(which_Module_Were_Not_Praxis_Near_Enough_node)
        graph.add_new_node_to_graph(which_Themes_Were_Especially_Worht_node)
        graph.add_new_node_to_graph(which_Subjekts_You_Want_To_Know_More_node)
        ##graph.add_new_node_to_graph(more_interaktive_node)

