class _DocumentWrapper:
  def __init__(self, filepath):
    print("Open")
    self.__file = open(filepath, "w+")

  @property
  def lines(self):
    return self.__file.readlines()

  def __del__(self):
    print("Close")
    self.__file.close()

  def __iadd__(self, lines):
    print("Write")
    
    separated_lines = []
    for line in lines:
      separated_lines.append(line + "\n")

    self.__file.writelines(separated_lines)

class _BasicLogger(_DocumentWrapper):
  def __init__(self):
    # set output file maybe from settings?
    super().__init__("log.txt")

class Logger:
  '''
  This class implements the singleton pattern, together with _Logger
  '''
  __instance = None

  def __new__(cls, logger_type):
      if cls.__instance is None:
          cls.__instance = _BasicLogger() 
      return cls.__instance

l = Logger()
l += ["Captain's log."]