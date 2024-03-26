import numpy as np
from numpy.typing import NDArray

from clustering_run import clustering_run

class generic_cluster_method:
    """
    base class for clustering, which includes generic methods
    """
    def __init__(self, **kwargs) -> None:
        """
        X(npoints,nfeatures) is the feature matrix
        D(npoints,npoints) is the distance/dissimilarity
        metric is the type of distance used
        metric=precomputed takes a precalculated distance matrix
        C is the cutoff
        scaledist is used to std distances
        keep_data is True if the final dataclass has to include
        D and X
        """
        prop_defaults = {
            "metric"    : "euclidean",
            "keep_data" : False,
            "name"      : "generic"
        }
        for (prop, default) in prop_defaults.items():
            setattr(self, prop, kwargs.get(prop, default))         
        
    def _check_input_arrays(self, X: NDArray[np.float32]|None, D: NDArray[np.float32]|None) -> bool:
        if self.metric=="precomputed": 
            assert isinstance(D, NDArray[np.float32]) and isinstance(X, None)
            return False
        else:
            assert isinstance(X, NDArray[np.float32]) and isinstance(D, None)
            return True

    def _set_problem_size(self, X: NDArray[np.float32]|None, D: NDArray[np.float32]|None) -> int:
            if isinstance(X, NDArray[np.float32]):
                N = self.X.shape[0]
            if isinstance(D, NDArray[np.float32]):
                N = self.X.shape[0]
            return N
        
    def _calculate_distance_matrix(self, X: NDArray[np.float32]) -> NDArray[np.float32]:
        # TODO pass to a triangular version
        D: NDArray[np.float32] = pdist(X, metric=self.metric)
        if self.scaledist:
            D = (D - np.mean(D))/np.std(D)
        return squareform(D)

    def _run_gromos(self, N: int, D: nd.ndarray) -> NDArray[np.float32]:
        clusters: NDArray[np.float32] = -1*np.ones(self.N, dtype='int')
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

    def _finalize(self, clusters: NDArray[np.float32]) -> (set, NDArray[np.float32], float):   
        # use hinting when calling from functions?
        medoids = set(list(clusters[clusters!=-1]))
        singletons = np.where(clusters==-1)[0]
        inertia = .0
        for m in medoids:
            inertia = inertia + np.sum(D[clusters==m,:][:,m])
        return medoids, singletons, inertia

    def do_clustering(self, X=None, D=None) -> clusteringRun:
        # preliminary operations
        do_dist = self.check_input_arrays(X, D)
        Npoints = self._set_problem_size
        if do_dist:
            D = self._calculate_distance_matrix(X) 
        # start algorithm
        clusters = self.__call__(N, D)
        # collect final descriptors
        medoids, singletons, inertia = self._finalize(clusters)
        # assemble dataclass
        run = clustering_run(self.keep_data, kwargs, medoids, \
          clusters, singletons, inertia, X, D)
        return run 
