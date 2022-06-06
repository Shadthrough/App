grammar fsm;
expr: start;
start : '#' start
| '#' s6
| '3' s6
| '#' s0
| 'x' s0
| '#' s3
| 'A' s3
| '#' s5
| 'l' s5
| '#' s4
| 'r' s4
;
s0 : '#' s0
| '#' s1
| 'B' s1
;
s1 : '#' s1
| '#' s8
| '3' s8
| '#' s2
| 'A' s2
;
s2 : '#' s2
| '#' s1
| 'B' s1
;
s3 : '#' s3
| '#' s0
| 'x' s0
;
s4 : '#' s4
| '#' s5
| EOF
| 'l' s5
;
s5 : '#' s5
| '#' s5
| 'r' s5
;
s6 : '#' s6
| '#' s0
| '3' s0
;
s7 : '#' s7
| '#' s0
| '3' s0
;
s8 : '#' s8
| EOF
;