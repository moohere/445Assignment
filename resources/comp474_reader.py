import re
import pandas as pd
import requests
import json
import spotlight
from time import sleep
import sys
import pickle


 
rx_dict = {
        
        #regex that matches a course. e.g. COMP 444 Name of course (3 credits)
        'course': re.compile(r'(?P<course>^[A-Z]{4} [0-9]{3,4} .+\))'),

}


class Course:
  
    def __init__(self, subject, number, name, description):
        self.name = name
        self.subject = subject
        self.number = number
        self.description = description
        self.uri = []
    


#parses the current line to find courses by matching the regex
def _parse_line(line):
    
    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            return key, match
    
    return None, None

#parses the file line by line returns two lists for courses and courses descriptions
def parse_file(filepath):
    
    courses = []
    descriptions = []
    temp = ''
    
    with open(filepath, 'r') as file_object:
        line = file_object.readline()
        
        while line:
            
            key, match = _parse_line(line)
            
            if key == 'course':
                descriptions.append(temp)
                course = match.group('course')
                temp = ''
            else:
                temp += line
      
            courses.append(course)
            
            line = file_object.readline()
    
        descriptions.append(temp)
    return courses, descriptions   



    
    
    
if __name__ == '__main__':
    
    filepath = 'test.txt'
    c, d = parse_file(filepath)
    c = list(dict.fromkeys(c))
    del d[0]

    courses = []
    
    print(len(d))
    print(len(c))
    
    for i in c:
        x = i.split()
        name = ''
        for t in range(2, len(x)-2):
            name += (x[t] + ' ')
        courses.append(Course(x[0], x[1], name, ''))
        
    
    for i in range(0, len(courses)):
        courses[i].description = d[i]
        
    
    pickle_out = open("courses_pickle.txt", "ab")
  
    
    for i in range(1416, len(courses)):
        
        try:
            index = i
            annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate', courses[i].description, confidence=0.5, support=0)
            print(i)
            for x in annotations:
                if x['URI'] != None:
                    courses[i].uri.append(x['URI'])
            courses[i].uri = list(dict.fromkeys(courses[i].uri))
        except:
            print('x')
            break
        
    #pickle.dump(index, pickle_out)
    print(index)
    
    for i in range(1416, index):
        pickle.dump(courses[i], pickle_out)
    
    
    
    
    pickle_out.close()
    
