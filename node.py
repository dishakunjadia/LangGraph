
from typing import Callable, Any
# defining the generic Node graph
class Node: 
    def __init__(self, name: str, process_fn: Callable[[Any], Any]):
        self.name = name
        self.process_fn = process_fn
        self.output = None
    
    def run(self, input_data: Any) -> Any:
        self.output = self.process_fn(input_data)
        return self.output
    