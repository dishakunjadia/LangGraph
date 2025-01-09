from typing import Any, List, Dict
from langgraph.node import Node

class Graph: 
    def __init__(self):
        self.nodes ={}
        self.edges = {}
    
    def add_node(self, node: Node):
        self.nodes[node.name] = node
    
    def add_edge(self, from_node: str, to_node: str):
        if from_node not in self.edges: 
            self.edges[from_node] = []
        self.edges[from_node].append(to_node)
    
    def run(self, start_node: str, input_data: Any) -> Dict[str, Any]:
        results = {}
        queue = [start_node]
        visited = set()
        
        while queue: 
            current_node = queue.pop(0)
            if current_node in visited: 
                continue
            visited.add(current_node)
                
            node = self.nodes[current_node]
            results[current_node] = node.run(
                input_data if current_node == start_node else results 
            )
        
            if current_node in self.edges:
                queue.extend(self.edges[current_node])
        
        return results 