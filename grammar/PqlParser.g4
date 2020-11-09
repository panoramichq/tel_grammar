/*
SQL-inspired "Pano Query Language" syntax
Subset of SQL Select statement with just 2 clauses supported:
    - select plethora of taxons and TEL expressions combination
    - where clause supporting plethora of taxons and TEL expressions logical comparisons

Subset of https://github.com/panoramichq/entity-tree-sql-service/blob/master/src/sql/SQLSelect.g4
*/

parser grammar PqlParser;

options {
  tokenVocab = PqlLexer;
}

// we have 2 entry points:
// parse Tel expression:
parseTel: expr EOF ;
// parse PQL statements with TEL inside:
parsePql : ( sqlStmtList )* EOF ;

sqlStmtList
 : ';'* sqlStmt ( ';'+ sqlStmt )* ';'*
 ;

// this is where you add more statement types, like SET and other top-level SQL statements
sqlStmt
 : selectStmt
 ;

selectStmt
 : K_SELECT columns
   ( whereClause )?
   ( orderByClause )?
   ( limitClause )?
 ;

columns: expr ( COMMA expr )* ;

whereClause
 : K_WHERE expr
 ;

orderByClause
 : K_ORDER K_BY orderExpr ( COMMA orderExpr )*
 ;

orderExpr
 : expr ( K_ASC | K_DESC )?
 ;

limitClause
 : K_LIMIT limit=expr // ( ( K_OFFSET | COMMA ) expr )?
 ;

expr
 : unary_operator=( MINUS | PLUS | K_NOT ) right=expr
 | left=expr operator=( STAR | FORWARD_SLASH | MOD ) right=expr
 | left=expr operator=( PLUS | MINUS ) right=expr
 | left=expr operator=( LT | LT_EQ | GT | GT_EQ ) right=expr
 | left=expr operator=( ASSIGN | EQ | NOT_EQ1 | NOT_EQ2 | K_IS ) right=expr
// | left=expr is_negated=K_NOT? operator=( K_LIKE | K_BETWEEN ) right=expr
// | left=expr is_negated=K_NOT? operator=K_IN '(' ( right=expr ( ',' right=expr )* )? ')'
 | left=expr operator=( K_AND | AND ) right=expr
 | left=expr operator=( K_OR | OR ) right=expr
 | OPEN_PAREN inner=expr CLOSE_PAREN
 | literalValue
 | function_name=identifierMultipart OPEN_PAREN ( expr ( COMMA expr )* )? CLOSE_PAREN
 | taxon
 ;

// TODO: TAXON_TAG_DELIMITER is being killed off. Remove when we migrate out of taxon tags.
taxon:
    TAXON_OPTIONAL_OPERATOR?
    ( namespace=identifierMultipart PIPE )?
    slug=identifierMultipart
    ( TAXON_TAG_DELIMITER tag=identifierMultipart )?
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
