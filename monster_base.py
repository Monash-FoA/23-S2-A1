from __future__ import annotations
import abc

from stats import Stats

class MonsterBase(abc.ABC):

    def __init__(self, simple_mode=True, level:int=1) -> None:
        """
        Initialise an instance of a monster.

        :simple_mode: Whether to use the simple or complex stats of this monster
        :level: The starting level of this monster. Defaults to 1.
        """
        self.simple_mode = simple_mode
        self.level = level
        self.hp = Stats.get_max_hp

    def get_level(self):
        """The current level of this monster instance"""
        return self.level

    def level_up(self):
        """Increase the level of this monster instance by 1"""
        return (self.level + 1)

    def get_hp(self):
        """Get the current HP of this monster instance"""
        return self.hp

    def set_hp(self, val):
        """Set the current HP of this monster instance"""
        self.hp = val
        return self.hp

    def get_attack(self):
        """Get the attack of this monster instance"""
        return Stats.get_attack

    def get_defense(self):
        """Get the defense of this monster instance"""
        return Stats.get_defense

    def get_speed(self):
        """Get the speed of this monster instance"""
        return Stats.get_speed

    def get_max_hp(self):
        """Get the maximum HP of this monster instance"""
        return Stats.get_max_hp

    def alive(self) -> bool:
        """Whether the current monster instance is alive (HP > 0 )"""
        if self.get_hp > 0:
            return True
        else:
            return False

    def attack(self, other: MonsterBase):
        """Attack another monster instance"""
        # Step 1: Compute attack stat vs. defense stat
        if other.get_defense < (self.get_attack/2):
            damage = self.get_attack - other.get_defense
        elif other.get_defense < self.get_attack:
            damage = (self.get_attack * (5/8)) - (other.get_defense / 4)
        else:
            damage = self.get_attack/4
        # Step 2: Apply type effectiveness
        # Step 3: Ceil to int
        # Step 4: Lose HP
        raise NotImplementedError

    def ready_to_evolve(self) -> bool:
        """Whether this monster is ready to evolve. See assignment spec for specific logic."""
        temp = self.get_simple_stats(self)
        if self.get_evolution == None:
            return False
        elif self.get_level == 1: #??????????
            print("not done")

    def evolve(self) -> MonsterBase:
        """Evolve this monster instance by returning a new instance of a monster class."""
        temp = self.get_evolution(self)

        health_diff = (self.get_max_hp - self.get_hp)

        temp_health = (temp.get_hp - health_diff)

        temp.set_hp(temp_health) #Setting the new hp

        return temp 

    ### NOTE
    # Below is provided by the factory - classmethods
    # You do not need to implement them
    # And you can assume they have implementations in the above methods.

    @classmethod
    @abc.abstractmethod
    def get_name(cls) -> str:
        """Returns the name of the Monster - Same for all monsters of the same type."""
        pass

    @classmethod
    @abc.abstractmethod
    def get_description(cls) -> str:
        """Returns the description of the Monster - Same for all monsters of the same type."""
        pass

    @classmethod
    @abc.abstractmethod
    def get_evolution(cls) -> type[MonsterBase]:
        """
        Returns the class of the evolution of the Monster, if it exists.
        Same for all monsters of the same type.
        """
        pass

    @classmethod
    @abc.abstractmethod
    def get_element(cls) -> str:
        """
        Returns the element of the Monster.
        Same for all monsters of the same type.
        """
        pass

    @classmethod
    @abc.abstractmethod
    def can_be_spawned(cls) -> bool:
        """
        Returns whether this monster type can be spawned on a team.
        Same for all monsters of the same type.
        """
        pass

    @classmethod
    @abc.abstractmethod
    def get_simple_stats(cls) -> Stats:
        """
        Returns the simple stats class for this monster, if it exists.
        Same for all monsters of the same type.
        """
        pass

    @classmethod
    @abc.abstractmethod
    def get_complex_stats(cls) -> Stats:
        """
        Returns the complex stats class for this monster, if it exists.
        Same for all monsters of the same type.
        """
        pass
