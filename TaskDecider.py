import Node
import TaskReader


def choose_task(task_file):
    node_info_list = TaskReader.read_file(task_file)
    task_tree = TaskReader.make_task_tree(node_info_list, print_tree=False)

    node = task_tree
    print("Enter -1 at any point to see all tasks matching current criteria.")
    while isinstance(node, Node.QuestionNode):
        i = int(input(format_question(node)))   # TODO: input checking
        if i == -1:
            break
        node = node.get_child(i)
    tasks = Node.find_tasks(node)
    if tasks:
        print("Potential tasks:")
        for i in range(len(tasks)):
            print(f"  {i}) {tasks[i]}")
    else:
        print("No tasks match your criteria.")
        



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
