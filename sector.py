import ImportingData
import gensim
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import pandas as pd
import nltk

job_sectors_initial = {'professional and business services':['accounting','consultant', 'manager', 'director', 'lawyer', 'chief', 'business','strategy', 'sales'], 'education': ['teacher', 'principal', 'school', 'student'], 'health services': ['nurse', 'doctor', 'physician', 'pharmacist', 'therapy', 'care', 'therapist'], 'leisure and hospitality': ['housekeeper','hotel', 'resort'], 'construction': ['construction', 'laborer', 'concrete', 'rebar' ],'engineering' : ['engineer', 'engineers', 'engineering'], 'government': ['police', 'firefighter', 'mail'], 'financial activities':['financial', 'finance', 'bank', 'banker','estate'], 'transportation and warehousing': ['driver', 'warehouse', 'truck'], 'manufacturing':['manufacturing', 'contractor'], 'information technology' : ['computer', 'programming', 'code', 'database', 'IT', 'software', 'hardware'], 'mining and logging': ['mining', 'miner', 'logging', 'forest', 'forestry'], 'utilities': ['electric', 'water', 'pipe', 'infastructure'], 'retail': ['retail', 'store', 'cashier', 'bagger', 'stocker'], 'security':['security', 'guard']}
job_sectors = {}

stemmer = SnowballStemmer('english')

for key, values in job_sectors_initial.items():
    job_sectors[key] = []
    for value in values:
        stem = stemmer.stem(value)
        job_sectors[key].append(stem)

print(job_sectors)



df = ImportingData.LoadAdjustedCSV()


df['sector'] = df['sector'].astype('str')
df['organization'] = df['organization'].astype('str')
df['job_text'] = df['sector'] + ' ' + df['organization'] + ' ' + df['job_title'] + ' ' + df['job_description']
df['job_text'] = df['job_text'].str.lower()


list = []

for job_description in df['job_text']:
    test_text = job_description.split(' ')
    stop_words = set(stopwords.words('english'))

    adjusted_text = []

    for word in test_text:
        if word not in stop_words:
            adjusted_text.append(word)

    frequency_distribution = nltk.FreqDist(adjusted_text)
    top_words = frequency_distribution.most_common(10)
    stemmed_top_words = []
    for word in top_words:
        stemmed_word = stemmer.stem(word[0])
        stemmed_top_words.append(stemmed_word)

    check = 0
    for word in stemmed_top_words:
        if check == 1:
            break
        else:
            for key, values in job_sectors.items():
                if word in values and check == 0:
                    list.append(key)
                    check = 1
                    break

    if check == 0:
        list.append('other')


df['new_sector'] = pd.Series(data = list, index = df.index)

print(df['new_sector'])
df = df.drop(columns = ['job_text'])

pd.DataFrame.to_csv(df, 'adjusted_csv.csv')