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
 : setStmt
 | selectStmt
 ;

// a way to set query context settings and avoid sending them inside PQL
// Example: set "fill in dates for date-ranged sparse data" flag for Husky.
setStmt
 : K_SET key=identifierMultipart ASSIGN values=expr
 ;

selectStmt
 : selectClause
   ( whereClause )?
   ( orderByClause )?
   ( limitClause )?
 ;

selectClause: K_SELECT columns ( COMMA columns )* ;
// Column is a complicated structure of many parts:
//  {tel expression (includes taxon)}{::Type Cast function or token} {{AS} taxon-like}
// Example:
//  (?ns3|taxon3 + (slug2 - 1234))::TypeHint(agg=ave) as ns1|custom_data1,
columns: value=expr (COLON COLON type_cast=function)? (K_AS alias=taxon)? ;
// TypeCasting with ::TypeCast() conflicts with end of taxon ":tag"
// This means that typecasting cannot be used on naked taxon
// Must wrap whatever expression into parens or other non-taxon before Type Casting
// WRONG:
//   ns1|taxon:tag:TypeCast()
//   ns1|taxon::TypeCast()
// CORRECT:
//   (ns1|taxon:tag)::TypeCast()
//   (ns1|taxon)::TypeCast()
// While SQL allows non-function and function type casts,
// we stick with requireing parens always for simplicity of syntax parser.

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
// | left=expr is_negated=K_NOT? operator=K_IN '(' exprList? ')'
 | left=expr operator=( K_AND | AND ) right=expr
 | left=expr operator=( K_OR | OR ) right=expr
 | OPEN_PAREN inner=expr CLOSE_PAREN
 | literalValue
 | function
 | taxon
 ;

// Note that function supports optional list of arguments trapped as `expr`
// which allows us to have
//  named (`arg1=value1, arg2=value2'` and
//  positional (`value1, value2`) args.
// Named ones will come as `expr` with left=expr,operator=ASSIGN,right=expr contents.
//  You might need to express these as ordered dict / list of tuples to preserve names of args.
// Positional will be whatever literal or other single-valued expr content could be.
function: function_name=identifierMultipart OPEN_PAREN arguments=exprList? CLOSE_PAREN;
exprList: expr ( COMMA expr )* ;

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
