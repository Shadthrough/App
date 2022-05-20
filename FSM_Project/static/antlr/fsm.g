grammar fsm;
options {language=Python;backtrack=true;}
start : '#' s1
| '2' s1
| '#' s0
| 'A' s0
| 'x' s0
;
s0 : '#' s1
| 'B' s1
;
s1 : '#' s2
| 'A' s2
;
s2 : '#' s1
| 'B' s1
;
