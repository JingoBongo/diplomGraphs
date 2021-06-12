import settings as s
import re
import random
import general_draw_module as dm



nodes_in_radius = []
last_working_result = []
local_results = []
last_working_radius = 99999999999999999999999999999999999


def dum_dum_floyd_alg(self):
    distance_matrix = s.nx.floyd_warshall_numpy(s.graph, s.graph.nodes)
    ind = 0
    sums = ({})
    for nd in s.graph.nodes:
        sums[nd] = str(distance_matrix[ind])
        ind += 1
    newlist = []
    for i in sums.values():
        newlist.append(str(i).strip(" "))
    two_d_array = []

    for i in newlist:
        x = i.strip().split(" ")
        one_d_arr = []
        for xi in x:
            xi = re.findall(r"[-+]?\d*\.\d+|\d+", str(xi))
            if len(xi) > 0:
                one_d_arr.append(float(xi[0]))
        two_d_array.append(one_d_arr)
    overall_sums = ({})
    index2 = 0
    for nd in s.graph.nodes:
        overall_sums[str(nd)] = max(two_d_array[index2])
        index2 += 1
    s.cust_print(self, ('and the winner is:'))
    minimal_sum = min(overall_sums.values())
    min_sum_name = ''
    for name, summ in overall_sums.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if summ == minimal_sum:
            min_sum_name = name
    s.cust_print(self, (min_sum_name + ' with a longest dist of ' + str(minimal_sum)))
    for nd in s.graph.nodes:
        s.graph.nodes[nd]['color'] = s.default_node_color
    s.graph.nodes[min_sum_name]['color'] = s.default_wh_color
    dm.draw_graph(self)
    s.successfulCommand = True


# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================

def dum_dum_shmoys_cycled(self, wh_max_number, init_radius, f_node, cycles):
    global local_results
    for i in range(int(cycles)):
        dum_dum_shmoys_cycled_small(self, wh_max_number, init_radius, f_node)
    local_best_rad = 99999999999999999999999999999999999
    for result in local_results:
        if local_best_rad > float(result['rad']):
            local_best_rad = float(result['rad'])
    for nd in s.graph.nodes:
        s.graph.nodes[nd]['color'] = s.default_node_color
    for el in local_results:
        if float(el['rad']) <= float(local_best_rad):
            s.cust_print(self, ('cycled shmoys: With radius of '+ str(el['rad'])))
            s.cust_print(self, ('cycled shmoys: These nodes will work: '+str(el['wh'])))
            for e in el['wh']:
                try:
                    s.graph.nodes[e]['color'] = s.default_wh_color
                except Exception as e:
                    s.cust_print(self, ('ycled shmoys: something went wrong while changing wh color'))
            break
    dm.draw_graph(self)
    local_results.clear()

def dum_dum_shmoys_cycled_small(self, wh_max_number, init_radius, f_node):
    global last_working_result
    global last_working_radius
    global local_results

    warehouse_current_number = 0
    warehouse_max_number = wh_max_number
    all_nodes = list(s.graph.nodes)
    all_warehouses = []
    first_node = None
    for k in range(int(warehouse_max_number)):
        # s.cust_print(self, 'dum_dum_shmoys: cycle ' + str(k + 1) + ' out of ' + str(warehouse_max_number))
        if f_node is None or f_node == 'None':
            first_node = random.choice(all_nodes)
        else:
            if f_node in s.graph.nodes:
                first_node = f_node  # there is no check if this node actually exists, now it is
            else:
                s.cust_print(self, ('dum_dum_shmoys: invalid node name, picking random'))
                first_node = random.choice(all_nodes)
        # s.cust_print(self, 'dum_dum_shmoys: start with node ' + str(first_node))
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
        f_node = None
        if len(all_nodes) <= 0:
            break
    if len(all_nodes) > 0:
        new_radius = int(init_radius) + int(int(init_radius)) / 4
        if new_radius < last_working_radius:
            dum_dum_shmoys_cycled_small(self, wh_max_number, new_radius, first_node)
        else:
            temp_dict = {'rad': last_working_radius, 'wh': list(last_working_result)}
            local_results.append(temp_dict)
            # local_results[-1].append(last_working_result)
            # local_results.append(temp_list)
            # for nd in s.graph.nodes:
            #     s.graph.nodes[nd]['color'] = s.default_node_color
            # for nd in last_working_result:
            #     s.graph.nodes[nd]['color'] = s.default_wh_color
            last_working_radius = 99999999999999999999999999999999999
            last_working_result.clear()
            s.successfulCommand = True
    else:
        last_working_result = all_warehouses
        last_working_radius = int(init_radius)
        new_radius = int(init_radius) - int(int(init_radius) / 32)
        dum_dum_shmoys_cycled_small(self, wh_max_number, new_radius, first_node)


def dum_dum_shmoys(self, wh_max_number, init_radius, f_node):
    global last_working_result
    global last_working_radius
    warehouse_current_number = 0
    warehouse_max_number = wh_max_number
    all_nodes = list(s.graph.nodes)
    all_warehouses = []
    first_node = None
    for k in range(int(warehouse_max_number)):
        # s.cust_print(self, 'dum_dum_shmoys: cycle ' + str(k + 1) + ' out of ' + str(warehouse_max_number))
        if f_node is None or f_node == 'None':
            first_node = random.choice(all_nodes)
        else:
            if f_node in s.graph.nodes:
                first_node = f_node # there is no check if this node actually exists
            else:
                s.cust_print(self, ('dum_dum_shmoys: invalid node name, picking random'))
                first_node = random.choice(all_nodes)
        # s.cust_print(self, 'dum_dum_shmoys: start with node ' + str(first_node))
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
        # s.cust_print(self, 'dum_dum_shmoys: current radius = ' + str(init_radius))
        # s.cust_print(self, 'dum_dum_shmoys: remaining nodes')
        # s.cust_print(self, all_nodes)
        # s.cust_print(self, 'dum_dum_shmoys: placed warehouses')
        # s.cust_print(self, all_warehouses)
        # s.cust_print(self, 'dum_dum_shmoys: warehouses current number = ' + str(warehouse_current_number))
        f_node = None
        if len(all_nodes) <= 0:
            break
    if len(all_nodes) > 0:
        s.cust_print(self, ('dum_dum_shmoys: there are still nodes that are not covered by warehouses, incrementing radius ('+str(init_radius)+') by quarter and starting again'))
        new_radius = int(init_radius) + int(int(init_radius)) / 4
        if new_radius < last_working_radius:
            dum_dum_shmoys(self, wh_max_number, new_radius, first_node)
        else:
            s.cust_print(self, ('dum_dum_shmoys: extended function execution failed, last successful radius = '+str(last_working_radius)))
            s.cust_print(self, ('dum_dum_shmoys: last successful placed warehouses: ' + str(last_working_result)))
            for nd in s.graph.nodes:
                s.graph.nodes[nd]['color'] = s.default_node_color
            for nd in last_working_result:
                s.graph.nodes[nd]['color'] = s.default_wh_color
            last_working_radius = 99999999999999999999999999999999999
            last_working_result.clear()
            s.successfulCommand = True
    else:
        s.cust_print(self, ('dum_dum_shmoys: function execution completed with radius = ' + str(init_radius)))
        s.cust_print(self, ('dum_dum_shmoys: placed warehouses: '+str(all_warehouses)))
        last_working_result = all_warehouses
        last_working_radius = int(init_radius)
        new_radius = int(init_radius) - int(int(init_radius) / 32)
        s.cust_print(self, ('dum_dum_shmoys: starting recursion with lesser radius = '+str(new_radius)))
        dum_dum_shmoys(self, wh_max_number, new_radius, first_node)
        # for nd in all_warehouses:
        #     s.graph.nodes[nd]['color'] = s.default_wh_color
        # s.successfulCommand = True


# TODO. if a warehouse cant do more than x amount of nodes nearby, drop the sequence I can just store not just
#  related edges, but also maybe amount of nodes being added, like. dont add more than y nodes starting from z point
def recursive_search(nodename, initial_weight, radius):
    global nodes_in_radius
    related_edges = extract_edges_from_str(s.graph.edges(nodename))
    # s.cust_print(self, 'recursive_search: starting with node: ' + str(nodename))
    # s.cust_print(self, 'recursive_search: found related edges: ' + str(related_edges) + '; size: ' + str(len(related_edges)))
    for r in related_edges:
        nd1 = r.split('\'')[1]
        nd2 = r.split('\'')[3]
        # s.cust_print(self, 'recursive_search: nodes found for ' + str(r) + ' edge: ' + nd1 + ' and ' + nd2)
        local_edge_weight = s.graph.get_edge_data(nd1, nd2)['weight']
        if int(initial_weight) + int(local_edge_weight) <= int(radius):
            # s.cust_print(self, 'recursive_search: init weight: ' + str(initial_weight) + '; local weight: ' + str(
            #     local_edge_weight) + '; radius: ' + str(radius))
            if nd1 not in nodes_in_radius:
                # s.cust_print(self, 'recursive_search: appending node to nodes_in_radius: ' + str(nd1))
                nodes_in_radius.append(nd1)
                recursive_search(nd1, int(initial_weight) + int(local_edge_weight), radius)
            if nd2 not in nodes_in_radius:
                # s.cust_print(self, 'recursive_search: appending node to nodes_in_radius: ' + str(nd2))
                nodes_in_radius.append(nd2)
                recursive_search(nd2, int(initial_weight) + int(local_edge_weight), radius)
            else:
                # s.cust_print(self, 'recursive_search: didnt find any new nodes from edge ' + str(r))
                pass
        else:
            # s.cust_print(self, 'recursive_search: ending point of edge ' + str(r) + ' is out of reach')
            pass


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
