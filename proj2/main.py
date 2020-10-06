#from reader import *
#from cross_validation import *
from ML import *
"""This is the main function that initializes all machine learning runs. The function instantiates many objects
    of the ML class, each object relating to a different run. The ML class is passed a list of configuration
     settings which are described more in depth below"""
def main():

    #ML("KNN", "classification", "off", [10, .1], 1, "./data/glass.data")
    #ML("KNN", "regression", "off", [10, .1], 1, "./data/abalone.data")
    # ML("KNN", "regression", "off", [10, .1], 1, "./data/forestfires.data")
    #ML("KNNedited", "classification", "on", [10, .1], 1, "./data/house-votes-84.data")
    #ML("KNN", "regression", "on", [10, .1], 1, "./data/machine.data")
    #ML("KNN", "classification", "on", [10, .1], 1, "./data/segmentation.data")

    #ML("KNN", "classification", "off", [5, .1], 1, "./data/house-votes-84.data")
    #ML("KNNedited", "classification", "off", [5, .1], 1, "./data/house-votes-84.data")
    ML("KNNcondensed", "classification", "off", [10, .1], 1, "./data/house-votes-84.data")

    #ML("KNNedited", "classification", "off", [10, .1], 1, "./data/house-votes-84.data")
    #ML("KNNcondensed", "classification", "off", [10, .1], 1, "./data/house-votes-84.data")
    #ML("KNN", "regression", "on", [10, .1], 1, "./data/machine.data")
    #ML("KNNedited", "regression", "on", [10, .1], 1, "./data/machine.data")
    #ML("KNNcondensed", "regression", "on", [10, .1], 1, "./data/machine.data")

    #ML("KNN_Cluster_Medoids", "classification", "on", [10, .1], 1, "./data/glass.data")

    """ ML params in order:
     1. algorithm name -> options: KNN, KNNedited, KNNcondensed, KNNcluster, KNN_Cluster_Medoids, KNNmenas
     2. classification type -> "classification" or "regression"
     3. data split options ->  [int k, float tuning_set %]
     4. hypertuning on or off -> "on" or "off"
     4. display option (TODO)-> 0 = k-fold-average only  1 = print all k-folds 2 = also show hypertuning
                                3 = also print data
     5. file name

      """

if __name__ == "__main__":
    main()
