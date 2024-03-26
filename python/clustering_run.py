import numpy as np
from numpy.typing import NDArray

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
  # 7. is or == in if
  try:
    if keywords.keep_data == True:
      X: NDArray[np.float32]
      D: NDArray[np.float32]
  except:
    print("keep_data not defined for this run")
  medoids: list
  nmedoids: int
  clusters: list
  # these are just aliases; once the first attribute is created,
  # keep the alias inside the class
  nclusters: int
  singletons: int
  noise: int
  inertia: float
  keywords: dict
