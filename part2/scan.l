%{
#include "parse.tab.h"
#define YY_SCKIP_YYWRAP
%}

	extern YYSTYPE yylval;
	extern int yywrap() {return 1;}
	extern int isatty();

%%

"T"	{return TRUE;}
"F"	{return FALSE;}
[ \t]	; // ignore all whitespace
.	{return yytext[0];}
%%


