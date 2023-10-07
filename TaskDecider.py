import Node
import TaskReader


def choose_task(task_file):
    node_list = TaskReader.read_file(task_file)
    task_tree = TaskReader.make_task_tree(node_list, print_tree=False)

    node = task_tree
    while isinstance(node, Node.QuestionNode):
        i = int(input(format_question(node)))   # TODO: input checking
        node = node.get_child(i)
    tasks = "\n  " + "\n  ".join([task for task in node.get_tasks()])
    print(f"Potential tasks: {tasks}")
        



def format_question(qnode):
    if not isinstance(qnode, Node.QuestionNode):
        raise TypeError("Can only format question of a QuestionNode.")
    question = qnode.get_question()
    options = []
    answers = qnode.get_answers()
    for i in range(len(answers)):
        options.append(f"{i} for {answers[i]}")
    return question + " " + ", ".join(options) + ". >"


if __name__ == "__main__":
    choose_task("tasks.txt")
