if __name__ == "__main__":
    f = open("Student list.txt", "r")

    toWrite = []
    num = ""

    toWrite.append("ex:Student a rdfs:Class .")
    toWrite.append("ex:name a rdf:Property .")
    toWrite.append("ex:Course a rdf:Property ;\n    rdfs:domain ex:Student ;\n    rdfs:range ex:term ;\n    rdfs:range ex:grade .")

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
            toWrite.append("ex:" + num + " foaf:name " + "\"" + name + "\"")
        num = l[2]
        toWrite.append("ex:" + num + " ex:" + course + " \"" + grade + "\" .")
        toWrite.append("ex:" + num + " ex:" + course + " \"" + term + "\" .")

    f.close();

    f = open("Output Test.txt", "w")

    for line in toWrite:
        f.write(line + "\n")

    f.close();