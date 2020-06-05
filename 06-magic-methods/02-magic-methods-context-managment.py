class DocumentWrapper:
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


def testDocumentWrapper():
  testfile = DocumentWrapper("testfile.txt")
  testfile.lines = ["Hi!", "How are you?"]
  testfile.lines += ["- Good!", "- And how are you?"]

#notice the file closing
testDocumentWrapper()
