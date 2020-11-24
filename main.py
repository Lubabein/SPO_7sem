from lexer import Lexer
from pars import Parser
from transfer_to_pn import PN
from stack_machine import stack_machine
from triad_processing import Triad

f = open('test5.txt')
inp = f.read()
f.close()

print('\nlexer:')
l = Lexer()
tokens = l.lex(inp)

p = Parser(tokens)
pars = p.lang()
print('\nparser:', pars)

if pars:
    pn = PN(tokens)
    transfer, fun = pn.transfer_PN()

    tr = Triad(transfer, fun)
    t, val = tr.triad_op()

    for i in range(len(fun)):
        print("\nFunctions triads processing:")
        triad = Triad(fun[i][-1], fun)
        fun[i][-1] = triad.triad_op(False)

    print('\nstack machine:')
    sm = stack_machine(t, val, fun)
    sm.stack_machine_run()