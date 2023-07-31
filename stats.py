import abc

from data_structures.referential_array import ArrayR

class Stats(abc.ABC):

    @abc.abstractmethod
    def get_attack(self):
        pass

    @abc.abstractmethod
    def get_defense(self):
        pass

    @abc.abstractmethod
    def get_speed(self):
        pass

    @abc.abstractmethod
    def get_max_hp(self):
        pass


class SimpleStats(Stats):

    def __init__(self, attack, defense, speed, max_hp) -> None:
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.max_hp = max_hp

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def get_max_hp(self):
        return self.max_hp
    
#ONLY FOR TESTING class SimpleStats
# monster_stats = SimpleStats(50, 30, 70, 100)

# print("Attack:", monster_stats.get_attack())    # Output: Attack: 50
# print("Defense:", monster_stats.get_defense())  # Output: Defense: 30
# print("Speed:", monster_stats.get_speed())      # Output: Speed: 70
# print("Max HP:", monster_stats.get_max_hp())    # Output: Max HP: 100

class ComplexStats(Stats):

    def __init__(
        self,
        attack_formula: ArrayR[str],
        defense_formula: ArrayR[str],
        speed_formula: ArrayR[str],
        max_hp_formula: ArrayR[str],
    ) -> None:
        # TODO: Implement
        pass

    def get_attack(self, level: int):
        raise NotImplementedError

    def get_defense(self, level: int):
        raise NotImplementedError

    def get_speed(self, level: int):
        raise NotImplementedError

    def get_max_hp(self, level: int):
        raise NotImplementedError
