# DS-5100-Project-Repo
## Metadata
Name: Alexander Lilly

Montecarlo Simulator

## Synopsis

### Installing
    montecarlo>pip install -e.

### Importing
    from montecarlo import Die, Game, Analyzer

### Creating dice objects
    Faces = ['H','T'] # create coin with heads or tails faces
    Die_Object = Die(Faces)

### Playing games
    Game = Game([Die_Object 1, Die_Object 2, Die_Object_3])
    Game.play(1000)

### Analyzing games
    Analysis = Analyzer(Game)
    Fair_Jackpot = Analysis.jackpot()/1000
    print(Fair_Jackpot)
## API description
A list of all classes with their public methods and attributes.
For each method:
Show the docstring
List and describe all parameters (with data types and defaults)
List and describe return values, if any
Do not describe private methods and attributes