grammar fsm;
@parser::members {
paths = []
}
expr: start;
start : '#' start
| '#' s0 {self.paths.append('-A>s0')}
| 'A' s0 {self.paths.append('-A>s0')}
| 'x' s0 {self.paths.append('-x>s0')}
;
s0 : '#' s0
| '#' s1 {self.paths.append('-B>s1')}
| 'B' s1 {self.paths.append('-B>s1')}
;
s1 : '#' s1
| '#' s2 {self.paths.append('-A>s2')}
| EOF
| 'A' s2 {self.paths.append('-A>s2')}
;
s2 : '#' s2
| '#' s1 {self.paths.append('-B>s1')}
| 'B' s1 {self.paths.append('-B>s1')}
;
