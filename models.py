class Quest:
  def __init__(self, description):
    self.description = description

  def to_line(self):
    return self.description + "\n"

  @staticmethod
  def from_line(line):
    return Quest(line.strip())
