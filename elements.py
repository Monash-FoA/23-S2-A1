from __future__ import annotations

from enum import auto
from typing import Optional

from base_enum import BaseEnum

from data_structures.referential_array import ArrayR

class Element(BaseEnum):
    """
    Element Class to store all different elements as constants, and associate indicies with them.

    Example:
    ```
    print(Element.FIRE.value)         # 1
    print(Element.GRASS.value)        # 3

    print(Element.from_string("Ice")) # Element.ICE
    ```
    """

    FIRE = auto()
    WATER = auto()
    GRASS = auto()
    BUG = auto()
    DRAGON = auto()
    ELECTRIC = auto()
    FIGHTING = auto()
    FLYING = auto()
    GHOST = auto()
    GROUND = auto()
    ICE = auto()
    NORMAL = auto()
    POISON = auto()
    PSYCHIC = auto()
    ROCK = auto()
    FAIRY = auto()
    DARK = auto()
    STEEL = auto()

    @classmethod
    def from_string(cls, string: str) -> Element:
        for elem in Element:
            if elem.name.lower() == string.lower():
                return elem
        raise ValueError(f"Unexpected string {string}")

class EffectivenessCalculator:
    """
    Helper class for calculating the element effectiveness for two elements.

    This class follows the singleton pattern.

    Usage:
        EffectivenessCalculator.get_effectiveness(elem1, elem2)
    """

    instance: Optional[EffectivenessCalculator] = None

    def __init__(self, element_names: ArrayR[str], effectiveness_values: ArrayR[float]) -> None:
        """
        Initialise the Effectiveness Calculator.

        The first parameter is an ArrayR of size n containing all element_names.
        The second parameter is an ArrayR of size n*n, containing all effectiveness values.
            The first n values in the array is the effectiveness of the first element
            against all other elements, in the same order as element_names.
            The next n values is the same, but the effectiveness of the second element, and so on.

        Example:
        element_names: ['Fire', 'Water', 'Grass']
        effectivness_values: [0.5, 0.5, 2, 2, 0.5, 0.5, 0.5, 2, 0.5]
        Fire is half effective to Fire and Water, and double effective to Grass [0.5, 0.5, 2]
        Water is double effective to Fire, and half effective to Water and Grass [2, 0.5, 0.5]
        Grass is half effective to Fire and Grass, and double effective to Water [0.5, 2, 0.5]
        """
        self.element_names = element_names
        self.effectiveness_values = effectiveness_values

    @classmethod
    def get_effectiveness(cls, type1: Element, type2: Element) -> float:
        """
        Returns the effectivness of elem1 attacking elem2.
        
        Example: EffectivenessCalculator.get_effectiveness(Element.FIRE, Element.WATER) == 0.5
        """
        if not isinstance(type1, Element) and not isinstance(type2, Element):    #WORST & BEST: O(1) Type checks, constant time operations, complexity is O(1) since they do not depend on the size of any data structure.
            raise ValueError("Arguments must be valid Element Enum values.")
        
        type1_index = None  #WORST & BEST: O(1) Assigning a value to a variable doesn't depend on the input size. Constant time operations
        type2_index = None  #WORST & BEST: O(1) Assigning a value to a variable doesn't depend on the input size. Constant time operations
        num_type = int(len(cls.instance.effectiveness_values)**0.5) #WORST & BEST: O(1) Calculating the length of a list and taking the square root are both constant time operations. Constant time complexity

        for index, name in enumerate(cls.instance.element_names):   #WORST: O(n) This loop iterates through the array, which contains n elements, where n is the number of elements in the array
            temp_name = Element.from_string(name)                   #BEST: O(1) If both elements are found at the beginning of the list
            if type1_index is None and temp_name == type1:  #Added None checking, if type1 or type2_index has a value, the code will skip checking temp_name == type1/2
                type1_index = index
            if type2_index is None and temp_name == type2:
                type2_index = index

        type_position = type1_index * num_type + type2_index    #WORST & BEST: O(1)
        type_value = cls.instance.effectiveness_values[type_position]   #WORST & BEST: O(1)
        
        return type_value
    
        #get_effectiveness has the complexity of O(n)

    @classmethod
    def from_csv(cls, csv_file: str) -> EffectivenessCalculator:
        # NOTE: This is a terrible way to open csv files, if writing your own code use the `csv` module.
        # This is done this way to facilitate the second half of the task, the __init__ definition.
        with open(csv_file, "r") as file:
            header, rest = file.read().strip().split("\n", maxsplit=1)
            header = header.split(",")
            rest = rest.replace("\n", ",").split(",")
            a_header = ArrayR(len(header))
            a_all = ArrayR(len(rest))
            for i in range(len(header)):
                a_header[i] = header[i]
            for i in range(len(rest)):
                a_all[i] = float(rest[i])
            return EffectivenessCalculator(a_header, a_all)

    @classmethod
    def make_singleton(cls):
        cls.instance = EffectivenessCalculator.from_csv("type_effectiveness.csv")

EffectivenessCalculator.make_singleton()


if __name__ == "__main__":
    print(EffectivenessCalculator.get_effectiveness(Element.FIRE, Element.WATER))       #0.5
    print(EffectivenessCalculator.get_effectiveness(Element.FIRE, Element.GRASS))       #2
    print(EffectivenessCalculator.get_effectiveness(Element.NORMAL, Element.GHOST))     #0
    print(EffectivenessCalculator.get_effectiveness(Element.DRAGON, Element.DRAGON))    #2
    print(EffectivenessCalculator.get_effectiveness(Element.WATER, Element.GRASS))      #0.5
    
    
    


