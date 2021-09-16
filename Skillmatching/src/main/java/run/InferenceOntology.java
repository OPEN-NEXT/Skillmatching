package run;

import java.io.IOException;

import org.semanticweb.owlapi.model.OWLOntologyCreationException;
import org.semanticweb.owlapi.model.OWLOntologyStorageException;

import process.OntoModeler;

public class InferenceOntology {

	//variable for instance ontology iri
	private static String instanceIRI="https://github.com/OPEN-NEXT/WP3_Skillmatching/raw/main/Skillmatching/data/on_Instances.owl";
	//directory where the project is stored
	private static String directory="C://Springboot-Repository//WP3_Skillmatching//Skillmatching//data//";
	
	public static void main (String[] args) throws IOException {
		
		
		//infer asserted axioms of the new ontology:
		OntoModeler instance= new OntoModeler();
		instance.setIRI(instanceIRI);
		try {
			instance.loadOnto();
			//instance.mergeOntology(skillIRI);
			//instance.mergeOntology(mapping.getIRIString());
			instance.assertInferences();
			try {
				instance.saveOntology(directory+"on_Instances.owl");
			} catch (OWLOntologyStorageException e) {
				e.printStackTrace();
			} catch (OWLOntologyCreationException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

		

	
	}
}
