import sys

# Import graph
sys.path.append("../graph")

from graph import Graph

def earliest_ancestor(ancestors, starting_node):
# Initiate graph
    graph = Graph()
    # For each parent and child within the given ancestors
    for (parent, child) in ancestors:
        # Add vertices
        # If there isnt a parent
        if not graph.vertex_exists(parent):
            # Add the parent vertex
            graph.add_vertex(parent)
        # If there isn't a child
        if not graph.vertex_exists(child):
            # Add the child vertex
            graph.add_vertex(child)

        # Add edges
        graph.add_edge(child, parent)

    # Initial ancestors of starting node
    node_ancestors = graph.get_neighbors(starting_node)

    # If the starting node has no parents
    if len(node_ancestors) == 0:
        # Return -1, as instructions say
        return -1

    # Setup
    current_node = starting_node

    # While ancestors exist
    while len(graph.get_neighbors(current_node)) > 0:
        node_ancestors = graph.get_neighbors(current_node)
        # Get the ancestor with the smaller ID value
        ancestor = min(node_ancestors)
        # Move current_node pointer to selected ancestor
        current_node = ancestor

    # Return earliest connected ancestor from starting_node
    return current_node