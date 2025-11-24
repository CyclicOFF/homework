import pandas as pd
usl = 'titanic.csv'
df = pd.read_csv(usl)
pd.set_option('display.max_columns', None)
print(df)
med=df['Age'].median()
df['Age']=df['Age'].fillna(med)
print(df.isna().sum())
print(df['Pclass'].value_counts())
df['FamilySize']=df['Parch']+df['SibSp']+1
print(df.iloc[14])