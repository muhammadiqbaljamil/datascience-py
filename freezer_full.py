class EmpNode:
    def __init__(self, emp_id):
        self.empID = emp_id
        self.attctr = 1
        self.left = None
        self.right = None


def find_node_to_insert(nodes, level):
    siblings_count = len(nodes)
    total_count = 2 ** level
    if siblings_count < total_count:
        return nodes

def insert(nodes, emp_id):
    if nodes.count() == 0:
        nodes.append(EmpNode(emp_id))
        return nodes


    child_nodes = []
    if not root.left:
        root.left = EmpNode(emp_id)
    elif not root.right:
        root.right = EmpNode(emp_id)
    else:
        insert(root.left, emp_id)


    # else:
    #     insert(root.right, emp_id)
    # current = EmpNode(10)


if __name__ == "__main__":
    root = None
    root = insert(root, 10)
    insert(root, 20)
    insert(root, 30)
    print(root.empID)
    node = root.left
    print(node.empID)
    node = root.right
    print(node.empID)
