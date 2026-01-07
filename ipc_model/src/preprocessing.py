import pandas as pd
import re
import ast

def clean_text(text):

    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_sections(sections):

    if isinstance(sections, str):
        try:
            return ast.literal_eval(sections)
        except:
            return None
    return sections

def normalize_ipc(sections):

    if sections is None:
        return None

    cleaned = []

    for sec in sections:
        
        sec = str(sec).strip()
        sec = sec.replace('ipc','').replace('IPC','').replace('Sec','').replace('sec','')
        sec = sec.replace('-', '').replace('.', '').replace(' ', '')
        sec = sec.upper()
        cleaned.append(sec)

    priority_sections = [
        "304B","302","376","307","364A","363","326","325","324","323",
        "354","498A","420","406","467","468","506","507","147","148","149","294","279"
    ]

    for priority in priority_sections:
        if priority in cleaned:
            return f"IPC {priority}"

    if cleaned:
        return f"IPC {cleaned[0]}"

    return None

df = pd.read_csv(r'C:\legal_ai_project\ipc_model\data\raw\indian_bail_judgments.csv')
df = df[['facts','ipc_sections','crime_type']]

df['facts'] = df['facts'].apply(clean_text)

df['ipc_sections'] = df['ipc_sections'].apply(parse_sections)

df['ipc_section'] = df['ipc_sections'].apply(normalize_ipc)

df = df.drop(columns=['ipc_sections'])

df.dropna(subset=['ipc_section'], inplace=True)

df.drop(df[df['crime_type'].isin(['Narcotics', 'Others'])].index, inplace=True)


df.to_csv(r'C:\legal_ai_project\ipc_model\data\processed\processed.csv', index=False)
