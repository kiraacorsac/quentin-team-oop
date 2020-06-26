# f = open("log.txt", "w")
# f.writelines(["hello"])
# f.close()


# with open("log.txt", "w") as f:
#   f.writelines(["hello"])

class DocumentWrapper():
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



def testDocumentWrapper():
  document = DocumentWrapper("log5.txt")
  document += "Hello world!"

print("Starting script...")
testDocumentWrapper()
print("After calling the function...")
testDocumentWrapper()
print("After calling the function second time...")