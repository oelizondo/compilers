## Flex and Bison

Flex y Bison son herramientas que nos ayudan a escribir parsers. Usan la
estrategia ```Look-Ahead-Left-Right``` (en vez de descenso recursivo)
parsea gramáticas no-amiguas y libres de contexto.

¿Por qué usar Flex y Bison?
En pocas palabras, está bien documenado y optimizado para cualquier solución que
haga en casa.

### Flex
El archivo para usar flex lo ponemos con la intensión ```.l```. Dentro de este
documento vamos a describir las reglas que el programa flex va a identificar, y
hacer algo de acuerdo con estas reglas.

Para este ejemplo vamos a hacer un parser de HTML que lo formatea de manera
correcta.

Primero vamos a definir las reglas.
Una regla es una función que se debe correr cuando se detecta un patrón (en este
caso una expresión regular) cuando se analiza un documento
```c
%{
  int tabsRequired = 0;
  void incrementTabs()
  {
    tabsRequired++;
  }

  void decrementTabs()
  {
    tabsRequired--;
  }

  void printTabs()
  {
    for(int i = 0; i <= tabsRequired; i++)
    {
      printf("    ");
    }
  }

  void openingTagPrint()
  {
   incrementTabs();
   printTabs();
   printf("%s\n", yytext);
  }

  void closingTagPrint()
  {
   printTabs();
   printf("%s\n", yytext);
   decrementTabs();
  }

 void wordPrint()
 {
  incrementTabs();
  printTabs();
  printf("%s\n", yytext);
  decrementTabs();
 }
%}
```

Posteriormente vamos a descibir los patrones que queremos encontrar dentro
del documento (en este caso un ```.html```). Usamos expresiones regulares
para poder detectar de maneraa fácil las etiquetas de html.

```
NEWLINE \n
DOCTYPE <!DOCTYPE>
WORD [a-z\.\:\ \&\;\á\é\í\ó\ú\ñA-Z0-9]*
INLINESTYLE ([a-z\ A-Z0-9]*=\"[\#a-zA-Z\ \_\&\-\:\.\/\/\0-9a-z\;]*\"*)*

HTML html
EXCEPTIONTAGS meta
TAGS head|body|div|ul|font|p|h1|h2|h3|title|li|table|th|tr|td|a|strong|EM

OHTML <{HTML}>
CHTML <\/{HTML}>
OHTMLTAG <{TAGS}>
CHTMLTAG <\/{TAGS}>
OHTMLWITHSTYLES <{TAGS}\ {INLINESTYLE}>
CEXCEPTIONS <\/{EXCEPTIONTAGS}>
OEXCEPTIONS <{EXCEPTIONTAGS}\ {INLINESTYLE}>

%%
```

Ya por ultimo tenemos que emparejar los patrones descritos arriba con las reglas
(funciones).
Cuando flex detecte un patrón, se va a correr la función con la que la hayamos
emparejado.
```
{NEWLINE} { continue; }

{DOCTYPE} { printf("%s \n", yytext); }

{OHTML} { printf("%s \n", yytext); }

{CHTML} { printf("%s \n", yytext); }

{OHTMLTAG} { openingTagPrint(); }

{OHTMLWITHSTYLES} { openingTagPrint(); }

{OEXCEPTIONS} { wordPrint(); }

{CHTMLTAG} { closingTagPrint(); }

{WORD} { wordPrint(); }

%%

int main()
{
  yylex();
}
```

Por último podemos tener un Makefile para organizar nuestros comandos:
```
build:
	flex formatter.l
	gcc -o formatter lex.yy.c -ll

run: build
	./formatter < index.html > formatted.html

clean:
	rm formatter
	rm lex.yy.c
```

### Bison

Bison es una herramienta para generar parsers de lenguajes. Para usar Bison
primero necesitamos tener un analizador lexico que agrupe y entienda un documento.

#### Usando Bison
Bison le pide a flex por diferentes tokens para que los pueda leer. Podemos
apoyarnos de otros lenguajes para definir los tipos de dato, por ejemplo.


Utilizando C. En este ejemplo solo vamos a ver un ejemplo de Bison vamos a
hacer un parser de números.

```
%{
#include <cstdio>
#include <iostream>
using namespace std;

// stuff from flex that bison needs to know about:
extern "C" int yylex();
extern "C" int yyparse();
extern "C" FILE *yyin;

void yyerror(const char *s);
%}

// Definiendo los tipos de C
%union {
	int ival;
	float fval;
}

// Definimos tokens terminales
%token <ival> INT
%token <fval> FLOAT

// Luego definimos la gramática
// Y sus funciones, (podemos ver que las gramáticas con tal cuales como vistas
//  en clase).

STMT:
	  INT STMT        { // Hacer algo aquí }
	| FLOAT STMT      { // Hacer algo aquí }
	| INT             { // Hacer algo aquí }
	| FLOAT           { // Hacer algo aquí }
	;
%%
```
Finalmente en nuestro ```Main``` ponemos lo que queremos hacer.
```
int main(int, char**) {
  // Leer el archivo
	FILE *miArchivo = fopen("a.archivo.file", "r");

  // Llamar a Flex y que lea el archivo
	yyin = myfile;

  // Llamar a Bison hasta que ya no haya contenido en flex
	do {
		yyparse();
	} while (!feof(yyin));

}
```
