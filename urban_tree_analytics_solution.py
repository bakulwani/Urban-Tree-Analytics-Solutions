
DATA_PATH = "./pune_tree_census"

import pandas as pd
import os
import sqlite3
dfs = []

for file in os.listdir(DATA_PATH):
    if file.endswith(".csv"):
        df_part = pd.read_csv(
            os.path.join(DATA_PATH, file)
        )
        dfs.append(df_part)

df = pd.concat(dfs, ignore_index=True)

df.head(10)

df.columns

df.info()

drop_columns=['FID','geom','sr_no','oid','other_remarks','saar_uid','ward_name']
df=df.drop(columns=drop_columns)

df.shape

print(df['remarks'].value_counts())

print(df.isnull().sum())

df = df.dropna(subset=['ward'])

print(df.isnull().sum())

df = df.drop('special_collar',axis=1)

df['remarks'] = df['remarks'].fillna('No Issue Reported')

bio_cols = ['botanical_name','economic_i','is_rare','phenology','flowering','society_name','road_name']
df[bio_cols] = df[bio_cols].fillna('Not Recorded')

print(df.isnull().sum())

df['remarks'] = df['remarks'].str.lower().str.strip()

remark_map = {
    'no issue reported': 'Normal',
    'mechanically cut': 'Human Damage',
    'mechanical cut': 'Human Damage',
    'diseased': 'Disease',
    'uprooted': 'Physical Damage',
    'dangerous': 'High Risk',
    'on the wall': 'Infrastructure Conflict'
}

df['remark_category'] = df['remarks'].map(remark_map)

df['remark_category'] = df['remark_category'].fillna('Other')

df['remark_category'].value_counts()

df['condition'].value_counts()

df['condition'] = df['condition'].str.lower().str.strip()

health_map = {
    'healthy': 3,
    'average': 2,
    'poor': 1,
    'dead': 0,
    'unknown': 1
}

df['health_score'] = df['condition'].map(health_map)
df['health_score'] = df['health_score'].fillna(1)

import numpy as np

df['canopy_area'] = np.pi * (df['canopy_dia_m'] / 2) ** 2

df['tree_size'] = pd.cut(
    df['girth_cm'],
    bins=[0, 50, 100, 200, 1000],
    labels=['Small', 'Medium', 'Large', 'Very Large']
)

ward_summary = df.groupby('ward').agg(
    total_trees=('id', 'count'),
    avg_health=('health_score', 'mean'),
    poor_trees=('health_score', lambda x: (x <= 1).sum()),  #means that many poor or dead trees (Score) in the ward, neglect dead trees
    total_canopy=('canopy_area', 'sum'), # means green cover of that ward
).reset_index()

ward_summary['poor_tree_ratio'] = (
    ward_summary['poor_trees'] / ward_summary['total_trees']
)

# poor_trees - how many trees need attention
# poor_tree_ratio - how bad the ward condition is   - this tells severity of wards

ward_summary['risk_index'] = (
    ward_summary['poor_tree_ratio'] * (1 / ward_summary['avg_health'])
)

# risk increases when avg_health decreases - inversely proportional
# risk increases when poor_tree_ratio increases

print(ward_summary['risk_index'].describe())

def assign_risk_level(x):
    if x <= 0.0060:        # Median - less than 50 percentile
        return 'Low'
    elif x <= 0.0084:     # 75th percentile
        return 'Medium'
    else:
        return 'High'

ward_summary['risk_level'] = ward_summary['risk_index'].apply(assign_risk_level)

print(ward_summary['risk_level'].value_counts())

print(df.head())

print(ward_summary.head())

conn = sqlite3.connect('urban_tree_analytics.db')
df.to_sql(name="tree_cleaned_row_level",con=conn, if_exists='replace',index=False)
ward_summary.to_sql(name='tree_ward_summary',con=conn,if_exists='replace', index=False)
conn.close()