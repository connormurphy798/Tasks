"""
Handles creation of a tree from a text file of tasks.

task file formatting requirements:
    - first line gives description of semicolon-separated columns:
        - id: node id
        - pid: id of parent node
        - p-answer: answer to the parent node's question
        - nodetype: question or task
        - value: the question for question nodes, list of comma-separated tasks for task nodes
    - second line gives root node, which must be a question node
    - all other lines are nodes which are descendents of the root node
"""

import Node


def read_file(fname):
    f = open(fname)
    f.readline()
    node_list = []
    for line in f.readlines():
        node_list.append(line.strip().split(";"))
        f.close()
    return node_list


def make_task_tree(node_list, print_tree=True):
    root_line = node_list[0]
    root = Node.QuestionNode(id=int(root_line[0]), question=root_line[4])

    for node_line in node_list[1:]:
        # node_line == [id, pid, p-answer, nodetype, value]
        parent = Node.get_node(root=root, id=int(node_line[1]))
        if node_line[3] == "question":
            child = parent.add_new_qchild(id=int(node_line[0]), answer=node_line[2], child_question=node_line[4])
        elif node_line[3] == "task":
            child = parent.add_new_tchild(id=int(node_line[0]), answer=node_line[2], child_tasks=node_line[4].split(","))
        else:
            raise ValueError(f"Must specify whether node is of type question or task (node {node_line[0]}, child of {node_line[1]})")
    
    if print_tree:
        Node.print_tree_neat(root)
    return root
    
    

if __name__ == "__main__":
    task_file = "tasks.txt"
    nodes = read_file(task_file)
    task_tree = make_task_tree(nodes, print_tree=True)
    # print(f"{Node.num_tasks(task_tree)} total tasks listed")