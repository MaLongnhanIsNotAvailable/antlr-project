//MSSV: 1812915
grammar CSEL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

// Parser
program: (statements)+ EOF;

statements : var_dec | arr_dec | const_dec | const_arr_dec | fun_dec | assignment | if_statement | for_statement | while_statement | (call_statement SEMICOLON) | key_words;

var_dec
:   LET ( (ID_VARIABLE) (COLON DATA_TYPE)? (ASSIGN exp )? COMMA)* (ID_VARIABLE) (COLON DATA_TYPE)? (ASSIGN exp )? SEMICOLON
;
arr_dec
:   LET ( (id_arr) (COLON DATA_TYPE)? (ASSIGN exp )? COMMA)* (id_arr) (COLON DATA_TYPE)? (ASSIGN exp )? SEMICOLON
;
const_dec
:   CONSTANT (ID_CONSTANT (COLON DATA_TYPE)? (ASSIGN exp ) COMMA)* ID_CONSTANT (COLON DATA_TYPE)? (ASSIGN exp ) SEMICOLON
;
const_arr_dec
:   CONSTANT (id_arr_const (COLON DATA_TYPE)? (ASSIGN exp ) COMMA)* id_arr_const (COLON DATA_TYPE)? (ASSIGN exp ) SEMICOLON
;

assignment
:   (ID_VARIABLE | id_arr | index_operators | key_operators) ASSIGN exp SEMICOLON  ////////////EXP CHI 3 LOAI THOI
;
if_statement
:   IF LP exp RP LCB (statements)* RCB
    (ELIF LP exp RP LCB (statements)* RCB)*
    (ELSE LCB (statements)* RCB)?
;
for_statement
:   FOR (ID | ID_VARIABLE) ((IN (arr_lit | ID_VARIABLE | ID_CONSTANT))|(OF (json_lit | ID_VARIABLE | ID_CONSTANT)))
    LCB statements* RCB
;
while_statement
:   WHILE LP exp RP LCB statements* RCB
;
fun_dec
:  FUNCTION ID_VARIABLE LP  ((params COMMA)* params)? RP  LCB statements* RCB 
;
params
: index_operators | ID | ID_VARIABLE | id_arr | ID_CONSTANT 
;

exp
:   exp1 (ADD_DOT | DEQUAL_DOT) exp1 | exp1  
;
exp1
:   exp2 (EQUALS | NOT_EQ | LESS_THAN | GREATER_THAN | LTE | GTE) exp2 | exp2
;
exp2
:   exp2 (AND | OR) exp3 | exp3
;
exp3
:   exp3 (ADD | MINUS) exp4 | exp4
;
exp4
:   exp4 (MUL | DIV | MOD) exp5 | exp5
;
exp5
:   NOT exp5 | exp6
;
exp6 // a < a < b
:   MINUS exp6 | exp7
;
exp7
:   index_operators | key_operators | exp8
;
exp8
:   call_statement | exp9 
;
exp9
:   LP exp RP | num_lit | arr_lit 
    | json_lit | BOOLEAN_LIT | STRING_LIT | ID_VARIABLE | ID | id_arr | ID_CONSTANT | id_arr_const
;

key_words
:   (BREAK | CONTINUE | (RETURN  exp)) SEMICOLON
;
index_operators
:   (ID | ID_VARIABLE | ID_CONSTANT | call_statement | key_operators) LSB index_operand RSB
;
index_operand
:   exp | (exp COMMA index_operand)
;
key_operators
: (ID | ID_VARIABLE | ID_CONSTANT | call_statement) key_operand
;
key_operand
:   LSB exp RSB | LSB exp RSB key_operand
;

call_statement
:   CALL LP ID_VARIABLE COMMA LSB ((exp COMMA)* exp)? RSB RP
;


arr_lit
:    LSB ((arr_element COMMA)* arr_element)? RSB
;
arr_element
:   arr_lit | num_lit | STRING_LIT | BOOLEAN_LIT | json_lit
;
json_lit
:   LCB ((json_element COMMA)* json_element)? RCB
;
json_element
:   (ID| ID_VARIABLE) COLON (num_lit | BOOLEAN_LIT | STRING_LIT | json_lit | arr_lit)
;
id_arr
:   (ID | ID_VARIABLE) LSB (NUM_LIT COMMA)* NUM_LIT? RSB
;
id_arr_const
:   ID_CONSTANT LSB (NUM_LIT COMMA)* NUM_LIT? RSB
;
num_lit
: (MINUS)? NUM_LIT
;

// Lexer
DATA_TYPE: STRING|NUMBER|BOOLEAN|JSON;

ID_VARIABLE//
:   [a-z][_a-zA-Z0-9]*
;
ID_CONSTANT
:   '$'[_a-zA-Z0-9]* 
;

ID
: [$a-z][_a-zA-Z0-9]* 
;


NUM_LIT
:  (POINT_FLOAT | EXPONENT_FLOAT)
;  


BOOLEAN_LIT
: TRUE | FALSE
;

STRING_LIT
:   '"' STRINGCHAR* '"' {
self.text=self.text[1:-1]
}
;



COMMENT
:   HASHTAGS  (.)*?  HASHTAGS ->skip
;
UNTERMINATED_COMMENT
: HASHTAGS (~[#{2}])*
;



fragment STRINGCHAR: ~["\\\n\r] | EscapeSequence | '\'"';

fragment EscapeSequence: '\\' [btnfr'\\];

// Error
ILLEGAL_ESCAPE
:   '"' STRINGCHAR* '\\' ~[btnfr'\\]{
    raise IllegalEscape(self.text[1:])
} 
;
// raise IllegalEscape(self.text[1:])
UNCLOSE_STRING
:	'"' STRINGCHAR* {
    raise UncloseString(self.text[1:])
}
;
//raise UncloseString(self.text[1:])
fragment HASHTAGS
:   '##'
;


//FRAGMENT
fragment POINT_FLOAT
 : INT_PART (FRACTION?)
 ;
 fragment EXPONENT_FLOAT
 : ( INT_PART | POINT_FLOAT ) EXPONENT
 ;
 fragment INT_PART
 : DIGIT+
 ;
 fragment FRACTION
 : '.' DIGIT*
 ;
 fragment EXPONENT
 : [eE] [+-]? DIGIT+
 ;
fragment DIGIT
: [0-9]
;
fragment NEGATIVE
: '-'
;  
//key_words
SEMICOLON: ';' ;
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELIF: 'Elif';
ELSE: 'Else';
WHILE: 'While'; 
FOR: 'For';
OF: 'Of';
IN: 'In';
FUNCTION: 'Function';
LET: 'Let';
TRUE: 'True';
FALSE: 'False';
CALL: 'Call';
RETURN: 'Return';
NUMBER: 'Number';
BOOLEAN: 'Boolean';
STRING: 'String';
JSON: 'JSON';
ARRAY: 'Array';
CONSTANT: 'Constant';
//OPERATOR:
ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';

AND: '&&';
OR: '||';
LESS_THAN : '<';
GREATER_THAN : '>';
ASSIGN: '=';
EQUALS : '==';
GTE : '>=';
LTE : '<=';
NOT_EQ : '!=';
//SEPERATOR
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
COLON: ':';
DOT: '.';
COMMA: ',';
LCB: '{';
RCB: '}';
ADD_DOT: '+.';
DEQUAL_DOT: '==.';


WS : [ \t\r\n]+ -> skip ;

ERROR_CHAR: .;
