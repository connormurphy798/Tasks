"""
Handles creation of a tree from a text file of tasks.

task file formatting requirements:
    - first line gives description of semicolon-separated columns:
        - id: node id
        - pid: id of parent node
        - p-answer: answer to the parent node's question
        - nodetype: question or task
        - question: the question for question nodes, '_' for task nodes
        - tasks: '_' for question nodes, a list of plus-sign-separated tasks for task nodes
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
        # node_line == [id, pid, p-answer, nodetype, question, tasks]
        parent = Node.get_node(root=root, id=int(node_line[1]))
        if node_line[3] == "question":
            parent.add_qchild(id=int(node_line[0]), answer=node_line[2], child_question=node_line[4])
        elif node_line[3] == "task":
            parent.add_tchild(id=int(node_line[0]), answer=node_line[2], child_tasks=node_line[5].split(","))
    
    if print_tree:
        Node.print_qt(root)
    return root
    
    

if __name__ == "__main__":
    task_file = "tasks.txt"
    nodes = read_file(task_file)
    make_task_tree(nodes, print_tree=True)