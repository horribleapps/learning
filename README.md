## Horrible apps learning

In order to teach myself varios programming languages. I have decided to keep a record of everything I do. The username horribleapps was a tongue in cheek because I would probably create horrible apps. I want to keep a record of all victories and losses of my coding to see what it takes to build projects.

### Chess

I am attempting to make a chess app using Python.
I initially did it using numpy and not using any classes. It quickly got very confusing and hard to take apart.
Here is the link: https://github.com/horribleapps/learning/tree/main/old_chess
I created a pytest, but it quickly became too hard for me take apart.

I decided to start using Object oriented program to see if that helps write better code.


I broke up the file into 3 files: chess.py, game.py and piece.py

### chess.py
```markdown
class Game():
    def __init__(self) # initialize the board
    def placePieces(self) # initialize the board
    def printBoard(self) #print out the board
    def check(self,newloc,pc) # looks if a move is a check
    def updateMove(self,newloc,pc)
```

### piece.py
```markdown
class Piece():
    def __init__(self,player,name,position) # initialize the piece
    def availableMoves(self)
    def checkBounds(self,intervals)
    def checkpiece(self,board,intervals)
    def __str__(self)
    def __repr__(self)

class Pawn(Piece) #inherits the piece class and will override availableMoves
class Rook(Piece) #inherits the piece class and will override availableMoves
class King(Piece) #inherits the piece class and will override availableMoves
class Queen(Piece) #inherits the piece class and will override availableMoves
class Knight(Piece) #inherits the piece class and will override availableMoves
class Bishop(Piece)#inherits the piece class and will override availableMoves
```


I will add more as time goes on. I am trying to balance too much code since people have access to my code as well.

