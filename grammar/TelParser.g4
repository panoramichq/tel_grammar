parser grammar TelParser;

options {
  tokenVocab = TelLexer;
}

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
