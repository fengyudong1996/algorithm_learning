#  广度优先算法的python
#  我能否知道我最终是通过几步找到结果的？（原书中没有）
#  解决方法： 创建一个散列表["you"]=0 ,在添加下一级的时候向散列表中查询并添加[“下一级”]=上一级的值+1;



# deque 是双端队列，两端都可以编辑，既可以实现队列 也可以实现栈
# 相比与list实现的队列deque 实现拥有更低的时间和空间复杂度
# list 的pop 和 insert 空间复杂度为 O（n）,deque 的pop 和 append 的时间复杂度都是O（1）
from collections import deque


def search(name):
    search_queue= deque()
    # 将起始元素对应的邻居加入队列
    search_queue += graph[name]
    # 用于标记检查过的元素
    searched = []
    while search_queue:
        # 将最左边的元素取出
        person = search_queue.popleft()
        # 如果这个元素没有被检查过就判断它是不是我们要找的元素
        if person not in searched:
            # 如果是要找的元素就返回True
            if person_is_seller(person):
                print(person+"is a mango seller")
                return True
            # 如果不是要找的元素就将该元素加入已检查列表，其的邻居加入队列
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False


# 这个方法用来判断这个元素是不是我们要找的元素
def person_is_seller(name):
    return name[-1] == 'm'





if __name__ == '__main__':
    #用散列表存储图结构
    #键值对的顺序不重要，散列表是无序的
    graph = {}
    graph["you"] = ["alice","bob","claire"]
    graph["bob"] = ["anuj","peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom","jonny"]
    graph["anuj"]=[]
    graph["peggy"]=[]
    graph["thom"] = []
    graph["jonny"] = []

    # True
    print(search("you"))




    pass









