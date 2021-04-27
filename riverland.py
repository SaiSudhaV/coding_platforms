
import pandas as pd
import numpy as np

class CityHappiness(object):

    def __init__(self, city, happiness):
        self.city = city
        self.happiness = happiness

    def happiness_table(self):
        dic = {
            'city': self.city,
            'happiness': self.happiness,
        }
        return pd.DataFrame(dic, columns=['city', 'happiness'], index=self.city)

    def get_happiness(self, city):
        table = self.happiness_table()
        return table.loc[city]['happiness']


class Node(object):

    def __init__(self, node_name):
        self.node_name = node_name

    def get_node(self):
        return self.node_name

    def set_node(self, new_node):
        self.node_name = new_node

    def __str__(self):
        return self.node_name


class Edge(object):

    def __init__(self, source, destination):
        self.src = source
        self.dst = destination

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dst

    def __str__(self):
        return self.src + ' -> ' + self.dst


class Mapping(object):

    def __init__(self, nodes, p, happiness):
        self.nodes = nodes
        self.p = p
        self.happiness = happiness
        self.adj_mat = None
        self.adj_mat_ferry = None
        self.b = None
        self.f = None
        self.sel_rout = None
        self.source = None


    def data_table(self):
        dic = {
            'city': self.nodes,
            'p': ['0'] + self.p,
            'happiness': self.happiness,
        }
        return pd.DataFrame(dic, columns=['city', 'p', 'happiness'], index=self.nodes)

    def happiness_table(self):
        dic = {
            'city': self.nodes,
            'happiness': self.happiness,
        }
        return pd.DataFrame(dic, columns=['city', 'happiness'], index=self.nodes)

    def get_happiness(self, city):
        table = self.happiness_table()
        return table.loc[city]['happiness']


    def adjacency_matrix(self):
        zero_matrix = np.zeros((len(self.nodes), len(self.nodes)), np.int8)

        for i in range(len(self.nodes[1:])):
            zero_matrix[int(self.nodes[1:][i])-1, int(self.p[i])-1] = 1

        self.adj_mat = pd.DataFrame(zero_matrix, index=self.nodes, columns=self.nodes)
        return None

    def adjacency_matrix_ferry(self):
        if self.adj_mat is None:
            self.adjacency_matrix()

        self.adj_mat_ferry = self.adj_mat + self.adj_mat.transpose()
        return None

    def next_cities(self, source, ferry=True):
        if ferry is False:
            if self.adj_mat is None:
                self.adjacency_matrix()
            rec_mat = self.adj_mat

        if ferry is True:
            if self.adj_mat_ferry is None:
                self.adjacency_matrix_ferry()
            rec_mat = self.adj_mat_ferry

        adj_l = rec_mat.loc[source][rec_mat.loc[source] == 1]
        if len(adj_l) > 0:
            return adj_l.index
        else:
            return []

    def routs_bfs(self, source, destination, ferry):

        journey_init = [source]
        paths_q = [journey_init]

        while len(paths_q) != 0:

            check_path = paths_q.pop()
            last_city = check_path[-1]

            if last_city == destination:
                return check_path

            for rout in self.next_cities(last_city, ferry):
                if rout not in check_path:
                    new_path = check_path + [rout]
                    paths_q.append(new_path)

        return None

    def routs_dfs(self, source, destination, paths, longest, ferry):

        paths = paths+[source]

        if source == destination:
            return paths

        available_rout = self.next_cities(source, ferry)
        for rout in available_rout:
            if rout not in paths:
                if longest == None or len(paths) > len(longest):
                    new_path = self.routs_dfs(rout, destination, paths, longest, ferry)

                    if new_path != None:
                        longest = new_path

            #else:
                #print("Already visited: ", rout)

        return longest

    def longest_rout(self, start, paths, ferry, closed):
        init = [start]
        path_q = [init]
        longest = []
        while len(path_q) != 0:

            temp = path_q.pop()
            last = temp[-1]

            for i in self.next_cities(last, ferry):
                if ferry:
                    if i not in temp and i not in closed:
                        new = temp + [i]
                        path_q.append(new)
                        if len(new)>len(longest):
                            longest = new
                else:
                    if i not in temp:
                        new = temp + [i]
                        path_q.append(new)
                        if len(new)>len(longest):
                            longest = new
                #else:
                    #print(i)
        return longest

    def select_city(self, source, closed):

        closed = closed + [source]
        cities = self.next_cities(source, False)
        b,f = None, None
        long = []
        for i in cities:
            if self.routs_bfs(source, i, False) is not None:
                closed.append(i)
                b = i
                path = self.longest_rout(i, [], True, closed)
                if len(path) > len(long):
                    long = path
                    #b = i
                    f = path[-1]

            else:
                return self.select_city(i, closed)

        self.b = b
        self.f = f
        self.sel_rout = long
        return None

    def set_destination(self, source):
        self.source = source
        ferry_rout = self.longest_rout(source, [], True, [])
        self.sel_rout = ferry_rout
        if len(ferry_rout) > 0:
            self.f = ferry_rout[-1]
        else:
            self.f = source

        return None

    def gain_happiness(self, source, closed, value):
        """
        ab+D⋅T,
        """
        if self.source == None or self.source != source or self.f == None:
            self.set_destination(source)

        if self.source == self.f:
            return int(self.get_happiness(self.source))

        max_boat_rout = self.longest_rout(self.source, [], False, closed)
        max_happiness = 0
        for i in max_boat_rout:
            if i not in closed:
                possible_ferry_rout = self.routs_dfs(i, self.f, [], None, True)

                if i in self.sel_rout:
                    happiness = int(self.get_happiness(i)) + ((len(possible_ferry_rout)-1)*value)
                    if happiness > max_happiness:
                        max_happiness = happiness
                elif i == '1':
                    happiness = int(self.get_happiness(i))
                    if happiness > max_happiness:
                        max_happiness = happiness
                else:
                    happiness = int(self.get_happiness(i))
                    if happiness > max_happiness:
                        max_happiness = happiness

        return max_happiness


def chef_happiness():
    x = input("N, Q: ",).split()
    n = list(np.arange(1, int(x[0])+1))
    p = input("p: ",).split()
    a = input('a: ',).split()
    mp= Mapping(n,p,a)
    close = []
    q = int(x[1])
    while q>0:
        y = input('query:',).split()
        if y[0] == '?':
            return mp.gain_happiness(int(y[1]), close, int(y[2]))
            print("HAPPINESS:   ",hap)
        elif y[0] == "-":
            close.append(int(y[1]))
        elif y[0] == "+":
            close.remove(int(y[1]))
        q -= 1


if __name__ == '__main__':
    chef_happiness()
