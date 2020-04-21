# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:09:34 2020

@author: luciano
"""

#returns an answer and an index corresponding to which question it is answering:
#index = 1 --> “What is the <course> about?” --> answer = course_name
#index = 2 --> “Which courses did <Student> take?” --> answer = student_name
#index = 3 --> “Which courses cover <Topic>?” --> answer = topic
#index = 4 --> “Who is familiar with <Topic>?” --> answer = topic
def parse_question(question):
    if 'what' in question.casefold():
        q = question.split()
        course = q[2] + ' ' + q[3]
        return course, 1
    elif 'who' in question.casefold():
        q = question.split()
        topic = q[4:]
        t = topic[0] + '_'
        for x in range(1, len(topic)-1):
            t += (topic[x].casefold() + '_')
        t += topic[-1].casefold()
        return t[:-1], 4
    elif 'cover' in question.casefold():
        q = question.split()
        topic = q[3:]
        t = topic[0] + '_'
        for x in range(1, len(topic)-1):
            t += (topic[x].casefold() + '_')
        t += topic[-1].casefold()
        return t[:-1], 3
    elif 'take' in question.casefold():
        q = question.split()
        student = q[3]
        return student, 2
    else:
        return None, -1
   

if __name__ == '__main__':
    
    while True:
        #Do not forget the '?' at the end of the last word (e.g. "about?") and capital letters for the topics
        question = input("Ask your question: \n")
        answer, index = parse_question(question) 
        if(index == -1):
            break
        else:
            print(answer)
            #use the index to call the corresponding SPARQL method
            if index == 1:
                print(index)
                #SPARQL
            elif index == 2:
                print(index)
                #SPARQL
            elif index == 3:
                print(index)
                #SPARQL
            else:
                print(index)
                #SPARQL
    





