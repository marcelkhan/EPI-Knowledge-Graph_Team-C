# Created by Marcel Khan on 27.11.25.
from GraphModel.Graph import Graph
from Structured_Knowledge_Graph.GraphStructure.EvaluationSubGraph import EvaluationSubGraph
from Structured_Knowledge_Graph.GraphStructure.InterviewsSubGraph import InterviewsSubGraph
from Structured_Knowledge_Graph.GraphStructure.PersonalExperiencesSubGraph import PersonalExperiencesSubGraph


class StructuredKnowledgeGraph:

    evaluation_subgraph: EvaluationSubGraph
    personal_experiences_subgraph: PersonalExperiencesSubGraph
    interviews_subgraph: InterviewsSubGraph

    def __init__(self, graph: Graph):
        self.assemble_graph(graph)
        self.connect_sub_graphs()

    def assemble_graph(self, graph):
        self.evaluation_subgraph = EvaluationSubGraph(graph)
        self.personal_experiences_subgraph = PersonalExperiencesSubGraph(graph)
        self.interviews_subgraph = InterviewsSubGraph(graph)

    def connect_sub_graphs(self):
        self.evaluation_subgraph.evaluation_node.connect(
            self.personal_experiences_subgraph.personal_experiences_node
        )
        self.evaluation_subgraph.evaluation_node.connect(
            self.interviews_subgraph.interviews_node
        )