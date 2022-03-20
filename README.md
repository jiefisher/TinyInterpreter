# TinyInterpreter
A simple Interpreter in python， which can excuted codes line by line. 
## You can write rule like this (test.gl):
```
def func(x){
    x = x+1;
    b = 8;
    return x+1;
}
a = func(100);
d = func(200);
c = a*d;
```
## Run `python3 main.py ` to use.
## Implement 
### Todo List
- [x] Basic OP: +, -, *, /, Parentheses
- [x] ASSIGN OP: =
- [x] Control Flow
  - [x] function
  - [x] if
- [x] Array
