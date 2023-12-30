class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data) -> None:
        if data <= self.data:
            if self.left == None:
                self.left = Node(data=data)
            else:
                self.left.insert(data=data)
        else:
            if self.right == None:
                self.right = Node(data=data)
            else:
                self.right.insert(data=data)
    
    def get_height(self) -> int:
        if self.left == None and self.right == None:
            return 0
        
        if self.left != None:
            left_height = self.left.get_height()
        else:
            left_height = 0

        if self.right != None:
            right_height = self.right.get_height()
        else:
            right_height = 0

        return max(left_height, right_height) + 1
        
    def print_in_order(self) -> None:
        if self.left != None:
            self.left.print_in_order()
        
        print(self.data)

        if self.right != None:
            self.right.print_in_order()
    
    def print_pre_order(self) -> None:
        print(self.data)

        if self.left != None:
            self.left.print_in_order()
        
        if self.right != None:
            self.right.print_in_order()
    
    def print_post_order(self) -> None:
        if self.left != None:
            self.left.print_in_order()
        
        if self.right != None:
            self.right.print_in_order()
        
        print(self.data)


root = Node(data=4)
root.left = Node(data=2)
root.right = Node(data=7)
root.left.left = Node(data=1)
root.left.right = Node(data=3)

print(root.get_height())