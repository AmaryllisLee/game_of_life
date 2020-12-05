from World import *
import copy

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world   


    def survival_of_the_cell(self,n_a):
        """
        check if a cells is dead or alive based on the 4 rules
        :param n_a: de amount of alive neighbours a cell has
        :return: 0 (dead) or 1 (alive)
        """
        if sum(n_a) == 2 or sum(n_a) == 3:
            return 1
        return 0
    
    def evolve_generation(self):

        # make a deep copy ofth current world
        # Source: https://www.programiz.com/python-programming/shallow-deep-copy#:~:text=help%20of%20examples.-,Copy%20an%20Object%20in%20Python,reference%20of%20the%20original%20object.
        new_world = copy.deepcopy(self.world)
    
        for i in range(0,self.get_world().width):
            for j in range(0,self.get_world().height):
                a_n = self.get_world().get_neighbours(i,j)
                new_world.set(i,j, self.survival_of_the_cell(a_n))
        self.set_world(new_world)
        return(self.world)


    def update(self) -> World: # set_generation
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        #TODO: Do something to evolve the generation
        #transition_rules(self)
        self.evolve_generation()
    
        
        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world
    