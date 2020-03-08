import re
import pandas as pd
import requests
import json
import spotlight
from time import sleep
import sys
import pickle


class Course:
  
    def __init__(self, subject, number, name, description):
        self.name = name
        self.subject = subject
        self.number = number
        self.description = description
    
    uri = []

#writes to a file in forms of triples
def write_file(filepath, courses):
    
    f = open(filepath, "a")
    
    
    
    #for every course
    for i in range(0, len(courses)):
        #e.g. ex:COMP444 a ex:Course .
        f.write('ex:' + courses[i].subject + courses[i].number + ' a ex:Course .\n')
        #e.g. ex:COMP444 foaf:name "Name of course" .
        f.write('ex:' + courses[i].subject + courses[i].number + ' foaf:name ' + '\"' + courses[i].name + '\"' + ' .\n')
        #e.g. ex:COMP444 ex:description "description" .
        f.write('ex:' + courses[i].subject + courses[i].number + ' ex:description ' + '\"' + courses[i].description + '\"' + ' .\n')
        #e.g. ex:COMP444 ex:number "444"^^xsd:int .
        f.write('ex:' + courses[i].subject + courses[i].number + ' ex:number ' + '\"' + courses[i].number + '\"' + '^^xsd:int .\n')
        #e.g. ex:COMP444 ex:subject "COMP" .
        f.write('ex:' + courses[i].subject + courses[i].number + ' ex:subject ' + '\"' + courses[i].subject + '\"' + ' .\n')
        
        for x in courses[i].uri:
            #e.g. <http://dbpedia.org/resource/Expert_system> a ex:Topic .
            f.write('<' + x + '>' + ' a ex:Topic .\n')
            #e.g. ex:COMP444 ex:covers <http://dbpedia.org/resource/Expert_system> .
            f.write('ex:' + courses[i].subject + courses[i].number + ' ex:covers ' + '<' + x + '>' + ' .\n')
            
            t = x.split('/')[-1]
            #e.g. <http://dbpedia.org/resource/Expert_system> foaf:name "Expert_system" .
            f.write( '<' + x + '> foaf:name \"' + t + '\" .\n')
            
        f.write('\n')
    
    f.close()
    print('done')
 
    
def name_fixing(courses):
    
    with open('nameFIX.txt', 'r') as file_object:
        line = file_object.readline()
        while line:
            
            l = line.split()
            name = ''
            for x in courses:
                if x.subject == l[2] and x.number == l[3]:
                    for i in range(4, len(l) - 1):
                        name += (l[i] + ' ')
                    x.name = name
            line = file_object.readline()
    
    return courses

if __name__ == '__main__':
    
    
    
    courses = []
    
    
    pickle_in = open("courses_pickle.txt", "rb")
    
    while True:
        try:
            courses.append(pickle.load(pickle_in))
        except EOFError:
            break
    
    pickle_in.close()
    
    print(len(courses))
    print(len(courses[-1].uri))
    
    for x in courses:
        x.description = x.description.replace('\n', '')
        
 
    courses = name_fixing(courses)
   
    
    
    #write_file('turtleTriples.txt', courses)
    
    pickle_out = open("coursesInfo.pickle", "wb")
    
    for x in courses:
        pickle.dump(x, pickle_out)   
        
            
            
            
            