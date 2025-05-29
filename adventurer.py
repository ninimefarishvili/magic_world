from models import TaskQueue, Quest, Worker

def main():
    name = input("sheiyvane gmiris saxeli")
    worker = Worker(name)
    queue = TaskQueue()
    quest = queue.get_task()
    if quest:
        Worker.process_quest(quest)
    else :
        print("questi ar aris")


if __name__ == "__main__":
    main()