%{
#include "parse.tab.h"
#define YY_SKIP_YYWRAP
%}

	extern YYSTYPE yylval;
	extern int yywrap() {return 1;};
	extern int isatty();

%%

T	{return True; }
F	{return False; }
&&	{return And; }
"||"	{return Or; }
"^"	{return Xor; }
~	{return Not; } 
[ \t]    ; // ignore all whitespace
.        { return yytext[0]; }

%%
