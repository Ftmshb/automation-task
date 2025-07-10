# automation-task

# Task Sorting Automation Script

## What does this script do?

This Python script automates the process of organizing tasks based on their deadlines.  
It helps you input multiple tasks along with the number of days left until their deadlines,  
then sorts the tasks from the closest deadline to the farthest,  
and finally saves the sorted list into a text file with a clear and readable format.

## How does it work?

1. The script asks you how many tasks you want to enter.  
2. For each task, it prompts you to enter the task name and how many days are left until the deadline.  
3. After collecting all tasks, it sorts them in ascending order based on the days left.  
4. The sorted tasks are saved in a file called `sorted_tasks.txt` with headers for easy reading.

## How to run the script?

1. Make sure you have Python installed on your computer.  
2. Download or clone this repository.  
3. Open your terminal or command prompt and navigate to the folder containing the script.  
4. Run the following command:

   ```bash
   python automation_script.py


Example input:

How many tasks do you want to enter? 3

Task #1:
Enter the task name: by a milk
How many days are left until the deadline? 1

Task #2:
Enter the task name: do homework
How many days are left until the deadline? 7

Task #3:
Enter the task name: car wash
How many days are left until the deadline? 13


Exaple output:

Your Tasks
----------
Task:               Time Left:
-------------------------------
by a milk           1 day(s)
do homework         7 day(s)
car wash            13 day(s)
