"""
Usage: prog <source> <target>
"""

import glob
import itertools
import random
import os
from jollaicon import icon
from docpie import docpie

collected = set()

for true_num in range(0, 4):
    result = [True for _ in range(true_num)]
    false_num = 4 - true_num
    result.extend(False for _ in range(false_num))
    collected.update(tuple(each) for each in itertools.permutations(result))

collected = list(collected)
args = docpie(__doc__)
source = args['<source>']
target_path = args['<target>']

for path in glob.glob(source + '/*.png'):
    _, file = os.path.split(path)
    style = random.choice(collected)
    target = os.path.join(target_path, file)
    icon(path, target, *style, bg=(0, 0, 0))