import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/dataset.csv')

print(df.describe())
print(df.info())
print(df["Discharge_Motive"].value_counts())

sns.countplot(x="Discharge_Motive", data=df)
plt.show()

groups = {
    "Perfil do Paciente": ["Age", "Complications"],
    "Desfecho e Internação": ["Stay_Length", "Public", "Emergency"],
    "Medicamentos e Intervenções": ["Antibiotics", "High_Alert", "Controlled"],
}

# Gerar gráficos para cada grupo
for title, variables in groups.items():
    corr_matrix = df[variables].corr()
    strong_corrs = corr_matrix[(corr_matrix > 0.5) | (corr_matrix < -0.5)]
    sns.heatmap(strong_corrs, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlação Forte (> 0.5 ou < -0.5)")
    plt.show()

df["Obito"] = (df["Discharge_Motive"] == "OBITO").astype(int)

# Subconjunto: Perfil do paciente
subset = ["Age", "Complications", "Obito"]
corr_matrix = df[subset].corr()

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlação: Perfil do Paciente e Óbito")
plt.show()

# Subconjunto: Internação
subset = ["Stay_Length", "Public", "Surgical", "IC", "Emergency", "Ambulatory", "COVID-19", "Obito"]
corr_matrix = df[subset].corr()

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlação: Características da Internação e Óbito")
plt.show()

# Subconjunto: Medicamentos e intervenções
subset = ["Antibiotics", "High_Alert", "Controlled", "Tube", "Different_Drugs", "Obito"]
corr_matrix = df[subset].corr()

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlação: Medicamentos e Intervenções com Óbito")
plt.show()