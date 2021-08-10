# Semantic skillmatching in Open Source Hardware (OSH) Project Communites

- This repository handles the third workpackage (WP3) of the [OPEN!NEXT project](https://opennext.eu/) to serve possible solutions for Open Source Hardware Commmunity needs.
- OPEN!NEXT received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement no. 869984.
- Skillmatching as a measure of community management was identified, which is the main focus here.\
  For this, a generic ontology model of a possible open souce hardware project landscape was developed.\
  The implementation of the ontology took results from a previous project (OPEN!) into account that also analysed processes and dynamics of OSH community.
- Purpose of the ontology model is to fulfill the concepted user stories defined below.

## USER FLOWS

To gather the needs of the OSH community, expert interviews have been conducted. The team derived user stories from the input of those interviews.\
User Stories of the D3.1 deliverable of the project can be accessed [here](https://github.com/OPEN-NEXT/wp3_pub)

Three main user stories are scope of the case:

 1.	As a contributor on an OSH online platform, I want to add my skills and interests to my profile, so that others know more about my abilities.
 2. As a contributor on an OSH online platform, I want to find projects that require my specific skills in tasks, so that I can use, improve or evolve my skills.
 3. As a project core team, we want to find contributors based on their skills and interests so that they can help in carrying out a specific task.

## CURRENT STATUS
The current development aim was to create a network that is able to give possibilities on assigning skills and interests to contributor profiles, tasks and projects and make them visible for queries. This was built based on the User flows described bevorhand. <br>

- The currently first draft of the ontology model is validated with a sample of project data from Wikifactory. For the validation, user flows were identified and, based on this, queries developed to check for existing results. 
- The ontology model has still to be validated by user interaction.
- Afterwards possible adaptions will taken into account.
- The repository will be updated respectively over time.

Building on this development, the next steps aim is to identify regularities for skill matching in order to integrate them into the semantic network and enable case-related automatic assignment.

## ONTOLOGY MODEL

For customization reasons, the ontology model consists of three ontologies referring to each other but are therefore replacable necessary:

1. Open source hardware product development (OSHPD) ontology
   - This OWL ontology holds the architecture and semantic restrictions of the project landscape
   - Main classes for the skillmatching case are "Person", "Project", "Task" and "Skill", that are related through properties.
   - Property restrictions arise from the use cases before mentioned
   - The OSHPD ontology imports the skill ontology

2. Skill ontology
   - This OWL ontology is based on the [ESCO skill hierarchy](https://ec.europa.eu/esco/portal/skill)
   - The ESCO hierarchy was cropped to the topics of mechanics, electrics/electronics, furniture and cars/mobiliy.
   - Afterwards a reclustering was done for ease of use purposes
   - The skill ontology is still to be validated with OSH project data

3. Instantiation file
   - This file holds needed project data of the individuals
   - The file refers to and uses class and property expressions from the other two ontologies.


## INSTRUCTIONS TO USE

The demonstrator has two the main functions instantiation and querying. Each of their usages are described below:<br>

  **i.	Instantiation** <br><p>
An ontology was created for the development goal of skill matching. To make it widely applicable, it was created without any instances. Project data from WIF was integrated via data mapping afterwards. This offers the advantage of simpler validation in case the data structure changes. If so, a new instantiation can simply be achieved by changing the mappings. The mapping approach is based on the idea of [Méndez et al.](http://ceur-ws.org/Vol-2721/paper593.pdf) and connects the ontology concepts with JSON formatted input data via annotation properties. That means, that the mapping information is directly stored in the ontology itself. The mapping process is visualized in Figure 24. Classes and properties in the semantic network are annotated with JSON pointers to the relating fields in the GraphQL API from WIF whose data was used for validation. For every mapping a new annotation property is created. This gives the possibility to use more than one data source from either the same or a different platform. During later instantiation it is possible to choose in the demonstrator code how the mapping should be used.
For the user flow three different JSON data source files were created from query results of the WIF GraphQL API. This was done, so the first validation was not compromised by changes in the data structure during its constant progression and also because the user data had to be anonymized before used for instantiation.
During the mapping process, the annotation with the JSON pointer is read out of the ontology and used to query the information in the JSON file that contains the input data. Afterwards those query results are instantiated based on which concept (class or property) was annotated in the first place. The instantiated individuals are saved in a separate file that uses the ontology vocabulary. 

|![mapping_process_short](https://user-images.githubusercontent.com/59953831/128838638-3b051997-62d2-42c8-946b-9b1cdbdbb381.png)| 
|:--:| 
| *Figure 24: Mapping process* |
</p>

  **ii.	Querying** <br><p>
After instantiation, the semantic network can be queried. The query functions in the demonstrator use a query string as input, therefore individual queries are also possible, if implemented in the code. More on this is explained in the step-by-step example section for querying.</p>

### Step-by-step example for contributor and project core team

<p>This sub-section provides an example of how a contributor and a project core team member can interact with the skill-matchmaking demonstrator. The contributor would like to update his/her profile and hence can select the suitable skills from a list of skills provided by querying the skill ontology. The project core team member can select the skills and tools required to fulfil a task in the project by querying the skill ontology in the backend. The current demonstrator is integrated with data from the Wikifactory platform and an example of these query results is shown below.</p>

Direct user interaction with the ontology takes place in user flows 2 and 3. The query process of those will be described in detail. To query the instantiated ontology, the code in the demonstrator can be used or every ontology editor with query interface as well (one suggestion would be the [Protégé](https://protege.stanford.edu/) editor with SPARQL plugin). The demonstrator provides queries based on the persona described. For the two user stories, the two queries are shown in the table below . For more elaborated insights on how to use SPARQL for queries, please refer to [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/). <br>

  |UF No.|SPARQL Query|
  |------|------------| 
  |UF2|*SELECT ?User ?Skill_Entity ?Project <br> WHERE{?User a oshpd:User; oshpd:User_id “uid113”; skills:skill_action ?Skill_Entity.<br> ?Skill_Entity oshpd:tags ?Project. ?Project a oshpd:Project.}*|
  |UF3|*SELECT ?User ?Skill_Entity <br> WHERE {?Skill_Entity skills:SkillEntity_name "3dprinting"; skills:possible_action ?User.}*|

The query for **UF2** looks for projects that are tagged with the same skills a user (here exemplary user *uid113*) provides.<br>
The query for **UF3** looks for all users that are connected to the *3dprinting Skill_Entity*.

####	Using the query code in the demonstrator
<p>There is also a query class provided in the demonstrator with some example queries. To use those, you need to clone the repository or copy the source code of the Queries.java class in the query package. For other queries, those have to be written in strings and given as parameters into the query function. A flow charts in the annex section gives a better illustration of the process.</p>

1.	At the beginning the repository has to be cloned or downloaded. (This step depends on the environment used and should accordingly be identified on an individual basis. An example for the stated software stack is given in the Installation section.)
2.	The *Queries.java* class from the query package provides exemplary queries according to the presented user stories that can be used. Otherwise new methods that return an individual query string can be added as well.<br>
    |![Method_to_create_a_query_string_for_user_interest](https://user-images.githubusercontent.com/59953831/128843826-ee5c4d5d-28f2-43b2-9bb1-7dc9acacf7b7.png)|
    |:---:|
    | *Figure 25: Method to create a query string for user interest* |
3.  If the ontologies were to be changed, the prefixes in the string variable prefixes of class Queries.java need to be changed accordingly as well.<br>
    |![Fig 26_Query_prefixes](https://user-images.githubusercontent.com/59953831/128845285-61620459-b42a-4e24-be1b-fdff175943e8.png)|
    |:---:|
    | *Figure 26: Query prefixes* |
    
    Now the *RunQuery.java* class from the *run* package has to be specified.
4.  The IRI of the ontology to query has to be set in the *RunQuery.java* class (cf. *Figure 27*)
5.  The language of the model to open has to be specified in the *openModel()* method in *RunQuery.java*.<br>
    |![Fig 27_Setup_for_query_execution_using_QueryExec java](https://user-images.githubusercontent.com/59953831/128845553-02de9fb2-1db0-4203-946d-5778fa5fc4ce.png)|
    |:---:|
    | *Figure 27: Setup for query execution using QueryExec.java class* |
6.  The query execution method of class *QueryExec.java* needs a SPARQL query as string parameter. For this, the query string generation methods of class *Queries.java* can be used. <br>
    |![Fig 28_Execution_of_query_using_the_query_generation_method](https://user-images.githubusercontent.com/59953831/128846095-36993b59-c5e0-4efd-a47e-ed07e2be0935.png)|
    |:---:|
    | *Figure 28: Execution of query using the query generation method* |
7.  he generated result list can now further be processed, e.g. for frontend display.
<br>

#### Using an editor with SPARQL functionality
  
<p>To show the general function, an example of the use is given with the ontology editor Protégé which also provides a SPARQL plugin for query. </p>

1.	Loading the ontology from its location. Here the repository location was used.<br>
    | ![Fig 29_Load_ontology_from_URI_via_protege](https://user-images.githubusercontent.com/59953831/128848793-e20b45f4-379f-4049-be1d-48d5a56bbcb5.png)|
    |:---:|
    |*Figure 29: Load ontology from URI via Protégé editor*|
2.  The editors SPARQL- /Query- interface needs to be opened.<br>
    | ![Fig 30_SPARQL_plugin_tab_in_protege](https://user-images.githubusercontent.com/59953831/128849792-75983c9a-e360-4a36-9c06-f628a722620d.png) |
    |:---:|
    |*Figure 30: SPARQL-plugin tab in Protégé editor*|
3.  Adding prefixes and query string to the interface and execution of query. Figure 31 exemplary shows the UF2 query.<br>
    | ![Fig 31_UF2_Query with prefixes](https://user-images.githubusercontent.com/59953831/128849821-18381df7-b819-43c0-9511-0294af318d78.png) |
    |:---:|
    |*Figure 31: UF2 query with prefixes*|
4.  Query results
    | ![Fig 33_UF2_Query_results](https://user-images.githubusercontent.com/59953831/128849873-f5f2ca2e-39c0-4407-9322-74f315a6db8f.png) | ![Fig 32_UF3_Query_results](https://user-images.githubusercontent.com/59953831/128849897-c8a14e3a-8f34-46cf-9fee-c9b3f467445b.png) |
    |:---:|:---:|
    |*Figure 32: UF2 query results*|*Figure 33: UF3 query results*|
  
### Step-by-step example for platform owner

<p>The core ontology is open source and can be used by other platforms similar to WIF for carrying out skill based matchmaking. There are three different ways platforms can use and integrate the demonstrator, they are:</p>

  - **Direct use** – To reuse the ontology directly <br>
  - **Customized use** - To customize and use the ontology based on the platforms need <br>

<p>To connect the ontology to the platform data the next step is to carry out instantiation, followed by developing suitable queries to retrieve matchmaking information from the ontology. Each of these steps are explained in the following sub-sections.</p>

#### Reference the ontologies or use for own purpose

-	**Direct use** <br>
<p>To use the ontology for own data connection, e. g. for any other platform owner, it is possible just to refer to its location on the repository as namespace 
  https://github.com/OPEN-NEXT/WP3_Skillmatching/raw/main/Skillmatching/data/on_Instances.owl
and use the vocabulary for instantiation. The ontology is public and directly accessible from the repository.</p>

-	**Customized use** <br>
<p>If it is desired to adapt or extend the ontology for individual use, e. g. if the data structure requires changes, the ontology can be downloaded from the repository and edited. For the ontology to be accessible, it is suggested to change the ontology namespaces in the ontology file (on_OSHPDP_schema.owl and on_skills.owl) from the repository namespace to the new ontology location (cf. Figure 39). This should also be considered for the import statement if it involves the respective ontologies (see bottom of Figure 39). Depending on which ontology is downloaded relating prefixes need to be changed as well (e. g. if the skills ontology is downloaded and adapted its prefix has to be changed in the OSHPDP ontology.</p>

  | ![Fig 39_Repository_namespaces_in_the_ontology_code](https://user-images.githubusercontent.com/59953831/128852101-1be0514f-6ff8-4d67-ade9-007b6457d6ce.png) |
  |:---:|
  |*Figure 39: Repository namespaces in the ontology code*|

<p>So, for customized use, the following steps have to be considered/executed:<br>
1.	Downloading the ontology to new folder structure (local or server) <br>
2.	Changing the namespace, prefixes and import statement in the ontology file accordingly to fit the new file's location(s).</p>

#### Custom instantiation

The mapping process is quite trivial. So, if there is very complicated data, that has to be mapped with rules and exceptions, an expansion based on the current mapping approach or another mapping process is recommended. <br>
1.	Cloning or downloading the repository <br>
2.	Opening the mapping ontology file *on_OSHPDP.owl* in the data folder of the repository (e. g. with a text editor).<br>
3.	Adding custom data mapping:<br>
To instantiate own JSON data, e. g. in case for a platform owner, that wants to connect his data, a change of the respective annotation is necessary. The figures below show a class-mapping declaration (Figure 39) and definition (Figure 40) for the class Project in the ontology.<br> <br>

  | ![Fig 40_Declaration_of_annotation_property_in_an_owl_file](https://user-images.githubusercontent.com/59953831/128853144-13428740-00fb-4d67-8568-970a07224830.png) | ![Fig 41_Mapping_annotation_for_Class_project_with_pointer_string_to_json_input_file](https://user-images.githubusercontent.com/59953831/128853193-16702354-288c-40b1-94b1-659841c3e078.png) |
  |:---:|:---:|
  |*Figure 39: Declaration of annotation property in an owl file*|*Figure 40: Mapping annotation for class "Project" with pointer string in JSON input file*|

For the given example, the mapping is called *"wif_project_2_cmap"*. The IRI section specifies which concept of the ontology is annotated (here the class Project) and the literal section includes a string of the JSON pointer, i. e. values for instances of the class Project can be found in the field *“/data/projects/result/edges/~/node/id”* in the corresponding input file. The *“~”* marks an array in the JSON data. Such markers will be automatically resolved into all existing entries of the array in the JSON file. <br>

For every new annotation property, a declaration axiom (Figure 39) and a definition (Figure 40) has to be added to the ontology file. That applies to classes, object properties and data properties in the ontology. Here for every concept “touched” by the instantiation, there has to be a mapping to JSON data. That means, for example to map a data property, there has to be a mapping annotation property to the data property itself but there also has to be a mapping annotation property to the relating domain class of the data property. To stay in the example: to map a Projects name, there has to be a mapping annotation property to the data property *Project_name* and a mapping annotation property to the corresponding domain class *Project* as well. Same logic is applied to object properties, but here are three mapping annotation properties are necessary, each one to the domain and range classes and one to the object property with a pointer to the specific individual. <br>

If the input data has multiple possible pointers for a concept in the ontology, extra mapping annotation properties can be created. E. g. the shown annotation is the second class-mapping for the concept Project, because in the input data were additional project data that could be reached with other pointers. <br>

Now it is time to prepare the main method in the *CreateInstances.java* class in the code for instantiation: <br>

1.	If the skill ontology or the OSHPDP ontology were changed, the corresponding string variables *skillIRI* or *mappingIRI* needs to be changed as well.<br>
    | ![Fig 41_skillIRI and mappingIRI variables in CreateInstances java](https://user-images.githubusercontent.com/59953831/128857086-0c35e5fa-986a-4bd3-9e83-2bf7dcda7b62.png) |
    |:---:|
    | *Figure 41: skillIRI and mappingIRI variables in CreateInstances.java* |
  
2.	The iri of the instantiated ontology to be created has to be specified. If public access to the instances is desired, the later location should be taken as namespace (like it is done in Figure 42)<br>
    | ![Fig 42_instanceIRI_variable_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128857187-b1f222ca-faa2-4399-8878-7101fd013b61.png) |
    |:---:|
    |*Figure 42: instanceIRI variable in CreateInstances.java*|

3.	The directory variable needs to be changed according to where the cloned/downloaded project is located. Add the path right away until the data folder of the project. (So to say that just the files name and extension have to be added in later use) <br>
    | ![Fig 43_directory_variable_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128857273-3e238a7a-a6e9-451d-aafb-d37be3b200dc.png) |
    |:---:|
    |*Figure 43: directory variable in CreateInstances.java*|
  
4.	For each JSON input file, a *JSONReader* object has to be instantiated and the location of the files needs to be set. At best they were already copied into the projects folder structure. <br>
    | ![Fig 44_Setting_up_JSONReader_objects_for_the_Json_input_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128857390-b4a85c49-1ba6-47ee-af5c-1754a3eeb606.png)|
    |:---:|
    |*Figure 44: Setting up JSONReader objects for the JSON input in CreateInstances.java*|

5.	**This step has to be done for every input source that should be instantiated:** The mappings that should be instantiated need to be set. The general case should be, that per mapping annotation there has to be instantiated a class mapping, object property mapping and data property mapping. Not all mappings from the ontology have to be instantiated if not necessary. The figure below shows the instantiation of each five class-, object property- and data property mappings that use the source *sampledata_issues_anonym.json* from the *JSONReader readIssues* (Figure 44).<br>
    | ![Fig 45_Instantiation_of_mapping_annotations_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128857494-46d78f71-f30b-4032-926e-1fb2d105dc33.png) |
    |:---:|
    |*Figure 45: Instantiation of mapping annotations in CreateInstances.java*|
  
In the given code of the demonstrator were three JSON input files. To instantiate all information of those, several mappings each were necessary, due to the repeated occurrence of the same classes in the same file. This is represented by the loop in Figure 45.<br>

6.	For each mapping annotation to be instantiated an *ArrayList<ArrayList<String>>* needs to be added in the code (Figure 46). Those have then to be filled with the corresponding annotations using the *get..Annotations()* methods of the *OntoModeler mapping* (cf. Figure 45).<br>
    | ![Fig 46_Lists_to_save_the_annotation_properties_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128857615-f86c1b36-f097-4aa6-b854-da856a0f0c21.png) |
    |:---:|
    |*Figure 46: Lists to save the annotation properties in CreateInstances.java*|
  
7.	The NT-file output location and name needs to be set. The instances are firstly stored in NT-format and afterwards converted to RDF language.<br>
    | ![Fig 47_Set_NT_output_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128858138-42e19d6f-4d8f-4f69-91ec-8f51f55a7ac0.png) |
    |:---:|
    |*Figure 47: Set NT output in CreateInstance.java*|
  
8.	At the end the ontology location for saving in *CreateInstances.java* has to be set.<br>
    | ![Fig 48_Setting_ontology_saving_location_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128858601-86bb6a5b-9171-4bdb-adb9-dafadff22ece.png) |
    |:---:|
    |*Figure 48: Setting ontology saving location in CreateInstances.java*|
  
9.	The last step is to run the *CreateInstances.java* class<br>
The reasoner to assert the inferences needs some time depending on the amount of data that should be instantiated. The instantiation process has ended, when the ontology saving statement (Figure 50) appears on the console.<br>
    | ![Fig 49_Running_the_CreateInstances java_class](https://user-images.githubusercontent.com/59953831/128858386-d4f6ab23-2abb-4164-bf0c-13ec7d16c738.png) |
    |:---:|
    |*Figure 49: Running the CreateInstances.java class*|

    | ![Fig 50_Saving_statement_for_the_ontology_on_the_console](https://user-images.githubusercontent.com/59953831/128858353-651e8cbf-fa2a-4e43-9bad-359be50930ec.png) |
    |:---:|
    |*Figure 50: Saving statement for the ontology on the console*|

#### Custom querying
  
The query process for a platform owner works the same way as for contributors. The queries just vary based on intended results. An example for a platform owner is given below. The query answers the question, what projects can be suggested for users to participate and vice versa.<br>

|SPARQL Query|
|----------------|
|*SELECT ?User ?Skill_Entity ?Project <br> WHERE {?Skill_Entity a skills:Skill_Entity; oshpd:interest_of ?User; oshpd:tags ?Project.<br> ?Project a oshpd:Project.}*|

| ![Fig 51_Exemplary_query_results](https://user-images.githubusercontent.com/59953831/128859421-3669e3dd-473e-4db3-9177-2034c57feb42.png) |
|:---:|
|*Figure 51: Exemplary query results*|
  
## DESIGN NOTES

The following diagrams visually facilitate the function of the main processes instantiation and querying. The instantiation process works differently for the skill instantiation and the project data instantiation. Both are shown below, for skill instantiation in Figure 9 and for the instantiation of the project data in Figure 10. The flow charts are provided in a sequential structure, indicated by the process arrows. At the same time the different classes used are displayed in a swim lane fashion, indicated by lines without arrows. Before starting the instantiation process, it is possible to change needed variables, shown in the manual input section of the flow charts. For the user flows of the project, all variables are set and the instantiation methods were executed resulting in a fully instantiated ontology, which is ready to be queried.<br>
  
The sequence for the instantiation process of the ontology in Figure 10 is shortened to a level of general understanding. To get a more elaborate insight of the explicit code function, the repository also provides a [complete flowchart](https://github.com/OPEN-NEXT/WP3_Skillmatching/blob/main/files/Flowchart_create_instances_complete.png) of all functions used, necessary to understand it. However, a detailed presentation of self-explanatory methods has been omitted (e.g. setter methods). Additionally, the methods are mostly described in the commented code as well.<br>
|![Flowchart_Skill_instantiation](https://user-images.githubusercontent.com/59953831/128865178-fbd9a52b-6e62-404d-8454-caafcd99ca5a.png)|
|:---:|
|*Figure 9: Skill instantiation flow*|

The skill instantiation is additionally presented shortly in writing. The CreateSkill.java class holds the main method and is responsible for the process flow.  <br>
At the beginning an instance of the SkillReader.java class is created and the location for the JSON input file is given. This input file is read by a reader that now holds all information needed. Now the different pointers are set: <br>
-	The pointer variable indicates which section of the input file is necessary for the instantiation <br>
-	The skill target variable indicates which values are instantiated as individuals (that counts e. g. for 3d-printing) <br>
-	The skill entity type variable shows how to classify a relating skill target variable (e. g. 3d-printing is an individual of the skill entity type class Process) <br>

After setting all variables, the instantiation process begins (instantiateTargets()): <br>
-	A pointer is created from the pointer string variable 
-	If the pointer exists, the void skill ontology is loaded to be instantiated. 
- The data array from the pointer variable is read 
-	For each entry in the array a skill target and skill entity type are read and instantiated. A skill target variable is instantiated as individual of the class indicated by the relating skill entity type. 
-	After instantiation of all skill targets, the instantiated ontology is saved. 
  
| ![Flowchart_create_instances_short](https://user-images.githubusercontent.com/59953831/128865985-b976712e-e765-40ea-9f78-34e004f972f7.png) |
|:---:|
|*Figure 10: Flowchart Instantiation*|  
