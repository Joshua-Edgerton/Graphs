"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        # Maintain list of visited nodes
        # Dive in till deepest node reached
        # Then back out to previous node
        # Repeat

        # Setup
        visited = {}
        stack = Stack()
        # Put root on top of stack
        stack.push(starting_vertex)
        # Mark visited
        visited[starting_vertex] = True

        while stack.size() > 0:
            # Pointer to current vertex
            current_vertex = stack.pop()

            for vertex in self.vertices[current_vertex]:
                if not visited.get(vertex):
                    # Push vertex
                    stack.push(vertex)
                    # Mark visited
                    visited[vertex] = True

            # Do work on vertex
            print(current_vertex)

    def dft_recursive(self, starting_vertex):
        visited = set([starting_vertex])
        def dive(current_vertex, visited):
            print(current_vertex)
            for vertex in self.get_neighbors(current_vertex):
                if vertex not in visited:
                    visited.add(vertex)
                    dive(vertex, visited)
        dive(starting_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        visited = set()
        queue = Queue()
        queue.enqueue([starting_vertex])
        while queue.size() != 0:
            path = queue.dequeue()
            current_vertex = path[-1]
            if current_vertex == destination_vertex:
                return path
            else:
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    for vertex in self.get_neighbors(current_vertex):
                        if vertex not in visited:
                            new_path = path.copy()
                            new_path.append(vertex)
                            queue.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() != 0:
            path = stack.pop()
            current_vertex = path[-1]
            if current_vertex == destination_vertex:
                return path
            else:
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    for vertex in self.get_neighbors(current_vertex):
                        if vertex not in visited:
                            new_path = path.copy()
                            new_path.append(vertex)
                            stack.push(new_path)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        visited = set()
        def dive(current_vertex, destination_vertex, visited):
            if current_vertex in visited:
                return None
            elif current_vertex == destination_vertex:
                return [destination_vertex]
            else:
                visited.add(current_vertex)
                for vertex in self.get_neighbors(current_vertex):
                    search = dive(vertex, destination_vertex, visited)
                    if search is not None:
                        return [current_vertex] + search
                return None
        return dive(starting_vertex, destination_vertex, visited)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
