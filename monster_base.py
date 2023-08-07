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
        self.level_evolve = level
        if simple_mode:
            self.stats = self.get_simple_stats()
        else:
            self.stats = self.get_complex_stats()
        #self.stats = self.get_simple_stats() if simple_mode else self.get_complex_stats()
        self.hp = self.get_max_hp() #Base Hp == max hp, can be adjusted by set_hp
        
    def __str__(self):
        """Return a string representation of the Monster instance."""
        return f"LV.{self.level} {self.get_name()}, {self.hp}/{self.get_max_hp()} HP"
        
    def get_level(self):
        """The current level of this monster instance"""
        return self.level

    def level_up(self):
        """Increase the level of this monster instance by 1"""
        original_max_hp = self.get_max_hp()         #Save the original HP
        original_hp = self.hp

        self.level_evolve = self.level          #The level before lvling up
        self.level += 1
        self.set_hp(self.get_max_hp() - (original_max_hp - original_hp))

        #Ratio way
        # ratio_max_hp = self.get_max_hp() / original_max_hp
        # if self.get_max_hp() % original_max_hp:
        #     self.set_hp(int((self.hp*ratio_max_hp)+1)) #ceil
        # else:
        #     self.set_hp(int(self.hp*ratio_max_hp))

    def get_hp(self):
        """Get the current HP of this monster instance"""
        return self.hp

    def set_hp(self, val):
        """Set the current HP of this monster instance"""
        self.hp = val #if val changes, self.hp changes

    def get_attack(self):
        """Get the attack of this monster instance"""
        return self.stats.get_attack()

    def get_defense(self):
        """Get the defense of this monster instance"""
        return self.stats.get_defense()

    def get_speed(self):
        """Get the speed of this monster instance"""
        return self.stats.get_speed()

    def get_max_hp(self):
        """Get the maximum HP of this monster instance"""
        return self.stats.get_max_hp()

    def alive(self) -> bool:
        """Whether the current monster instance is alive (HP > 0 )"""
        return self.hp > 0
    
    def attack(self, other: MonsterBase): #NOTE: other is the enemy (other has similar structures)
        """Check if your Pokeman is still alive""" #BASE
        if not self.alive(): #your Pokeman is ded
            raise ValueError("Stop, Stop! Your Monster is already fainted")
        if not other.alive(): #Don't attack ded Monster pls :( 
            raise ValueError("Stop, Stop! The Opponent is already fainted")
        
        """Compare speed"""
        self_speed = self.stats.get_speed()
        other_speed = other.stats.get_speed()
        #Self attack first
        if self_speed > other_speed:
            self.attack_single(other)
            if other.alive():
                other.attack_single(self)

        #Self attack second
        elif self_speed < other_speed:
            other.attack_single(self)
            if self.alive():
                self.attack_single(other)
        
        #Same speed (ignoring whether the attack they are receiving would kill them.)
        else:
            self.attack_single(other)
            other.attack_single(self)

    def attack_single (self, other: MonsterBase):
        """Attack another monster instance"""
        # Step 1: Compute attack stat vs. defense stat
        attack_stat = self.stats.get_attack()
        defense_stat = other.stats.get_defense()
        damage = 0

        if defense_stat < attack_stat / 2:
            damage = attack_stat - defense_stat
        elif defense_stat < attack_stat:
            damage = attack_stat * 5/8 - defense_stat / 4
        else:
            damage = attack_stat / 4
        
        # Step 2: Apply type effectiveness
        #If type effectiveness applicable?
        #TODO
        effective_damage = damage * 2

        # Step 3: Ceil to int
        effective_damage = int(effective_damage + 1)  # Round up to the nearest (larger?) integer

        # Step 4: Lose HP
        other.set_hp(other.get_hp() - effective_damage)  

        if self.alive() and not other.alive(): #level up
            self.level_up()

    def ready_to_evolve(self) -> bool:
        """Whether this monster is ready to evolve. See assignment spec for specific logic."""
        return self.level_evolve != self.level and self.get_evolution() is not None

    def evolve(self) -> MonsterBase:
        """Evolve this monster instance by returning a new instance of a monster class."""
        evolution_class = self.get_evolution()
        if self.ready_to_evolve():
            evolved_monster = evolution_class(simple_mode=self.simple_mode, level=self.level)
            evolved_monster.set_hp(evolved_monster.get_max_hp() - (self.get_max_hp() - self.hp))
            return evolved_monster
        else:
            raise ValueError("The Monster cannot evolve")

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
