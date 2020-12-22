with open("input.txt") as r:
    buses = r.readlines()

timestamp = int(buses[0])
def get_busids(buses_ids):
    end = False
    number = ''
    ids = []
    buses_ids = buses_ids.strip().split(",")
    for busid in buses_ids:
        try:
            busid = int(busid)
            ids.append(busid)
        except:
            pass
    return ids
def get_function(buses_ids):
    buses_ids = get_busids(buses_ids)
    closes_buses = list(map(lambda x: abs(timestamp%x - x), buses_ids))
    busid = buses_ids[closes_buses.index(min(closes_buses))]
    return busid*min(closes_buses) 
buses_ids = buses[1]
print(get_function(buses_ids))

#--------------------------------part2-----------------------------------------------------

with open("input.txt") as r:
    buses = r.readlines()

timestamp = int(buses[0])
def get_busids(buses_ids):
    buses_ids = buses_ids.strip().split(",")
    return buses_ids
def get_function(buses_ids):
    buses_ids = get_busids(buses_ids)
    buses = []
    timestamps = []
    for t,busid in enumerate(buses_ids):
        try:
            busid = int(busid)
            buses.append(busid)
            timestamps.append(t)
        except:
            pass
    init_timestamp = 100000000000000
    def check(t,b,timestmp):
        for ti,bi in zip(t,b):
            if (timestmp+ti)%bi != 0:
                return False
        return True
    def check2(t,b,timestmp):
        for ti,bi in zip(t,b):
            if bi == 41 or bi == 659:
                if timestmp%bi != 0:
                    return False
        return True

    while True:
        if check2(timestamps,buses,init_timestamp):
            if check(timestamps,buses, init_timestamp-41):
                return init_timestamp
        init_timestamp+=41*659
print(get_function(buses[1]))

