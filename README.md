# DS-5100-Project-Repo
## Metadata
Name: Alexander Lilly

Montecarlo Simulator

Version: 1.0.0

Date: December, 2022

Description:

## Synopsis

### Installation
    ~\montecarlo>pip install -e.

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
***class*** montecarlo.Die

    montecarlo.Die(Faces)

__Initialization Parameters__:

Faces : ***list of integer, float, or string***.

<ul>A list of possible outcomes for a given random event. For example, for a 6-sided die, faces would be a list of length 6 where each element represents a face of the dice. By default, the Die class assumes equal probabilistic weights for each possible outcome.</ul>

#### Methods: 

    Die.change_weight(face, new weight): 
<ul>

Changes the weight of `face` to `new weight`. Inputs must match the data type of original face list. 

__Parameters__: 

&ensp;&ensp;**face** : The value of the face to change.

&ensp;&ensp;**new weight** : The new value of the face weight. </ul>
    
    Die.roll(num_rolls):

<ul>

Rolls the die `num_rolls` times. Stores results of each roll in Die.results as a dataframe. 

__Parameters__: 

&ensp;&ensp;**num_rolls** : Number of times to roll the dice (***integer***)</ul>

    Die.show_weights(): 

<ul>

__Returns__ : A dataframe of the die faces and their corresponding weights. </ul>

#### Attributes:

    Die.faces 
<ul>

__Returns__ : A list of possible outcomes associated with the Die object. </ul>
    
    Die.results
<ul>

__Returns__ : A dataframe with the roll number as the index and the rolled face as the value. Accesible only after the roll() method has been executed.</ul>

### montecarlo.Game
***class*** montecarlo.Game

    montecarlo.Game(montecarlo.Die objects)

__Initialization Parameters__:

Faces : ***list of montecarlo.Die objects***.
