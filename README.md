## sudoku-cli

Run Game: `python3 sudoku-cli.py`

Interface:

```
#######Menu##########
1) new game
2) load game
3) exit

1
>>> Enter filled cells count, integer from [0..80]
80
[state : game_running | free cells : 1 | last_move : ]

 1 6 2  3 5 9  8 4 7 
 5 7 4  6 8 2  3 9 1 
 8 9 3  7 4 1  5 2 6 

 9 4 5  1 3 6  2 7 8 
 3 2 1  8 9 7  4 6 5 
 6 8 7  5 2 4  1 3 9 

 4 1 6  2 7 8  9 5 3 
 7 5 9  4 1 3  6 8 2 
 2 3 8  9 6 5  7 _ 4 

>>> Enter command : ['move', 'save', 'exit']
move
>>> Enter [x] [y] [value]
9 8 1
>>> You successfully solved sudoku!
```

