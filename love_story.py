"""
A Short, Non-Heteronormative Love Story.
"""

import nature
import random
from people import Girl, Boy

a = random.choice([Girl, Boy])()
b = random.choice([Girl, Boy])()

tree = nature.Tree()
a.sit_under(tree)
b.sit_under(tree)
a.kiss(b)
