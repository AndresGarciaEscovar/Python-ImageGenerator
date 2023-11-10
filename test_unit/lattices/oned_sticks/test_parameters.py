
from pathlib import Path

import src.lattices.oned_sticks.parameters as lparams

print("\nTesting parameters.py")
configuration = lparams.get()
lparams.validate(configuration)
print("\nDone testing parameters.py")
