'''
狄克斯特拉算法 ：
        只是适用于 有向无环图 且不可以有负权边
三个散列表
GRAPH 存储图结构
COSTS 存储到达某个节点的权重（这里最小） 需要一直更新的
PARENTS 存储节点的父节点
'''
graph = {}
# 在散列表中嵌套散列表 [节点][邻居] = 权重
graph ["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph ["a"] ={}
graph ["a"]["fin"] = 1
graph ["b"]={}
graph ["b"]["a"] = 3
graph ["b"]["fin"]=5
graph ["fin"] = {}
# [节点] = 累积最小权重
infinity =float("inf")
costs ={}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
# [节点] = 父节点
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
# 用来装已经检查过的节点
processed =[]
# 存找最小节点函数
def find_lowest_coat_node(coste):
    lowset_cost = float("inf")
    lowset_cost_node = None
    for node in costs:
        cost = coste[node]
        if cost < lowset_cost and node not in processed:
            lowset_cost_node = node
            lowset_cost = cost
    return lowset_cost_node
# 算法主体

if __name__ == '__main__':
    # 找到costs中最小开销最小的节点，作为开始的节点
    node = find_lowest_coat_node(costs)
    #循环知道全部costs中的节点计算结束
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_coat_node(costs)
# 打印最短路径的权重
print(costs["fin"])
























