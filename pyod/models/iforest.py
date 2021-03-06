# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

from sklearn.ensemble import IsolationForest
from sklearn.utils.validation import check_is_fitted
from sklearn.utils import check_array

from .base import BaseDetector


class IForest(BaseDetector):
    """
    Wrapper of scikit-learn Isolation Forest Class with more functionalities.

    The IsolationForest [1, 2] 'isolates' observations by randomly selecting a feature
    and then randomly selecting a split value between the maximum and minimum
    values of the selected feature.

    Since recursive partitioning can be represented by a tree structure, the
    number of splittings required to isolate a sample is equivalent to the path
    length from the root node to the terminating node.

    This path length, averaged over a forest of such random trees, is a
    measure of normality and our decision function.

    Random partitioning produces noticeably shorter paths for anomalies.
    Hence, when a forest of random trees collectively produce shorter path
    lengths for particular samples, they are highly likely to be anomalies.

    :param n_estimators: The number of base estimators in the ensemble.
    :type n_estimators: int, optional (default=100)

    :param max_samples: The number of samples to draw from X to train
        each base estimator.

            - If int, then draw `max_samples` samples.
            - If float, then draw `max_samples * X.shape[0]` samples.
            - If "auto", then `max_samples=min(256, n_samples)`.
    :type max_samples: int or float, optional (default="auto")

    :param contamination: The amount of contamination of the data set,
        i.e. the proportion of outliers in the data set. Used when fitting to
        define the threshold on the decision function.
    :type contamination: float in (0., 0.5), optional (default=0.1)

    :param max_features: The number of features to draw from X to
        train each base estimator.

            - If int, then draw `max_features` features.
            - If float, then draw `max_features * X.shape[1]` features.
    :type max_features: int or float, optional (default=1.0)

    :param bootstrap: If True, individual trees are fit on random subsets of
        the training data sampled with replacement. If False, sampling without
        replacement is performed.
    :type bootstrap: bool, optional (default=False)

    :param n_jobs: The number of jobs to run in parallel for both `fit` and
        `predict`. If -1, then the number of jobs is set to the number of cores
    :type n_jobs: int, optional (default=1)

    :param random_state: If int, random_state is the seed used by the random
        number generator; If RandomState instance, random_state is the random
        number generator; If None, the random number generator is the
        RandomState instance used by `np.random`.
    :type random_state: int, RandomState instance or None, optional
        (default=None)

    :param verbose: Controls the verbosity of the tree building process.
    :type verbose: int, optional (default=0)

    :var estimators_(list): The collection of fitted sub-estimators.

    :var estimators_samples_(list): The subset of drawn samples (i.e., the
        in-bag samples) for each base estimator.

    :var max_samples_(int): The actual number of samples.


    .. [1] Liu, Fei Tony, Ting, Kai Ming and Zhou, Zhi-Hua. "Isolation forest."
           Data Mining, 2008. ICDM'08. Eighth IEEE International Conference on.
    .. [2] Liu, Fei Tony, Ting, Kai Ming and Zhou, Zhi-Hua. "Isolation-based
           anomaly detection." ACM Transactions on Knowledge Discovery from
           Data (TKDD) 6.1 (2012): 3.

    """

    def __init__(self, n_estimators=100,
                 max_samples="auto",
                 contamination=0.1,
                 max_features=1.,
                 bootstrap=False,
                 n_jobs=1,
                 random_state=None,
                 verbose=0):
        super(IForest, self).__init__(contamination=contamination)
        self.n_estimators = n_estimators
        self.max_samples = max_samples
        self.max_features = max_features
        self.bootstrap = bootstrap
        self.n_jobs = n_jobs
        self.random_state = random_state
        self.verbose = verbose

    def fit(self, X, y=None):
        # Validate inputs X and y (optional)
        X = check_array(X)
        self._set_n_classes(y)

        self.detector_ = IsolationForest(n_estimators=self.n_estimators,
                                         max_samples=self.max_samples,
                                         contamination=self.contamination,
                                         max_features=self.max_features,
                                         bootstrap=self.bootstrap,
                                         n_jobs=self.n_jobs,
                                         random_state=self.random_state,
                                         verbose=self.verbose)
        self.detector_.fit(X=X,
                           y=None,
                           sample_weight=None)

        # invert decision_scores_. Outliers comes with higher decision_scores_
        self.decision_scores_ = self.detector_.decision_function(X) * -1
        self._process_decision_scores()
        return self

    def decision_function(self, X):
        check_is_fitted(self, ['decision_scores_', 'threshold_', 'labels_'])
        # invert decision_scores_. Outliers comes with higher decision_scores_
        return self.detector_.decision_function(X) * -1

    @property
    def estimators_(self):
        """
        The collection of fitted sub-estimators.

        Decorator for scikit-learn Isolation Forest attributes.

        :return: The collection of fitted sub-estimators.
        :rtype: list of DecisionTreeClassifier
        """
        return self.detector_.estimators_

    @property
    def estimators_samples_(self):
        """
        The subset of drawn samples (i.e., the in-bag samples) for
        each base estimator.

        Decorator for scikit-learn Isolation Forest attributes.

        :return: The subset of drawn samples (i.e., the in-bag samples) for
            each base estimator.
        :rtype: list or arrays
        """
        return self.detector_.estimators_samples_

    @property
    def max_samples_(self):
        """
        The actual number of samples.

        Decorator for scikit-learn Isolation Forest attributes.

        :return: The actual number of samples
        :rtype: int
        """
        return self.detector_.max_samples_
