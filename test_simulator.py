from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)
    
    def test_survival_of_the_cell(self):
        #TODO figure out if cell is already dead or alive
        #check if cell has 0 to 1 neighbour and cell is dead
        self.assertEqual(self.sim.survival_of_the_cell(0), 0)
        self.assertEqual(self.sim.survival_of_the_cell(1), 0)

        #check if cell has 4 or  more neigbours and cell is dead
        self.assertEqual(self.sim.survival_of_the_cell(4),0)
        self.assertEqual(self.sim.survival_of_the_cell(5),0)
        self.assertEqual(self.sim.survival_of_the_cell(6),0)
        self.assertEqual(self.sim.survival_of_the_cell(7),0)
        self.assertEqual(self.sim.survival_of_the_cell(8),0)

        #check if cell has  2 or 3 neihbours and cell is alive
        self.assertEqual(self.sim.survival_of_the_cell(2),1)
        self.assertEqual(self.sim.survival_of_the_cell(3),1)


    # def test_transition_rules(self):
    #     """
    #     Test whether a cell follows the 4 "normal" rules of Game of Life 
    #     """
