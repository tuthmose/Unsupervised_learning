import numpy as np

class clustering_run:
  """
  Creates a container class for the results of a cluster analysis run.
  Used by all methods
  For methods that define noise (e. g. DBSCAN) singletons and noise are the
  same thing
  Attributes should be self.explaining.
  Keywords is the list of specific keywords collected in init.
  """
  def __init__(self, method_name: str, keywords: dict,\
    medoids: np.ndarray,clusters: np.ndarray, singletons: np.ndarray,\
    inertia: np.float32, X: np.ndarray, D: np.ndarray) -> ???
    # check:
    # 1. how to return a custom datatype
    # 2. how dataclasses work
    # 3. how to set precision in np.ndarray and if the hint is correct
    # 4. how to hint lists
    # 5. see if/how scikit learn accellerates
    # 6. add an ID, hash or timestamp
    # 7. is or == in if
    self.method_name: str = method_name
    try:
      if keywords.keep_data == True:
        self.X: np.ndarray = X
        self.D: np.ndarray = D
    except:
      print("keep_data not defined for this run")
    self.medoids: list = medoids
    self.nmedoids: int = len(medoids)
    self.clusters: list = medoids
    # these are just aliases; once the first attribute is created,
    # keep the alias inside the class
    self.nclusters: int = self.nmedoids
    self.singletons: int = singletons
    self.noise: int = self.singletons
    self.inertia: float = inertia
    self.keywords: dict = keywords
    return None
