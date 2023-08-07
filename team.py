from __future__ import annotations
from enum import auto
from typing import Optional, TYPE_CHECKING

from base_enum import BaseEnum
from monster_base import MonsterBase
from random_gen import RandomGen
from helpers import get_all_monsters
from data_structures.referential_array import ArrayR    #This one for back
from data_structures.stack_adt import ArrayStack    #This one for Front 
from data_structures.array_sorted_list import ArraySortedList   #This one for optimize team_mode
from data_structures.sorted_list_adt import ListItem
from helpers import Flamikin, Aquariuma, Vineon, Normake, Thundrake, Rockodile, Mystifly, Strikeon, Faeboa, Soundcobra #for testing
if TYPE_CHECKING:
    from battle import Battle

class MonsterTeam:

    class TeamMode(BaseEnum):

        FRONT = auto()
        BACK = auto()
        OPTIMISE = auto()

    class SelectionMode(BaseEnum):

        RANDOM = auto()
        MANUAL = auto()
        PROVIDED = auto()

    class SortMode(BaseEnum):

        HP = auto()
        ATTACK = auto()
        DEFENSE = auto()
        SPEED = auto()
        LEVEL = auto()

    TEAM_LIMIT = 6
    counter = 0                                         #Track the monster index of add_to_team
    retrieve_counter = 0                                #Track the monster index of retrieve_from_team
    pokeman_size = 0                                    #Number of Monster currently in the team


    team_collection = ArrayR(TEAM_LIMIT)                #Array for TEAMMODE Back
    team_collection_sort = ArraySortedList(TEAM_LIMIT)  #Array for TEAMMODE Optimize
    team_collection_stack = ArrayStack(TEAM_LIMIT)      #Array for TEAMMODE Front 
    

    def __init__(self, team_mode: TeamMode, selection_mode, **kwargs) -> None:
        self.team_mode = team_mode
        # Add any preinit logic here.
        for value in kwargs.values():   #O(1)
            if isinstance(value, ArrayR) or isinstance(value, ArraySortedList) or isinstance(value, ArrayStack):
                if len(value) <= self.TEAM_LIMIT: 
                    for monster in value:                    
                        self.add_to_team(monster)
                        # print(self.team_collection)
                        
                else:
                    raise ValueError(f"The number of monsters in the team exceeds the allowed limit.\nThe current team limit is {self.TEAM_LIMIT}")
            if isinstance(value, MonsterTeam.SortMode):
                self.sort_mode = value

        if selection_mode == self.SelectionMode.RANDOM:
            self.select_randomly()
        elif selection_mode == self.SelectionMode.MANUAL:
            self.select_manually(**kwargs)
        elif selection_mode == self.SelectionMode.PROVIDED:
            self.select_provided(**kwargs)
        else:
            raise ValueError(f"selection_mode {selection_mode} not supported.")
        
    def __len__(self) -> int:
        """Returns the number of Monster in the team
        :complexity: O(1)
        """
        return self.pokeman_size
    
    def _update_keys(self): #Maybe need
        """Recalculate the keys for all monsters in the team."""
        for index, monster in enumerate(self.team_collection):
            
            monster.key = index

    def __str__(self):
        """Returns the number of Monster and team line-up
        :complexity: O(1)
        """
        if self.team_mode == self.TeamMode.FRONT:
            line_up = self.team_collection_stack.array
        elif self.team_mode == self.TeamMode.BACK:
            line_up = self.team_collection
        else:
            line_up = self.team_collection_sort
        return f"Number of Monsters in the team: {len(self)}\nTeam line-up: {line_up}"
    
    def add_to_team(self, monster: MonsterBase):


        if self.pokeman_size < self.TEAM_LIMIT:
            if self.team_mode == self.TeamMode.FRONT:
                self.team_collection_stack.push(monster)
           
            elif self.team_mode == self.TeamMode.BACK: #add to the back
            # Add the new monster to team_collection if there's room


                
                #WORKING DONT DELETE
                # if self.pokeman_size != 0:
                #     for i in range(self.pokeman_size, 0, -1):
                #         self.team_collection[i] = self.team_collection[i - 1]
                # self.team_collection[0] = monster

                #TESTING
                # if not self.index_stack.is_empty():
                #     print("POPED")
                #     self.team_collection[self.TEAM_LIMIT - len(self.index_stack)] = monster
                #     self.index_stack.pop()
                #     print(f"LEN STACK POP {len(self.index_stack)}")
                #     print(f"COUNTER {self.counter}")
                # else:
                #     self.team_collection[self.pokeman_size] = monster
                # print(self.team_collection)

                #TEST
                # self.team_collection[self.counter] = monster
                # if self.counter == self.TEAM_LIMIT-1:
                #     self.counter = 0 #End of the array, return to the first one, also retrieve monster from here
                # else:
                #     self.counter += 1
                
                #TEST
                
                self.team_collection[self.counter] = monster
                self.counter = (self.counter + 1) % self.TEAM_LIMIT #(0 + 1) % 6 = 0, (1 + 1) % 6 = 1, ... (5 + 1) % 6 = 0, (6 + 1) % 6 = 1
                
            elif self.team_mode == self.TeamMode.OPTIMISE:

                 #Create monster's instance to access data
                #REAL
                

                sort_key = monster().get_attack()
                monster = ListItem(monster,sort_key)
                self.team_collection_sort.add(monster)
                
                

                
            self.pokeman_size += 1
            
        else:
            raise ValueError(f"The team is already full.\nThere are currently {self.pokeman_size} Monster(s) in the team")


    def retrieve_from_team(self) -> MonsterBase:

        if self.pokeman_size == 0:
            raise ValueError("The team is empty")
        else:
            if self.team_mode == self.TeamMode.FRONT:
                return self.team_collection_stack.pop()
            elif self.team_mode == self.TeamMode.BACK:
                #WORKING DO NOT DELETE
                # monster_retrieved = self.team_collection[self.pokeman_size-1]
                # self.pokeman_size -= 1
                # return monster_retrieved
                
                #FINAL
                # self.index_stack.push(self.counter)
                # print(f"BEFORE COUNTER {self.counter}")
                # if self.counter >= self.TEAM_LIMIT - 1:
                #     self.counter = 0
                # else:
                #     self.counter += 1
                
                # print(f"AFTER COUNTER {self.counter}")
                # monster_retrieve = self.team_collection[self.index_stack.peek()]
                # print(f"len stack {len(self.index_stack)}")
                # print(self.team_collection)
                # self.pokeman_size -= 1
                
                
                # if self.counter == self.TEAM_LIMIT-1:
                #     self.counter = 0 #End of the array, return to the first one, also retrieve monster from here
                # else:
                #     self.counter += 1
                # self.pokeman_size -= 1
                # monster_retrieve = self.team_collection[self.counter]
                # print(f'counter {self.counter}')
                # print(self.team_collection)

                #FINAL FINAL BOI

                
                monster_retrieve = self.team_collection[self.retrieve_counter]

                self.team_collection[self.retrieve_counter] = None
                self.retrieve_counter = (self.retrieve_counter + 1) % self.TEAM_LIMIT

                
                self.pokeman_size -= 1
                return monster_retrieve
                
            else:
                
                retrieve_from = self.team_collection_sort
        
        


    def special(self) -> None:
        raise NotImplementedError

    def regenerate_team(self) -> None:
        raise NotImplementedError

    def select_randomly(self):
        team_size = RandomGen.randint(1, self.TEAM_LIMIT)
        monsters = get_all_monsters()
        n_spawnable = 0
        for x in range(len(monsters)):
            if monsters[x].can_be_spawned():
                n_spawnable += 1

        for _ in range(team_size):
            spawner_index = RandomGen.randint(0, n_spawnable-1)
            cur_index = -1
            for x in range(len(monsters)):
                if monsters[x].can_be_spawned():
                    cur_index += 1
                    if cur_index == spawner_index:
                        # Spawn this monster
                        self.add_to_team(monsters[x]()) #####SOMETHING IS WRONG HERE
                        break
            else:
                raise ValueError("Spawning logic failed.")

    def select_manually(self):
        """
        Prompt the user for input on selecting the team.
        Any invalid input should have the code prompt the user again.

        First input: Team size. Single integer
        For _ in range(team size):
            Next input: Prompt selection of a Monster class.
                * Should take a single input, asking for an integer.
                    This integer corresponds to an index (1-indexed) of the helpers method
                    get_all_monsters()
                * If invalid of monster is not spawnable, should ask again.

        Add these monsters to the team in the same order input was provided. Example interaction:

        How many monsters are there? 2
        MONSTERS Are:
        1: Flamikin [✔️]
        2: Infernoth [❌]
        3: Infernox [❌]
        4: Aquariuma [✔️]
        5: Marititan [❌]
        6: Leviatitan [❌]
        7: Vineon [✔️]
        8: Treetower [❌]
        9: Treemendous [❌]
        10: Rockodile [✔️]
        11: Stonemountain [❌]
        12: Gustwing [✔️]
        13: Stormeagle [❌]
        14: Frostbite [✔️]
        15: Blizzarus [❌]
        16: Thundrake [✔️]
        17: Thunderdrake [❌]
        18: Shadowcat [✔️]
        19: Nightpanther [❌]
        20: Mystifly [✔️]
        21: Telekite [❌]
        22: Metalhorn [✔️]
        23: Ironclad [❌]
        24: Normake [❌]
        25: Strikeon [✔️]
        26: Venomcoil [✔️]
        27: Pythondra [✔️]
        28: Constriclaw [✔️]
        29: Shockserpent [✔️]
        30: Driftsnake [✔️]
        31: Aquanake [✔️]
        32: Flameserpent [✔️]
        33: Leafadder [✔️]
        34: Iceviper [✔️]
        35: Rockpython [✔️]
        36: Soundcobra [✔️]
        37: Psychosnake [✔️]
        38: Groundviper [✔️]
        39: Faeboa [✔️]
        40: Bugrattler [✔️]
        41: Darkadder [✔️]
        Which monster are you spawning? 38
        MONSTERS Are:
        1: Flamikin [✔️]
        2: Infernoth [❌]
        3: Infernox [❌]
        4: Aquariuma [✔️]
        5: Marititan [❌]
        6: Leviatitan [❌]
        7: Vineon [✔️]
        8: Treetower [❌]
        9: Treemendous [❌]
        10: Rockodile [✔️]
        11: Stonemountain [❌]
        12: Gustwing [✔️]
        13: Stormeagle [❌]
        14: Frostbite [✔️]
        15: Blizzarus [❌]
        16: Thundrake [✔️]
        17: Thunderdrake [❌]
        18: Shadowcat [✔️]
        19: Nightpanther [❌]
        20: Mystifly [✔️]
        21: Telekite [❌]
        22: Metalhorn [✔️]
        23: Ironclad [❌]
        24: Normake [❌]
        25: Strikeon [✔️]
        26: Venomcoil [✔️]
        27: Pythondra [✔️]
        28: Constriclaw [✔️]
        29: Shockserpent [✔️]
        30: Driftsnake [✔️]
        31: Aquanake [✔️]
        32: Flameserpent [✔️]
        33: Leafadder [✔️]
        34: Iceviper [✔️]
        35: Rockpython [✔️]
        36: Soundcobra [✔️]
        37: Psychosnake [✔️]
        38: Groundviper [✔️]
        39: Faeboa [✔️]
        40: Bugrattler [✔️]
        41: Darkadder [✔️]
        Which monster are you spawning? 2
        This monster cannot be spawned.
        Which monster are you spawning? 1
        """
        raise NotImplementedError

    def select_provided(self, provided_monsters:Optional[ArrayR[type[MonsterBase]]]=None):
        """
        Generates a team based on a list of already provided monster classes.

        While the type hint imples the argument can be none, this method should never be called without the list.
        Monsters should be added to the team in the same order as the provided array.

        Example input:
        [Flamikin, Aquariuma, Gustwing] <- These are all classes.

        Example team if in TeamMode.FRONT:
        [Gustwing Instance, Aquariuma Instance, Flamikin Instance]
        """
        raise NotImplementedError

    def choose_action(self, currently_out: MonsterBase, enemy: MonsterBase) -> Battle.Action:
        # This is just a placeholder function that doesn't matter much for testing.
        from battle import Battle
        if currently_out.get_speed() >= enemy.get_speed() or currently_out.get_hp() >= enemy.get_hp():
            return Battle.Action.ATTACK
        return Battle.Action.SWAP

if __name__ == "__main__":
    # my_monsters = ArrayR(4)
    # my_monsters[0] = Flamikin
    # my_monsters[1] = Aquariuma
    # my_monsters[2] = Vineon
    # my_monsters[3] = Thundrake

    RandomGen.set_seed(123456789)
    team = MonsterTeam(
        team_mode=MonsterTeam.TeamMode.BACK,
        selection_mode=MonsterTeam.SelectionMode.RANDOM
    )

    m1 = team.retrieve_from_team()
    m2 = team.retrieve_from_team()
    m3 = team.retrieve_from_team()
    m4 = team.retrieve_from_team()
    m5 = team.retrieve_from_team()
    m6 = team.retrieve_from_team()
    team.add_to_team(Flamikin)
    team.add_to_team(Aquariuma)
    team.add_to_team(Vineon)
    team.add_to_team(Thundrake)
    team.add_to_team(Aquariuma)
    m7 = team. retrieve_from_team()
    m7 = m7()
    print("Add after this")
    team.add_to_team(Thundrake)
    m8 = team.retrieve_from_team()
    m9 = team.retrieve_from_team()
    
    # print(f"M1: {type(m1)}")
    # print(f"M2: {type(m2)}")
    # print(f"M3: {type(m3)}")
    print(f"M1: {m1}")
    print(f"M2: {m2}")
    print(f"M3: {m3}")
    print(f"M4: {m4}")
    print(f"M4: {m5}")
    print(f"M4: {m6}")
    print(f"M7 {m7}")
    print(f"M8 {m8}")
    print(f"M9 {m9}")
    print(team)

    #monster_retrieved.value.__class__ Find the class


    # team = MonsterTeam(
    #     team_mode=MonsterTeam.TeamMode.OPTIMISE,
    #     selection_mode=MonsterTeam.SelectionMode.RANDOM,
    #     sort_key=MonsterTeam.SortMode.HP, bla = my_monsters
    # )
    # print(team.retrieve_from_team())
    # while len(team):
    #     print(team.retrieve_from_team())
