# DS-5100-Project-Repo
## Metadata
Name: Alexander Lilly

Montecarlo Simulator

## Synopsis

### Installing
    montecarlo>pip install -e.

### Importing
    from montecarlo import Die, Game, Analyzer

### Creating Dice Objects
Create coin with heads or tails faces.
    
    Faces = ['H','T']

Create the die object.
    
    Die_Object = Die(Faces)

### Playing Games
Initialize the game class by passing the die objects as inputs. 

    Game = Game([Die_Object_1, Die_Object_2, Die_Object_3])

Play the game N times. 
    
    N = 1000
    Game.play(N)

### Analyzing Games
Initialize the Analyzer class. 

    Analysis = Analyzer(Game)

Get the number of jackpots (the number of times all die objects rolled the same face) in N plays.
    
    Jackpots = Analysis.jackpot()

Get the percentage of jackpots across N plays.

    Jackpots_Percentage = Analysis.jackpot()/N

Get sorted (descending) dataframe of most frequent roll combinations.
    
    Analysis.Combo()
    Combos = Analysis.combo()
    
## API description
### montecarlo.Die
***class*** montecarlo.Die(Faces)

__Initialization Parameters__:
<ul>
Faces : ***list of numerics or strings***.

<ul>A list of possible outcomes for a given random event. For example, for a 6-sided die, faces would be a list of length 6 where each element represents a face of the dice. By default, the Die class assumes equal probabilistic weights for each possible outcome.</ul></ul>

METHODS:

    change_weight(face, new weight): To alter the default equal weight among die faces, pass the face you wish 
    the change the weight of and the weight to which to change it to the change_weight() method. 
    roll(num_rolls): Rolls the die num_rolls times. Stores results of each roll in .results as a dataframe. 
    show_weights(): Returns a dataframe of the die faces and their corresponding weights. 

ATTRIBUTES:

    Die.faces 
a list of possible outcomes associated with the Die object. 
    
    Die.results
Accesible only after the roll() method has been executed, Die.results returns a dataframe with the roll number as the index and the value as the outcome of the rolled die. 

A list of all classes with their public methods and attributes.
For each method:
Show the docstring
List and describe all parameters (with data types and defaults)
List and describe return values, if any
Do not describe private methods and attributes