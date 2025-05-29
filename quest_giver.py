from models import Quest, Worker, TaskQueue

def main():
    description = input("sheiyvane questis agwera:")
    quest = Quest(description)
    queue = TaskQueue()
    queue.add_task(quest)
    return "warmatebit daemata"

if __name__ == "__main__":
    main()