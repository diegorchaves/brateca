import pandas as pd

df_admission = pd.read_csv("data/B1_Admission.csv")
df_admission = df_admission.sample(frac=0.1, random_state=42)

df_admission['Age'] = (pd.to_datetime(df_admission['Admission_Date']) - pd.to_datetime(df_admission['Birth_Date'])).dt.days // 365
df_admission['Stay_Length'] = (pd.to_datetime(df_admission['Discharge_Date']) - pd.to_datetime(df_admission['Admission_Date'])).dt.days

df_admission = df_admission.drop(['Admission_ID', 'Birth_Date', 'Admission_Date', 'Discharge_Date', 'Unnamed: 11', 'Unnamed: 12'], axis=1)

df_admission['Discharge_Motive'] = df_admission['Discharge_Motive'].str.upper()

discharge_mapping = {
    'ALTA': 'ALTA',
    'OBITO SEM NECROPSIA APOS 48 HORAS DA INTERNACAO':'OBITO',
    'ÓBITO': 'OBITO',
    'OBITO SEM NECROPSIA APOS 48 HORAS DA INTERNACAO': 'OBITO',
    'OBITO SEM NECROPSIA APOS 48HS INTERNAÇÃO': 'OBITO',
    'ALTA POR EVASÃO': 'ALTA',
    'HOME CARE': 'ALTA',
    'ÓBITO SEM NECROPSIA ATE 24 HORAS DE INTERNAÇÃO': 'OBITO',
    'TRANSFERÊNCIA': 'TRANSFERENCIA',
    'OBITO COM NECROPSIA APOS 48HS INTERNAÇÃO': 'OBITO',
    'DESISTÊNCIA DO TRATAMENTO': 'DESISTENCIA',
    'OBITO COM NECROPSIA ATE 48HS PAC.EM ESTADO AGONICO': 'OBITO',
    'ÓBITO COM NECROPSIA APOS 48 HORAS DA INTERNACAO': 'OBITO',
    'EVASÃO': 'DESISTENCIA',
    'PERMAN. POR PROCESS. DE DOEN. ORG.': 'PERMANENCIA',
    'PERMANENCIA POR INTERCORRENCIA DO PROCEDIMENTO': 'PERMANENCIA',
    'ALTA DA PUERPERA E OBITO DO RECEM NASCIDO': 'ALTA',
    'PERMANENCIA P/OUTRA INTERNAÇAO':'PERMANENCIA',
    'ALTA DA PARTURIENTE E RN': 'ALTA',
    'ALTA PARA INTERNAÇÃO': 'ALTA',
    'ALTA MELHORADO': 'ALTA',
    'OBITO COM DECLARAÇÃO FORNECIDA PELO MED.ASSISTENTE': 'ALTA',
    'OBITO SEM NECROPSIA ATE 48 HORAS DA INTERNACAO': 'ALTA',
    'ALTA MELHORADA': 'ALTA',
    'ALTA POR OUTROS MOTIVOS': 'ALTA',
    'TRANSFERIDO PARA OUTRO ESTABELECIMENTO': 'TRANSFERENCIA',
    'TRANSFERENCIA PARA OUTRO ESTABELECIMENTO': 'TRANSFERENCIA',
    'ALTA CURADO': 'ALTA',
    'ALTA COM AMBULÂNCIA': 'ALTA',
    'OBITO SEM NECROPSIA ATE 48HS PAC.EM ESTADO AGONICO': 'OBITO',
    'OBITO SEM NECROPSIA ATE 48HS PAC.EM ESTADO NÃO AGONICO': 'OBITO',
    'ALTA DA PUERPERA COM PERMANÊNCIA DO RECEM NASCIDO': 'OBITO',
    'TRANSFERÊNCIA HOSPITALAR': 'TRANSFERENCIA',
    'ALTA DA PUERPERA E DO RECEM NASCIDO': 'OBITO',
    'ALTA A PEDIDO': 'ALTA',
    'OBITO COM DECLARAÇÃO FORNEC. PELA * I.M.L. *': 'OBITO',
    'OBITO DA PARTURIENTE SEM NECROPSIA COM PERMANENCIA': 'OBITO',
    'ALTA DA CONSULTA AMBULATORIAL': 'ALTA',
    'ALTA ADMINISTRATIVA': 'ALTA',
    'ALTA P/ COMPLEMENTAÇÃO DE TRATAMENTO AMBULATORIAL': 'ALTA',
    'ALTA PARA COMPLEMENTO EM REGIME AMBULATORIAL': 'ALTA',
    'ALTA A PEDIDO/ TERMO DE RESPONSABILIDADE': 'ALTA',
    'TRANSFERENCIA - CLINICA MEDICA': 'TRANSFERENCIA',
    'TRANSFERENCIA OUTROS MOTIVOS': 'TRANSFERENCIA',
    'ALTA PARA PRONTO ATENDIMENTO': 'ALTA',
    'ALTA DA PUERPERA E OBITO FETAL': 'ALTA',
    'ALTA INALTERADO': 'ALTA',
    'TRANSFERENCIA - PSIQUIATRIA': 'ALTA'
}

df_admission['Discharge_Motive'] = df_admission['Discharge_Motive'].replace(discharge_mapping)

df_exam = pd.read_csv("data/B1_Exam.csv")
df_exam = df_exam.sample(frac=0.1, random_state=42)
df_prescription = pd.read_csv("data/B1_Prescription.csv")
df_prescription = df_prescription.sample(frac=0.1, random_state=42)

df_exam = df_exam.drop(['Admission_ID'], axis=1)
df_prescription = df_prescription.drop(['Admission_ID', 'Prescription_ID', 'Prescription_Date', 'Expiration_Date', 'Assessment_Date'], axis=1)

df = pd.merge(df_admission, df_exam, on=['Hospital_ID', 'Patient_ID'], how='inner')
df = pd.merge(df, df_prescription, on=['Hospital_ID', 'Patient_ID'], how='inner')

df = df.drop(['Hospital_ID', 'Patient_ID', 'Skin_Color', 'Weight', 'Height', 'Exam_Date', 'Pharmacy_Assessment', 'Unit'], axis=1)
df = df.dropna()

# One-hot encoding
df = pd.get_dummies(df, columns=['Sex', 'Exam_Name'], drop_first=True)

print(df.head)
print(df.dtypes)
print(df.columns)

df.to_csv('data/dataset.csv')