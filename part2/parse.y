%{
#include <stdio.h>
int yylex();
void yyerror(char * s);
%}

%token True False And Or Xor Not

%start expr

%%

expr : True And True         	{ printf("T"); }
	| True And False       	{ printf("F"); }
	| False And False    	{ printf("F"); }
	| False And True      	{ printf("F"); }
	| True Or True		{ printf("T"); }
	| True Or False		{ printf("T"); }
	| False Or False	{ printf("F"); }
	| False Or True		{ printf("T"); }
	| True Xor True		{ printf("F"); }
	| True Xor False	{ printf("T"); }
	| False Xor False	{ printf("F"); }
	| False Xor True	{ printf("T"); }
	| Not True		{ printf("F"); }
	| Not False		{ printf("T"); }
	;

%%

void yyerror(char* s) {fprintf(stderr,"%s\n",s);}

int main(int argc, char* argv[]) {
	yyparse();
	return 0;
}
