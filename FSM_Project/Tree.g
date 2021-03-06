grammar Tree;

options
{
    language=Python3;
}

@members
{
    node_list   = []
    connections = []
    node_count  = 0

    def add_node(self, name):
        self.node_count += 1
        internal_name = "Node" + str(self.node_count)
        #print "Adding node", (internal_name, name)
        self.node_list.append((internal_name, '"' + name + '"'))
        return internal_name

    def connect(self, node1, node2):
        #print "Connection", node1, "->", node2
        self.connections.append( (node1, node2) )
}

fragment NUM      : '0'..'9';
fragment CHAR     : 'a'..'z' | 'A'..'Z';
fragment SPECIALS : ('_'|'-'|':'|'*'|'.'|'/');

WORD   : (CHAR|SPECIALS|NUM)*;
WS     : (' '|'\t'|'\n'|'\r')+ { self.skip(); } ;

/* Root */
tree_def : '(' tree_form ')';

/* A tree description is 
    - a WORD referencing the tree's head 
    - plus a set of subnodes of the tree
 */
tree_form returns [head=""]
      /* head is added as a node to our table. */
    : a=WORD { head = self.add_node($a.text)} 
      /* Additional subnodes are not added here (this is done in the subnode
         rule. Instead, we add a connection from our head to the node's new
         internal names (which come from the subnode).
       */
      ( b=subnode { self.connect(head, $b.node_name) }
      )*
    ;

/* A subnode is either a single WORD or INT token (then we add it as a node here
   and are done) or another subtree for which we then recurse.
 */
subnode returns [node_name]
        : b=WORD                  { print "1"; node_name = self.add_node($b.text) }
        | '(' tree_form ')'       { print "2"; node_name = $tree_form.head }
        ;
