grammar Tel;

parse: expr EOF; // main rule for parsing

expr
: NOT expr                                                     #notExpr
| expr op=(MULT | DIV) expr                                    #multiplicationExpr
| expr op=(PLUS | MINUS) expr                                  #additiveExpr
| expr op=(OR | AND | EQ | NEQ | GT | LT | GTEQ | LTEQ) expr   #logicalExpr
| expr KW_IS NOT? KW_NULL                                      #nullTestExpr
| atom                                                         #atomExpr
;

atom
: L_BRACKET expr R_BRACKET  #bracketExpr
| (INT | REAL)              #numberAtom
| (TRUE | FALSE)            #booleanAtom
| SINGLE_QUOTED_ELEMENT     #singleQuotedAtom
| STRING_CONSTANT           #stringConstantAtom
| fn                        #fnExpr
| taxon                     #taxonSlugAtom
;

fn : WORD L_BRACKET expr? (FN_PARAMETER_DELIMITER expr)* R_BRACKET ;
taxon: OPTIONAL_TAXON_OPERATOR? WORD (TAXON_NAMESPACE_DELIMITER WORD)? (TAXON_TAG_DELIMITER WORD)? ;

INT : '-'? DIGIT+ ;                 // integer
REAL : '-'? DIGIT+ '.' DIGIT+ ;     // integer
TRUE : T R U E;
FALSE : F A L S E;
NOT : N O T;
KW_IS : I S;
KW_NULL : N U L L;
WORD : [a-zA-Z_][a-zA-Z_0-9$.]*;     // one word (either part of slug or fn name). must start with non-digit

STRING_CONSTANT : '"' ( '\\"' | ~'"' )* '"' ;    // string constant. Not greedy, and supports \ to escape " char.
SINGLE_QUOTED_ELEMENT: '\'' ( '\\\'' | ~'\'' )* '\'' ;    // string element surrounded by single quotes. Not greedy, and supports \ to escape ' char.

L_BRACKET: '(';
R_BRACKET: ')';
TAXON_NAMESPACE_DELIMITER: '|';
TAXON_TAG_DELIMITER: ':';
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
OPTIONAL_TAXON_OPERATOR: '?'; // Taxon slug prefix noting, that the taxon slug is optional.

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment DIGIT : [0-9];
fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];
