import pandas as pd
import numpy as np
import xgboost as xgb
from imblearn.over_sampling import SMOTE
import shap

# Load data
df1 = pd.read_csv('data/Output1.csv')
df2 = pd.read_csv('data/output2.csv')
df3 = pd.read_csv('data/output3.csv')
df = pd.concat([df1, df2, df3], ignore_index=True)

# Feature Engineering
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[f'{col}_diff'] = df[col].diff().fillna(0)
    df[f'{col}_ema'] = df[col].ewm(alpha=0.3, adjust=False).mean()

# SHAP-RFE Selection
X = df.drop(columns=[df.columns[-1]])
y = df[df.columns[-1]]
model = xgb.XGBClassifier().fit(X, y)
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)
shap_abs_mean = np.abs(shap_values).mean(axis=0)
top_7_indices = np.argsort(shap_abs_mean)[-7:]
X_optimized = X.iloc[:, top_7_indices]

# Hierarchical SMOTE
smote = SMOTE(random_state=42)
X_balanced, y_balanced = smote.fit_resample(X_optimized, y)
final_ds = pd.concat([X_balanced, y_balanced], axis=1)
final_ds.to_csv('data/XPE-Memory-DS.csv', index=False)
print("Dataset Generated Successfully!")
