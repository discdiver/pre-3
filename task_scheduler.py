from task_worker import my_background_task

if __name__ == "__main__":
    my_background_task.delay("Ford")
    my_background_task.delay("Prefect")
    my_background_task.delay("Slartibartfast")
