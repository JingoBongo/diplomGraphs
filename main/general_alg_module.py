import settings as s
import re

V = len(s.graph.edges)
INF = 99999


def dum_dum_floyd_alg(graph):
    distance_matrix = s.nx.floyd_warshall_numpy(s.graph, s.graph.nodes)
    # print(distance_matrix)
    # print(*distance_matrix, sep='\n')
    print(s.graph.nodes)
    # for nd in s.graph.nodes:
    #     print(" "+str(nd)+" ")
    ind = 0
    sums = ({})
    for nd in s.graph.nodes:
        print(str(nd) + " " + str(distance_matrix[ind]))
        sums[nd] = str(distance_matrix[ind])
        ind += 1
    # print(sums)
    # print(str(sums.get('a1')))
    newlist = []
    for i in sums.values():
        newlist.append(str(i).strip(" "))

    two_d_array = []
    for i in newlist:
        x = i.split(".")
        one_d_arr = []
        for xi in x:
            xi = re.sub("[^0-9]", "", xi)
            if len(xi) > 0:
                one_d_arr.append(int(xi))
        two_d_array.append(one_d_arr)
    # print('resulting arrays: ')
    # print(two_d_array)
    overall_sums = ({})
    index2 = 0
    for nd in s.graph.nodes:
        overall_sums[str(nd)] = sum(two_d_array[index2])
        index2 += 1
    # print(overall_sums)
    print('and the winner is:')
    minimal_sum = min(overall_sums.values())
    min_sum_name = ''
    for name, summ in overall_sums.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if summ == minimal_sum:
            min_sum_name = name
    print(name+' with a sum of '+str(minimal_sum))
    s.graph.nodes[name]['color'] = 'green'
    s.successfulCommand = True

    # for i in sums.values():
    #     sums[i] = re.sub("[^0-9]]", "", sums[i])
    # sums_arrays

    # dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    # for k in range(V):
    #     for i in range(V):
    #         for j in range(V):
    #             dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # print_solution(dist)


def print_solution(dist):
    print(dist)
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                # print "%7s" % ("INF"),
                print(" " + str(INF))
                # print("%7s" % "INF", )
            else:
                # print("%7d\t" % (dist[i][j]),)
                print(" " + str(dist[i][j]))
            if j == V - 1:
                print("")
