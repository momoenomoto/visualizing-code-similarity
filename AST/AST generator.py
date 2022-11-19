import ast
import astpretty

DEFAULT_INDENT = "  "

class CreateTuple():
    def __init__(self, name):
        self.text_file = open(name, "r")
        #read whole file to a string
        self.data = self.text_file.read()
        self.text_file.close()
        self.result = astpretty.pformat(ast.parse(self.data).body[0],indent='  ',show_offsets=False)
        self.all_tuples = []

    def generate_tuples(self, string = "", withIndentNum = 0, Parent = "start"):
        if (string == ""):
            string = self.result
        parsed = string.split("\n")
        if (len(parsed) == 1):
            return 
        for item in parsed:
            if (item == ""):
                continue
            if (start(item) == (DEFAULT_INDENT * (withIndentNum + 1))):
                child_block = self.checkChildBlock(item, withIndentNum + 1)
                if (child_block == None):
                    return
                self.generate_tuples(child_block, withIndentNum + 1, Parent = item.strip())
                self.all_tuples.append([Parent, item.strip()])
        

    def checkChildBlock(self, s, indentNum):

        parsed = self.result.split("\n")
        output = "\n"
        flag = False
        # print(indentNum)

        for item in parsed:
            if (flag):
                if (start(item) == (DEFAULT_INDENT * indentNum)):
                    flag = False
                    return output.strip()
                output = output + "\n" + item
            if (s == item):
                flag = True
                output = output + "\n" + item


def start(string):
    output = ""
    for i in range(len(string)):
        if (string[i] == " "):
            output += " "
        else :
            return output


def main():
    data = {}
    for i in range(1, 21):
        testcast = CreateTuple("{0}_SingleLL.py".format(i))
        testcast.generate_tuples()
        data[i] = testcast.all_tuples
        print(data)

main()


