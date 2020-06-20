#  贪婪算法之集合覆盖问题

# 这个列表包含要覆盖的州以及剩余
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])
# 广播台以及其可以覆盖的州
stations = {}
stations["kone"] =set(["id","nv","ut"])
stations["ktwo"] =set(["wa","id","mt"])
stations["kthree"]=set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])
# 使用一个集合来存储最终选择的广播台
final_stations = set()

# 最终目的是清空需要覆盖的州
while states_needed:
    # 选出覆盖了最多未覆盖州的广播台
    best_station = None
    # best广播台所覆盖的州组成的set
    states_covered = set()
    # 分别迭代出 广播台stations ,其可以覆盖的州 states
    for station,states in stations.items():
        covered = states_needed & states
        if len(covered) >  len(states_covered):
            best_station = station
            states_covered = covered
    # 减去每次最终选择的广播台所覆盖的州
    states_needed -= states_covered
    final_stations.add(best_station)
# 打印最终选择的广播台
print(final_stations)
































