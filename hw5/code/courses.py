def selection(courselist):
    csl = sorted(courselist, key=lambda a: a['finish_time']) 

    res = [csl[0]]
    curr = 0
    for i in range(1, len(csl)):
        if csl[i]['start_time'] >= res[curr]['finish_time']:
            curr = curr+1
            res.append(csl[i])

    return res 


courses = [
    {"course":"English", "start_time":1, "finish_time":2 },
    {"course":"Mathematics", "start_time":3, "finish_time":4 },
    {"course":"Physics", "start_time":0, "finish_time":6 },
    {"course":"Chemistry", "start_time":5, "finish_time":7 },
    {"course":"Biology", "start_time":8, "finish_time":9 },
    {"course":"Geography", "start_time":5, "finish_time":9 }
]

selected = selection(courses)
for i in range(len(selected)):
    print("{0}th course: {1}".format(i, selected[i]))
