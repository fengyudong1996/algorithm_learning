# 《算法图解》 习题一


# 散列表嵌套散列表 建立图结构
graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7
graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3
graph["d"] = {}
graph["d"]["fin"] = 1
# fin虽然没有任何节点 但是不要忘记了
graph["fin"] = {}

# 散列表装取每个节点的最小已知最小开销
# infinity 未知开销的点 的开销设为正无穷
infinity = float("inf")

costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

# 散列表更新节点的父节点，得到每个节点的最小开销
# 除了初始节点其他的父节点都是未知的None
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None
# 用来装已经检查过的点
processed = []
# 方法用来找costs中开销最小的点
def find_lowset_cost_node(costs):
    lowset_cost = float("inf")
    lowset_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowset_cost and node not in processed:
            lowset_cost = cost
            lowset_cost_node = node

    return lowset_cost_node


if __name__ == '__main__':
    node = find_lowset_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowset_cost_node(costs)
    # 打印终点的最小开销
    print(costs["fin"])
    # 打印所有节点的以及父节点
    print(parents)
    # 验证，计算成功
