%{
#include <stdio.h>
int yylex();
void yyerror(char * s);
%}

%token True False

%left Xor
%left Or
%left And
%left Not

%start program


%%
program : expr '.' { }
	;


expr : True And True         	{ printf("T"); }
	| True And False       	{ printf("F"); }
	| expr And True		{}
	| False And False    	{ printf("F"); }
	| False And True      	{ printf("F"); }
	| expr And False	{}
	| True Or True		{ printf("T"); }
	| True Or False		{ printf("T"); }
	| expr Or True		{}
	| False Or False	{ printf("F"); }
	| False Or True		{ printf("T"); }
	| expr Or False		{}
	| True Xor True		{ printf("F"); }
	| True Xor False	{ printf("T"); }
	| expr Xor True		{}
	| False Xor False	{ printf("F"); }
	| False Xor True	{ printf("T"); }
	| expr Xor False	{}
	| Not True		{ printf("F"); }
	| Not False		{ printf("T"); }
	| Not expr		{}
	;

%%

void yyerror(char* s) {fprintf(stderr,"%s\n",s);}

int main(int argc, char* argv[]) {
	yyparse();
	return 0;
}
