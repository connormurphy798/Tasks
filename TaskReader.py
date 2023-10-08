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
        - need not be in order, i.e. if node A descends from node B, A and B can appear in any order in the file
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

    trees = []  # list of tuples (node, pid, answer)
    for node_line in node_list[1:]: # node_line == [id, pid, p-answer, nodetype, value]
        id  = int(node_line[0])
        pid = int(node_line[1]) 

        # create new node
        if node_line[3] == "question":
            new_node = Node.QuestionNode(id=id, question=node_line[4])
        elif node_line[3] == "task":
            new_node = Node.TaskNode(id=id, tasks=node_line[4].split(","))
        else:
            raise ValueError(f"Must specify whether node is of type question or task (node {node_line[0]}, child of {node_line[1]})")
        
        # attempt to add to existing tree
        parent = Node.get_node(root=root, id=pid)
        if parent:
            parent.add_existing_child(child=new_node, answer=node_line[2])
        else:
            trees.append((new_node, pid, node_line[2]))

    # go back and try to add any unconnected nodes
    while trees:
        to_remove = -1
        for i in range(len(trees)):
            node, pid, answer = trees[i]
            parent = Node.get_node(root=root, id=pid)
            if parent:
                parent.add_existing_child(child=node, answer=answer)
                to_remove = i
                break
        if to_remove == -1:
            raise ValueError(f"Node(s) without parent present in file, (node, pid, answer): {trees}")
        trees.pop(i)
    
    if print_tree:
        Node.print_tree_neat(root)
    return root
    
    

if __name__ == "__main__":
    task_file = "tasks.txt"
    nodes = read_file(task_file)
    task_tree = make_task_tree(nodes, print_tree=True)
    # print(f"{Node.num_tasks(task_tree)} total tasks listed")