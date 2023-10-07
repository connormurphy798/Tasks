"""
Logic for implementing a tree of questions and tasks.
"""


import Utils as U   
    

class Node():
    def __init__(self, id):
        self.id = id


    def get_id(self):
        return self.id


class QuestionNode(Node):
    def __init__(self, id, question=""):
        self.id = id
        self.question = question
        self.children = []
        self.answers = []   # parallel list with children, denoting what answer each child corresponds to
    

    def add_qchild(self, id, answer="", child_question="", i=None):
        child = QuestionNode(id=id, question=child_question)
        if not i or i >= len(self.children):
            self.children.append(child)
            self.answers.append(answer)
        else:
            self.children.insert(i, child)
            self.answers.insert(i, answer)
        return child
    

    def add_tchild(self, id, answer="", child_tasks=[],  i=None):
        child = TaskNode(id=id, tasks=child_tasks)
        if not i or i >= len(self.children):
            self.children.append(child)
            self.answers.append(answer)
        else:
            self.children.insert(i, child)
            self.answers.insert(i, answer)
        return child
    

    def get_chilren(self):
        return self.children


    def get_child(self, i):
        try:
            return self.children[i]
        except IndexError:
            raise IndexError(f"Node {self.id} has no {U.ordinal(i)} child.")
    

    def num_children(self):
        return len(self.children)


    def get_answers(self):
        return self.answers
    

    def get_answer(self, i):
        try:
            return self.answers[i]
        except IndexError:
            raise IndexError(f"Node {self.id} has no {U.ordinal(i)} answer.")


    def set_question(self, question):
        self.question = question
    

    def get_question(self):
        return self.question
    

    def __str__(self):
        return f"<QNode {self.id}: {self.question} ({len(self.children)} children)>"
        

class TaskNode(Node):
    def __init__(self, id, tasks=[]):
        self.id = id
        self.tasks = tasks
    

    def add_task(self, task):
        self.tasks.append(task)
    

    def insert_task(self, task, i):
        self.tasks.insert(i, task)
    

    def remove_task(self, i):
        if type(i) == int:
            self.tasks.remove(i)
        elif type(i) == str:
            for j in range(len(self.tasks)):
                if self.tasks[j] == i:
                    self.tasks.remove(j)
        else:
            raise TypeError("Must specify an index (int) or task (str) to be removed.")

    
    def get_tasks(self):
        return self.tasks
    

    def __str__(self):
        return f"<TNode {self.id}: {self.tasks})>"


def get_node(root, id):
    """
    gets a descendent of root whose id is id,
    returns None if no such descendent is found
    """
    if isinstance(root, Node):
        if root.get_id() == id:
            return root
        if isinstance(root, QuestionNode):
            for child in root.get_chilren():
                node = get_node(child, id)
                if node:
                    return node
        return None
    raise TypeError("Root must be of type Node")



def traverse(node, v=False, indents = 0, ind=" "*2):
    """
    counts the number of nodes in the tree
    """
    if isinstance(node, QuestionNode):
        if v:
            print(f"{ind*indents}{node.__str__()}")
        ret = 1
        children = node.get_chilren()
        if children:
            for child in range(len(children)):
                if v:
                    print(f"{ind*(indents+1)}{node.get_answer(child)}:")
                ret += traverse(children[child], v=v, indents=indents+2, ind=ind)
        return ret
    if isinstance(node, TaskNode):
        if v:
            print(f"{ind*indents}{node.__str__()}")
        return 1


def print_qt(node, indents = 0, ind=" "*2):
    if isinstance(node, QuestionNode):
        print(f"{ind*indents}{node.get_question()}")
        ret = 1
        children = node.get_chilren()
        if children:
            for child in range(len(children)):
                print(f"{ind*(indents+1)}{node.get_answer(child)}:")
                ret += print_qt(children[child], indents=indents+2, ind=ind)
        return ret
    if isinstance(node, TaskNode):
        print(f"{ind*indents}{node.get_tasks()}")
        return 1