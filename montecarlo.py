import numpy as np
import pandas as pd
class Die:
    """ INITIALIZATION
        INPUTS: 
            faces = a list of possible outcomes for a given random event. For example, for a 6-sided die, faces would 
                    be a list of length 6 where each element represents a face of the dice. By default, the Die class
                    assumes equal probabilistic weights for each possible outcome. 
        ATTRIBUTES:
            Die.faces = a list of possible outcomes associated with the Die object. 
            Die._weight = a list of weights associated with each face of the Die object. 
            Die._faces_weight = a dataframe of faces and weights associated with the Die object. 
            Die.results = Accesible only after the roll() method has been executed, Die.results returns a dataframe with 
                    the roll number as the index and the value as the outcome of the rolled die. 
        METHODS:
            change_weight(face, new weight): To alter the default equal weight among die faces, pass the face you wish 
            the change the weight of and the weight to which to change it to the change_weight() method. 
            roll(num_rolls): Rolls the die num_rolls times. Stores results of each roll in .results as a dataframe. 
            show_weights(): Returns a dataframe of the die faces and their corresponding weights.  
    """
    def __init__(self, faces):
        self.faces = faces
        self._weight = np.ones(len(faces))
        self._faces_weight = pd.DataFrame({'Faces':self.faces,'Weights':self._weight})
    
    def change_weight(self, face, new_weight):
        """change_weight(face, new weight): To alter the default equal weight among die faces, pass the face you wish 
            the change the weight of and the weight to which to change it to the change_weight() method. """
        if face in self.faces:
            if isinstance(new_weight,float):
                self._faces_weight.loc[self._faces_weight["Faces"] == face, "Weights"] = new_weight
            else:
                try:
                    float(new_weight)
                    self._faces_weight.loc[self._faces_weight["Faces"] == face, "Weights"] = new_weight
                except:
                    raise Exception('New weight must be float or convertable to float!')

        else:
            raise Exception('Face is not in list of faces') 
    
    def roll(self,num_rolls=1):
        """Rolls the die num_rolls times using np.random.choice. Stores results of each roll in .results as a dataframe. """
        self._faces_weight['Probability'] = self._faces_weight['Weights']/self._faces_weight['Weights'].sum()
        outcomes = np.random.choice(self._faces_weight['Faces'],size=num_rolls, p=self._faces_weight['Probability'])
        self.results = pd.DataFrame({'Results':outcomes})
        self.results.index.name = 'Roll'

    def show_weights(self):
        """Returns a dataframe of the die faces and their corresponding weights."""
        return self._faces_weight[['Faces','Weights']]

class Game():
    """ INITIALIZATION
        INPUTS: 
            dies: a list of die objects created by the Die class. Each die object must have the same faces, although each die 
                object can have different weights associated with the die faces. 
        ATTRIBUTES:
            Game.dies: a list of die objects passed through the Game initialization method. 
            Game._results: Accessible only after the play() method has been executed. Each row corresponds to a roll, and
                each column corresponds to an outcome of one of the die objects.  
        METHODS:
            Game.play(N): Rolls each die object N times, stores results in a dataframe Game._results. 
            Game.show(form='Wide'): form = 'Wide' (default) or form = 'Narrow'. If form = 'Wide', Game.show() returns 
                the Game._results dataframe. If form = 'Narrow', Game.show() returns a multi-index array where the roll 
                number and die ID are the indices, and the value are the outcomes of the associates roll number and die ID. 
    """
    def __init__(self, dies):
        if isinstance(dies,list):
            self.dies = dies
        else:
            raise Exception('Dies object must be passed as a list!')
        
    def play(self, N):
        """Rolls each die object N times, stores results in a dataframe Game._results. """
        self._results = pd.DataFrame()
        i = 1
        for die in self.dies:
            die.roll(num_rolls = N)
            self._results[f"Die #{i}"] = die.results['Results'] 
            i += 1

    def show(self,form='Wide'):
        """form = 'Wide' (default) or form = 'Narrow'. If form = 'Wide', Game.show() returns 
                the Game._results dataframe. If form = 'Narrow', Game.show() returns a multi-index array where the roll 
                number and die ID are the indices, and the value are the outcomes of the associates roll number and die ID. """
        if form == 'Wide':
            return self._results
        elif form == 'Narrow':
            self._results['Roll'] = self._results.index
            narrow = pd.wide_to_long(self._results, stubnames = 'Die #',i=["Roll"],j='Die')
            narrow = narrow.rename(columns={'Die #':'Result'})
            return narrow

class Analyzer():
    """ INITIALIZATION
        INPUTS: 
            game: the game object generated by the Game class. 
        ATTRIBUTES:
            Analyzer.game: the game object passed through the Analyzer initialization method. 
            Analyzer.face_counts: Accessible after executing the face_counts_per_roll() method. Analyzer.face_counts is a dataframe
                where each row corresponds to a roll event, and each column is a face of the die object. The values of this dataframe
                correspond to the number of times a given face was rolled in a given roll event. 
            Analyzer.num_jackpots: The number of times all dice rolled the same face. 
            Analyzer.combo: A multi-index dataframe where the indices are different combinations of rolled faces, and the values correspond
                to the number of times those faces were rolled. This dataframe is sorted in descending order, so combinations with the highest
                frequency of occurrence are at the top.  
        METHODS:
            Analyzer.face_counts_per_roll(): Counts the number of each possible face that was rolled for each roll event. Returns the dataframe
                .face_counts. 
            Analyzer.jackpot(): Counts the number of times all dice rolled the same face. Returns the integer .num_jackpots.
            Analyzer.Combo(): Counts the frequency of a given combination of rolled faces, sorted in descending order based on frequency. 
                Returns the dataframe .combo. 

    """
    def __init__(self, game):
        self.game = game
    
    def face_counts_per_roll(self):
        """Counts the number of each possible face that was rolled for each roll event using pd.get_dummies. Returns the dataframe .face_counts. """
        face_counts = self.game.show(form='Narrow')
        face_counts = pd.get_dummies(face_counts.Result)
        self.face_counts = face_counts.groupby(['Roll']).sum()
        return self.face_counts

    def jackpot(self):
        """Counts the number of times all dice rolled the same face. Returns the integer .num_jackpots."""
        self.face_counts_per_roll()
        jackpotdf = self.face_counts.apply(lambda x: np.count_nonzero(x, axis=0),axis=1)
        self.jackpotdf = jackpotdf.loc[jackpotdf == 1]
        num_jackpots = len(self.jackpotdf)
        return num_jackpots
    
    def Combo(self):
        """Counts the frequency of a given combination of rolled faces, sorted in descending order based on frequency. Returns the dataframe .combo. """
        self.face_counts_per_roll()
        self.combo = pd.pivot_table(self.game.show(), index=self.game.show().columns.to_list()[:-1],aggfunc=np.count_nonzero)
        self.combo = self.combo.rename(columns = {'Roll':'Count'})
        self.combo = self.combo.sort_values(by='Count',ascending=False)