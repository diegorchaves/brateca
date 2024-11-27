import pandas as pd

# Agregacao dos exames

# df = pd.read_csv('brateca2/B1_Exam.csv')

# agg_df = (
#     df.groupby(["Patient_ID", "Hospital_ID", "Exam_Name"])["Value"]
#     .mean()
#     .reset_index()
#     .rename(columns={"Value": "Average_Value"})
# )

# print(agg_df)

# agg_df.to_csv('Agg_Exams.csv')

# Agregacao das prescricoes

# df = pd.read_csv('brateca2/B1_Prescription.csv')
# df = df.drop(['Prescription_ID','Prescription_Date', 'Expiration_Date', 'Pharmacy_Assessment', 'Assessment_Date'], axis=1)

# aggregated_df = df.groupby(["Patient_ID", "Hospital_ID"]).agg({
#     # Valores booleanos: verifica se alguma prescrição contém True
#     "Public": "any",
#     "Surgical": "any",
#     "IC": "any",
#     "Obstetrics": "any",
#     "Emergency": "any",
#     "Ambulatory": "any",
#     "COVID-19": "any",
#     # Valores numericos
#     "Allergy": "mean",
#     "Alerts": "sum",
#     "Prescription_Score": "mean",
#     "Score_One": "mean",
#     "Score_Two": "mean",
#     "Score_Three": "mean",
#     "Antibiotics": "mean",
#     "High_Alert": "mean",
#     "Controlled": "mean",
#     "Not_Default": "mean",
#     "Tube": "mean",
#     "Different_Drugs": "mean",
#     "Alert_Exams": "mean",
#     "Interventions": "sum",
#     "Complications": "sum"
# }).reset_index()

# # print(aggregated_df)

# aggregated_df.to_csv('Agg_Prescription.csv')

# df = pd.read_csv('brateca2/B1_Admission.csv')
# df['Age'] = (pd.to_datetime(df['Admission_Date']) - pd.to_datetime(df['Birth_Date'])).dt.days // 365
# df['Stay_Length_Days'] = (pd.to_datetime(df['Discharge_Date']) - pd.to_datetime(df['Admission_Date'])).dt.days

# df = df.drop(['Skin_Color', 'Admission_ID', 'Birth_Date', 'Admission_Date', 'Discharge_Date', 'Unnamed: 11', 'Unnamed: 12', 'Height', 'Weight'], axis=1)

# df['Discharge_Motive'] = df['Discharge_Motive'].str.upper()

# discharge_mapping = {
#     'ALTA': 'ALTA',
#     'OBITO SEM NECROPSIA APOS 48 HORAS DA INTERNACAO':'OBITO',
#     'ÓBITO': 'OBITO',
#     'OBITO SEM NECROPSIA APOS 48 HORAS DA INTERNACAO': 'OBITO',
#     'OBITO SEM NECROPSIA APOS 48HS INTERNAÇÃO': 'OBITO',
#     'ALTA POR EVASÃO': 'ALTA',
#     'HOME CARE': 'ALTA',
#     'ÓBITO SEM NECROPSIA ATE 24 HORAS DE INTERNAÇÃO': 'OBITO',
#     'TRANSFERÊNCIA': 'TRANSFERENCIA',
#     'OBITO COM NECROPSIA APOS 48HS INTERNAÇÃO': 'OBITO',
#     'DESISTÊNCIA DO TRATAMENTO': 'DESISTENCIA',
#     'OBITO COM NECROPSIA ATE 48HS PAC.EM ESTADO AGONICO': 'OBITO',
#     'ÓBITO COM NECROPSIA APOS 48 HORAS DA INTERNACAO': 'OBITO',
#     'EVASÃO': 'DESISTENCIA',
#     'PERMAN. POR PROCESS. DE DOEN. ORG.': 'PERMANENCIA',
#     'PERMANENCIA POR INTERCORRENCIA DO PROCEDIMENTO': 'PERMANENCIA',
#     'ALTA DA PUERPERA E OBITO DO RECEM NASCIDO': 'ALTA',
#     'PERMANENCIA P/OUTRA INTERNAÇAO':'PERMANENCIA',
#     'ALTA DA PARTURIENTE E RN': 'ALTA',
#     'ALTA PARA INTERNAÇÃO': 'ALTA',
#     'ALTA MELHORADO': 'ALTA',
#     'OBITO COM DECLARAÇÃO FORNECIDA PELO MED.ASSISTENTE': 'ALTA',
#     'OBITO SEM NECROPSIA ATE 48 HORAS DA INTERNACAO': 'ALTA',
#     'ALTA MELHORADA': 'ALTA',
#     'ALTA POR OUTROS MOTIVOS': 'ALTA',
#     'TRANSFERIDO PARA OUTRO ESTABELECIMENTO': 'TRANSFERENCIA',
#     'TRANSFERENCIA PARA OUTRO ESTABELECIMENTO': 'TRANSFERENCIA',
#     'ALTA CURADO': 'ALTA',
#     'ALTA COM AMBULÂNCIA': 'ALTA',
#     'OBITO SEM NECROPSIA ATE 48HS PAC.EM ESTADO AGONICO': 'OBITO',
#     'OBITO SEM NECROPSIA ATE 48HS PAC.EM ESTADO NÃO AGONICO': 'OBITO',
#     'ALTA DA PUERPERA COM PERMANÊNCIA DO RECEM NASCIDO': 'OBITO',
#     'TRANSFERÊNCIA HOSPITALAR': 'TRANSFERENCIA',
#     'ALTA DA PUERPERA E DO RECEM NASCIDO': 'OBITO',
#     'ALTA A PEDIDO': 'ALTA',
#     'OBITO COM DECLARAÇÃO FORNEC. PELA * I.M.L. *': 'OBITO',
#     'OBITO DA PARTURIENTE SEM NECROPSIA COM PERMANENCIA': 'OBITO',
#     'ALTA DA CONSULTA AMBULATORIAL': 'ALTA',
#     'ALTA ADMINISTRATIVA': 'ALTA',
#     'ALTA P/ COMPLEMENTAÇÃO DE TRATAMENTO AMBULATORIAL': 'ALTA',
#     'ALTA PARA COMPLEMENTO EM REGIME AMBULATORIAL': 'ALTA',
#     'ALTA A PEDIDO/ TERMO DE RESPONSABILIDADE': 'ALTA',
#     'TRANSFERENCIA - CLINICA MEDICA': 'TRANSFERENCIA',
#     'TRANSFERENCIA OUTROS MOTIVOS': 'TRANSFERENCIA',
#     'ALTA PARA PRONTO ATENDIMENTO': 'ALTA',
#     'ALTA DA PUERPERA E OBITO FETAL': 'ALTA',
#     'ALTA INALTERADO': 'ALTA',
#     'TRANSFERENCIA - PSIQUIATRIA': 'ALTA',
#     'OBITO COM NECROPSIA ATE 48HS PAC.EM ESTADO NAO AGONICO': 'OBITO',
#     'TRANSFERENCIA POR PSIQUIATRIA': 'TRANSFERENCIA',
#     'PERMANENCIA POR CARACTERISTICAS PROPRIAS DA DOENÇA': 'PERMANENCIA',
#     'INTERNADO P/DIAGNOSTICO': 'PERMANENCIA'
# }

# df['Discharge_Motive'] = df['Discharge_Motive'].replace(discharge_mapping)

# df = pd.get_dummies(df, columns=['Sex'], drop_first=False)

# # print(df['Discharge_Motive'].unique())
# df.to_csv('Remap_Admission.csv')


# Agregando os 3 datasets

df_admission = pd.read_csv('Remap_Admission.csv')
df_exam = pd.read_csv('Agg_Exams.csv')
# Remove duplicatas da tabela antes de fazer o merge


df_prescription = pd.read_csv('Agg_Prescription.csv')

df_merged = pd.merge(df_admission, df_exam, on=['Hospital_ID', 'Patient_ID'], how='inner')
df_merged = pd.merge(df_merged, df_prescription, on=['Hospital_ID', 'Patient_ID'], how='inner')
df_merged = df_merged.dropna()
df_merged = df_merged.drop(['Unnamed: 0_x', 'Unnamed: 0', 'Unnamed: 0_y'], axis=1)
df_merged = df_merged.drop_duplicates(subset=['Patient_ID', 'Hospital_ID', 'Exam_Name', 'Average_Value'])

df_merged.to_csv('Dataset_Merged.csv')

