"""
compare names from linkedin and arnetminer
"""

def get_aminer():
    f = open("na_person.txt")
    name_set = set()
    for line in f:
        names = line.strip("\"").split(",")
        for name in names:
            name_set.add(name.strip())
    return name_set

if __name__ == "__main__":
    aminer_name  = get_aminer()
    print "we have %s aminer names" % (len(aminer_name))
    cnt = 0
    
    ## iterate linkedin names
    f = open("name.txt")
    for line in f:
        names = line.split("#")
        if names[0] in aminer_name or names[1] in aminer_name:
            cnt += 1
    print "%s names are the same" % cnt
