grammar fsm;
options {language=Python3;output=AST;}

expr: start;
start : '#' s0
| '#' start
| 'A' s0
| 'x' s0
;
s0 : '#' s1
| '#' s0
| 'B' s1
;
s1 : '#' s2
| '#' s1
| EOF
| 'A' s2
;
s2 : '#' s1
| '#' s2
| 'B' s1
;
