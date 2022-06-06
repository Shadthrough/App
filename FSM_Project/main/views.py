import os
import sys
from cgi import print_directory
from django.http import HttpResponse
from django.shortcuts import render
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

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
    line = request.POST.get('grammar') # ''.join(list(request.POST.values()))
    grammarFile = open('static/antlr/fsm.g4', 'w+')
    grammarFile.write(line)
    grammarFile.close()
    os.system('antlr4 -Dlanguage=Python3 .\static\\antlr\\fsm.g4')
    sys.path.append('.\static\\antlr')
    from fsmLexer import fsmLexer
    from fsmParser import fsmParser
    input = InputStream(input)
    lexer = fsmLexer(input)
    lexer.addErrorListener( MyErrorListener() )
    stream = CommonTokenStream(lexer)
    parser = fsmParser(stream)
    parser.addErrorListener( MyErrorListener() )

        # Java
    # os.system('cd C:\\Users\\maxim\\Desktop\\Subj\\Diplom\\App\\FSM_Project\\static\\antlr')
    # os.system('antlr4 .\static\\antlr\\fsm.g4') #antlr-3.3-complete.jar
    # os.system('javac .\static\\antlr\\*.java')
    # os.system(f'java org.antlr.v4.gui.TestRig fsm expr -tree {input}')
    # tree = parser.expr()
    # tree.toStringTree(parser)
    # print(Trees.inspect(tree, parser))

    # if (fsmParser.over):
    #     return HttpResponse('Rejected')

    # tree = parser.expr()
    try: # java org.antlr.v4.gui.TestRig fsm expr -tree .\test.txt > ast.dot
        tree = parser.expr()
    except:
        print('Rejected')
        return HttpResponse('Rejected')
    


    return HttpResponse('Accepted')

def index(request):
    return render(request, 'main/index.html')


# Create your views here.  
