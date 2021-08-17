package run;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;

import query.Queries;
import query.QueryExec;

public class RunQuery {
	private static String ontology_iri="https://github.com/OPEN-NEXT/WP3_Skillmatching/raw/main/Skillmatching/data/on_Instances.owl";
	public static void main (String[] args) throws IOException {
		
		Queries q= new Queries();
		QueryExec searchforme= new QueryExec();
		searchforme.setIRI(ontology_iri);
		searchforme.openModel("OWL");
		
		LinkedList<ArrayList<String>> result=searchforme.execQuery(q.UserSkillInterest("uid113"));
		
		
		for (Iterator<ArrayList<String>> rs=result.iterator(); rs.hasNext();) {
			ArrayList<String> resultat = rs.next();
			resultat.forEach(System.out::println);
		}
		
		System.out.println(q.UserSkillInterest("uid113"));
			
		}
		
}
