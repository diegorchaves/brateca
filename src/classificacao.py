import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from imblearn.over_sampling import SMOTE
# Cross Validation
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer, precision_score

df = pd.read_csv('data/dataset.csv')

df["Obito"] = (df["Discharge_Motive"] == "OBITO").astype(int)

features = ["Age", "Complications", "Interventions", "High_Alert", 
            "Controlled", "Different_Drugs", "Stay_Length", "Public", 
            "Surgical", "Emergency", "IC"]
target = "Obito"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

model = xgb.XGBClassifier(
    scale_pos_weight=0.6,        
    max_depth=8,
    min_child_weight=2,
    learning_rate=0.02,
    n_estimators=200,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(X_train_balanced, y_train_balanced)

# Predições e avaliação (final)
y_pred = model.predict(X_test)
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))

# AUC-ROC
y_prob = model.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test, y_prob)
print(f"AUC-ROC: {roc_auc:.2f}")

# Avaliar modelo no conjunto de treino
y_train_pred = model.predict(X_train_balanced)
print("Métricas no Treino:")
print(classification_report(y_train_balanced, y_train_pred))

# Avaliar modelo no conjunto de teste
y_test_pred = model.predict(X_test)
print("Métricas no Teste:")
print(classification_report(y_test, y_test_pred))

cm = confusion_matrix(y_test, y_test_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Alta', 'Óbito'], yticklabels=['Alta', 'Óbito'])
plt.xlabel('Predição')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

# Métrica para a precisão da classe 1 (óbito)
precision_scorer = make_scorer(precision_score, pos_label=1)

# Realize a validação cruzada
cv_scores = cross_val_score(
    model,
    X_train_balanced,
    y_train_balanced,
    cv=8,  # Número de folds
    scoring=precision_scorer,  # Métrica de avaliação (precisão para óbito)
    n_jobs=-1  # Núcleos CPU (-1 usa todos)
)

print(f"Scores de Precisão para Óbito em cada fold: {cv_scores}")
print(f"Precisão média: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
