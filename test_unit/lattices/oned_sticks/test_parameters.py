
from pathlib import Path

import src.lattices.oned_sticks.parameters as lparams



FPATH = f"{Path(__file__).parent.resolve()}"

lparams.create_configuration(FPATH)
