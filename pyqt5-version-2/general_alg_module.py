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
    for name, summ in overall_sums.items():
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
            s.cust_print(self, ('cycled shmoys: With radius of ' + str(el['rad'])))
            s.cust_print(self, ('cycled shmoys: These nodes will work: ' + str(el['wh'])))
            for e in el['wh']:
                try:
                    s.graph.nodes[e]['color'] = s.default_wh_color
                except Exception as e:
                    s.cust_print(self, ('cycled shmoys: something went wrong while changing wh color'))
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
    amount_of_cycles = int(warehouse_max_number)
    if f_node is not None and f_node != 'None':
        if '(' not in f_node or ')' not in f_node:
            s.cust_print(self,
                         ('cycled shmoys: nodes should be passed inside brackets without spaces, separated by \',\''))
            return
        raw_given_nodes = str(f_node).split('(')[1].split(')')[0].split(',')
        given_nodes = [n for n in raw_given_nodes if n in s.graph.nodes]
        given_nodes = list(set(given_nodes))
        if int(wh_max_number) < len(given_nodes):
            s.cust_print(self, ('cycled shmoys: there are more given nodes than max number of warehouses, aborting'))
            return
        amount_of_cycles = amount_of_cycles - len(given_nodes)
        for n in given_nodes:
            all_warehouses.append(n)
            warehouse_current_number += 1
            nodes_in_radius.append(first_node)
            recursive_search(n, 0, init_radius)
            for n in nodes_in_radius:
                try:
                    all_nodes.remove(n)
                except ValueError:
                    pass  # do nothing!
            nodes_in_radius.clear()
            if len(all_nodes) <= 0:
                break

    for k in range(amount_of_cycles):
        first_node = random.choice(all_nodes)
        all_warehouses.append(first_node)
        warehouse_current_number += 1
        nodes_in_radius.append(first_node)
        recursive_search(first_node, 0, init_radius)
        for n in nodes_in_radius:
            try:
                all_nodes.remove(n)
            except ValueError:
                pass
        nodes_in_radius.clear()
        if len(all_nodes) <= 0:
            break

    if len(all_nodes) > 0:
        new_radius = int(init_radius) + int(int(init_radius)) / 4
        if new_radius < last_working_radius:
            dum_dum_shmoys_cycled_small(self, wh_max_number, new_radius, f_node)
        else:
            temp_dict = {'rad': last_working_radius, 'wh': list(last_working_result)}
            local_results.append(temp_dict)
            last_working_radius = 99999999999999999999999999999999999
            last_working_result.clear()
            s.successfulCommand = True
    else:
        last_working_result = all_warehouses
        last_working_radius = int(init_radius)
        new_radius = int(init_radius) - int(int(init_radius) / 32)
        dum_dum_shmoys_cycled_small(self, wh_max_number, new_radius, f_node)


def dum_dum_shmoys(self, wh_max_number, init_radius, f_node):
    # from now on f_node will be a list of nodes or None. list ex.: (1,2,3)
    global last_working_result
    global last_working_radius
    warehouse_current_number = 0
    warehouse_max_number = wh_max_number
    all_nodes = list(s.graph.nodes)
    all_warehouses = []
    first_node = None
    amount_of_cycles = int(warehouse_max_number)
    if f_node is not None and f_node != 'None':
        if '(' not in f_node or ')' not in f_node:
            s.cust_print(self,
                         ('dum_dum_shmoys: nodes should be passed inside brackets without spaces, separated by \',\''))
            return
        raw_given_nodes = str(f_node).split('(')[1].split(')')[0].split(',')
        given_nodes = [n for n in raw_given_nodes if n in s.graph.nodes]
        given_nodes = list(set(given_nodes))
        if int(wh_max_number) < len(given_nodes):
            s.cust_print(self, ('dum_dum_shmoys: there are more given nodes than max number of warehouses, aborting'))
            return
        amount_of_cycles = amount_of_cycles - len(given_nodes)
        for n in given_nodes:
            all_warehouses.append(n)
            warehouse_current_number += 1
            nodes_in_radius.append(first_node)
            recursive_search(n, 0, init_radius)
            for n in nodes_in_radius:
                try:
                    all_nodes.remove(n)
                except ValueError:
                    pass  # do nothing!
            nodes_in_radius.clear()
            if len(all_nodes) <= 0:
                break

    for k in range(amount_of_cycles):
        first_node = random.choice(all_nodes)
        all_warehouses.append(first_node)
        warehouse_current_number += 1
        nodes_in_radius.append(first_node)
        recursive_search(first_node, 0, init_radius)
        for n in nodes_in_radius:
            try:
                all_nodes.remove(n)
            except ValueError:
                pass
        nodes_in_radius.clear()
        if len(all_nodes) <= 0:
            break

    if len(all_nodes) > 0:
        s.cust_print(self, (
                'dum_dum_shmoys: there are still nodes that are not covered by warehouses, incrementing radius (' + str(
            init_radius) + ') by quarter and starting again'))
        new_radius = int(init_radius) + int(int(init_radius)) / 4
        if new_radius < last_working_radius:
            dum_dum_shmoys(self, wh_max_number, new_radius, f_node)
        else:
            s.cust_print(self, ('dum_dum_shmoys: extended function execution failed, last successful radius = ' + str(
                last_working_radius)))
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
        s.cust_print(self, ('dum_dum_shmoys: placed warehouses: ' + str(all_warehouses)))
        last_working_result = all_warehouses
        last_working_radius = int(init_radius)
        new_radius = int(init_radius) - int(int(init_radius) / 32)
        s.cust_print(self, ('dum_dum_shmoys: starting recursion with lesser radius = ' + str(new_radius)))
        dum_dum_shmoys(self, wh_max_number, new_radius, f_node)


def recursive_search(nodename, initial_weight, radius):
    global nodes_in_radius
    related_edges = extract_edges_from_str(s.graph.edges(nodename))
    for r in related_edges:
        nd1 = r.split('\'')[1]
        nd2 = r.split('\'')[3]
        local_edge_weight = s.graph.get_edge_data(nd1, nd2)['weight']
        if int(initial_weight) + int(local_edge_weight) <= int(radius):
            if nd1 not in nodes_in_radius:
                nodes_in_radius.append(nd1)
                recursive_search(nd1, int(initial_weight) + int(local_edge_weight), radius)
            if nd2 not in nodes_in_radius:
                nodes_in_radius.append(nd2)
                recursive_search(nd2, int(initial_weight) + int(local_edge_weight), radius)


def extract_edges_from_str(string: str):
    arr2 = str(string).split('[')[1].split(']')[0].split('(')
    del arr2[0]
    return arr2
