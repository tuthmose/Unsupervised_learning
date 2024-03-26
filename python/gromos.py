import numpy as np
import random
import sys

from math import exp,sqrt
from scipy.spatial.distance import cdist,pdist,squareform

from base_clustering import generic_cluster_method
from clustering_run import clustering_run

class gromos_clustering(generic_cluster_method):
    """
    See Torda, A. E. & van Gunsteren, W. F. 
    Journal of computational chemistry 15, 1331–1340 (1994).
    A sort of average linkage
    """
    def __init__(self, **kwargs) -> None:
        """
        X(npoints,nfeatures) is the feature matrix
        D(npoints,npoints) is the distance/dissimilarity
        metric is the type of distance used
        metric=precomputed takes a precalculated distance matrix
        C is the cutoff
        scaledist is used to std distances
        """
        prop_defaults = {
            "metric"    : "euclidean",
            "C"         : 1.0,
            "scaledist" : True,
            "keep_data" : False,
            "name"      : "gromos"
        }
        for (prop, default) in prop_defaults.items():
            setattr(self, prop, kwargs.get(prop, default))         
        # check some input
        assert isinstance( self.C, float)
        assert isinstance( self.scaledist, bool)
        assert isinstance( self.keep_data, bool)
        
    def _run_gromos(self, N: int, D: nd.ndarray) -> np.ndarray:
        clusters: np.ndarray = -1*np.ones(self.N, dtype='int')
        a: int = 0
        while True:
            #index of point non assigned with highest number of neighbours
            new_med: int = np.argsort(np.count_nonzero(self.D[clusters==-1] <= self.C,axis=0))[-1]
            nn: int = 0
            for point:int in range(N):
                if D[point,new_med] <= self.C and clusters[point]==-1:
                    clusters[point] = new_med
                    nn += 1
            #print(clusters)
            if np.count_nonzero(clusters!=-1) == N or nn <= 1:
                break
        return clusters

    def __call__(self, N: int, D: nd.ndarray) -> np.ndarray:) -> np.ndarray:
      clusters: np.ndarray = self._run_gromos(N, D)
      return clusters
