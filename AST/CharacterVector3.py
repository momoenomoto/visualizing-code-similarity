import ast
import astpretty

DEFAULT_INDENT = "  "

DEFAULT_LENGTH = 600
DEFAULT_LENGTH_COM = 920

# a Character List that allows dynamic appending
class CharacterList:
    def __init__(self): 
        self.list = []
        self.length = 0
        self.charToNum = {}
        self.numToChar = {}

    def addCharacter(self, s):
        self.list.append(s)
        self.charToNum[s] = self.length
        self.numToChar[self.length] = s
        self.length += 1

### form the CharacterList

characterList = CharacterList()
characterList2 = CharacterList()


class TreeNode:
    def __init__(self, content): 
        self.content = content
        self.children = []
        self.checked = False
        self.characterVector = [0] * DEFAULT_LENGTH
        self.totalCharactorVector = [0] * DEFAULT_LENGTH
        self.num = 0

    def addChild(self, t):
        self.children.append(t)
    

    def detect(self):
        if self.content in characterList.list:
            self.characterVector[characterList.charToNum[self.content]] += 1
        else:
            characterList.addCharacter(self.content)
            self.characterVector[characterList.charToNum[self.content]] += 1


            
    def calculate(self):
        # print("character" + str(self.totalCharactorVector))
        if self.checked:
            return self.totalCharactorVector
        else:
            self.add(self.characterVector)

            for child in self.children:
                # print("calculate" + str(child.calculate()))
                self.add(child.calculate())
            self.checked = True
            return self.totalCharactorVector
 
    def add(self, l):
        # print("l", l)
        for i in range(DEFAULT_LENGTH):
            self.totalCharactorVector[i] = self.totalCharactorVector[i] + l[i]

class CreateTuple():
    def __init__(self, name):
        self.text_file = open(name, "r")
        #read whole file to a string
        self.data = self.text_file.read()
        self.text_file.close()
        self.result = astpretty.pformat(ast.parse(self.data).body[0],indent = DEFAULT_INDENT,show_offsets=False)
        # print(self.result)
        self.all_tuples = []
        self.parsed = self.result.split("\n")

    def generate_tuples(self, parsed = [], withIndentNum = 0, parent = ""):
        if (parsed == []):
            parsed = self.result.split("\n")
        next_round_parsed = []
        currentNode = None
        for item in parsed:
            # print(item)
            if (self.start(item) == DEFAULT_INDENT * withIndentNum):
                if (next_round_parsed == []):
                    if (item.strip().startswith("value=Constant") and (parent.content == "ex")):
                        continue
                    if (deal_with_item(item.strip())):
                        currentNode = TreeNode(deal_with_item(item.strip()))
                        currentNode.detect()
                        # print(currentNode.characterVector)
                        parent.addChild(currentNode)
                else:
                    self.generate_tuples(next_round_parsed, withIndentNum + 1, currentNode)
                    next_round_parsed = []
                    if (item.strip().startswith("value=Constant") and (parent.content == "ex")):
                        continue
                    if (deal_with_item(item.strip())):
                        currentNode = TreeNode(deal_with_item(item.strip()))
                        parent.addChild(currentNode)
            else:
                # print(next_round_parsed)
                next_round_parsed.append(item)

    def start(self, string):
        output = ""
        for i in range(len(string)):
            if (string[i] == " "):
                output += " "
            else :
                return output

def deal_with_item(item):

    # clean data
    if item in ["],", "),", ")", "ctx=Store(),", "ctx=Load(),", "returns=None,"]:
        return
    elif item.endswith("=[],"):
        return
    elif item.endswith("=None,"):
        return
    # simplify expression
    elif item == "ClassDef(":
        return "c"
    elif item == "body=[":
        return "b"
    elif item == "FunctionDef(":
        return "f"
    elif item == "Expr(":
        return "ex"
    elif item == "args=arguments(":
        return "aar"
    elif item == "Assign(":
        return "A"
    elif item == "args=[":
        return "args"
    elif item == "Attribute(":
        return "At"
    elif item == "targets=[":
        return "t"
    elif item == "Tuple(":
        return "tu"
    elif item == "AugAssign(":
        return "aua"
    elif item.startswith("name="):
        return "n"
    elif "attr=" in item:
        return item.replace("attr=", "").replace("'","")
    elif item.startswith("value=Constant"):
        return valueConstant(item)

    elif item.startswith("arg(arg=") or item.startswith("args=[arg(arg"):
        return arg(item)

    elif item.startswith("value=Name"):
        return value(item)
    elif item.startswith("left=Name"):
        return leftName(item)
    elif item.startswith("target=Name(") or item.startswith("targets=[Name("):
        return target(item)

    else:
        return item

    
def leftName(item):
    item = item.replace("left=Name(", "")
    item_list = item.split(",")
    for i in item_list:
        if "id=" in i:
            return i.replace("id=", "").replace("'", "")

def target(item):
    item = item.replace("target=Name(", "")
    item_list = item.split(",")
    for i in item_list:
        if "id=" in i:
            return i.replace("id=", "").replace("'", "")

def valueConstant(item):
    item = item.replace("value=Constant(", "").replace("targets=[Name(", "")
    item_list = item.split(",")
    for i in item_list:
        if "value=" in i:
            return i.replace("value=", "").replace("'", "")

def value(item):
    item = item.replace("value=Name(", "")
    item_list = item.split(",")
    for i in item_list:
        if "id=" in i:
            return i.replace("id=", "").replace("'", "")

def arg(item):
    item = item.replace("args=[arg(", "").replace("arg(", "")
    item_list = item.split(",")
    for i in item_list:
        if "arg=" in i:
            return i.replace("arg=", "").replace("'", "")

def prettyPrint(node, all_list = [], all_collection = []):
    if node.children == []:
        return
    else:
        for child in node.children:
            if (node.content != "b" and child.content != "ex"):
                combination = node.content + child.content
                all_list.append([node.content + child.content])
                if combination in characterList2.list:
                    all_collection[characterList2.charToNum[combination]] += 1
                else:
                    # print(characterList2.list)
                    # print(characterList2.charToNum)
                    characterList2.addCharacter(combination)
                    all_collection[characterList2.charToNum[combination]] = 1
        for child in node.children:
            prettyPrint(child, all_list, all_collection)

def printCharacter(node):
    return node.totalCharactorVector

def main():
    # testcast = CreateTuple("{0}_SingleLL.py".format(1))
    # root_Node = TreeNode("start")
    # testcast.generate_tuples(parent = root_Node)
    # result = []
    # prettyPrint(root_Node, result)
    # print(result)
    # print(len(result))
    # print("While" in testcast.all_tuples)

    # data is the original tuple of lists
    # data2 is the collection that represents the num
    # data3 is the collection that represents the output
    data = {}
    data2 = {}
    data3 = {}
    # test_dataset_2/{0}_DP.py
    # test_dataset_3/sums_{0}.py
    # test_dataset_1/{0}_SingleLL.py
    for i in range(1, 21):
        testcast = CreateTuple("test_dataset_3/sums_{0}.py".format(i))
        root_Node = TreeNode("start")
        root_Node.detect()
        testcast.generate_tuples(parent = root_Node)

        result = []
        result1 = [0] * DEFAULT_LENGTH_COM
        root_Node.calculate()
        prettyPrint(root_Node, result, result1)
        # print(len(result))
        data[i] = result
        data2[i] = printCharacter(root_Node)
        data3[i] = result1
        # print(root_Node.children)
        print(data3)
        # print(root_Node.characterVector)
        # print(characterList.list)
        # print(result)
        # print(data)
    print(characterList.list)

main()