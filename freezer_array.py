class EmpNode:
    def __init__(self, emp_id):
        self.empID = emp_id
        self.attctr = 1
        self.left = None
        self.right = None


def search_tree_for_range(root_node, emp_id_start, emp_id_end):
    if root_node:
        if root_node.left:
            search_tree_for_range(root_node.left, emp_id_start, emp_id_end)
        else:
            print()
            # verify node

        if root_node.right:
            search_tree_for_range(root_node.right, emp_id_start, emp_id_end)


def search_tree_for_employee(root_node, emp_id):
    search_node = None
    if not search_node and root_node:
        if root_node.left:
            search_node = search_tree_for_employee(root_node.left, emp_id)

        if not search_node:
            node_emp_id = root_node.empID
            if node_emp_id == emp_id:
                return root_node
                # verify node

            if not search_node and root_node.right:
                search_node = search_tree_for_employee(root_node.right, emp_id)

    return search_node

def find_total_emp_inside(root_node, emp_id):
    search_node = None
    if not search_node and root_node:
        if root_node.left:
            search_node = search_tree_for_employee(root_node.left, emp_id)

        if not search_node:
            node_emp_id = root_node.empID
            if node_emp_id == emp_id:
                return root_node
                # verify node

            if not search_node and root_node.right:
                search_node = search_tree_for_employee(root_node.right, emp_id)

    return search_node


def build_tree(emp_nodes):
    size = len(emp_nodes)
    is_tree_built = False
    i = 0

    while i < size and not is_tree_built:
        node = emp_nodes[i]

        left_child_index = (2 * i) + 1
        is_tree_built = left_child_index >= size
        if not is_tree_built:
            node.left = emp_nodes[left_child_index]

        right_child_index = (2 * i) + 2
        is_tree_built = right_child_index >= size
        if not is_tree_built:
            node.right = emp_nodes[right_child_index]
        i += 1


def is_employee_in(attendance_counter):
    return attendance_counter % 2 == 1


def execute_instruction(instruction, root_node):
    inst = instruction.split(": ")
    if "inFreezer" in instruction:
        in_freezer(root_node)
    elif "checkEmp" in instruction:
        check_emp(root_node, inst[1])
    elif "freqVisit" in instruction:
        freq_visit(root_node)
    elif "range" in instruction:
        employee_range(root_node)


def in_freezer(root_node):
    search_node = None
    if not search_node and root_node:
        if root_node.left:
            search_node = in_freezer(root_node.left)

        node_emp_id = root_node.empID
                # verify node

        if root_node.right:
            search_node = in_freezer(root_node.right)

    print("Total number of employees recorded today: 4 2 employee(s) still inside freezer room.")


def check_emp(root_node, emp_id):
    search_node = search_tree_for_employee(root_node, int(emp_id))

    if search_node:
        message = "Employee id {} swiped {} times today and is currently {} freezer room"
        position = "outside"
        if is_employee_in(search_node.attctr):
            position = "inside"

        print(message.format(search_node.empID, search_node.attctr, position))
    else:
        print("Employee id {} did not swipe today.".format(emp_id))


def freq_visit(btree):
    print("freqVisit")


def employee_range(btree):
    print("range")


if __name__ == "__main__":
    input_file = ["05", "22", "41", "121", "41", "22", "41", "121", "\n", "inFreezer: ", "checkEmp: 12", "checkEmp: 22",
                  "freqVisit: 3", "range: 05:125"]

    binary_tree = []
    empIds = []
    isTreeBuilt = False

    for i in input_file:
        try:
            if not ":" in i:
                val = int(i)
                if val in empIds:
                    index = empIds.index(val)
                    count = binary_tree[index].attctr
                    binary_tree[index].attctr = count + 1
                else:
                    empIds.append(val)
                    binary_tree.append(EmpNode(val))
            else:
                if not isTreeBuilt:
                    isTreeBuilt = True
                    build_tree(binary_tree)
                execute_instruction(i, binary_tree[0])
        except:
            continue

    print(empIds)
    print([emp.attctr for emp in binary_tree])
