package process;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

import org.apache.jena.ontology.OntModel;
import org.apache.jena.ontology.Ontology;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.util.FileManager;

/**This class loads an nt-format file and creates rdf/turtle triples from it.
 * It uses the JENA package for ontology handling*/
public class NTParser {
	
	private String file;
	private OntModel model= ModelFactory.createOntologyModel();
	private Ontology ontology;
	private InputStream is;
	private OutputStream output;
	
	
	
	public NTParser(String file) {
		setFile(file);
	}
	
	public NTParser(InputStream streamy) {
		setIntputStream(streamy);
	}
		
	public void parseNT() {
	    if (is != null) {
	        //model.read(is, null, "N-TRIPLE");
	        model.write(output, "TURTLE");
	        
	    } else {
	        System.err.println("cannot parse " + file+". Please set file/inputstream and outputstream.");;
	    }
	}
	public void parseNT(String baseIRI) {
	    if (is != null) {
	        //model.read(is, null, "N-TRIPLE");
	        model.write(output, "TURTLE",baseIRI);
	        
	    } else {
	        System.err.println("cannot parse " + file+". Please set file/inputstream and outputstream.");;
	    }
	}
	public void parseNT(String baseIRI, String language) {
	    if (is != null) {
	        //model.read(is, null, "N-TRIPLE");
	        model.write(output, language,baseIRI);
	        
	    } else {
	        System.err.println("cannot parse " + file+". Please set file/inputstream and outputstream.");;
	    }
	}
	
	public void readNTModel() {
	    if (is != null) {
	        model.read(is, null, "N-TRIPLE");
	    } else {
	    	System.err.println("cannot read " + file+". Please set file/inputstream and outputstream.");;
	    }
	}
	
	public void setIntputStream(InputStream streamy) {
		is=streamy;
	}
	
	public void setFile(String a) {
		file=a;
		is=FileManager.get().open(file);
		//readNTModel();
	}
	
	public void setPrefix(String prefix, String uri) {
		model.setNsPrefix(prefix, uri+"#");
	}
	
	public void setOutput(String outputsource) {
		try {
			output=new FileOutputStream(outputsource);
		} catch (FileNotFoundException e) {
			System.out.println("Could not create FileOutputStream for "+outputsource);
			e.printStackTrace();
		}
		
	}
	public void setOntologyIRI(String bas) {
		ontology=model.createOntology(bas);
		
	}
	
	public void addImport(String ontologyIRI) {
//		model.setDynamicImports(true);
//        model.addLoadedImport(ontologyIRI);
		ontology.addImport(model.createResource(ontologyIRI));
	       
       
	}

	
}
