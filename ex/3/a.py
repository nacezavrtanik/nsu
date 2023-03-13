"""Class 3, Exercise A: Meta-classification, Meta-regression"""

import pandas as pd
import os
from sklearn.model_selection import train_test_split

from aml import compare_models_cross_validation


# 1 Preprocess data

# Read data
abs_path = os.path.abspath(__file__)
file_dir = os.path.dirname(abs_path)
parent_dir = os.path.dirname(file_dir)

X_meta = pd.read_csv(parent_dir + '\\2\\c_meta_features.csv', index_col=0).set_index('dataset')
y_meta = pd.read_csv(
    parent_dir + '\\2\\b_model_accuracy_comparison_for_datasets.csv', index_col=0).set_index('dataset')
del abs_path, file_dir, parent_dir

# Clean data
X_meta.dropna(axis=1, inplace=True)
y_meta = y_meta['best']  # keep target variable only

# Split dataset
X_meta_train, X_meta_test, y_meta_train, y_meta_test = train_test_split(X_meta, y_meta, train_size=0.8, random_state=0)

# 2 Cross-validate and compare meta-models
comparison = compare_models_cross_validation(X_meta, y_meta, 'classification',
                                             ['random_forrest_classifier',
                                              'dummy_classifier'])
