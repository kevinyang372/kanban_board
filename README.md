# Flask Kanban Board
Simple Flask Kanban Board for managing your to-do list

## Features

![image](https://user-images.githubusercontent.com/30107576/54415484-69bd8900-4722-11e9-96e1-f5238c156a7a.png)

- Deletion and addition of new tasks
- Switch tasks between three categories: to-do, doing and done
- Color coding of overdue tasks (red)

![image](https://user-images.githubusercontent.com/30107576/54416012-1ba98500-4724-11e9-9573-b86910db5836.png)

- Calendar showing the due date of each task
- Drag and Drop tasks to change its due date
- Color coding of different task categories (blue: to-do, red: doing, green: done)

## Installation

Install necessary dependencies

    $ pip install -r requirements.txt

Start flask server

    $ python routes.py

Your Kanban board should be up and running at http://127.0.0.1:5000/

## Unit Testing

On the project root directory, run

    $ python test_basic.py
