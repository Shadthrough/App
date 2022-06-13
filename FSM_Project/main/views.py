import os
import sys
from cgi import print_directory
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
# from pygrun import 

class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        raise Exception("Oh no!!")

    # def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
    #     raise Exception("Oh no!!")

    # def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    #     raise Exception("Oh no!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("Oh no!!")


def antlr(request):

    input = request.POST.get('input').replace('*', '#' * (int(request.POST.get('states')) - 1))
    print(input)
    inputFile = open('test.txt', 'w+')
    inputFile.write(input)
    inputFile.close()
    line = request.POST.get('grammar') # ''.join(list(request.POST.values()))
    grammarFile = open('fsm.g4', 'w+')
    grammarFile.write(line)
    grammarFile.close()
    os.system('antlr4 -Dlanguage=Python3 .\\fsm.g4')
    # sys.path.append('.\static\\antlr')
    from fsmLexer import fsmLexer
    from fsmParser import fsmParser
    # from fsmListener import fsmListener
    input = InputStream(input)
    lexer = fsmLexer(input)
    lexer.addErrorListener( MyErrorListener() )
    stream = CommonTokenStream(lexer)
    parser = fsmParser(stream)
    parser.addErrorListener( MyErrorListener() )

        # Java
    os.system('antlr4 .\\fsm.g4') #antlr-3.3-complete.jar
    os.system('javac .\\*.java')
    os.system(f'java org.antlr.v4.gui.TestRig fsm expr -gui .\\test.txt')
    with open('.\\antlr4_parse_tree.svg', "r") as f:
        svg = f.read()
    # tree = parser.expr()
    # tree.toStringTree(parser)
    # print(Trees.inspect(tree, parser))

    # if (fsmParser.over):
    #     return HttpResponse('Rejected')

    # tree = parser.expr()
    # print(tree.toString())

    os.system('python .\\pygrun.py fsm expr -t .\\test.txt > output.txt')
    with open("output.txt", "r") as f:
        data = f.read()
    # os.system(f'python .\\Tree2Dot.py "{data}" > dot.txt')
    try: # java org.antlr.v4.gui.TestRig fsm expr -tree .\test.txt > ast.dot
        parser.buildParseTrees = True
        tree = parser.expr()
        # parser.paths.reverse()
        # print(parser.paths)
    except:
        print('Rejected')
        # print(parser.paths)
        return HttpResponse([f'Rejected|{svg}'])
    


    return HttpResponse(f'Accepted|{svg}')

def index(request):
    return render(request, 'main/index.html')


# Create your views here.  
