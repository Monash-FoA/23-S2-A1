from monster_base import MonsterBase
# These classes inherit from MonsterBase,
# but you don't need to implement them explicitly.
from helpers import *
t:MonsterBase = Metalhorn(simple_mode=True, level=2)
h:MonsterBase = Flamikin(simple_mode=True, level=1)
print(t.get_simple_stats().get_attack()) #3
print(h.get_simple_stats().get_speed()) #2
print(str(t))
print("hey")