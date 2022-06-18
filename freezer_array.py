class EmpNode:
    def __init__(self, emp_id):
        self.empID = emp_id
        self.attctr = 1
        self.left = None
        self.right = None


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


def execute_instruction(instruction, btree):
    if "inFreezer" in instruction:
        in_freezer(btree)
    elif "checkEmp" in instruction:
        check_emp(btree)
    elif "freqVisit" in instruction:
        freq_visit(btree)
    elif "range" in instruction:
        employee_range(btree)


def in_freezer(btree):
    print("inFreezer")


def check_emp(btree):
    print("checkEmp")


def freq_visit(btree):
    print("freqVisit")


def employee_range(btree):
    print("range")


if __name__ == "__main__":
    input = ["05", "22", "41", "121", "41", "22", "41", "121", "\n", "inFreezer: ", "checkEmp: 12", "checkEmp: 22",
             "freqVisit: 3", "range: 05:125"]
    binary_tree = []
    empIds = []
    isEmpId = True

    for i in input:
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
                execute_instruction(i, binary_tree)
        except:
            continue

    print(empIds)
    print([emp.attctr for emp in binary_tree])
