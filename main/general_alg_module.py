import settings as s
import re
import random


nodes_in_radius = []


def dum_dum_floyd_alg():
    distance_matrix = s.nx.floyd_warshall_numpy(s.graph, s.graph.nodes)
    print(s.graph.nodes)
    ind = 0
    sums = ({})
    for nd in s.graph.nodes:
        print(str(nd) + " " + str(distance_matrix[ind]))
        sums[nd] = str(distance_matrix[ind])
        ind += 1
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
    overall_sums = ({})
    index2 = 0
    for nd in s.graph.nodes:
        overall_sums[str(nd)] = sum(two_d_array[index2])
        index2 += 1
    print('and the winner is:')
    minimal_sum = min(overall_sums.values())
    min_sum_name = ''
    for name, summ in overall_sums.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if summ == minimal_sum:
            min_sum_name = name
    print(name + ' with a sum of ' + str(minimal_sum))
    s.graph.nodes[name]['color'] = 'green'
    s.successfulCommand = True


# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


def dum_dum_shmoys(wh_max_number, init_radius, f_node):
    warehouse_current_number = 0
    warehouse_max_number = wh_max_number
    all_nodes = list(s.graph.nodes)
    all_warehouses = []
    first_node = None
    for k in range(int(warehouse_max_number)):
        print('dum_dum_shmoys: cycle ' + str(k + 1) + ' out of ' + str(warehouse_max_number))
        if f_node is None or f_node == 'None':
            first_node = random.choice(all_nodes)
        else:
            first_node = f_node
        print('dum_dum_shmoys: start with node ' + str(first_node))
        all_warehouses.append(first_node)
        warehouse_current_number += 1
        nodes_in_radius.append(first_node)
        recursive_search(first_node, 0, init_radius)
        for n in nodes_in_radius:
            try:
                all_nodes.remove(n)
            except ValueError:
                pass  # do nothing!
        nodes_in_radius.clear()
        print('dum_dum_shmoys: current radius = ' + str(init_radius))
        print('dum_dum_shmoys: remaining nodes')
        print(all_nodes)
        print('dum_dum_shmoys: placed warehouses')
        print(all_warehouses)
        print('dum_dum_shmoys: warehouses current number = ' + str(warehouse_current_number))
        f_node = None
        if len(all_nodes) <= 0:
            break
    if len(all_nodes) > 0:
        print('dum_dum_shmoys: there are still nodes that are not covered by warehouses, incrementing radius by half '
              'and starting again')
        int_rad_value = int(init_radius)
        dum_dum_shmoys(wh_max_number, int_rad_value + int(int_rad_value / 2), None)
    else:
        print('dum_dum_shmoys: function execution completed with radius = ' + str(init_radius))
        for nd in all_warehouses:
            s.graph.nodes[nd]['color'] = 'green'
        s.successfulCommand = True


# TODO. if a warehouse cant do more than x amount of nodes nearby, drop the sequence I can just store not just
#  related edges, but also maybe amount of nodes being added, like. dont add more than y nodes starting from z point
def recursive_search(nodename, initial_weight, radius):
    global nodes_in_radius
    related_edges = extract_edges_from_str(s.graph.edges(nodename))
    print('recursive_search: starting with node: ' + str(nodename))
    print('recursive_search: found related edges: ' + str(related_edges) + '; size: ' + str(len(related_edges)))
    for r in related_edges:
        nd1 = r.split('\'')[1]
        nd2 = r.split('\'')[3]
        print('recursive_search: nodes found for ' + str(r) + ' edge: ' + nd1 + ' and ' + nd2)
        local_edge_weight = s.graph.get_edge_data(nd1, nd2)['weight']
        if int(initial_weight) + int(local_edge_weight) <= int(radius):
            print('recursive_search: init weight: ' + str(initial_weight) + '; local weight: ' + str(
                local_edge_weight) + '; radius: ' + str(radius))
            if nd1 not in nodes_in_radius:
                print('recursive_search: appending node to nodes_in_radius: ' + str(nd1))
                nodes_in_radius.append(nd1)
                recursive_search(nd1, int(initial_weight) + int(local_edge_weight), radius)
            if nd2 not in nodes_in_radius:
                print('recursive_search: appending node to nodes_in_radius: ' + str(nd2))
                nodes_in_radius.append(nd2)
                recursive_search(nd2, int(initial_weight) + int(local_edge_weight), radius)
            else:
                print('recursive_search: didnt find any new nodes from edge ' + str(r))
        else:
            print('recursive_search: ending point of edge ' + str(r) + ' is out of reach')


# def extract_nodes_from_str(string: str):
#     arr = string.split('),')
#     arr2 = []
#     for n in arr:
#         n1 = n.split('\'')[1]
#         n2 = n.split('\'')[3]
#         if n2 not in arr2:
#             arr2.append(n2)
#         if n1 not in arr2:
#             arr2.append(n1)
#     return arr2


def extract_edges_from_str(string: str):
    arr2 = str(string).split('[')[1].split(']')[0].split('(')
    del arr2[0]
    return arr2
