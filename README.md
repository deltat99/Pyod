# Python Outlier Detection (PyOD)
[![PyPI version](https://badge.fury.io/py/pyod.svg)](https://badge.fury.io/py/pyod) [![Documentation Status](https://readthedocs.org/projects/pyod/badge/?version=latest)](https://pyod.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.org/yzhao062/Pyod.svg?branch=master)](https://travis-ci.org/yzhao062/Pyod) [![Coverage Status](https://coveralls.io/repos/github/yzhao062/Pyod/badge.svg?branch=master&service=github)](https://coveralls.io/github/yzhao062/Pyod?branch=master) 
[![GitHub stars](https://img.shields.io/github/stars/yzhao062/Pyod.svg)](https://github.com/yzhao062/Pyod/stargazers) 
[![GitHub forks](https://img.shields.io/github/forks/yzhao062/Pyod.svg)](https://github.com/yzhao062/Pyod/network)

--------------------------

PyOD is a comprehensive **Python toolkit** to **identify outlying objects** in 
multivariate data with both unsupervised and supervised approaches. 
This exciting yet challenging field is commonly referred as 
***[Outlier Detection](https://en.wikipedia.org/wiki/Anomaly_detection)*** 
or ***[Anomaly Detection](https://en.wikipedia.org/wiki/Anomaly_detection)*** .
The toolkit has been successfully used in various academic researches [4, 8] and commercial products.
Unlike existing libraries, PyOD provides:

- **Unified and consistent APIs** across various anomaly detection algorithms.
- **Compatibility with both Python 2 and 3**. All implemented algorithms are also **scikit-learn compatible**.
- **Advanced functions**, e.g., **Outlier Ensemble Frameworks** to combine multiple detectors.
- **Detailed API Reference, Examples and Tests** for better reliability. 


**Table of Contents**:
<!-- TOC -->

- [Key Links & Resources](#key-links-resources)
- [Quick Introduction](#quick-introduction)
- [Installation](#installation)
- [API Cheatsheet & Reference](#api-cheatsheet-reference)
- [Quick Start for Outlier Detection](#quick-start-for-outlier-detection)
- [Quick Start for Combining Outlier Scores from Various Base Detectors](#quick-start-for-combining-outlier-scores-from-various-base-detectors)
- [Reference](#reference)

<!-- /TOC -->

------------------------------
# Key Links & Resources

- **[Documentation & API Reference](https://pyod.readthedocs.io)** [![Documentation Status](https://readthedocs.org/projects/pyod/badge/?version=latest)](https://pyod.readthedocs.io/en/latest/?badge=latest)

- **[Current version on PyPI](https://pypi.org/project/pyod/)** [![PyPI version](https://badge.fury.io/py/pyod.svg)](https://badge.fury.io/py/pyod) 

- **[Github repository with examples](https://github.com/yzhao062/Pyod)** | **[Example Documentation](https://pyod.readthedocs.io/en/latest/example.html)**

- **[Anomaly detection resources](https://github.com/yzhao062/anomaly-detection-resources)**, e.g., courses, books, papers and videos.

-----------------------------------

### Quick Introduction

PyOD toolkit consists of three major groups of functionalities: (i) **outlier detection algorithms**; (ii) **outlier ensemble frameworks** and (iii) **outlier detection utility functions**.

- Individual Detection Algorithms:  
  1. **Local Outlier Factor, LOF** [1]
  2. **Isolation Forest, iForest** [2]
  3. **One-Class Support Vector Machines** [3]
  4. **k Nearest Neighbors Detector (kNN)** (use the distance to the kth nearest neighbor as the outlier score)
  5. **Average kNN** Outlier Detection (use the average distance to k nearest neighbors as the outlier score)
  6. **Median kNN** Outlier Detection (use the median distance to k nearest neighbors as the outlier score)
  7. **Histogram-based Outlier Score, HBOS** [5]
  8. **Angle-Based Outlier Detection, ABOD** [7]
  9. **Fast Angle-Based Outlier Detection, FastABOD** [7]
  10. More to add...

- Outlier Ensemble Framework (Outlier Score Combination Frameworks)
  1. **Feature bagging** [9]
  2. **Average** & **Weighted Average** [6]
  3. **Maximization** [6]
  4. **Average of Maximum (AOM)** [6]
  5. **Maximum of Average (MOA)** [6]
  6. **Threshold Sum (Thresh)** [6]

- Utility functions:
   1. **score_to_lable()**: convert raw outlier scores to binary labels
   2. **precision_n_scores()**: one of the popular evaluation metrics for outlier mining (precision @ rank n)
   3. **generate_data()**: generate pseudo data for outlier detection experiment
   4. **wpearsonr()**: weighted pearson is useful in pseudo ground truth generation
------------

### Installation

It is advised to use **pip**. Please make sure **the latest version** is installed since PyOD is currently updated on **a daily basis**:
````cmd
pip install pyod
pip install --upgrade pyod # make sure the latest version is installed!
````
or 
````cmd
pip install pyod==x.y.z  # (x.y.z) is the current version number
````
 Alternatively, [downloading/cloning the Github repository](https://github.com/yzhao062/Pyod) also works. You could unzip the files and execute the following command in the folder where the files get decompressed.

````cmd
python setup.py install
````
Python Version:
- Python 2: 2.7 only
- Python 3: 3.4, 3.5 or 3.6

Library Dependency: 
````cmd
matplotlib                       # optional. Only needed for running examples
nose                             # optional. Only needed for running tests
numpy>=1.13
pytest                           # optional. Only needed for running tests
scipy>=0.19.1
scikit_learn>=0.19.1
````
------------
### API Cheatsheet & Reference

Full API Reference: (http://pyod.readthedocs.io/en/latest/api.html). API cheatsheet for all detectors:

- **fit(X)**: Fit detector.
- **fit_predict(X)**: Fit detector and predict if a particular sample is an outlier or not.
- **fit_predict_evaluate(X, y)**: Fit, predict and then evaluate with predefined metrics (ROC and precision @ rank n).
- **decision_function(X)**: Predict anomaly score of X of the base classifiers.
- **predict(X)**: Predict if a particular sample is an outlier or not. The model must be fitted first.
- **predict_proba(X)**: Predict the probability of a sample being outlier. The model must be fitted first.
- **predict_rank(X)**: Predict the outlyingness rank of a sample.

Full package structure can be found below:
- http://pyod.readthedocs.io/en/latest/genindex.html
- http://pyod.readthedocs.io/en/latest/py-modindex.html

------------

### Quick Start for Outlier Detection
See **examples directory** for more demos. ["examples/knn_example.py"](https://github.com/yzhao062/Pyod/blob/master/examples/knn_example.py)
demonstrates the basic APIs of PyOD using kNN detector. **It is noted the APIs for other detectors are similar**. 

1. Initialize a kNN detector, fit the model, and make the prediction.
    ```python
    
    from pyod.models.knn import KNN   # kNN detector
 
    # train kNN detector
    clf_name = 'KNN'
    clf = KNN()
    clf.fit(X_train)

    # get the prediction label and decision_scores_ on the training data
    y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
    y_train_scores = clf.decision_scores_  # raw outlier scores

    # get the prediction on the test data
    y_test_pred = clf.predict(X_test)  # outlier labels (0 or 1)
    y_test_scores = clf.decision_function(X_test)  # outlier scores
    ```
2. Evaluate the prediction by ROC and Precision@rank *n* (p@n):
    ```python
    # evaluate and print the results
    print("\nOn Training Data:")
    evaluate_print(clf_name, y_train, y_train_scores)
    print("\nOn Test Data:")
    evaluate_print(clf_name, y_test, y_test_scores)
    ```
 3. See a sample output & visualization
    ````python
    On Training Data:
    KNN ROC:1.0, precision @ rank n:1.0
    
    On Test Data:
    KNN ROC:0.9989, precision @ rank n:0.9
    ````
    ````python
    visualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred,
              y_test_pred, show_figure=True, save_figure=False)
    ````
    
Visualization ([knn_figure](https://github.com/yzhao062/Pyod/blob/master/examples/KNN.png)):
![kNN example figure](https://github.com/yzhao062/Pyod/blob/master/examples/KNN.png)

---
### Quick Start for Combining Outlier Scores from Various Base Detectors

"examples/comb_example.py" illustrates the APIs for combining multiple base detectors. Given we have *n* individual outlier detectors, each of them generates an individual score for all samples. The task is to combine the outputs from these detectors effectivelly.

**Key Step: conducting Z-score normalization on raw scores before the combination.** Four combination mechanisms are shown in this demo:

1. Average: take the average of all base detectors.
2. maximization : take the maximum score across all detectors as the score.
3. Average of Maximum (AOM): first randomly split n detectors in to p groups. For each group, use the maximum within the group as the group output. Use the average of all group outputs as the final output.
4. Maximum of Average (MOA): similarly to AOM, the same grouping is introduced. However, we use the average of a group as the group output, and use maximum of all group outputs as the final output.
To better understand the merging techniques, refer to [6].

The walkthrough of the code example is provided:

0. Import models and generate sample data
    ````python
    
    from pyod.models.knn import KNN
    from pyod.models.combination import aom, moa, average, maximization
    from pyod.utils.data import generate_data
    
    X, y = generate_data(train_only=True)  # load data
    ````
    
1. First initialize 20 kNN outlier detectors with different k (10 to 200), and get the outlier scores:
    ```python
    # initialize 20 base detectors for combination
    k_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140,
                150, 160, 170, 180, 190, 200]

    train_scores = np.zeros([X_train.shape[0], n_clf])
    test_scores = np.zeros([X_test.shape[0], n_clf])

    for i in range(n_clf):
        k = k_list[i]

        clf = KNN(n_neighbors=k, method='largest')
        clf.fit(X_train_norm)

        train_scores[:, i] = clf.decision_scores_
        test_scores[:, i] = clf.decision_function(X_test_norm)
    ```
2. Then the output codes are standardized into zero mean and unit std before combination.
    ```python
    from pyod.utils.utility import standardizer
    train_scores_norm, test_scores_norm = standardizer(train_scores, test_scores)
    ```
3. Then four different combination algorithms are applied as described above:
    ```python
    comb_by_average = average(test_scores_norm)
    comb_by_maximization = maximization(test_scores_norm)
    comb_by_aom = aom(test_scores_norm, 5) # 5 groups
    comb_by_moa = moa(test_scores_norm, 5)) # 5 groups
    ```
4. Finally, all four combination methods are evaluated with 10 iterations:
    ````bash
    Combining 20 kNN detectors
    ite 1 comb by average, ROC: 0.9014 precision@n_train: 0.4531
    ite 1 comb by maximization, ROC: 0.9014 precision@n_train: 0.5
    ite 1 comb by aom, ROC: 0.9081 precision@n_train: 0.5
    ite 1 comb by moa, ROC: 0.9052 precision@n_train: 0.4843
    ...
    
    Summary of 10 iterations
    comb by average, ROC: 0.9196, precision@n: 0.5464
    comb by maximization, ROC: 0.9198, precision@n: 0.5532
    comb by aom, ROC: 0.9260, precision@n: 0.5630
    comb by moa, ROC: 0.9244, precision@n: 0.5523
    ````
---    

### Reference
[1] Breunig, M.M., Kriegel, H.P., Ng, R.T. and Sander, J., 2000, May. LOF: identifying density-based local outliers. In *ACM SIGMOD Record*, pp. 93-104. ACM.

[2] Liu, F.T., Ting, K.M. and Zhou, Z.H., 2008, December. Isolation forest. In *ICDM '08*, pp. 413-422. IEEE.

[3] Ma, J. and Perkins, S., 2003, July. Time-series novelty detection using one-class support vector machines. In *IJCNN' 03*, pp. 1741-1745. IEEE.

[4] Y. Zhao and M.K. Hryniewicki, "DCSO: Dynamic Combination of Detector Scores for Outlier Ensembles," *ACM SIGKDD Workshop on Outlier Detection De-constructed*, 2018. Submitted, under review.

[5] Goldstein, M. and Dengel, A., 2012. Histogram-based outlier score (hbos): A fast unsupervised anomaly detection algorithm. In *KI-2012: Poster and Demo Track*, pp.59-63.

[6] Aggarwal, C.C. and Sathe, S., 2015. Theoretical foundations and algorithms for outlier ensembles.*ACM SIGKDD Explorations Newsletter*, 17(1), pp.24-47.

[7] Kriegel, H.P. and Zimek, A., 2008, August. Angle-based outlier detection in high-dimensional data. In *KDD '08*, pp. 444-452. ACM.

[8] Y. Zhao and M.K. Hryniewicki, "XGBOD: Improving Supervised Outlier Detection with Unsupervised Representation Learning," *IEEE International Joint Conference on Neural Networks*, 2018.

[9] Lazarevic, A. and Kumar, V., 2005, August. Feature bagging for outlier detection. In *KDD '05*. 2005.
