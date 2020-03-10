'''
Created on Mar 7, 2020

@author: kevin
'''
from rdflib import *
from rdflib.namespace import RDF, FOAF
from rdflib.plugins.sparql.processor import prepareQuery


def num_triples(graph):
    num = 0
    qres = graph.query(
         """SELECT DISTINCT ?s ?p ?o
            WHERE {
              ?s ?p ?o .
            }""")
    for row in qres:
        num += 1
    return num

#print("number of triples are:",num_triples(g))

def num_students(graph):
    num = 0
    qres = graph.query(
        """PREFIX ex: <http://example.org/>
           SELECT DISTINCT ?student
           WHERE {
              ?student rdf:type ex:Student .
           }""")
    for row in qres:
        num += 1
    return num
#print("number of student is:", num_students(g))

def num_courses(graph):
    num = 0
    qres = graph.query(
        """PREFIX ex: <http://example.org/>
           SELECT DISTINCT ?course
           WHERE {
              ?course rdf:type ex:Course .
           }""")
    for row in qres:
        num += 1
    return num
#print("number of course is:", num_courses(g))

def num_topics(graph):
    num = 0
    qres = graph.query(
        """PREFIX ex: <http://example.org/>
           SELECT DISTINCT ?topic
           WHERE {
              ?topic rdf:type ex:Topic .
           }""")
    for row in qres:
        num += 1
    return num
#print("number of topics is:", num_topics(g))

def course_topics(course,graph):
    q = prepareQuery('''PREFIX ex: <http://example.org/>
                        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                        SELECT DISTINCT ?t ?topics
                        WHERE {
                            ?course ex:covers ?topics.
                            ?topics foaf:name ?t.
                        }''')   
    qres = graph.query(q, initBindings = {'course': course})
    for row in qres:
        print(row)

#print("the topic that this course cover is:")
#print(course_topics(ex.COMP248, g))    

def list_course(graph,student):
    q = prepareQuery('''PREFIX ex: <http://example.org/>
                        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                        SELECT DISTINCT ?course ?g
                        WHERE {
                            ?student ?foaf:name ?studentName .
                            ?student ?course ?g .
                        }''')
    qres = graph.query(q, initBindings = {'studentName': student})
    for row in qres:
        print (row)
        
#list_course(g, bob)

def list_student(graph,topic):
    q = prepareQuery('''PREFIX ex: <http://example.org/>
                        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                        SELECT DISTINCT ?student
                        WHERE {
                            ?course ex:Covers ?topic.
                            ?s ?course ?grade.
                            ?s foaf:name ?student
                            FILTER(?grade != 'F')
                        }''')
    qres = graph.query(q, initBindings = {'topic': topic})
    for row in qres:
        print (row)

#list_student(g,ex.Expert_system)

def list_topics(graph, student):
    q = prepareQuery('''PREFIX ex: <http://example.org/>
                        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                        SELECT DISTINCT ?t
                        WHERE {
                            ?student foaf:name ?studentName
                            ?student ex:COMPLETED ?course .
                            ?student ?course ?grade .
                            ?course ex:Covers ?t .
                            FILTER(?grade != 'F')
                        }''')
    qres = graph.query(q, initBindings = {'studentName': student})
    for row in qres:
        print (row)

if __name__ == '__main__':
    
    
    g = Graph()
    
    g.parse("turtleTriples.txt", format="ttl")
    ex = Namespace("http://example.org/")
    
    ##print(course_topics(ex.COMP6231,g))
    student = Literal('Zapp Brannigan')
    print(list_course(g, student))
 
    
    
    
    
    
    
    
    
    
    
    
    
