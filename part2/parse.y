%{
#include <stdio.h>
int yylex();
void yyerror(char *s);
%}

%start program
%token TRUE FALSE OPERATOR


%%
program	: expr '.'		{ }
	| '(' expr  ')'		{ }
	;

expr 	: TRUE '&&' TRUE 	{printf("T");}
	| TRUE '&&' FALSE 	{printf("F");}
	| FALSE '&&' FALSE	{printf("F");}
	| FALSE '&&' TRUE	{printf("F");}
	| TRUE '||' TRUE	{printf("T");}
	| TRUE '||' FALSE	{printf("T");}
	| FALSE '||' FALSE 	{printf("F");}
	| FALSE '||' TRUE 	{printf("T");}
	| TRUE '^' TRUE        	{printf("F");}
        | TRUE '^' FALSE       	{printf("T");}
        | FALSE '^' FALSE      	{printf("F");}
        | FALSE '^' TRUE       	{printf("T");}
	| '~' TRUE 		{printf("F");}
	| '~' FALSE		{printf("T");}
%%

void yyerror(char *s) {
	fprintf(stderr, "%s\n", s);
}

int main (int argc, char* argv[]) {
	yyparse();
	return 0;
} 

