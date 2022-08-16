import os
import pandas as pd

 # Read the data path
data_path = 'data/archive'

region_na=['US','CA','MX']
region_eu=['GB','DE','FR','RU']
region_as=['KR','IN','JP']
data_path

# Read the youtube statistics for each country as a data frame
for index, filename in enumerate(os.listdir(data_path)):
    if filename.endswith('.csv'):
        print(filename)
        if index == 0:
            df = pd.read_csv(os.path.join(data_path,filename),low_memory=False,encoding='latin')
            df['country'] = filename[:2]
        else:
            df_new = pd.read_csv(os.path.join(data_path,filename),low_memory=False,encoding='latin')
            df_new['country'] = filename[:2]
            df = pd.concat([df_new, df],axis=0)

# Drop duplicates - video_id might have some
df = df.drop_duplicates(subset='video_id')

# Reset index post dropping duplicates
df = df.reset_index(drop=True)   

# Replace escape chars appropriately 
df = df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r",r' +',r'\.+'], value=["",""," ","."], regex=True)

# Save processed csv to the relevant location
df.to_csv(os.path.join('data/processed', 'processed.csv'), index=False)
