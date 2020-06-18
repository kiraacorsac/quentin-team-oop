class _DocumentWrapper:
  def __init__(self, filepath):
    self.__file = open(filepath, "w+")

  @property
  def lines(self):
    return self.__file.readlines()

  @lines.setter
  def lines(self, lines):
    separated_lines = []
    for line in lines:
      separated_lines.append(line + "\n")

    self.__file.writelines(separated_lines)

  def __del__(self):
    self.__file.close()

class _Logger(_DocumentWrapper):
  def __init__(self):
    super().__init__("log.txt")

  def log(self, message):
    self.lines += [message]

class Logger:
  '''
  This class implements the singleton pattern, together with _Logger
  '''
  __instance = None

  def __new__(cls):
      if cls.__instance is None:
          cls.__instance = _Logger() 
      return cls.__instance