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
    

    def add_existing_child(self, child, answer="", i=None):
        if not i or i >= len(self.children):
            self.children.append(child)
            self.answers.append(answer)
        else:
            self.children.insert(i, child)
            self.answers.insert(i, answer)
        return child


    def add_new_qchild(self, id, answer="", child_question="", i=None):
        child = QuestionNode(id=id, question=child_question)
        return self.add_existing_child(child=child, answer=answer, i=i)
    

    def add_new_tchild(self, id, answer="", child_tasks=[],  i=None):
        child = TaskNode(id=id, tasks=child_tasks)
        return self.add_existing_child(child=child, answer=answer, i=i)
    

    def get_children(self):
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
            for child in root.get_children():
                node = get_node(child, id)
                if node:
                    return node
        return None
    raise TypeError("Root must be of type Node")


def traverse(root, v=False, indents = 0, ind=" "*2):
    """
    counts the number of nodes in the tree starting at root
    """
    if isinstance(root, QuestionNode):
        if v:
            print(f"{ind*indents}{root.__str__()}")
        ret = 1
        children = root.get_children()
        if children:
            for child in range(len(children)):
                if v:
                    print(f"{ind*(indents+1)}{root.get_answer(child)}:")
                ret += traverse(children[child], v=v, indents=indents+2, ind=ind)
        return ret
    if isinstance(root, TaskNode):
        if v:
            print(f"{ind*indents}{root.__str__()}")
        return 1


def print_tree(root, indents = 0, ind=" "*2):
    if isinstance(root, QuestionNode):
        print(f"{ind*indents}{root.get_question()}")
        children = root.get_children()
        if children:
            for child in range(len(children)):
                print(f"{ind*(indents+1)}{root.get_answer(child)}:")
                print_tree(children[child], indents=indents+2, ind=ind)
    if isinstance(root, TaskNode):
        tasks = root.get_tasks()
        for i in range(len(tasks)):
            print(f"{ind*indents}{i}) {tasks[i]}")


def print_tree_neat(root, prefix=""):
    if isinstance(root, QuestionNode):
        print(f"{prefix}{root.get_question()}")
        children = root.get_children()
        if children:
            for child in range(len(children)):
                print(f"{prefix}|-{root.get_answer(child)}:")
                if child < len(children)-1:
                    print_tree_neat(children[child], prefix+"|   ")
                else:
                    print_tree_neat(children[child], prefix+"    ")
    if isinstance(root, TaskNode):
        tasks = root.get_tasks()
        for i in range(len(tasks)):
            print(f"{prefix}{i}) {tasks[i]}")


def find_tasks(root):
    if isinstance(root, QuestionNode):
        ret = []
        for child in root.get_children():
            ret.extend(find_tasks(child))
        return ret
    if isinstance(root, TaskNode):
        return root.get_tasks()
    raise TypeError("root must be a QuestionNode or TaskNode.")


def num_tasks(root):
    if isinstance(root, QuestionNode):
        return sum([num_tasks(child) for child in root.get_children()])
    if isinstance(root, TaskNode):
        return len(root.get_tasks())
    raise TypeError("root must be a QuestionNode or TaskNode.")


def get_tree_ids(root):
    ret = [root.get_id()]
    if isinstance(root, QuestionNode):
        for child in root.get_children():
            ret.extend(get_tree_ids(child))
        return ret
    elif isinstance(root, TaskNode):
        return ret
    else:
        raise TypeError("Root must be of Node type")
