# 图结构
graph = {}
graph["start"] ={}
graph["start"]["a"] = 10
graph["a"]={}
graph["a"]["b"]=20
graph["b"]={}
graph["b"]["c"]=1
graph["b"]["fin"]=30
graph["c"]={}
graph["c"]["a"]=1
graph["fin"]={}
# 最小开销
infinity = float("inf")

costs = {}
costs["a"]=10
costs["b"]=infinity
costs["c"]=infinity
costs["fin"]=infinity

# 父节点
parents ={}
parents["a"]="start"
parents["b"]=None
parents["c"]=None
parents["fin"]=None
# 已检查的节点
precssed=[]

# 用来找最小开销节点的
def find_lowset_cost(costs):
    lowset_cost = float("inf")
    lowset_cost_node = None
    for node in costs:
        n = costs[node]
        if n < lowset_cost and node not in precssed:
            lowset_cost = n
            lowset_cost_node = node
    return lowset_cost_node

# 算法主体
def dijkstra():
    node = find_lowset_cost(costs)
    while node is not  None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n]=new_cost
                parents[n]=node
        precssed.append(node)
        node=find_lowset_cost(costs)
    return costs["fin"]


if __name__ == '__main__':
    print(dijkstra())


























