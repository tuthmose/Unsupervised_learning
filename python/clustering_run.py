from dataclasses import dataclass
from numpy.typing import NDArray

import numpy as np

@dataclass
class clustering_run:
  """
  Creates a container class for the results of a cluster analysis run.
  Used by all methods
  For methods that define noise (e. g. DBSCAN) singletons and noise are the
  same thing
  Attributes should be self.explaining.
  Keywords is the list of specific keywords collected in init.
  """
  # check:
  # 1. how to return a custom datatype
  # 5. see if/how scikit learn accellerates
  # 6. add an ID, hash or timestamp
  X: NDArray[np.float32] | None
  D: NDArray[np.float32] | None
  medoids: NDArray
  nmedoids: int
  clusters: NDArray
  # these are just aliases; once the first attribute is created,
  # keep the alias inside the class
  nclusters: int
  singletons: NDArray | bool
  noise: NDArray | bool
  inertia: float
  keywords: dict
