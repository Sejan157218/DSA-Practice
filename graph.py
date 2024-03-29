# import sys
# sys.setrecursionlimit(15000)


class Graph:
    def __init__(self, edge) -> None:
        self.edge = edge
        self.graph_dict = {}
        for start, end in edge:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("graph",  self.graph_dict)
    
    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                print("new_path")
                new_path = self.find_path(node, end, path)
                print(new_path)
                for p in new_path:
                    paths.append(p)
        return paths


    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path
if __name__ == '__main__':

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]
    
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    
    
    route_graph = Graph(routes)
    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.find_path(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))