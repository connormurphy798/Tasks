# Tasks

I'm often bored at home and can neither 1) think of activities that are available to me nor 2) actually get myself to do an activity once I think of it. This project helps me with both issues by keeping track of all of my tasks in an organized tree structure and helping me decide on ones to engage in.


## Task tree

The task tree is composed of two fundamental units: tasks and questions. Tasks are activities that I can partake in (e.g. cleaning the kitchen, reading a book), while questions help to narrow down the task space (e.g. Does the task involve leaving the house?, Is the task productive?).

Both tasks and questions are represented as nodes in the task tree. Internal nodes are of class `QuestionNode`. They represent a question, and their children are tasks or further questions that follow from particular answers to that question. Leaf nodes are of class `TaskNode`. They list a series of tasks consistent with all of the answers chosen so far.

Questions and tasks are stored in a `.txt` file in a specified format described in `TaskReader.py`; see `exampletasks.txt`.


## Functionality and examples

There are two primary ways of interacting with the task tree, enabled by the `TaskReader` and `TaskDecider` modules.

### TaskReader

`TaskReader` allows you to simply view all of your tasks in a tree structure. For instance:

```
Do you want to do something productive?
|-No:
|   Should the task involve leaving the house?
|   |-No:
|   |   0) play video games
|   |   1) read a book
|   |   2) find a movie to watch
|   |-Yes:
|       Inside or outside?
|       |-Inside:
|       |   0) see a movie
|       |   1) go to a coffee shop
|       |-Outside:
|           0) go for a walk
|           1) go to the river
|-Yes:
     Real or fake productive (i.e. needs to get done vs. would be good to do)?
     |-Real:
     |   Primarily physical or thinking-based?
     |   |-Physical:
     |   |   0) clean bathroom
     |   |   1) run errands
     |   |   2) clean mildred's litter
     |   |-Thinking:
     |       0) budgeting
     |       1) studying/classwork
     |       2) make that doctor's/dentist appointment
     |-Fake:
         0) devise a new programming project
         1) exercise
         2) pick a subject and learn about it
```

### TaskDecider

Alternatively, `TaskDecider` will prompt you with a series of questions and use your answers to help you decide on a task that fits your current desires. For instance, here is one path down the above tree:

```
Enter -1 at any point to see all tasks matching current criteria.
Do you want to do something productive? 0 for No, 1 for Yes. >1
Real or fake productive (i.e. needs to get done vs. would be good to do)? 0 for Real, 1 for Fake. >0
Primarily physical or thinking-based? 0 for Physical, 1 for Thinking. >0
Input 0 to list all tasks matching your criteria, or 1 to pick a random one. >0
Potential tasks:
  0) clean bathroom
  1) run errands
  2) clean mildred's litter
```
