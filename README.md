# aml-bonjour
Main repo for the task projects of the Advanced Machine Learning course at ETHZ.

- `Task 0:` Warm up and set up of tools and repo.
- `Task 1:` Brain age prediction using [MRI](https://en.wikipedia.org/wiki/Magnetic_resonance_imaging) features.
- `Task 2:` Heart rhythm classification from raw [ECG](https://en.wikipedia.org/wiki/Electrocardiography) signals.

## `Task 1:` Brain age prediction using [MRI](https://en.wikipedia.org/wiki/Magnetic_resonance_imaging) features.

**Approach:** We broken up the work in a data processing phase to recover a clean and proper dataset rom the initial one that was perturbed with missing values and extra unrelevant features and a model selection phase. Our data cleaning pipeline include the following important steps:

1. `Outlier detection:` We used the [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html) unsupervised model from sklearn to find and erase outliers from original dataset. But we had to deal with a small subtlety because this model can only handle full datasets. So we temporarily imputed all the `NaN` values in our table with a [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html) with median strategy across features.

2. `Data scaling:` We performed data normalization using a [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) so that each of our features has the same relative importance. 

3. `Feature selection:` We removed constant features, correlated features and features generated at random. For the last feature selection approach we used sklearn [f_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html) method that roughly indicates correlation between features and label outcome. Again, this specific method requires a full dataset, so we temporarily imputed all the `NaN` values in our table with the [KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html) strategy.

4. `Data imputation:` We finally imputed all the missing values of our remaining data samples with remaining relevant features with the experimental [IterativeImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html) strategy implementing [MICE](https://cran.r-project.org/web/packages/miceRanger/vignettes/miceAlgorithm.html) algorithm.

After the data processing phase, we trained multiple models and fine tuned their hyperparameters using a [grid search](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) approach. Models we explored include [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html), [`Random Forest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html), [`Support Vector Regression (SVR)`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html), [`Gradient Boosting Regression (GBR)`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.htmland) and [`Adaboost`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html). The one giving the best validation score with tuned hyperparamters is `SVR`, closely followed by `GBR`.

## `Task 2:` Heart rhythm classification from raw [ECG](https://en.wikipedia.org/wiki/Electrocardiography) signals.