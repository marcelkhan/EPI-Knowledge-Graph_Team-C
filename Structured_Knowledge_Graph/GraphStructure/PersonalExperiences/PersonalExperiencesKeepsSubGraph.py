# Created by Marcel Khan on 27.11.25.


from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Knowledge_Graph.GraphContent.KeepsDropsTrys import KeepsNodeData
from Structured_Knowledge_Graph.GraphContent.PersonalExperiences.Keeps import ProjectorientedModulesNodeData, \
    TeamworkNodeData, ModernSoftwareDevelopmentConceptsNodeData, PersonalResponsibilityNodeData, AvailabilityNodeData, \
    ClearModuleStructuresNodeData, LectureAndExercisesNodeData, FundamentalConceptsNodeData, CoreSubjectsNodeData, \
    AcademicResearchNodeData, CourseSpotAvailabilityNodeData, DigitalOrganisationNodeData, YearlyStructureNodeData, \
    PracticalRelevanceNodeData, CreativeCourseDesignNodeData, IntroductoryModulesNodeData, WorkWithCompaniesNodeData, \
    WorkingWithProfsNodeData, ModuleStructureNodeData, ModernEquipmentNodeData, GuestLecturesNodeData, \
    ExercisesNodeData, FeedbackCultureNodeData, SchoolEquipmentNodeData


class PersonalExperiencesKeepsSubGraph:
    personal_experiences_keeps_node: NodeIllustration

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.personal_experiences_keeps_node = NodeIllustration(titel=KeepsNodeData.TITLE,
                                                                image_name=KeepsNodeData.IMAGE_NAME)

        projectoriented_modules_node = NodeKnowledge(titel=ProjectorientedModulesNodeData.TITLE,
                                                description=ProjectorientedModulesNodeData.CONTENT)

        teamwork_node = NodeKnowledge(titel=TeamworkNodeData.TITLE,
                                      description=TeamworkNodeData.CONTENT)

        modern_software_development_concepts_node = NodeKnowledge(titel=ModernSoftwareDevelopmentConceptsNodeData.TITLE,
                                                                  description=ModernSoftwareDevelopmentConceptsNodeData.CONTENT)

        personal_responsibility_node = NodeKnowledge(titel=PersonalResponsibilityNodeData.TITLE,
                                                     description=PersonalResponsibilityNodeData.CONTENT)

        availability_node = NodeKnowledge(titel=AvailabilityNodeData.TITLE,
                                          description=AvailabilityNodeData.CONTENT)

        clear_module_structures_node = NodeKnowledge(titel=ClearModuleStructuresNodeData.TITLE,
                                                     description=ClearModuleStructuresNodeData.CONTENT)

        lecture_and_exercises_node = NodeKnowledge(titel=LectureAndExercisesNodeData.TITLE,
                                                   description=LectureAndExercisesNodeData.CONTENT)

        fundamental_concepts_node = NodeKnowledge(titel=FundamentalConceptsNodeData.TITLE,
                                                  description=FundamentalConceptsNodeData.CONTENT)

        core_subjects_node = NodeKnowledge(titel=CoreSubjectsNodeData.TITLE,
                                           description=CoreSubjectsNodeData.CONTENT)

        academic_research_node = NodeKnowledge(titel=AcademicResearchNodeData.TITLE,
                                               description=AcademicResearchNodeData.CONTENT)

        course_spot_availability_node = NodeKnowledge(titel=CourseSpotAvailabilityNodeData.TITLE,
                                                      description=CourseSpotAvailabilityNodeData.CONTENT)

        digital_organisation_node = NodeKnowledge(titel=DigitalOrganisationNodeData.TITLE,
                                                  description=DigitalOrganisationNodeData.CONTENT)

        yearly_structure_node = NodeKnowledge(titel=YearlyStructureNodeData.TITLE,
                                              description=YearlyStructureNodeData.CONTENT)

        practical_relevance_node = NodeKnowledge(titel=PracticalRelevanceNodeData.TITLE,
                                                 description=PracticalRelevanceNodeData.CONTENT)

        creative_course_design_node = NodeKnowledge(titel=CreativeCourseDesignNodeData.TITLE,
                                                    description=CreativeCourseDesignNodeData.CONTENT)

        introductory_modules_node = NodeKnowledge(titel=IntroductoryModulesNodeData.TITLE,
                                                  description=IntroductoryModulesNodeData.CONTENT)

        work_with_companies_node = NodeKnowledge(titel=WorkWithCompaniesNodeData.TITLE,
                                                 description=WorkWithCompaniesNodeData.CONTENT)

        working_with_profs_node = NodeKnowledge(titel=WorkingWithProfsNodeData.TITLE,
                                                description=WorkingWithProfsNodeData.CONTENT)

        module_structure_node = NodeKnowledge(titel=ModuleStructureNodeData.TITLE,
                                              description=ModuleStructureNodeData.CONTENT)

        modern_equipment_node = NodeKnowledge(titel=ModernEquipmentNodeData.TITLE,
                                              description=ModernEquipmentNodeData.CONTENT)

        guest_lectures_node = NodeKnowledge(titel=GuestLecturesNodeData.TITLE,
                                            description=GuestLecturesNodeData.CONTENT)
        exercises_node = NodeKnowledge(titel=ExercisesNodeData.TITLE,
                                       description=ExercisesNodeData.CONTENT)
        feedback_culture_node = NodeKnowledge(titel=FeedbackCultureNodeData.TITLE,
                                              description=FeedbackCultureNodeData.CONTENT)
        school_equipment_node = NodeKnowledge(titel=SchoolEquipmentNodeData.TITLE,
                                              description=SchoolEquipmentNodeData.CONTENT)

        self.personal_experiences_keeps_node.connect(projectoriented_modules_node)
        self.personal_experiences_keeps_node.connect(teamwork_node)
        self.personal_experiences_keeps_node.connect(modern_software_development_concepts_node)
        self.personal_experiences_keeps_node.connect(personal_responsibility_node)
        self.personal_experiences_keeps_node.connect(availability_node)
        self.personal_experiences_keeps_node.connect(clear_module_structures_node)
        self.personal_experiences_keeps_node.connect(lecture_and_exercises_node)
        self.personal_experiences_keeps_node.connect(fundamental_concepts_node)
        self.personal_experiences_keeps_node.connect(core_subjects_node)
        self.personal_experiences_keeps_node.connect(academic_research_node)
        self.personal_experiences_keeps_node.connect(course_spot_availability_node)
        self.personal_experiences_keeps_node.connect(digital_organisation_node)
        self.personal_experiences_keeps_node.connect(yearly_structure_node)
        self.personal_experiences_keeps_node.connect(practical_relevance_node)
        self.personal_experiences_keeps_node.connect(creative_course_design_node)
        self.personal_experiences_keeps_node.connect(introductory_modules_node)
        self.personal_experiences_keeps_node.connect(work_with_companies_node)
        self.personal_experiences_keeps_node.connect(working_with_profs_node)
        self.personal_experiences_keeps_node.connect(module_structure_node)
        self.personal_experiences_keeps_node.connect(modern_equipment_node)
        self.personal_experiences_keeps_node.connect(guest_lectures_node)
        self.personal_experiences_keeps_node.connect(exercises_node)
        self.personal_experiences_keeps_node.connect(feedback_culture_node)
        self.personal_experiences_keeps_node.connect(school_equipment_node)

        graph.add_new_node_to_graph(self.personal_experiences_keeps_node)
        graph.add_new_node_to_graph(projectoriented_modules_node)
        graph.add_new_node_to_graph(teamwork_node)
        graph.add_new_node_to_graph(modern_software_development_concepts_node)
        graph.add_new_node_to_graph(personal_responsibility_node)
        graph.add_new_node_to_graph(availability_node)
        graph.add_new_node_to_graph(clear_module_structures_node)
        graph.add_new_node_to_graph(lecture_and_exercises_node)
        graph.add_new_node_to_graph(fundamental_concepts_node)
        graph.add_new_node_to_graph(core_subjects_node)
        graph.add_new_node_to_graph(academic_research_node)
        graph.add_new_node_to_graph(course_spot_availability_node)
        graph.add_new_node_to_graph(digital_organisation_node)
        graph.add_new_node_to_graph(yearly_structure_node)
        graph.add_new_node_to_graph(practical_relevance_node)
        graph.add_new_node_to_graph(creative_course_design_node)
        graph.add_new_node_to_graph(introductory_modules_node)
        graph.add_new_node_to_graph(work_with_companies_node)
        graph.add_new_node_to_graph(working_with_profs_node)
        graph.add_new_node_to_graph(module_structure_node)
        graph.add_new_node_to_graph(modern_equipment_node)
        graph.add_new_node_to_graph(guest_lectures_node)
        graph.add_new_node_to_graph(exercises_node)
        graph.add_new_node_to_graph(feedback_culture_node)
        graph.add_new_node_to_graph(school_equipment_node)