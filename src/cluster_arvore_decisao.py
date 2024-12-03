from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

df = pd.read_csv('data/Dataset_Final_Binary.csv')

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df_obito = df[df['Discharge_Motive'] == 'Obito']

columns_for_clustering = [
    'Age', 'Stay_Length_Days', 'Sex_F', 'Sex_M', 'Public', 'Surgical', 'IC',
    'Obstetrics', 'Emergency', 'Ambulatory', 'COVID-19', 'Allergy',
    'Alerts', 'Prescription_Score', 'Score_One', 'Score_Two', 'Score_Three',
    'Antibiotics', 'High_Alert', 'Controlled', 'Not_Default', 'Tube',
    'Different_Drugs', 'Alert_Exams', 'Interventions', 'Complications',
    'Albumina', 'Amilase', 'Basófilos', 'Bilirrubina Direta',
    'Bilirrubina Total', 'Bilirrubina indireta', 'Bilirrubinas Totais',
    'C.H.C.M.', 'COAGULOGRAMA - INR', 'Ciclosporina', 'Creatinina',
    'Creatinina 2', 'Cálcio', 'Cálcio Iônico', 'D-dímero', 'DDímero',
    'Eosinófilos', 'Eritrócitos', 'Eritócitos', 'Fenitoína', 'Ferro',
    'Fosfatase Alcalina', 'Fósforo', 'Fósforo Inorgânico', 'Gama GT',
    'Glicose', 'H.C.M.', 'Hematócrito', 'Hemocultura',
    'Hemocultura - germe 1', 'Hemocultura - germe 2', 'Hemocultura - oneg1',
    'Hemoglobina', 'Hemoglobina Glicada', 'LACTATO (Plasma Fluoretado)',
    'LACTATO (Sangue Arterial c/ Heparina)', 'Lactato', 'Leucócitos',
    'Leucócitos (Hemograma)', 'Linfócitos', 'Magnésio', 'Monócitos',
    'Neutrófilos', 'Plaquetas', 'Potássio', 'Procalcitonina ',
    'Proteína C Reativa', 'Proteína C-reativa', 'Proteínas',
    'Proteínas Totais', 'R.D.W.', 'Razão de Normatização Internacional',
    'Saturação - Gasometria', 'Sódio', 'Tacrolimus',
    'Tempo de Tromboplatina Parcial', 'Transaminase Glutâmico-Oxalacética',
    'Transaminase Glutâmico-Pirúvica', 'Ureia', 'Urocultura (germe1)',
    'V.C.M.', 'Vancomicina', 'Vancomicina NS', 'pCO2 - Gasometria',
    'pH - Gasometria', 'pO2 - Gasometria'
]

df_obito_clustering = df_obito[columns_for_clustering]
df_obito_clustering = df_obito_clustering.dropna()

scaler = StandardScaler()
df_obito_scaled = scaler.fit_transform(df_obito_clustering)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(df_obito_scaled)
    wcss.append(kmeans.inertia_)

# plotar o gráfico do método do cotovelo
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss)
plt.title('Método do Cotovelo')
plt.xlabel('Número de Clusters')
plt.ylabel('WCSS')
plt.show()

exam_columns = [
    'Albumina', 'Amilase', 'Basófilos', 'Bilirrubina Direta',
    'Bilirrubina Total', 'Bilirrubina indireta', 'Bilirrubinas Totais',
    'C.H.C.M.', 'COAGULOGRAMA - INR', 'Ciclosporina', 'Creatinina',
    'Creatinina 2', 'Cálcio', 'Cálcio Iônico', 'D-dímero', 'DDímero',
    'Eosinófilos', 'Eritrócitos', 'Eritócitos', 'Fenitoína', 'Ferro',
    'Fosfatase Alcalina', 'Fósforo', 'Fósforo Inorgânico', 'Gama GT',
    'Glicose', 'H.C.M.', 'Hematócrito', 'Hemocultura',
    'Hemocultura - germe 1', 'Hemocultura - germe 2', 'Hemocultura - oneg1',
    'Hemoglobina', 'Hemoglobina Glicada', 'LACTATO (Plasma Fluoretado)',
    'LACTATO (Sangue Arterial c/ Heparina)', 'Lactato', 'Leucócitos',
    'Leucócitos (Hemograma)', 'Linfócitos', 'Magnésio', 'Monócitos',
    'Neutrófilos', 'Plaquetas', 'Potássio', 'Procalcitonina ',
    'Proteína C Reativa', 'Proteína C-reativa', 'Proteínas',
    'Proteínas Totais', 'R.D.W.', 'Razão de Normatização Internacional',
    'Saturação - Gasometria', 'Sódio', 'Tacrolimus',
    'Tempo de Tromboplatina Parcial', 'Transaminase Glutâmico-Oxalacética',
    'Transaminase Glutâmico-Pirúvica', 'Ureia', 'Urocultura (germe1)',
    'V.C.M.', 'Vancomicina', 'Vancomicina NS', 'pCO2 - Gasometria',
    'pH - Gasometria', 'pO2 - Gasometria'
]

bins = [0, 18, 30, 40, 50, 60, 70, 80, 100]
labels = ['0-17', '18-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

age_groups = df.groupby('Age_Group')

for col in exam_columns:
    # preenche com a media da faixa etaria
    df[col] = df.groupby('Age_Group')[col].transform(lambda x: x.fillna(x.mean()))

    # preenche com a media geral
    df[col] = df[col].fillna(df[col].mean())


kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=42)
y_kmeans = kmeans.fit_predict(df_obito_scaled)

# adicionar o cluster ao dataframe
df_obito['Cluster'] = y_kmeans

# visualizar os clusters
# reduzir a dimensionalidade para 2D ccom o pca
pca = PCA(n_components=2)
principal_components = pca.fit_transform(df_obito_scaled)

# criar um df com as duas componentes principais
df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
df_pca['Cluster'] = y_kmeans


import matplotlib.colors as mcolors
cluster_colors = {0: '#440154', 1: '#21918c', 2: '#fde725'}

plt.figure(figsize=(10, 6))
for cluster in cluster_colors.keys():
    cluster_data = df_pca[df_pca['Cluster'] == cluster]
    plt.scatter(cluster_data['PC1'], cluster_data['PC2'], 
                color=cluster_colors[cluster], label=f'Cluster {cluster}', alpha=0.7)
    
plt.title('Clustering dos Pacientes que Vieram a Óbito')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

df_obito_clustering['Cluster'] = kmeans.fit_predict(df_obito_scaled)

X = df_obito_clustering.drop(columns=['Cluster'])
y = df_obito_clustering['Cluster']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

from sklearn.metrics import classification_report, accuracy_score
y_pred = clf.predict(X_test)
print(f'Acurácia: {accuracy_score(y_test, y_pred):.4f}')
print(classification_report(y_test, y_pred))

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

color_map = {0: '#440154', 1: '#21918c', 2: '#fde725'}

plt.figure(figsize=(20, 10))
plot_tree(clf, filled=True, feature_names=X.columns,
          class_names=[f'Cluster {i}' for i in range(3)], 
          rounded=True, impurity=False,
          node_ids=False, proportion=True,
          fontsize=6)
plt.show()