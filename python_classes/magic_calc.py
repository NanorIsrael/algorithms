Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:


LOAD_CONST               1 (0)
STORE_FAST               2 (result)

SETUP_LOOP              94 (to 103)
LOAD_GLOBAL              0 (range)
LOAD_CONST               2 (1)
LOAD_CONST               3 (3)
CALL_FUNCTION            2 (2 positional, 0 keyword pair)
GET_ITER
FOR_ITER                77 (to 102)
STORE_FAST               3 (i)

SETUP_EXCEPT            49 (to 80)

LOAD_FAST                3 (i)
LOAD_FAST                0 (a)
COMPARE_OP               4 (>)
POP_JUMP_IF_FALSE       58

LOAD_GLOBAL              1 (Exception)
LOAD_CONST               4 ('Too far')
CALL_FUNCTION            1 (1 positional, 0 keyword pair)
RAISE_VARARGS            1
JUMP_FORWARD            18 (to 76)

58 LOAD_FAST                2 (result)
61 LOAD_FAST                0 (a)
64 LOAD_FAST                1 (b)
BINARY_POWER
LOAD_FAST                3 (i)
BINARY_TRUE_DIVIDE
INPLACE_ADD
STORE_FAST               2 (result)
POP_BLOCK
JUMP_ABSOLUTE           22

POP_TOP
POP_TOP
POP_TOP

LOAD_FAST                1 (b)
LOAD_FAST                0 (a)
BINARY_ADD
STORE_FAST               2 (result)

BREAK_LOOP
POP_EXCEPT
JUMP_ABSOLUTE           22
END_FINALLY
JUMP_ABSOLUTE           22
POP_BLOCK

LOAD_FAST                2 (result)
RETURN_VALUE