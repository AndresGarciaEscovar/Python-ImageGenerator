
from pathlib import Path

import src.lattices.oned_sticks.parameters as lparams


configuration = lparams.get()
lparams.validate(configuration)
