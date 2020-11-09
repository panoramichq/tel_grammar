lexer grammar TelLexer;

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

// support SQL, JavaScript and Python style syntax for single-line comment
SINGLE_LINE_COMMENT : ('--'|'//'|'#') ~[\r\n]* -> channel(HIDDEN) ;

WS : [ \t\r\n]+ -> channel(HIDDEN) ; // skip spaces, tabs, newlines

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
