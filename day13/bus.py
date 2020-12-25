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
import numpy as np

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

    N = np.prod(buses)
    w = []
    timestamps = list(map(lambda x: (-x[0])%x[1], zip(timestamps,buses) ))
    for bus,a in zip(buses,timestamps):
        zi = int(N/bus)
        yi = pow(zi,-1,bus)
        w.append(a*zi*yi)
    return sum(w)%N


print(get_function(buses[1]))
