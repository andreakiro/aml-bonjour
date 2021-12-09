# aml-bonjour
Main repo for the task projects of the Advanced Machine Learning course at ETHZ.

- `Task 0:` Warm up and set up of tools and repo.
- `Task 1:` Brain age prediction using MRI features.
- `Task 2:` Heart rhythm classification from raw ECG signals.
- `Task 3:` Mitral valve segmentation.

## `Task 1:` Brain age prediction using [MRI](https://en.wikipedia.org/wiki/Magnetic_resonance_imaging) features.

**Approach:** We broken up the work in a data processing phase to recover a clean and proper dataset from the initial one that was perturbed with missing values and extra unrelevant features and a model selection phase. Our data cleaning pipeline include the following important steps:

1. `Outlier detection:` We used the `LocalOutlierFactor` unsupervised model from `sklearn` to find and erase outliers from original dataset. But we had to deal with a small subtlety because this model can only handle full datasets. So we temporarily imputed all the `NaN` values in our table with a `SimpleImputer` with median strategy across features 

2. `Data scaling:` We performed data normalization using a `StandardScaler` so that each of our features has the same relative importance. 

3. `Feature selection:` We removed constant features, correlated features and features generated at random. For the last feature selection approach we used sklearn `f_regression` method that roughly indicates correlation between features and label outcome. Again, this specific method requires a full dataset, so we temporarily imputed all the `NaN` values in our table with the `KNNImputer` strategy.

4. `Data imputation:` We finally imputed all the missing values of our remaining data samples with remaining relevant features with the experimental `IterativeImputer` strategy implementing [MICE](https://cran.r-project.org/web/packages/miceRanger/vignettes/miceAlgorithm.html) algorithm.

After the data processing phase, we trained multiple models and fine tuned their hyperparameters using a grid search approach. Models we explored include `Lasso`, `Random Forest`, `Support Vector Regression (SVR)`, `Gradient Boosting Regression (GBR)` and `Adaboost`. The one giving the best validation score with tuned hyperparamters is `SVR`, closely followed by `GBR`.

## `Task 2:` Heart rhythm classification from raw [ECG](https://en.wikipedia.org/wiki/Electrocardiography) signals.

**Approach:** We first focused on a feature extraction phase to retrieve as many information as we could on the ecg signals we were provided and then hope getting decent results with ensembles of standard classification models.

The `feature extraction` pipeline takes out a bunch of interesting features including mean, std, quantiles, skew, kurtosis and many more on 1) `{QRS} peaks` and almost every convoluted features between them e-g. differences, ratios, `pNN`, `logRSMMD` 2) signal-to-noises 3) power features and 4) wavelet features from Fourrier analysis.

Afterward, we standardized our data to ensure all features have the same importance. We also applied an important feature selection process very similar to the one we used in `task 1` to get rid of features we created that were too correlated and provided little information in order to increase model accuracy and reduce training complexity. We finally detected very few outliers using again the same techniques as in `task 1`.

We then trained almost any sklearn classification model and fine tuned their hyperparamters using a grid search approach. In particular, we explored performance of `Ridge`, `Logistic`, `MLP`, `Support Vector Classification (SVC)`, `Random Forest (RF)`, `Gradient Boosting Classification (GBC)`, `KNeighbors`, `Gaussian Process` and `AdaBoost`. Our final model consist of an ensemble of the best performing classification models. The ensemble giving us the best validation score keeping a low std only contains `RF` and `GBC`.

## `Task 3:` Mitral valve segmentation.