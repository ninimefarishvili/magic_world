class Quest:
  def __init__(self, description):
    self.description = description

  def to_line(self):
    return self.description + "\n"

  @staticmethod
  def from_line(line):
    return Quest(line.strip())


class TaskQueue:
  def __init__(self, filename = queue.txt):
    self.filename = filename

  def add_task(self, quest):
    with open (self.filename, "a") as f:
      f.write(quest.to_line())

  def get_task(self):
    with open (self.filename, "r") as f:
      lines = f.readlines()

import random
class Worker:
  def __init__(self, name):
    self.name = name

  def process_quest(self, quest):
    print(quest.description)
    success = random.random() < 0.8

    if success:
      print(f"{self.name} warmatebit shesrulda questi")

    else:
      print(f"{self.name} ver shesrulda questi")
