import os
from prefect import task, flow
from prefect.transactions import transaction


@task
def write_file(contents: str):
    "Writes to a file."
    print(f"Writing to file: {contents}")
    with open("side-effect.txt", "w") as f:
        f.write(contents)


@write_file.on_rollback
def del_file(transaction):
    "Deletes file."
    print("Deleting file.")
    os.unlink("side-effect.txt")


@task
def quality_test():
    "Checks contents of file."
    with open("side-effect.txt", "r") as f:
        data = f.readlines()

    if len(data) < 2:
        raise ValueError("Not enough data!")


@flow(log_prints=True)
def pipeline(contents: str):
    with transaction():
        write_file(contents)
        quality_test()


if __name__ == "__main__":
    pipeline(contents="Hello, world!")
