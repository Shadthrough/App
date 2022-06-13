grammar fsm;
expr: start;
start : '#' start
| '#' s0 
| 'A' s0 
| 'x' s0 
;
s0 : '#' s0
| '#' s1 
| 'B' s1 
;
s1 : '#' s1
| '#' s2 
| EOF
| 'A' s2 
;
s2 : '#' s2
| '#' s1 
| 'B' s1 
;
