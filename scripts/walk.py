"""
Efficient way of iterating LARGE mongo DB with generator.
"""

def walk(col):
    skip = 0
    limit = 1000
    hasMore = True
    while hasMore:
        res = col.find(skip=skip, limit=limit)
        hasMore = (res.count(with_limit_and_skip=True) == limit)
        docs = []
        for x in res:
            yield x
        skip += limit
        print skip

if __name__ == '__main__':
    import pymongo
    import codecs # this is a workaround for writing unicode string to file.
    con = pymongo.Connection("10.1.1.110")
    db = con['scrapy']
    col = db['person_profiles']
    name = codecs.open("name.text", 'w', encoding="utf-8")
    
    for person in walk(col):
        try:
            n = person['name']
            first_name = n["given_name"]
            last_name = n['family_name']
            name.write("%s %s#%s %s\n" % (first_name, last_name, last_name, first_name) )
        except Exception, e:
            print e
            continue
    name.close()
