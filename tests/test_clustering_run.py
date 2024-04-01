from numpy.typing import NDArray

import numpy as np
import pytest
import scipy as sp

from .context import clustering_run

@pytest.fixture
def cluster_run():
  kd: bool = True
  metric: str = "euclidean"
  size: int = (50,10)
  kwd: dict = {"metric":"euclidean", "C": 1.0}
  X: NDArray = np.asarray(np.random.rand(size[0], size[1]), dtype=np.float32)
  D: NDArray = sp.spatial.distance.squareform(\
    sp.spatial.distance.pdist(X, metric=metric))
  nm: int = 3
  m: NDArray = np.random.randin(low=0, high=size[0], size=nm)
  cl: NDArray = np.random.choice(m, size=size[0])
  ncl: int = len(cl)
  sg: bool = False
  nn: bool = sg
  inrt: float = np.random.rand()
  sample_data = clustering_run.clustering_run(X, D, m, nm, cl, ncl, sg, nn, inrt, kdws)

def test_values_should_be_present(cluster_run: clustering_run):
  # singletons / noise not tested
  assert isinstance(cluster_run.X, np.ndarray)
  assert isinstance(cluster_run.D, np.ndarray)
  assert isinstance(cluster_run.medoids, np.ndarray)
  assert isinstance(cluster_run.clusters, np.ndarray)
  assert isinstance(cluster_run.nmedoids, int)
  assert isinstance(cluster_run.nclusters, int)
  assert isinstance(cluster_run.inertia, float)
  assert isinstance(cluster_run.keywords, dict)
