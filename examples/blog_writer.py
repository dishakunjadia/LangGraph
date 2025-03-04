from langgraph.node import Node
from langgraph.graph import Graph

def idea_generator(data):
    return "Generate a blog ........."

def content_creator(idea):
    return f"Content for the Idea {idea}"

def optimizer(content):
    return f"Optimized content {content}"

def reviewer(content):
    return f"Reviewed {content}"


# creating nodes 

idea_node = Node("Idea Generator", idea_generator)
content_node = Node("Content Creator", content_creator)
optimizer_node = Node("Optimizer", optimizer)
reviewer_node = Node("Reviewer", reviewer )


# Building the graph
blog_graph = Graph()
blog_graph.add_node(idea_node)
blog_graph.add_node(content_node)
blog_graph.add_node(optimizer_node)
blog_graph.add_node(reviewer_node)



# Edges (for data flow)
blog_graph.add_edge("Idea Generator", "Content Creator")
blog_graph.add_edge("Content Creator", "Optimizer")
blog_graph.add_edge("Optimizer", "Reviewer")

#Run Graph
result = blog_graph.run("Idea Generator", None)
print(result)

