import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/Dataset_Final_Binary.csv')

df['Age'].hist(bins=20, edgecolor='black')
plt.title('Distribuição de Idades')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

sns.countplot(x='Age_Group', data=df, order=['0-17', '18-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+'])
plt.title('Distribuição Faixa Etária')
plt.show()

sns.boxplot(x='Discharge_Motive', y='Different_Drugs', data=df)
plt.title('Distribuição de Drogas Diferentes por Tipo de Alta')
plt.show()

sns.scatterplot(
    x='Age', 
    y='Stay_Length_Days', 
    hue='Discharge_Motive', 
    data=df, 
    alpha=0.6
)
plt.title('Idade vs Score de Prescrição por Motivo da Alta')
plt.show()

df_grouped = df.groupby('Age_Group')['Discharge_Motive'].value_counts(normalize=True).unstack()
df_grouped.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.title('Proporção de Altas e Óbitos por Faixa Etária')
plt.ylabel('Proporção')
plt.show()

contingency_table = pd.crosstab(df['Age_Group'], df['Discharge_Motive'])
sns.heatmap(contingency_table, annot=True, fmt='d', cmap='Blues')
plt.title('Frequência de Altas e Óbitos por Faixa Etária')
plt.show()

sns.boxplot(x='Discharge_Motive', y='Stay_Length_Days', data=df)
plt.title('Duração da Internação por Motivo da Alta')
plt.show()