### PyBison

Finalmente, PyBison es una herramienta que hace lo mismo que Bison pero para
el lenguaje de python. Que es el lenguaje en el que haremos nuestro proyecto final.

### Creando un archivo PyBison

en parser.py
```python
  from bison import BisonParser, BisonNode
```

Después tenemos que diseñar nuestra gramática

```
%token NUM
%left '-' '+'
%left '*' '/'
%left NEG     /* negation--unary minus */
%right '^'    /* exponentiation        */

/* Grammar follows */
%%
input:    /* empty string */
        | input line
;

line:     '\n'
        | exp '\n'  { printf ("\t%.10g\n", $1); }
;

exp:      NUM                { $$ = $1;         }
        | exp '+' exp        { $$ = $1 + $3;    }
        | exp '-' exp        { $$ = $1 - $3;    }
        | exp '*' exp        { $$ = $1 * $3;    }
        | exp '/' exp        { $$ = $1 / $3;    }
        | '-' exp  %prec NEG { $$ = -$2;        }
        | exp '^' exp        { $$ = pow ($1, $3); }
        | '(' exp ')'        { $$ = $2;         }
;
```

No

```python
class Parser(BisonParser):

    tokens = ['NUMBER',
              'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POW',
              'LPAREN', 'RPAREN',
              'NEWLINE', 'QUIT',
              ]

    precedences = (
        ('left', ('MINUS', 'PLUS')),
        ('left', ('TIMES', 'DIVIDE')),
        ('left', ('NEG', )),
        ('right', ('POW', )),
        )

    start = 'input'
    def on_input(self, target, option, names, items):
        """
        input :
              | input line
        """
        return

    def on_line(self, target, option, names, items):
        """
        line : NEWLINE
             | exp NEWLINE
        """
        if option == 1:
            print "on_line: got exp %s" % items[0]

    def on_exp(self, target, option, names, items):
        """
        exp : NUMBER
            | exp PLUS exp
            | exp MINUS exp
            | exp TIMES exp
            | exp DIVIDE exp
            | MINUS exp %prec NEG
            | exp POW exp
            | LPAREN exp RPAREN
        """
        if option == 0:
            return float(items[0])
        elif option == 1:
            return items[0] + items[2]
        elif option == 2:
            return items[0] - items[2]
        elif option == 3:
            return items[0] * items[2]
        elif option == 4:
            return items[0] / items[2]
        elif option == 5:
            return - items[1]
        elif option == 6:
            return items[0] ** items[2]
        elif option == 7:
            return items[1]
```

finalmente usamos un script nuevo ```miscanner.py```:

```python
#!/usr/bin/env python
import parser
p = parser.Parser()
p.run()
```
