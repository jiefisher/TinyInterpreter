grammar LabeledExpr; // rename to distinguish from Expr.g4
root:(functionDecl|statement )*  EOF ;
block:  (statement|functionDecl)*( Return expr SCOL )?; //(statement|functionDecl )* ( Return expr SCOL )?
statement: assignment  SCOL
    | functionCall SCOL
    | ifStatement
    | forStat
    ;

assignment: rid=ID EQUAL right=expr                 # AssignExpr
    ;
functionCall
 : ID '(' expr ')'                       #identifierFunctionCall
 ;
ifStatement
 : ifStat elseIfStat* elseStat?          #IfStatementExpr
 ;

ifStat
 : If '(' expr ')' START block END       #IfExpr
 ;

elseIfStat
 : Else If '(' expr ')' START block END  #ElseIfExpr
 ;

elseStat
 : Else START block END                  #ElseExpr
 ;
forStat
 : For '(' assignment ';' expr ';' assignment ')' START block END       #ForExpr
 ;
functionDecl : DEF ID '(' ID ')' START block END                # FuncdelcExpr
 ;


expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | left=expr op=('>'|'<'|'>='|'<=') right=expr           # InfixExpr
    | left=expr op=('=='|'!=') right=expr           # InfixExpr
    | left=expr op=('&&'|'||') right=expr           # InfixExpr
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
If       : 'if';
Else     : 'else';
For      : 'for';
HELLO: ('hello'|'hi')  ;
BYE  : ('bye'| 'tata') ;
INT  : [0-9]+         ;

ID   : [a-zA-Z_][a-zA-Z_0-9]*;
EQUAL : '=';
SCOL    : ';';
Space
 : [ \t\r\n\u000C] -> skip
 ;
 
