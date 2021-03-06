#this appends the triples to the end of turtleTriples.txt

if __name__ == "__main__":
    f = open("resources/Student list.txt", "r")

    toWrite = []
    num = ""

    toWrite.append("ex:Student a rdfs:Class ;\n rdfs:label \"Student class\"@en .")
    toWrite.append("ex:name a rdf:Property .")
    toWrite.append("ex:term a rdfs:Class ;\n rdfs:label \"term class\"@en .")
    toWrite.append("ex:grade a rdfs:Class ;\n rdfs:label \"grade class\"@en .")
    toWrite.append("ex:Course a rdf:Property ;\n    rdfs:domain ex:Student ;\n    rdfs:range ex:term ;\n    rdfs:range ex:grade .")
    #toWrite.append("\n")
    #toWrite.append("\"A+\" rdf:type ex:grade")
    #toWrite.append("\"A\" rdf:type ex:grade")
    #toWrite.append("\"A-\" rdf:type ex:grade")
    #toWrite.append("\"B+\" rdf:type ex:grade")
    #toWrite.append("\"B\" rdf:type ex:grade")
    #toWrite.append("\"B-\" rdf:type ex:grade")
    #toWrite.append("\"C+\" rdf:type ex:grade")
    #toWrite.append("\"C\" rdf:type ex:grade")
    #toWrite.append("\"C-\" rdf:type ex:grade")
    #toWrite.append("\"D+\" rdf:type ex:grade")
    #toWrite.append("\"D\" rdf:type ex:grade")
    #toWrite.append("\"D-\" rdf:type ex:grade")
    #toWrite.append("\"F\" rdf:type ex:grade")
    #toWrite.append("\n")

    for line in f:
        l = line.split()

        name = l[0] + ' ' + l[1]
        #l[2] = student number (used later)
        #l[3] = "completed"
        course = l[4]
        #l[5] = "Grade"
        grade = l[6]
        term = l[7] + ' ' + l[8]

        if (not (l[2] == num)):
            num = l[2]
            toWrite.append("ex:" + num + " a ex:Student .")
            toWrite.append("ex:" + num + " foaf:name " + "\"" + name + "\" .")
        num = l[2]
        toWrite.append("ex:" + num + " ex:" + course + " \"" + grade + "\" .")
        toWrite.append("ex:" + num + " ex:" + course + " \"" + term + "\" .")

    f.close();

    f = open("turtleTriples.txt", "a")

    f.write("\n")
    for line in toWrite:
        f.write(line + "\n")

    f.close();