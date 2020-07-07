class __DocumentWrapper:
  def __init__(self, name):
    print("Opening file")
    self.name = name
    self.file_mode = "a"
    try:
      self._file  = open(name, self.file_mode)
      self._file_open = True
    except OSError as e:
      self._file_open = False
      print(e)

  # +=
  def __iadd__(self, text):
    self._file.writelines([text, "\n"])

  def __del__(self):
    print("Close")
    if(self._file_open):
      self._file.close()
    else:
      print("Nothing to close...")


class _BasicLoggerImplementation(__DocumentWrapper):
  def __init__(self):
    super().__init__("logLesson.txt")

class BasicLogger():


  __instance = None

  def __new__(cls):
    if BasicLogger.__instance is None:
      BasicLogger.__instance = _BasicLoggerImplementation()
    return BasicLogger.__instance


logger = BasicLogger()
logger2 = BasicLogger()

print(logger == logger2)