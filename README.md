[![DOI](https://zenodo.org/badge/391876438.svg)](https://zenodo.org/badge/latestdoi/391876438)
[![GitHub license](https://img.shields.io/github/license/OPEN-NEXT/WP3_Skillmatching.svg?style=flat)](./LICENSE)

# Semantic skill matching in Open Source Hardware (OSH) Project Communities

- This repository handles the third workpackage (WP3) of the [OPEN!NEXT project](https://opennext.eu/) to serve possible solutions for Open Source Hardware Commmunity needs.
- OPEN!NEXT received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement no. 869984.
- Skillmatching as a measure of community management was identified, which is the main focus here.\
  For this, a generic ontology model of a possible open souce hardware project landscape was developed.\
  The implementation of the ontology took results from a previous project (OPEN!) into account that also analysed processes and dynamics of OSH community.
- Purpose of the ontology model is to fulfill the concepted user stories defined below.

## TABLE OF CONTENTS
#### [User flows](#UF)
#### [Current status](#CS)
#### [Semantic network](#SN)
#### [Prerequisites](#PQ)
#### [Installation](#IN)
#### [Instructions to use](#IU)
#### [Design notes](#DN)
#### [References](#RF)

## <a name="UF"/>USER FLOWS

To gather the needs of the OSH community, expert interviews have been conducted. The team derived user stories from the input of those interviews.\
User Stories of the D3.1 deliverable of the project can be accessed [here](https://github.com/OPEN-NEXT/wp3_pub)

Three main user stories are scope of the case:

 1.	As a contributor on an OSH online platform, I want to add my skills and interests to my profile, so that others know more about my abilities.
 2. As a contributor on an OSH online platform, I want to find projects that require my specific skills in tasks, so that I can use, improve or evolve my skills.
 3. As a project core team, we want to find contributors based on their skills and interests so that they can help in carrying out a specific task.

## <a name="CS"/>CURRENT STATUS
The current development aim was to create a network that is able to give possibilities on assigning skills and interests to contributor profiles, tasks and projects and make them visible for queries. This was built based on the User flows described bevorhand. <br>

- The currently first draft of the ontology model is validated with a sample of project data from Wikifactory. For the validation, user flows were identified and, based on this, queries developed to check for existing results. 
- The ontology model has still to be validated by user interaction.
- Afterwards possible adaptions will taken into account.
- The repository will be updated respectively over time.

Building on this development, the next steps aim is to identify regularities for skill matching in order to integrate them into the semantic network and enable case-related automatic assignment.

## <a name="SN"/>SEMANTIC NETWORK
Based on the user flows a semantic network was developed. The net structure of the main classes of the semantic network for the application case are shown in Figure 1.
| ![ontology_use_case_import](https://user-images.githubusercontent.com/59953831/128870214-5ceb8362-77d5-4299-9ca8-9be6e09207a8.png) |
|:---:|
| *Figure 1: Ontology classes for the user flow application* |

For customization reasons, the semantic consists of two ontologies referring to each other but are therefore replacable, if necessary. A third lightweight ontology imports the other two ontologies to use the vocabulary for instantiation, hence also can be adapted easily.

1. OSH project ontology [(on_OSHPDP.owl)](https://github.com/OPEN-NEXT/WP3_Skillmatching/tree/main/Skillmatching/data/on_OSHPD.owl)
   - This OWL ontology holds the architecture and semantic restrictions of the project landscape
   - Main classes for the skillmatching case are "Person", "Project", "Task" and "Skill_Entity", that are related through properties.
   - Property restrictions arise from the use cases before mentioned
   - The OSHPD ontology imports the skill ontology

2. Skill ontology [(on_skills.owl)](https://github.com/OPEN-NEXT/WP3_Skillmatching/tree/main/Skillmatching/data/on_skills.owl)
   - This OWL ontology is based on the [ESCO skill hierarchy](https://ec.europa.eu/esco/portal/skill)
   - The ESCO hierarchy was cropped to the topics of mechanics, electrics/electronics, furniture and cars/mobiliy.
   - Afterwards a reclustering was done for ease of use purposes
   - The skill ontology is still to be validated with OSH project data

3. Instantiation file [(on_Instances.owl)](https://github.com/OPEN-NEXT/WP3_Skillmatching/tree/main/Skillmatching/data/on_Instances.owl)
   - This file holds needed project data of the individuals
   - The file refers to and uses class and property expressions from the other two ontologies.

## <a name="PQ"/>PREREQUISITES
The following pre-requisites are recommended for the following sections: <br>
- Basic knowledge about Ontology and semantics. An ontology is a concept used to model semantics (study of meaning, which enables developing parts of a language that can be understood and used commonly). A comprehensive overview can be found in [(Guarino et al. 2009)](#Gua). <br>
- Knowledge about the constitution of RDF and OWL graphs, and constants: RDF <sup>[1](https://www.w3.org/TR/rdf-schema/)</sup> and OWL <sup>[2](https://www.w3.org/TR/owl-features/),[3](https://www.w3.org/TR/owl2-overview/)</sup> are used to model semantics. Both use triple patterns to create graphs interrelating resources and setting them into an interconnected network. An introduction into the topic is for example explained by [(Pan et al. 2017)](#Pan). <br>
- SPARQL knowledge: SPARQL <sup>[4](https://www.w3.org/TR/2013/REC-sparql11-overview-20130321/),[5](https://www.w3.org/TR/sparql11-query/),[6](https://www.w3.org/TR/sparql-features/)</sup> is a query language for RDF data using graph patterns to restrict query response results. The referenced links provide a comprehensive overview about the functionality of SPARQL.<br>
- JSON and JSON pointer: [(Pezoa et al. 2016)](#Pez) provides understandable insights for a quick introduction to the topic: JSON is based on the Java Script programming language and is used for web applications in order to send and retrieve API requests and responses. JSON pointer are both, a query language and a concept used for information retrieval from JSON documents via defined formatted strings, relating to a unique value in the JSON document.<br>
- JAVA and JAVA APIs OWLAPI <sup>[7](https://github.com/owlcs/owlapi/)</sup> and JENA <sup>[8](https://jena.apache.org/)</sup> knowledge is helpful for developers who want to contribute to the demonstrator code. JENA API is an RDF open-source-framework for semantic networks. Most functionality is given for RDF graphs (like loading, serializing, saving, reasoning and querying) but functionality is also given to some extend on OWL based graphs. [(Antoniou und van Harmelen 2009)](#Ant) indicate which expressions overlap in RDF and OWL and which ones shift the scope of RDF. For OWL ontologies the OWLAPI provides complete functionality.<br>
- Since the repository is stored on GitHub, general knowledge about GitHub and Git is assumed, referring to the GitHub guides <sup>[9](https://guides.github.com/)</sup>. <br>

## <a name="IN"/>INSTALLATION

There is no specific installation needed. Depending on the use, the repository may have to be cloned. That is the case, when the mapping annotation properties in the ontology needs to be changed or if the query functionality provided in the demonstrator is used. For this general knowledge about Git is required. Furthermore, the structure of RDF and SPARQL should be known for the query use of the ontology. Interested developers, that need to change, adapt or improve the ontology, should be familiar with OWL and its extensions in contrast to RDF if aspiring reasoning or axiomizing. The following tables document the used software stack and the dependencies in software code. <br>

  
  |Software or Tool|Purpose|
  |-------------|---------------------| 
  |GitHub|Ontology hosting and demonstrator documentation|
  |[Protégé editor v5.5.0](https://protege.standford.edu)|Ontology modeling|
  |Eclipse IDE(v2020-03 R.0) with JRE1.8 |Coding and development of the demonstrator, including ontology files, JSON inputs and connection to GitHub repository|

  
  
  |Dependency package|Purpose|
  |------|------------| 
  |[ONTAPI v2.1.0](https://github.com/owlcs/ont-api)|JAVA package for ontology handling. It combines the JAVA ontology APIs OWL API and [JENA API](https://jena.apache.org). This was used for parsing and serializing NT data during the instantiation process and for the SPARQL query.|
  |[OWLAPI](https://github.com/owlcs/owlapi) v5.1.14|Java package for handling OWL ontologies. This was used to extract the mapping annotation properties and to create the skill instances in the on_skills.owl|
  |Hermit v1.3.8.510   |JAVA OWL Reasoner to assert inferences|
  |javax.json v1.1.2   | JAVA package for JSON processing, especially providing the use of JSON pointers|  
 

For changes in the mapping process, handling of the JAVA ontology APIs, OWL API and JENA API are used. They are JAVA implementations to build and handle semantic applications and provide functions to create, manipulate and serialize ontologies. To understand the functioning of the demonstrator, a short example is detailed below. It is oriented on the software stack shown in Table 4. Changing and further handling of the demonstrator is explained in the step-by-step examples section of the main document. For further developmental changes, refer to the flowcharts in the previous design notes section for an in-depth understanding.
The following steps can be followed to run the demonstrator:
1) Visit the GitHub repository: https://github.com/OPEN-NEXT/WP3_Skillmatching <br>
2) Copy the repository link

|![F14](https://user-images.githubusercontent.com/59953831/133502534-8d9f996a-5fab-43c6-b469-f980b9cbdff1.png)| 
|:--:| 
| *Figure 2: Coping the link of the GitHub repository page* |


3) If not already done, an SSH key should be created to connect to the repository. Please refer to the [Connecting to GitHub with SSH guide](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) <br>

4) Open the Eclipse IDE and choose a workspace

|![F15](https://user-images.githubusercontent.com/59953831/133502567-c8cd81a9-7cad-4a9b-88b6-a5502a366a2c.png)| 
|:--:| 
| *Figure 3: Starting Eclipse and choosing a workspace* |

5) Check if Eclipse uses the SSH key from GitHub

|![F16_ges](https://user-images.githubusercontent.com/59953831/133556999-1b63dbd4-62cc-4de9-b895-c38fc377a8d8.png)| 
|:--:| 
| *Figure 4: Setting the SSH2 key in the preferences* |

The SSH keys used in Eclipse can be found under Window>Preferences>General>Network Connection>SSH2.
If the key is not found there, it has to be added from the location it was saved during step 5) of this section. <br>

6) Open the git perspective
Following Windows>Perspective>Open Perspective>Other…

|![F17](https://user-images.githubusercontent.com/59953831/133502664-95471177-e1c6-46ff-be76-7ac0bb0e8c99.png)| 
|:--:| 
| *Figure 5: Open Git perspective in Eclipse (1/2)* |

Select Git.<br>

|![F18](https://user-images.githubusercontent.com/59953831/133502690-3aad1645-2dde-4ca5-95ad-f68faa25fe00.png)| 
|:--:| 
| *Figure 6: Open Git perspective in Eclipse (2/2)* |

7) Click on Clone a git repository in the Git Repositories tab.<br>

|![F19](https://user-images.githubusercontent.com/59953831/133502706-df8ffac3-d582-425f-90b6-52ce3f6dbdaa.png)| 
|:--:| 
| *Figure 7: Clone a Git repository from the Git repositories tab* |

Afterwards the dialogue box for cloning a repository then opens.<br>

8) Specify the repository to clone

After inserting the repository link into the URI field, the other fields should be filled automatically. If this does not happen, the fields have to be filled according to Figure 8.

|![F20](https://user-images.githubusercontent.com/59953831/133502732-da20fca1-c182-4b6b-9f5b-f74cee14569a.png)| 
|:--:| 
| *Figure 8: Inserting the repository URI to clone* |

Click Next <br>

9) Select the branch. The usual case is to clone the main branch.

|![F21](https://user-images.githubusercontent.com/59953831/133502746-beec9f3d-6a8b-4031-b56d-b2ee0e3b2d38.png)| 
|:--:| 
| *Figure 9: Selection the branch to clone* |

Click on Next. <br>

10) Choose the local destination of the Git repository by filling the Directory field.

|![F22](https://user-images.githubusercontent.com/59953831/133502756-4f4b9f8a-23c8-4098-95db-6658faeb0e97.png)| 
|:--:| 
| *Figure 10: Choosing a local directory for the git repository* |

Click on Finish. The repository WP3_Skillmatching should now be displayed in the Git Repositories tab (cf. Figure 7).
Now a Maven project needs to be imported that integrates the Git. <br>

11) Import a Maven project
Following File>Import>Existing Maven Projects

|![F23_ges](https://user-images.githubusercontent.com/59953831/133557136-b9c72ebb-5e0a-4b61-81d9-43beceae8908.png)| 
|:--:| 
| *Figure 11: Importing existing Maven project* |

Choose the root directory with WP3_Skillmatching. For this manual another project WP3_Skillmatching_manual was created to be imported which is why it is displayed in the figures. For the use of the skill matching demonstrator the WP3_Skillmatching but has to be used.

|![F24](https://user-images.githubusercontent.com/59953831/133502820-bb5ddf54-b004-4e8a-8eaf-064eec4095c0.png)| 
|:--:| 
| *Figure 12: Choosing root directory* |

Click on Finish.
The Maven project will appear in the Project Explorer tab.

|![F25](https://user-images.githubusercontent.com/59953831/133502835-c415a2c3-00a8-4af0-82b8-b10e2d81f8ad.png)| 
|:--:| 
| *Figure 13: Imported project in the project explorer tab* |

If there are some errors right away, most likely the JAVA compiler version has to be set to 1.8. <br>

12) Set JAVA Compiler Version
This can be done in the properties of the project. (Right click on the project)

|![F26_ges](https://user-images.githubusercontent.com/59953831/133557064-c0b34b33-1141-4c82-b3f0-e4eb000561ec.png)| 
|:--:| 
| *Figure 14: Setting JAVA Compiler level* |

In the Java Compiler tab the Use compliance from execution environment ‘J2SE-X.X’ on the Java Build Path needs to be unchecked and the Compiler compliance level has to be set to 1.8.<br>
Click Apply and Close.

|![F27](https://user-images.githubusercontent.com/59953831/133502878-a620ac3f-ed22-4c43-8b8b-dd1ffcdd247a.png)| 
|:--:| 
| *Figure 15: Agreeing to the project build* |

The rebuild of the project has to be accepted by clicking on *Yes*.
If an error on the JUnit import statement occurs in the *OntoModeler.java* class, the library has to be added to the project.

|![F28](https://user-images.githubusercontent.com/59953831/133502935-a2830b0d-75b4-4d26-ab49-139b8ee9c33c.png)| 
|:--:| 
| *Figure 16: JUnit import error* |

The library can be added in the Java Build Path by right clicking the project and following *Properties>Java Build Path>Libraries>Add Library >Junit >Junit5*.

|![F29_ges](https://user-images.githubusercontent.com/59953831/133557100-b7426697-d557-4e5e-b928-d736e18fd58d.png)| 
|:--:| 
| *Figure 17: Adding JUnit library* |

Click Next. Choose Junit5. Click Apply and Close. <br>
Now the demonstrator is ready to use.

## <a name="IU"/>INSTRUCTIONS TO USE

**In this section classes from the code are mentioned and code lines are reffered to. To better understand the usage section it is advised here, to study the class diagram and the descriptions of the classes functions from the DESIGN NOTE section of the repository.** <br><br>
The demonstrator has two the main functions instantiation and querying. Each of their usages are described below:<br>

  **i.	Instantiation** <br><p>
An ontology was created for the development goal of skill matching. To make it widely applicable, it was created without any instances. Project data from WIF was integrated via data mapping afterwards. This offers the advantage of simpler validation in case the data structure changes. If so, a new instantiation can simply be achieved by changing the mappings. The mapping approach is based on the idea of [Méndez et al.](http://ceur-ws.org/Vol-2721/paper593.pdf) and connects the ontology concepts with JSON formatted input data via annotation properties. That means, that the mapping information is directly stored in the ontology itself. The mapping process is visualized in Figure 18. Classes and properties in the semantic network are annotated with JSON pointers to the relating fields in the GraphQL API from WIF whose data was used for validation. For every mapping a new annotation property is created. This gives the possibility to use more than one data source from either the same or a different platform. During later instantiation it is possible to choose in the demonstrator code how the mapping should be used.
For the user flow three different JSON data source files were created from query results of the WIF GraphQL API. This was done, so the first validation was not compromised by changes in the data structure during its constant progression and also because the user data had to be anonymized before used for instantiation.
During the mapping process, the annotation with the JSON pointer is read out of the ontology and used to query the information in the JSON file that contains the input data. Afterwards those query results are instantiated based on which concept (class or property) was annotated in the first place. The instantiated individuals are saved in a separate file that uses the ontology vocabulary. 

|![mapping_process_short](https://user-images.githubusercontent.com/59953831/128838638-3b051997-62d2-42c8-946b-9b1cdbdbb381.png)| 
|:--:| 
| *Figure 18: Mapping process* |
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
    | *Figure 19: Method to create a query string for user interest* |
3.  If the ontologies were to be changed, the prefixes in the string variable prefixes of class Queries.java need to be changed accordingly as well.<br>
    |![Fig 26_Query_prefixes](https://user-images.githubusercontent.com/59953831/128845285-61620459-b42a-4e24-be1b-fdff175943e8.png)|
    |:---:|
    | *Figure 20: Query prefixes* |
    
    Now the *RunQuery.java* class from the *run* package has to be specified.
4.  The IRI of the ontology to query has to be set in the *RunQuery.java* class (cf. *Figure 21*) 

5.  The language of the model to open has to be specified in the *openModel()* method in *RunQuery.java*.<br>
    |![Fig 27_Setup_for_query_execution_using_QueryExec java](https://user-images.githubusercontent.com/59953831/128845553-02de9fb2-1db0-4203-946d-5778fa5fc4ce.png)|
    |:---:|
    | *Figure 21: Setup for query execution using QueryExec.java class* |
6.  The query execution method of class *QueryExec.java* needs a SPARQL query as string parameter. For this, the query string generation methods of class *Queries.java* can be used. <br>
    |![Fig 28_Execution_of_query_using_the_query_generation_method](https://user-images.githubusercontent.com/59953831/128846095-36993b59-c5e0-4efd-a47e-ed07e2be0935.png)|
    |:---:|
    | *Figure 22: Execution of query using the query generation method* |
7.  he generated result list can now further be processed, e.g. for frontend display.
<br>

#### Using an editor with SPARQL functionality
  
<p>To show the general function, an example of the use is given with the ontology editor Protégé which also provides a SPARQL plugin for query. </p>

1.	Loading the ontology from its location. Here the repository location was used.<br>
    | ![Fig 29_Load_ontology_from_URI_via_protege](https://user-images.githubusercontent.com/59953831/128848793-e20b45f4-379f-4049-be1d-48d5a56bbcb5.png)|
    |:---:|
    |*Figure 23: Load ontology from URI via Protégé editor*|
2.  The editors SPARQL- /Query- interface needs to be opened.<br>
    | ![Fig 30_SPARQL_plugin_tab_in_protege](https://user-images.githubusercontent.com/59953831/128849792-75983c9a-e360-4a36-9c06-f628a722620d.png) |
    |:---:|
    |*Figure 24: SPARQL-plugin tab in Protégé editor*|
3.  Adding prefixes and query string to the interface and execution of query. Figure 25 exemplary shows the UF2 query.<br>
    | ![Fig 31_UF2_Query with prefixes](https://user-images.githubusercontent.com/59953831/128849821-18381df7-b819-43c0-9511-0294af318d78.png) |
    |:---:|
    |*Figure 25: UF2 query with prefixes*|
4.  Query results
    | ![Fig 33_UF2_Query_results](https://user-images.githubusercontent.com/59953831/128849873-f5f2ca2e-39c0-4407-9322-74f315a6db8f.png) | ![Fig 32_UF3_Query_results](https://user-images.githubusercontent.com/59953831/128849897-c8a14e3a-8f34-46cf-9fee-c9b3f467445b.png) |
    |:---:|:---:|
    |*Figure 26: UF2 query results*|*Figure 27: UF3 query results*|
  
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
<p>If it is desired to adapt or extend the ontology for individual use, e. g. if the data structure requires changes, the ontology can be downloaded from the repository and edited. For the ontology to be accessible, it is suggested to change the ontology namespaces in the ontology file (on_OSHPDP_schema.owl and on_skills.owl) from the repository namespace to the new ontology location (cf. Figure 28). This should also be considered for the import statement if it involves the respective ontologies (see bottom of Figure 28). Depending on which ontology is downloaded relating prefixes need to be changed as well (e. g. if the skills ontology is downloaded and adapted its prefix has to be changed in the OSHPDP ontology.</p>

  | ![Fig 39_Repository_namespaces_in_the_ontology_code](https://user-images.githubusercontent.com/59953831/128852101-1be0514f-6ff8-4d67-ade9-007b6457d6ce.png) |
  |:---:|
  |*Figure 28: Repository namespaces in the ontology code*|

<p>So, for customized use, the following steps have to be considered/executed:<br>
1.	Downloading the ontology to new folder structure (local or server) <br>
2.	Changing the namespace, prefixes and import statement in the ontology file accordingly to fit the new file's location(s).</p>

#### Custom instantiation

The mapping process is quite trivial. So, if there is very complicated data, that has to be mapped with rules and exceptions, an expansion based on the current mapping approach or another mapping process is recommended. <br>
1.	Cloning or downloading the repository <br>
2.	Opening the mapping ontology file *on_OSHPDP.owl* in the data folder of the repository (e. g. with a text editor).<br>
3.	Adding custom data mapping:<br>
To instantiate own JSON data, e. g. in case for a platform owner, that wants to connect his data, a change of the respective annotation is necessary. The figures below show a class-mapping declaration (Figure 29) and definition (Figure 30) for the class Project in the ontology.<br> <br>

  | ![Fig 40_Declaration_of_annotation_property_in_an_owl_file](https://user-images.githubusercontent.com/59953831/128853144-13428740-00fb-4d67-8568-970a07224830.png) | ![Fig 41_Mapping_annotation_for_Class_project_with_pointer_string_to_json_input_file](https://user-images.githubusercontent.com/59953831/128853193-16702354-288c-40b1-94b1-659841c3e078.png) |
  |:---:|:---:|
  |*Figure 29: Declaration of annotation property in an owl file*|*Figure 30: Mapping annotation for class "Project" with pointer string in JSON input file*|

For the given example, the mapping is called *"wif_project_2_cmap"*. The IRI section specifies which concept of the ontology is annotated (here the class Project) and the literal section includes a string of the JSON pointer, i. e. values for instances of the class Project can be found in the field *“/data/projects/result/edges/~/node/id”* in the corresponding input file. The *“~”* marks an array in the JSON data. Such markers will be automatically resolved into all existing entries of the array in the JSON file. <br>

For every new annotation property, a declaration axiom (Figure 29) and a definition (Figure 30) has to be added to the ontology file. That applies to classes, object properties and data properties in the ontology. Here for every concept “touched” by the instantiation, there has to be a mapping to JSON data. That means, for example to map a data property, there has to be a mapping annotation property to the data property itself but there also has to be a mapping annotation property to the relating domain class of the data property. To stay in the example: to map a Projects name, there has to be a mapping annotation property to the data property *Project_name* and a mapping annotation property to the corresponding domain class *Project* as well. Same logic is applied to object properties, but here are three mapping annotation properties are necessary, each one to the domain and range classes and one to the object property with a pointer to the specific individual. <br>

If the input data has multiple possible pointers for a concept in the ontology, extra mapping annotation properties can be created. E.g. the shown annotation is the second class-mapping for the concept Project, because in the input data were additional project data that could be reached with other pointers. <br>

Now it is time to prepare the main method in the *CreateInstances.java* class in the code for instantiation: <br>

1.	If the skill ontology or the OSHPDP ontology were changed, the corresponding string variables *skillIRI* or *mappingIRI* needs to be changed as well.<br>
    | ![Fig 41_skillIRI and mappingIRI variables in CreateInstances java](https://user-images.githubusercontent.com/59953831/128857086-0c35e5fa-986a-4bd3-9e83-2bf7dcda7b62.png) |
    |:---:|
    | *Figure 31: skillIRI and mappingIRI variables in CreateInstances.java* |
  
2.	The iri of the instantiated ontology to be created has to be specified. If public access to the instances is desired, the later location should be taken as namespace (like it is done in Figure 32)<br>
    | ![Fig 42_instanceIRI_variable_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128857187-b1f222ca-faa2-4399-8878-7101fd013b61.png) |
    |:---:|
    |*Figure 32: instanceIRI variable in CreateInstances.java*|

3.	The directory variable needs to be changed according to where the cloned/downloaded project is located. Add the path right away until the data folder of the project. (So to say that just the files name and extension have to be added in later use) <br>
    | ![Fig 43_directory_variable_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128857273-3e238a7a-a6e9-451d-aafb-d37be3b200dc.png) |
    |:---:|
    |*Figure 33: directory variable in CreateInstances.java*|
  
4.	For each JSON input file, a *JSONReader* object has to be instantiated and the location of the files needs to be set. At best they were already copied into the projects folder structure. <br>
    | ![Fig 44_Setting_up_JSONReader_objects_for_the_Json_input_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128857390-b4a85c49-1ba6-47ee-af5c-1754a3eeb606.png)|
    |:---:|
    |*Figure 34: Setting up JSONReader objects for the JSON input in CreateInstances.java*|

5.	**This step has to be done for every input source that should be instantiated:** The mappings that should be instantiated need to be set. The general case should be, that per mapping annotation there has to be instantiated a class mapping, object property mapping and data property mapping. Not all mappings from the ontology have to be instantiated if not necessary. The figure below shows the instantiation of each five class-, object property- and data property mappings that use the source *sampledata_issues_anonym.json* from the *JSONReader readIssues* (cf. Figure 34).<br>
    | ![Fig 45_Instantiation_of_mapping_annotations_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128857494-46d78f71-f30b-4032-926e-1fb2d105dc33.png) |
    |:---:|
    |*Figure 35: Instantiation of mapping annotations in CreateInstances.java*|
  
In the given code of the demonstrator were three JSON input files. To instantiate all information of those, several mappings each were necessary, due to the repeated occurrence of the same classes in the same file. This is represented by the loop in Figure 35.<br>

6.	For each mapping annotation to be instantiated an *ArrayList<ArrayList<String>>* needs to be added in the code (Figure 36). Those have then to be filled with the corresponding annotations using the *get..Annotations()* methods of the *OntoModeler mapping* (cf. Figure 35).<br>
    | ![Fig 46_Lists_to_save_the_annotation_properties_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128857615-f86c1b36-f097-4aa6-b854-da856a0f0c21.png) |
    |:---:|
    |*Figure 36: Lists to save the annotation properties in CreateInstances.java*|
  
7.	The NT-file output location and name needs to be set. The instances are firstly stored in NT-format and afterwards converted to RDF language.<br>
    | ![Fig 47_Set_NT_output_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128858138-42e19d6f-4d8f-4f69-91ec-8f51f55a7ac0.png) |
    |:---:|
    |*Figure 37: Set NT output in CreateInstance.java*|
  
8.	At the end the ontology location for saving in *CreateInstances.java* has to be set.<br>
    | ![Fig 48_Setting_ontology_saving_location_in_CreateInstances java](https://user-images.githubusercontent.com/59953831/128858601-86bb6a5b-9171-4bdb-adb9-dafadff22ece.png) |
    |:---:|
    |*Figure 38: Setting ontology saving location in CreateInstances.java*|
  
9.	The last step is to run the *CreateInstances.java* class<br>
The reasoner to assert the inferences needs some time depending on the amount of data that should be instantiated. The instantiation process has ended, when the ontology saving statement (Figure 40) appears on the console.<br>
    | ![Fig 49_Running_the_CreateInstances java_class](https://user-images.githubusercontent.com/59953831/128858386-d4f6ab23-2abb-4164-bf0c-13ec7d16c738.png) |
    |:---:|
    |*Figure 39: Running the CreateInstances.java class*|

    | ![Fig 50_Saving_statement_for_the_ontology_on_the_console](https://user-images.githubusercontent.com/59953831/128858353-651e8cbf-fa2a-4e43-9bad-359be50930ec.png) |
    |:---:|
    |*Figure 40: Saving statement for the ontology on the console*|

#### Custom querying
  
The query process for a platform owner works the same way as for contributors. The queries just vary based on intended results. An example for a platform owner is given below. The query answers the question, what projects can be suggested for users to participate and vice versa.<br>

|SPARQL Query|
|----------------|
|*SELECT ?User ?Skill_Entity ?Project <br> WHERE {?Skill_Entity a skills:Skill_Entity; oshpd:interest_of ?User; oshpd:tags ?Project.<br> ?Project a oshpd:Project.}*|

| ![Fig 51_Exemplary_query_results](https://user-images.githubusercontent.com/59953831/128859421-3669e3dd-473e-4db3-9177-2034c57feb42.png) |
|:---:|
|*Figure 41: Exemplary query results*|
  
## <a name="DN"/>DESIGN NOTES
  
  The following section gives insights how the code is constituted and how the methods are handled to instantiate and query the ontology.

### Class diagram
  
| ![Code structure_v2](https://user-images.githubusercontent.com/59953831/133493500-268b36f4-02dd-4d7a-8a6d-218a91105eab.png)|
|:---:|
|*Figure 42: Class diagram*| 
  
*OntoModeler.java* <br>
The *OntoModeler.java* class is used to create, load and save, handle and serialize OWL ontologies and ontology files. The main functionality in the demonstrator is, besides loading and saving the ontologies, to read out the mappings of the OSH project ontology, get information about the relating concepts (e. g. get the domain class of an object property) and to instantiate information from the JSON input files (this happens mainly in case of skill data instantiation). Also it is used for reasoning during the instantiation of the project data and saving the instances ontology. <br>

*SkillReader.java* <br>
This class provides functionality to read skill information from the provided JSON input file (*skills_schema.json*). It uses a JSON-pointer to specify the location of desired data in the JSON file and creates a JSON array. Defined key attributes are used to read out values from this array. Afterwards, the predefined skill schema (*on_skills_void.owl*) is loaded with the help of the OntoModeler.java class and the resulting values are instantiated as OWL ontology (*on_skills.owl*) and saved. <br>

*CreateSkill.java* <br>
This class holds the *main()* method for the skill instantiation process and coordinates it by passing parameters and calling functions of the *SkillReader.java* and *OntoModeler.java* classes. The parameters required for skill instantiation are initiated here in the beginning. <br>

*JSONReader.java* <br>
The *JSONReader.java* class holds functionality to extract data from the JSON formatted inputs over JSON pointers. If pointers contain array markers, there is functionality to parse those arrays into its entries and coordinates the connection of value information to its respective entry in the array. <br>
  
*JSON2NTmapper.java* <br>
This class uses the results of JSON data extraction from the combination of *JSONReader.java* and *OntoModeler.java* methods and converts them into a NT-file. N-Triples  (NT) is a plain text format for RDF graphs and serves for the instantiation as intermediate format from JSON to OWL translation. <br>
  
*NTParser.java* <br>
This class loads an NT-file (in the instantiation case provided by methods from *JSON2NTmapper.java* class) and provides a methods to enrich the file, e.g. with a statement to import the vocabulary of another ontology or setting different prefixes to the ontology. Also there are functions to convert the NT-file to another RDF based format. <br>
  
*CreateInstances.java* <br>
This class contains the *main()* method for the instantiation of project data. It provides variables for prerequisite input files and their locations. Connecting the *OntoModeler.java*, *JSONReader.java*, *JSON2NTmapper.java* and *NTParser.java* classes, it coordinates the calling of methods and handover of parameters and results of methods during instantiation. <br>

*InferenceOntology.java* <br>
This class provides reasoning functionality, if it is necessary. It contains the *main()* method for reasoning and inferencing an instantiated ontology and provides a variable for the ontology IRI to load it and an output variable to save the ontology after reasoning. To load the ontology, assert inferences and save the ontology afterwards, the methods of the *OntoModeler.java* class are used. <br>
  
*Queries.java* <br>
This class provides methods to return SPARQL query strings based on the described user flows. <br>
  
*QueryExec.java* <br>
The *QueryExec.java* class connects to an ontology and executes queries on it. In case of the demonstrators, the instantiated project data (*on_Instances.owl*) is queried with the query strings provided by the *Queries.java* class. <br>
  
*RunQuery.java* <br>
This class holds the *main()* method for the querying process and uses SPARQL queries from the Queries.java class passing it to the *QueryExec.java* class.

  
### Flow charts

The following diagrams visually facilitate the function of the main processes instantiation and querying. The instantiation process works differently for the skill instantiation and the project data instantiation. Both are shown below, for skill instantiation in Figure 40 and for the instantiation of the project data in Figure 11. The flow charts are provided in a sequential structure, indicated by the process arrows. At the same time the different classes used are displayed in a swim lane fashion, indicated by lines without arrows. Before starting the instantiation process, it is possible to change needed variables, shown in the manual input section of the flow charts. For the user flows of the project, all variables are set and the instantiation methods were executed resulting in a fully instantiated ontology, which is ready to be queried.<br>
  
The sequence for the instantiation process of the ontology in Figure 44 is shortened to a level of general understanding. To get a more elaborate insight of the explicit code function, the repository also provides a [complete flowchart](https://github.com/OPEN-NEXT/WP3_Skillmatching/blob/main/files/Flowchart_create_instances_complete.png) of all functions used, necessary to understand it. However, a detailed presentation of self-explanatory methods has been omitted (e.g. setter methods). Additionally, the methods are mostly described in the commented code as well.<br>

  #### Skill instantiation flow

The skill instantiation is additionally presented shortly in writing. The *CreateSkill.java* class holds the main method and is responsible for the process flow.  <br>
At the beginning an instance of the *SkillReader.java* class is created and the location for the JSON input file is given. This input file is read by a reader that now holds all information needed. Now the different pointers are set: <br>
-	The pointer variable indicates which section of the input file is necessary for the instantiation <br>
-	The skill target variable indicates which values are instantiated as individuals (that counts e. g. for *3d-printing*) <br>
-	The skill entity type variable shows how to classify a relating skill target variable (e. g. *3d-printing* is an individual of the skill entity type class Process) <br>

After setting all variables, the instantiation process begins (instantiateTargets()): <br>
-	A pointer is created from the pointer string variable 
-	If the pointer exists, the void skill ontology is loaded to be instantiated. 
- The data array from the pointer variable is read 
-	For each entry in the array a skill target and skill entity type are read and instantiated. A skill target variable is instantiated as individual of the class indicated by the relating skill entity type. 
-	After instantiation of all skill targets, the instantiated ontology is saved and needs to be stored manually in the public project repository.  
  
|![Flowchart_Skill_instantiation](https://user-images.githubusercontent.com/59953831/133494912-177c60e8-4cfc-4f98-8ac2-4c9fa878a1cb.png)|
|:---:|
|*Figure 43: Skill instantiation flow*|


  #### Project data instantiation flow
  
The instantiation process will be shortly described divided into three main parts. 
  
1.	Getting the mapping annotation properties from the OSH project ontology <br>
  
This parts relates in the flow chart to the section between the steps *“Start CreateInstance.java”* and *“END OntoModeler.java”*. After setting the manual inputs, the instantiation process starts with the initialization of an *OntoModeler.java* object in the *CreateInstances.java* class. After that the following short steps take place: <br>
-	The IRI of the mapping ontology is set and the ontology file is loaded
-	The mapping ontology is merged with the ontology find behind the skill ontology IRI (here the skill ontology)
-	The mapping annotations are set, which should be searched in the following process. (*setClassmapping()*, *setOPmapping()* and *setDPmapping()*) <br>
  
After setting what mapping annotations should be searched, the mapping annotations of every class, object property and data property are read out of the ontology and the results are saved into lists. Each list contains of three arrays and is arranged as follows for each of the subsequent cases:
-	Class mapping annotations: The first array contains all mapping annotation pointers for the individuals to be instantiated. The second array simply contains an *“rdf:type”* statement and the third array holds the respective class IRI of the instances class.
-	Object property annotations: The first array contains the pointers of the domain class from the respective object properties, which´s IRIs are stored in the second array. The third array stores the object property annotation pointers of the range classes from the respective object properties.
-	Data property annotations: The first array contains the pointers for the individuals to be instantiated. The second array contains the data property IRIs and the third array contains the respective data property annotation pointers. 

2.	Creating an NT file from the mapping annotation pointers <br>
  
The explanations in this part refer to the steps from *“Start JSONReader.java” to “END JSON2NTMapper.java”*. After the initialization of a *JSONReader.java* object, the file location of the JSON inputs is set and the file is opened. A *JSON2NTmapper.java* object is created and the mapping ontology IRI, to load the existing OSH project ontology, and the instance IRI, in which the new instances are to be stored, are set. With the *JSONReader.java* object annotation pointers from the lists of class- , object property- and data property annotations created in the first step are replaced with their corresponding values. With the values and the IRIs from the ontologies, NT statements are created and saved as NT file.
  
3.	Converting the NT file into an RDF format <br>
  
This section concentrates on steps between *“Start NTParser.java”* and *“END NTParser.java”*. When created, the *NTParser.java* creates an ontology model that will be added with the further described information. Necessary prefixes are added to the ontology model with the *setPrefix()* method. The *readNTModel()* method reads the NT file with instances information from its location that was handed over to the constructor at creation. After setting the ontology IRI, adding necessary statements to import concepts and vocabulary from other ontologies and setting the output file location, the ontology model is saved in OWL format.<br>
Afterwards, the ontology file needs to be manually stored in the public project repository. 
  
|![Flowchart_create_instances_short_v2](https://user-images.githubusercontent.com/59953831/133495302-8dc3e824-7d11-4d5b-ac5d-47306b22253a.png)|
|:---:|
|*Figure 44: Instantiation flow*| 

#### Reasoning over the ontology and assert inferences   
  
The reasoning process is shown in Figure 45. After setting the manual inputs, an *OntoModeler.java* object is initialized that loads the instance ontology from its IRI. The *assertInferences()* method creates a reasoner, that precomputes inferences, creating new axioms for the ontology. A loop runs through the set of new axiom, adds it to the ontology and saves it. Afterwards the ontology with asserted inferences has to be manually stored to the public project repository.

|![Flowchart_reasoning](https://user-images.githubusercontent.com/59953831/133495708-44d08ec7-581c-42d8-9366-bc1e45152496.png)|
|:---:|
|*Figure 45: Reasoning process flow*| 

  #### Query execution flow
  
  The query execution flow is shown in Figure 46 and starts with the *RunQueries.java*. In this class the ontology IRI to be loaded and queried is provided as string variable. After initiation of a *Queries.java* and a *QueryExec.java* object, the ontology IRI is set for the query execution and the ontology model is loaded. The *Queries.java* class provides methods to return query strings for the execution on the ontology. In Figure 46 the example of the *UserSkillInterest()* query generation method is shown in the process. This can be replaced with other query generation methods from the *Queries.java* class. The generated query string is handed over to the query execution method of the *QueryExec.java* class. To execute the query a *Query* and a *QueryExecution* type variable are created and the result set from the query is generated. The result set is run through and the results for every variable is saved into a result list. The number of variables depends on the number of variables in SELECT clause of the query. At the end the result list is post-processed to match a table like layout.
  
| ![Flowchart_query](https://user-images.githubusercontent.com/59953831/130364272-3ccb3ce2-e212-4f3e-847f-9f10c86b1172.png) |
|:---:|
|*Figure 46: Flowchart Query execution*| 
  
  
  

## <a name="RF"/>REFERENCES

<a id="Ant">Antoniou, Grigoris; van Harmelen, Frank (2009): Web Ontology Language: OWL. In: Steffen Staab und Rudi Studer (Hg.): Handbook on Ontologies. Berlin, Heidelberg: Springer Berlin Heidelberg, S. 91–110.</a>

<a id="Gua">Guarino, Nicola; Oberle, Daniel; Staab, Steffen (2009): What Is an Ontology? In: Steffen Staab und Rudi Studer (Hg.): Handbook on Ontologies. Berlin, Heidelberg: Springer Berlin Heidelberg, S. 1–17.</a>

<a id="Pan">Pan, Jeff Z.; Vetere, Guido; Gomez-Perez, Jose Manuel; Wu, Honghan (2017): Exploiting Linked Data and Knowledge Graphs in Large Organisations. Cham: Springer International Publishing.</a>

<a id="Pez">Pezoa, Felipe; Reutter, Juan L.; Suarez, Fernando; Ugarte, Martín; Vrgoč, Domagoj (2016): Foundations of JSON Schema. In: Jacqueline Bourdeau, Jim A. Hendler, Roger Nkambou Nkambou, Ian Horrocks und Ben Y. Zhao (Hg.): Proceedings of the 25th International Conference on World Wide Web. WWW ‘16: 25th International World Wide Web Conference. Montréal Québec Canada, 11.04.2016-15.04.2016. Republic and Canton of Geneva, Switzerland: International World Wide Web Conferences Steering Committee, S. 263–273.</a>
