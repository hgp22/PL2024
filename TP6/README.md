# TPC 6

+ Título
+ Autor: Henrique Guimarães Pereira, A97205
+ 
Programa que simula uma gramática independente de contexto, para os seguintes casos:
- ?a
- b=a*2/(27-3)
- !a+b
- c=a*b/(a/b)

Ter em conta:

- Prioridade dos operadores
- Garantir que é LL(1)
- Calcular os Look Ahead para todas as regras de produção

## Solução
```
T = {'?', '!', '(', ')', '=', '*', '/', '-', '+', var, num}

N = {S, Expr, Expr2, Expr3, Op, Op2}

S = S

P = {
    S -> '?' var            LA = {'?'}
       | '!' Expr           LA = {'!'}
       | var '=' Expr       LA = {var}

    Expr -> Expr2 Op

    Op -> '+' Expr          LA = {'+'}
        | '-' Expr          LA = {'-'}
        | &                 LA = {$, ')'}

    Expr2 -> Expr3 Op2      LA = {'(', var, num}

    Op2 -> '*' Expr         LA = {'*'}
         | '/' Expr         LA = {'/'}
         | &                LA = {'+', '-', $, ')'}

    Expr3 -> '(' Expr ')'   LA = {'('}
           | var            LA = {var}
           | num            LA = {num}
}
```