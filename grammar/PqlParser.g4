/*
SQL-inspired "Pano Query Language" syntax
focusing on Expressions

Weird parts:
- Taxon is a SQL-column-like object with similar heritage (namespace etc)
  and extra syntax for optionality
- Some operator characters are more "programming" than SQL
  Example: Eq compare '==' vs SQL-like '=' (though '=' could be converted to '==' internally)
*/

parser grammar PqlParser;

options {
  tokenVocab = PqlLexer;
}

// entry point
parseTel: expr EOF ;

expr
 : unary_operator=( MINUS | PLUS | K_NOT ) right=expr
 | left=expr operator=( STAR | FORWARD_SLASH | MOD ) right=expr
 | left=expr operator=( PLUS | MINUS ) right=expr
 | left=expr operator=( LT | LT_EQ | GT | GT_EQ ) right=expr
 | left=expr operator=( ASSIGN | EQ | NOT_EQ1 | NOT_EQ2 | K_IS ) right=expr
 | left=expr is_negated=K_NOT? operator=(K_LIKE | K_ILIKE) right=expr
 | left=expr is_negated=K_NOT? operator=K_IN OPEN_PAREN right_list=exprList CLOSE_PAREN
 | left=expr operator=( K_AND | AND ) right=expr
 | left=expr operator=( K_OR | OR ) right=expr
 // BETWEEN must come after AND or risk being parsed before it
 // resulting in `a BETWEEN b` where `AND c` fragment is outside of BETWEEN expression
 | left=expr is_negated=K_NOT? operator=K_BETWEEN right=expr
 | OPEN_PAREN inner=expr CLOSE_PAREN
 | literalValue
 | fn
 | taxon
 ;

exprList: expr ( COMMA expr )* ;

// Note that function supports optional list of arguments trapped as `expr`
// which allows us to have
//  named (`arg1=value1, arg2=value2'` and
//  positional (`value1, value2`) args.
// Named ones will come as `expr` with left=expr,operator=ASSIGN,right=expr contents.
//  You might need to express these as ordered dict / list of tuples to preserve names of args.
// Positional will be whatever literal or other single-valued expr content could be.
fn: function_name=identifierMultipart OPEN_PAREN arguments=fnArgs? CLOSE_PAREN ;
fnArgs: fnArg ( COMMA fnArg)* ;
fnArg: ( argument_name=WORD ASSIGN)? argument_value=expr ;

// TODO: TAXON_TAG_DELIMITER is being killed off. Remove when we migrate out of taxon tags.
taxon:
    is_optional=QUESTION_MARK?
    ( namespace=identifierMultipart PIPE )?
    slug=identifierMultipart
    // TODO: drop this when we drop Data Tags system.
    // May conflict with TypeCast expression
    ( COLON tag=identifierMultipart )?
 ;

identifierMultipart: WORD ( DOT WORD )* ;

literalValue
 : NUMERIC_LITERAL
 | DOUBLE_QUOTED_STRING
 | SINGLE_QUOTED_STRING
 | K_NULL
 | K_TRUE
 | K_FALSE
 ;
