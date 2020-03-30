grammar Tel;

INT : '-'? [0-9]+ ;                 // integer
REAL : '-'? [0-9]+ '.' [0-9]+ ;     // integer
TRUE : 'true' ;                     // true
FALSE : 'false' ;                   // false
NOT : 'not';
WORD : [a-zA-Z0-9_]+;               // one word (either part of slug or fn name)
STRING_CONSTANT : '"' ( '\\"' | ~'"' )* '"' ;    // string constant. Not greedy, and supports \ to escape " char.

L_BRACKET: '(';
R_BRACKET: ')';
TAXON_NAMESPACE_DELIMITER: '|';
FN_PARAMETER_DELIMITER: ',';
// OPERATORS
OR : '||';
AND : '&&';
EQ : '==';
NEQ : '!=';
GT : '>';
LT : '<';
GTEQ : '>=';
LTEQ : '<=';
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// auxiliarly rules
fn : WORD L_BRACKET expr? (FN_PARAMETER_DELIMITER expr)* R_BRACKET ; // matches functions
taxon: WORD (TAXON_NAMESPACE_DELIMITER WORD)? ;  // matches a taxon slug

// final rules
parse: expr EOF; // main rule for parsing

expr
: NOT expr                                                     #notExpr
| expr op=(OR | AND | EQ | NEQ | GT | LT | GTEQ | LTEQ) expr   #logicalExpr
| expr op=(MULT | DIV) expr                                    #multiplicationExpr
| expr op=(PLUS | MINUS) expr                                  #additiveExpr
| atom                                                         #atomExpr
;

atom
:  L_BRACKET expr R_BRACKET  #bracketExpr
| (INT | REAL)              #numberAtom
| fn                        #fnExpr
| (TRUE | FALSE)            #booleanAtom
| taxon                     #taxonSlugAtom
| STRING_CONSTANT           #stringConstantAtom
;
