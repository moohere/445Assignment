'''
Created on Mar 7, 2020

@author: kevin
'''
from rdflib import *
from rdflib.namespace import RDF, FOAF
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()
ex = Namespace("http://example.org/")
bob = Literal('bob')
linda = Literal('linda')
john = Literal('john')
COMP248 = Literal('COMP248')
COMP248_Name = Literal("Name of the Course_248")
COMP248_Description = Literal("Description of the course")
COMP249 = Literal('COMP249')
COMP249_Name = Literal("Name of the Course_249")
COMP249_Description = Literal("Description of the course_249")
Expert_system = Literal("Introduction to JAVA")
Expert_system_link = URIRef("http://dbpedia.org/page/Expert_system")
Java_Intro = Literal("Expert System")
Java_Intro_link = URIRef("http://dbpedia.org/page/Java_Intro")
g.add( (bob, RDF.type, FOAF.Person))
g.add( (linda, RDF.type, FOAF.Person))
g.add( (john, RDF.type, FOAF.Person))
g.add( (ex.Course, RDF.type, RDFS.Class))
g.add( (ex.Description, RDF.type, RDF.Property))
g.add( (ex.Topic, RDF.type, RDFS.Class))
g.add( (ex.Covers, RDF.type, RDFS.Class))
g.add( (ex.COMP248, RDF.type, ex.Course))
g.add( (ex.COMP248, RDF.type, RDF.Property))
g.add( (ex.COMP248, FOAF.Name, COMP248_Name))
g.add( (ex.COMP248, ex.Description, COMP248_Description))
g.add( (ex.COMP249, RDF.type, ex.Course))
g.add( (ex.COMP249, FOAF.Name, COMP249_Name))
g.add( (ex.COMP249, ex.Description, COMP249_Description))
g.add( (ex.Expert_system, RDF.type, ex.Topic))
g.add( (ex.Expert_system, FOAF.name, Literal('Intro to JAVA')))
g.add( (ex.Expert_system, RDFS.seeAlso, Expert_system_link))
g.add( (ex.COMP248, ex.Covers, ex.Expert_system))
g.add( (ex.Java_Intro, RDF.type, ex.Topic))
g.add( (ex.Java_Intro, FOAF.name, Literal('Expert System')))
g.add( (ex.Java_Intro, RDFS.seeAlso, Java_Intro_link))
g.add( (ex.COMP249, ex.Covers, ex.Java_Intro))


COMP248_GradeBob1 = Literal('A')
COMP248_GradeBob2 = Literal('F')
COMP248_GradeLinda = Literal('B')
COMP248_YearBob1 = Literal('Fall 2020')
COMP248_YearBob2 = Literal('Fall 2018')
g.add( (ex.COMPLETED, RDF.type, RDFS.Class))
#g.add( (COMP248_GradeBob1, RDF.type, RDF.Property))
g.add( (bob, ex.COMPLETED, ex.COMP248))
g.add( (bob, ex.COMP248, COMP248_GradeBob1))
#g.add( (COMP248_GradeBob1, ex.Term, COMP248_YearBob1))
g.add( (bob, ex.COMP248, COMP248_GradeBob2))
#g.add( (COMP248_GradeBob2, ex.Term, COMP248_YearBob2))
g.add( (bob, ex.COMPLETED, ex.COMP249))
g.add( (bob, ex.COMP249, Literal('F')))
#g.add( (bob, ex.COMP249, Literal('B+')))
#g.add( (Literal('B+'), ex.Term, Literal('Fall 2018')))
g.add( (linda, ex.COMPLETED, ex.COMP249))
g.add( (linda, ex.COMP249, Literal('C+')))
g.add( (john, ex.COMPLETED, ex.COMP249))
g.add( (john, ex.COMP249, Literal('A+')))


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
        """PREFIX foaf: <http://xmlns.com/foaf/0.1/>
           SELECT DISTINCT ?student
           WHERE {
              ?student rdf:type foaf:Person .
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
                        SELECT DISTINCT ?t ?l
                        WHERE {
                            ?course ex:Covers ?topics.
                            ?topics foaf:name ?t.
                            ?topics rdfs:seeAlso ?l.
                        }''')
    qres = graph.query(q, initBindings = {'course': course})
    for row in qres:
        print(row)

#print("the topic that this course cover is:")
#print(course_topics(ex.COMP248, g))    

def list_course(graph,student):
    q = prepareQuery('''PREFIX ex: <http://example.org/>
                        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                        SELECT DISTINCT ?c ?g
                        WHERE {
                            ?student ex:COMPLETED ?course .
                            ?course foaf:Name ?c .
                            ?student ?course ?g.
                        }''')
    qres = graph.query(q, initBindings = {'student': student})
    for row in qres:
        print (row)
        
#list_course(g, bob)

def list_student(graph,topic):
    q = prepareQuery('''PREFIX ex: <http://example.org/>
                        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                        SELECT DISTINCT ?s
                        WHERE {
                            ?course ex:Covers ?topic.
                            ?s ex:COMPLETED ?course.
                            ?s ?course ?grade.
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
                            ?student ex:COMPLETED ?course .
                            ?student ?course ?grade .
                            ?course ex:Covers ?t .
                            FILTER(?grade != 'F')
                        }''')
    qres = graph.query(q, initBindings = {'student': student})
    for row in qres:
        print (row)

