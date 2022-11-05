from montecarlo import Die, Game, Analyzer
import unittest

class MontecarloTestSuite(unittest.TestCase):

    def test_change_weight(self):
        # Test that the change_weight() method of the Die class correctly changes the weight of the assigned face. 
        faces = [1,2,3,4]
        dice = Die(faces)
        dice.change_weight(3,2)
        df_faces_weights = dice.show_weights()
        assert df_faces_weights['Weights'][2] == 2

    def test_roll(self):
        # Test that the roll() method of the Die class generates a dataframe object with length N for number of rolls. 
        faces = [1,2,3,4]
        dice = Die(faces)
        dice.roll(num_rolls=10)
        assert len(dice.results) == 10

    def test_play(self):
        # Test that the play() method of the Game class generates a dataframe object with length N for number of rolls. 
        faces = [1,2,3,4]
        dice = Die(faces)
        game = Game([dice])
        game.play(10)
        assert len(game._results) == 10

    def test_show_wide(self):
        # Test that the show() method of the Game class generates a wide form dataframe object with length N for number of rolls and width W for number of dice. 
        faces = [1,2,3,4]
        dice = Die(faces)
        game = Game([dice,dice,dice])
        game.play(10)
        df = game.show()
        assert (df.shape[0] == 10 and df.shape[1]==3)     

    def test_show_narrow(self):
        # Test that the show() method of the Game class generates a narrow form dataframe object with length N x W for number of rolls N and number of dice W. 
        faces = [1,2,3,4]
        dice = Die(faces)
        game = Game([dice,dice,dice])
        game.play(10)
        df = game.show(form='Narrow')
        assert (len(df) == 30)

    def test_face_counts_per_roll(self):
        # Tests that the face_counts_per_roll() method of the Analyzer class produces a dataframe of size N x F for number of rolls N and number of faces F, and has an internal sum of values (face counts) equal to N x W for N number of rolls and W number of dice. 
        faces = [1,2,3,4,5]
        dice = Die(faces)
        game = Game([dice,dice,dice])
        game.play(20)
        Analysis=Analyzer(game)
        df = Analysis.face_counts_per_roll()
        shape = df.shape
        internal_sum = df.sum().sum()
        assert (shape[0]==20 and shape[1]==5 and internal_sum==60)

    def test_jackpot(self):
        # Tests that the jackpot() method of the Analyzer class returns an integer. 
        faces = [1,2,3,4,5]
        dice = Die(faces)
        game = Game([dice,dice,dice])
        game.play(20)
        Analysis=Analyzer(game)
        assert isinstance(Analysis.jackpot(),int) == True

    def test_combo(self):
        # Tests that the combo() method of the Analyzer class returns a dataframe of only 1 column with a sum of combinations equal to the number of rolls minus 1. 
        faces = [1,2,3,4,5,6]
        dice = Die(faces)
        game = Game([dice,dice,dice,dice,dice])
        game.play(1000)
        Analysis=Analyzer(game)
        Analysis.Combo()
        assert(Analysis.combo.shape[1]==1 and Analysis.combo['Count'].sum()==999)
                   
if __name__ == '__main__':

    unittest.main(verbosity=3)
