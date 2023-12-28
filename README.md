# Mini-LISP-lexer-and-parser
Simplified LISP lexer and parser.

## Description
> Note: Please, if you can do it on your own, it'll be great. 
> I know it's very boring.
> However, copy-pasting isn't going to bring you anywhere.
> This may be your last time writing a "compiler" (well, this project doesn't really count).
> Why not try it yourself?
> It's still a project. You can still learn a lot from it.
> May you pass the class with flying colors.

This project contains two main files, a lexer and a parser.
The lexer generates tokens from an input stream, and the parser goes through the tokens. At the end, the parser returns a list which contains the results.

For simplicity, the lexical details and the grammar is modified.
(The lexical details and the grammar will be covered in the following sections)


## Lexical Details & Grammar
### Lexical Details
- Preliminary Definitions
    - number    ::= 0|(-?[1-9][0-9]*)
    - ID        ::= [a-zA-Z][a-zA-Z0-9-]*
    - bool_val  ::= #t|#f
    - separator ::= [\t\n\r ]+

- Numerical Operators
    - PLUS      ::= \+
    - MINUS     ::= -
    - MULTIPLY  ::= \*
    - DIVIDE    ::= /
    - MODULUS   ::= mod
    - GREATER   ::= >
    - SMALLER   ::= <
    - EQUAL     ::= =

- Logical Operators
    - AND       ::= and
    - OR        ::= or
    - NOT       ::= not

- Other:
    - LPAREN    ::= \(
    - RPAREN    ::= \)

- Reserved Words
    - PRINT_NUM ::= print-num
    - PRINT_BOOL::= print-bool
    - DEFINE    ::= define
    - IF        ::= if
    - FUN       ::= fun

> All operators are reserved words, such as 'mod', 'and', etc.


### Grammar Overview
    PROGRAM     : STMTS
    
    STMTS       : STMT STMTS
    
    STMT        : EXP
                | DEF_STMT
                | PRINT_STMT
    
    PRINT_STMT  : LPAREN PRINT_NUM EXP RPAREN'
                | LPAREN PRINT_BOOL EXP RPAREN'

    EXPS        : EXP EXPS
                | ;

    EXP         : bool_val
                | number
                | VARIABLE
                | NUM_OP
                | LOGIC_OP
                | IF_EXP
                | FUN_EXP
                | FUN_CALL

    VARIABLE    : ID
    
    NUM_OP      : LPAREN PLUS EXP EXP EXPS RPAREN
                | LPAREN MINUS EXP EXP RPAREN
                | LPAREN MULTIPLY EXP EXP EXPS RPAREN
                | LPAREN DIVIDE EXP EXP RPAREN
                | LPAREN MODULUS EXP EXP RPAREN
                | LPAREN GREATER EXP EXP RPAREN
                | LPAREN SMALLER EXP EXP RPAREN
                | LPAREN EQUAL EXP EXP EXPS RPAREN

    LOGIC_OP    : LPAREN AND EXP EXP EXPS RPAREN
                | LPAREN OR EXP EXP EXPS RPAREN
                | LPAREN NOT EXP RPAREN

    FUN_EXP     : LPAREN FUN FUN_IDS FUN_BODY RPAREN

    FUN_IDS     : LPAREN IDS RPAREN

    IDS         : ID IDS
                | empty

    FUN_BODY    : number
                | bool_val
                | FUN_VAR
                | LPAREN OP OPERANDS RPAREN

    OPERANDS    : FUN_BODY OPERANDS
                | empty

    FUN_VAR     : ID

    OP          : PLUS
                | MINUS
                | MULTIPLY
                | DIVIDE
                | MODULUS
                | GREATER
                | SMALLER
                | EQUAL
                | AND
                | OR
                | NOT
                | IF

    FUN_CALL    : LPAREN FUN_EXP EXPS RPAREN
                | LPAREN ID EXPS RPAREN

    DEF_STMT    : LPAREN DEFINE ID EXP RPAREN

    IF_EXP      : LPAREN IF TEST_EXP THEN_EXP ELSE_EXP RPAREN

    TEST_EXP    : EXP

    THEN_EXP    : EXP

    ELSE_EXP    : EXP

## Notes
This lexer/ parser uses PLY. [Click here for the document.](https://www.dabeaz.com/ply/ply.html)

Here are the things covered:
1. Syntax Validation: Print “syntax error” when parsing invalid syntax
2. Print: Implement print-num statement
3. Numerical Operations: Implement all numerical operations
4. Logical Operations: Implement all logical operations
5. if Expression: Implement if expression
6. Variable Definition: Able to define a variable
7. Function: Able to declare and call an anonymous function
8. Named Function: Able to declare and call a named function
9. Type Checking: Print error messages for type errors

> If you want to test it out, run `main.py`. Feel free to modify `test.lsp` and see the results!


