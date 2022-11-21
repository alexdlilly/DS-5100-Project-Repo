# DS-5100-Project-Repo
## Metadata
Name: Alexander Lilly

Montecarlo Simulator

Version: 1.0.0

Date: December, 2022

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

    Die.change_weight(face, new_weight): 
<ul>

Changes the weight of `face` to `new_weight`. Inputs must match the data type of original face list. 

__Parameters__: 

&ensp;&ensp;`face` : The value of the face to change.

&ensp;&ensp;`new_weight` : The new value of the face weight. </ul>
    
    Die.roll(num_rolls):

<ul>

Rolls the die `num_rolls` times. Stores results of each roll in `Die.results` as a dataframe. 

__Parameters__: 

&ensp;&ensp;`num_rolls` : Number of times to roll the dice (***integer***)</ul>

    Die.show_weights(): 

<ul>

__Returns__ : A dataframe of the die faces and their corresponding weights. </ul>

#### Attributes:

    Die.faces 
<ul>

__Returns__ : A list of possible outcomes associated with the Die object. </ul>
    
    Die.results
<ul>

__Returns__ : A dataframe with the roll number as the index and the rolled face as the value. Accesible only after the `Die.roll()` method has been executed.</ul>

### montecarlo.Game
***class*** montecarlo.Game

    montecarlo.Game(Dies)

__Initialization Parameters__:

Dies : ***list of montecarlo.Die objects***.

#### Methods: 

    Game.play(N): 

<ul>

Rolls each die object `N` times.

__Parameters__:

`N` : Number of times to roll the dice (***integer***)</ul>

    Game.show(form): 
<ul>  

__Parameters__:

`form` : `'Wide'` (***default***) or `'Narrow'`. 

__Returns__ : A dataframe with columns for each die, rows for each `N` rolls, and values as the rolled face if `form = 'Wide'`. If `form = 'Narrow'`, `Game.show()` returns a multi-index array where the roll number and die ID are the indices, and the value are the outcomes of the associated roll number and die ID. </ul>

#### Attributes:

    Game.dies: 

<ul> 

__Returns__ : a list of `monetcarlo.Die` objects passed through `montecarlo.Game()` during initialization. </ul>
    
### montecarlo.Analyzer

***class*** montecarlo.Analyzer

    montecarlo.Analyzer(Games)

__Initialization Parameters__:

Games : ***list of montecarlo.Game objects***.

#### Methods: 

    Analyzer.face_counts_per_roll() 

<ul> 

Counts the number of each possible face that was rolled for each roll event. 

__Returns__: the dataframe `Analyzer.face_counts`. </ul>

    Analyzer.jackpot(): 

<ul>

Counts the number of times all dice rolled the same face. 

__Returns__: the integer `Analyzer.num_jackpots`.</ul>

    Analyzer.Combo(): 

<ul>

Counts the frequency of a given combination of rolled faces, sorted in descending order based on frequency. 

__Returns__: the dataframe `Analyzer.combo`. </ul>

#### Attributes:

    Analyzer.game

<ul>

__Returns__: The game object passed through the Analyzer initialization method.</ul> 
    
    Analyzer.face_counts

<ul>

__Returns__: A dataframe where each row corresponds to a roll event, and each column is a face of the die object. The values of this dataframe correspond to the number of times a given face was rolled in a given roll event. Accessible only after executing the `Analyzer.face_counts_per_roll()` method. </ul>
    
    Analyzer.num_jackpots

<ul>

__Returns__: The number (***integer***) of times all dice rolled the same face. </ul>
    
    Analyzer.combo

<ul>

__Returns__: A multi-index dataframe where the indices are different combinations of rolled faces, and the values correspond to the number of times those faces were rolled. This dataframe is sorted in descending order, so combinations with the highest frequency of occurrence are at the top.  </ul>
