grammar LabeledExpr; // rename to distinguish from Expr.g4
root:(functionDecl|statement )*  EOF ;
block:  (statement|functionDecl)*( Return expr SCOL )?; //(statement|functionDecl )* ( Return expr SCOL )?
statement: assignment  SCOL
    | functionCall SCOL
    ;
functionDecl : DEF ID '(' ID ')' START block END                # FuncdelcExpr
 ;
functionCall
 : ID '(' expr ')'                       #identifierFunctionCall
 ;
assignment: rid=ID EQUAL right=expr                 # AssignExpr
    ;


expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    |functionCall                              # FunctionCallExpr
    | atom=INT                                 # NumberExpr
    | atom=ID                                 # IdExpr
    | '(' expr ')'                             # ParenExpr 

    ;

// Instruccions
DEF : 'def';
START : '{';
END : '}';
Return : 'return';

HELLO: ('hello'|'hi')  ;
BYE  : ('bye'| 'tata') ;
INT  : [0-9]+         ;

ID   : [a-zA-Z_][a-zA-Z_0-9]*;
EQUAL : '=';
SCOL    : ';';
Space
 : [ \t\r\n\u000C] -> skip
 ;
 
