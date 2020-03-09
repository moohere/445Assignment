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
    print(len(courses[-1].uri), courses[-1].subject)
    
    for x in courses:
        x.description = x.description.replace('\n', '')
        
 
    courses = name_fixing(courses)
   
    
    
    #write_file('turtleTriples.txt', courses)
    
    pickle_out = open("coursesInfo.pickle", "wb")
    
    for x in courses:
        pickle.dump(x, pickle_out)   
        
            
            
            
            