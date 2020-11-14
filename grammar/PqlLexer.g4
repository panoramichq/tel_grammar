lexer grammar PqlLexer;

// mostly SQL-compatible (except for some TEL-isms where marked):

AND : '&&'; // TEL
EQ : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ1 : '!=';
NOT_EQ2 : '<>';
OR : '||'; // TEL. !! CONFLICT WITH SQL where it's string concatenator !!
SHIFT_LEFT : '<<';
SHIFT_RIGHT : '>>';

AMP : '&';
ASSIGN : '=';
CLOSE_PAREN : ')';
COLON: ':';
COMMA : ',';
DOT : '.';
FORWARD_SLASH : '/';
GT : '>';
LT : '<';
MINUS : '-';
MOD : '%';
OPEN_PAREN : '(';
PIPE : '|';
PLUS : '+';
QUESTION_MARK: '?';
SCOL : ';';
STAR : '*';
TILDE : '~';
UNDER: '_';

// SQL keywords we adapt:
K_AND : A N D;
K_AS : A S;
K_ASC : A S C;
K_BY : B Y;
K_DESC : D E S C;
K_FALSE : F A L S E;
K_IS : I S;
K_ISNULL : I S N U L L;
K_LIKE : L I K E;
K_LIMIT : L I M I T;
K_NOT : N O T;
K_NOTNULL : N O T N U L L;
K_NULL : N U L L;
K_OR : O R;
K_ORDER : O R D E R;
K_SELECT : S E L E C T;
K_SET : S E T;
K_TRUE : T R U E;
K_WHERE : W H E R E;

NUMERIC_LITERAL
 : DIGIT+ ( '.' DIGIT* )? ( E [-+]? DIGIT+ )?
 | '.' DIGIT+ ( E [-+]? DIGIT+ )?
 ;

// Note, use of TEL escaping variant,
// escaping is NOT SQL style "double-char":
// TODO: allow both in TEL to avoid translation headaches
DOUBLE_QUOTED_STRING: DOUBLE_QUOTED_STRING_TEL ;
DOUBLE_QUOTED_STRING_TEL : '"' ( '\\"' | ~'"' )* '"' ;
DOUBLE_QUOTED_STRING_SQL : '"' ( '""' | ~'"' )* '"' ;

// Note, use of TEL escaping variant,
// Note, escaping is NOT SQL style "double-char":
// TODO: allow both in TEL to avoid translation headaches
SINGLE_QUOTED_STRING: SINGLE_QUOTED_STRING_TEL ;
SINGLE_QUOTED_STRING_TEL: '\'' ( '\\\'' | ~'\'' )* '\'' ;
SINGLE_QUOTED_STRING_SQL: '\'' ( '\'\'' | ~'\'' )* '\'' ;

SINGLE_LINE_COMMENT
 : ('--'|'//'|'#') ~[\r\n]* -> channel(HIDDEN)
 ;

MULTILINE_COMMENT
 : '/*' .*? ( '*/' | EOF ) -> channel(HIDDEN)
 ;

SPACES
 : [ \u000B\t\r\n] -> channel(HIDDEN)
 ;

WORD
 : [a-zA-Z_][a-zA-Z_0-9]*
 ;

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
