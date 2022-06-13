#!/usr/bin/python

# This script parses a string representation of an ANTLR tree and
# translates it into GraphViz' Dot language so that you can visualize
# this as a DAG with the dot tool.

from antlr4 import *
from TreeParser import TreeParser
from TreeLexer import TreeLexer
import sys

def evaluateTree(string):
   if not string[-1] == '\n': string += "\n"
   lex = TreeLexer(InputStream(string))
   tokens = CommonTokenStream(lex)
   parser = TreeParser(tokens)
   parser.tree_def()
   return parser.node_list, parser.connections

def usage():
    print ("Usage: Tree2Dot  <string>")

def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    string = sys.argv[1]

    # Graph header
#    print ("/* Original string: '%s' */" % string)
    print ("digraph g {")
    print ("\tnode [color=lightblue2, style=filled];")

#    string = string.replace("/", "\/")
    # Now we go parsing. Evaluate() returns us a list of nodes and
    # a list of connections.
    nodes, connections = evaluateTree(string)

    # print (nodes)
    for (node, label) in nodes :
        print ("\t", node, "[", "label =", label, "];")
    # print (connections)
    for (n1, n2) in connections:
        print ("\t", n1, "->", n2, ";")

    # Graph footer
    print ("}")

main()
