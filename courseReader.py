# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:28:19 2020

@author: luciano
"""

import pandas as pd
from time import sleep
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

if __name__ == '__main__':
    
    courses = []

    pickle_in = open("coursesInfo.pickle", "rb")
    
    while True:
        try:
            courses.append(pickle.load(pickle_in))
        except EOFError:
            break
    
    pickle_in.close()
    
    
    write_file('turtleTriples.txt', courses)
    
