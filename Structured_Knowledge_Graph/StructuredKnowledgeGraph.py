# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from Structured_Knowledge_Graph.GraphStructure.EvaluationSubGraph import EvaluationSubGraph
from Structured_Knowledge_Graph.GraphStructure.InterviewsSubGraph import InterviewsSubGraph
from Structured_Knowledge_Graph.GraphStructure.PersonalExperiences.PersonalExperiencesDropsSubGraph import PersonalExperiencesDropsSubGraph
from Structured_Knowledge_Graph.GraphStructure.PersonalExperiences.PersonalExperiencesKeepsSubGraph import PersonalExperiencesKeepsSubGraph
from Structured_Knowledge_Graph.GraphStructure.PersonalExperiences.PersonalExperiencesSubGraph import PersonalExperiencesSubGraph
from Structured_Knowledge_Graph.GraphStructure.PersonalExperiences.PersonalExperiencesTrysSubGraph import PersonalExperiencesTrysSubGraph


class StructuredKnowledgeGraph:

    evaluation_subgraph: EvaluationSubGraph
    personal_experiences_subgraph: PersonalExperiencesSubGraph
    personal_experiences_keeps_subgraph: PersonalExperiencesKeepsSubGraph
    personal_experiences_drops_subgraph: PersonalExperiencesDropsSubGraph
    personalExperiencesTrysSubGraph: PersonalExperiencesTrysSubGraph
    interviews_subgraph: InterviewsSubGraph

    def __init__(self, graph: Graph):
        self.assemble_graph(graph)
        self.connect_sub_graphs()

    def assemble_graph(self, graph):
        self.evaluation_subgraph = EvaluationSubGraph(graph)
        self.personal_experiences_subgraph = PersonalExperiencesSubGraph(graph)
        self.personal_experiences_keeps_subgraph = PersonalExperiencesKeepsSubGraph(graph)
        self.personal_experiences_drops_subgraph = PersonalExperiencesDropsSubGraph(graph)
        self.personalExperiencesTrysSubGraph = PersonalExperiencesTrysSubGraph(graph)
        self.interviews_subgraph = InterviewsSubGraph(graph)

    def connect_sub_graphs(self):
        # evaluation
        self.evaluation_subgraph.evaluation_node.connect(
            self.personal_experiences_subgraph.personal_experiences_node
        )
        self.evaluation_subgraph.evaluation_node.connect(
            self.interviews_subgraph.interviews_node
        )

        # personal experiences
        self.personal_experiences_subgraph.personal_experiences_node.connect(
            self.personal_experiences_keeps_subgraph.personal_experiences_keeps_node
        )
        self.personal_experiences_subgraph.personal_experiences_node.connect(
            self.personal_experiences_drops_subgraph.personal_experiences_drops_node
        )
        self.personal_experiences_subgraph.personal_experiences_node.connect(
            self.personalExperiencesTrysSubGraph.personal_experiences_trys_node
        )