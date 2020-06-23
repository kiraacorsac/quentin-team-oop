class DocumentWrapper:
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

def testDocumentWrapper():
  testfile = DocumentWrapper("testfile.txt")
  testfile += ["Hi!", "How are you?"]

#notice the file closing
testDocumentWrapper()
