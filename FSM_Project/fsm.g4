grammar fsm;
@parser::members {
paths = []
}
expr: start;
start : '#' start
| '#' start {self.paths.append('-R>start')}
| EOF
| 'R' start {self.paths.append('-R>start')}
| '#' s0 {self.paths.append('-S>s0')}
| EOF
| 'S' s0 {self.paths.append('-S>s0')}
;
s0 : '#' s0
| '#' s0 {self.paths.append('-R>s0')}
| 'R' s0 {self.paths.append('-R>s0')}
| '#' start {self.paths.append('-A>start')}
| 'A' start {self.paths.append('-A>start')}
| 'S' s0 {self.paths.append('-S>s0')}
;
