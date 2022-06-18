class EmpNode:
    def __init__(self, emp_id):
        self.empID = emp_id
        self.attctr = 1
        self.left = None
        self.right = None


def insert(root, emp_id):
    if not root:
        root = EmpNode(emp_id)
        return root
    isInserted = False

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
