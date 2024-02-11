import numpy as np
import random
import sys

from math import exp,sqrt
from scipy.spatial.distance import cdist,pdist,squareform

from clusteringRun import *  

class gromos_clustering:
    """
    See Torda, A. E. & van Gunsteren, W. F. 
    Journal of computational chemistry 15, 1331–1340 (1994).
    A sort of average linkage
    """
    def __init__(self, **kwargs) -> None:
        """
        X(npoints,nfeatures) is the feature matrix
        D(npoints,npoints) is the distance/dissimilarity (for PAM)
        metric is the type of distance used
        metric=precomputed takes a precalculated distance matrix
        C is the cutoff
        scaledist is used to std distances
        """
        prop_defaults = {
            "metric"    : "euclidean",
            "C"         : 1.0,
            "scaledist" : True
        }
        for (prop, default) in prop_defaults.items():
            setattr(self, prop, kwargs.get(prop, default))         
        # check some input
        assert isinstance( self.C, float)
        
    def _check_input_arrays(self, X: np.ndarray|None, D: np.ndarray|None) -> bool:
        if self.metric=="precomputed": 
            assert isinstance(D, np.ndarray) and isinstance(X, None)
            return False
        else:
            assert isinstance(X, np.ndarray) and isinstance(D, None)
            return True

    def _set_problem_size(self, X: np.ndarray|None, D: np.ndarray|None) -> int:
            if isinstance(X, np.ndarray):
                N = self.X.shape[0]
            if isinstance(D, np.ndarray):
                N = self.X.shape[0]
            return N
        
    def _calculate_distance_matrix(self, X: np.ndarray) -> np.ndarray:
        # pass to a triangular version
        D: np.ndarray = pdist(X, metric=self.metric)
        if self.scaledist:
            D = (D - np.mean(D))/np.std(D)
        return squareform(D)

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

    def _finalize(self, clusters: np.ndarray) -> (set, np.ndarray, float):   
        # use hinting when calling from functions?
        medoids = set(list(clusters[clusters!=-1]))
        singletons = np.where(clusters==-1)[0]
        inertia = .0
        for m in medoids:
            inertia = inertia + np.sum(D[clusters==m,:][:,m])
        return medoids, singletons, inertia

    def do_clustering(self, X=None, D=None) -> clusteringRun:
        # preliminary operations
        # what does scikit?
        # can I use numba here
        # force typing in init
        do_dist = self.check_input_arrays(X, D)
        N = self._set_problem_size
        if do_dist:
            D = self._calculate_distance_matrix(X) 
        # start algorithm
        clusters = self._run_gromos(N, D)
        # collect final descriptors
        medoids, singletons, inertia = self._finalize(clusters)
        nmedoids: int = len(medoids)
        singletons: int = len(singletons)
        # assemble dataclass
        XXX
        return run 
