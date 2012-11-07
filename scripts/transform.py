from sys import argv

global_id_mark = 0
linkedin_id_map = {}


def get_id(x):
    global global_id_mark
    global linkedin_id_map
    if x in linkedin_id_map:
        return linkedin_id_map[x]
    global_id_mark += 1
    linkedin_id_map[x] = global_id_mark
    return global_id_mark


if __name__ == '__main__':
    if len(argv) != 3:
        print "Error"
        exit()
    old_graph = open(argv[1])
    new_graph = open(argv[2], 'w')
    edges = 0
    for line in old_graph:
        f, t = line.split(",")
        fid = get_id(f)
        tid = get_id(t)
        new_graph.write("%s\t%s\n" % (fid, tid)  )
        edges += 1
        if edges%10000 == 0:
            print edges
    print 'done'
    print """
    Edges %s
    Nodes %s
    """ % (edges, len(linkedin_id_map.keys()))
