import pandas as pd
import pandas.io.sql as psql
import sqlite3
import numpy as np
#this could be a guide: http://pandas.pydata.org/pandas-docs/stable/indexing.html
#time series: http://pandas.pydata.org/pandas-docs/stable/computation.html
#missing data: http://pandas.pydata.org/pandas-docs/stable/missing_data.html
#groupby: http://pandas.pydata.org/pandas-docs/stable/groupby.html
#merging: http://pandas.pydata.org/pandas-docs/stable/merging.html
#plotting: http://pandas.pydata.org/pandas-docs/stable/visualization.html

#definition: pandas is an "in-memory" database

#creating an in memory dataframe
dates = pd.date_range('1/1/2000',periods=8)
df_in_memory = pd.DataFrame(np.random.randn(8,4), index=dates, columns=['A','B','C','D'])
#print df_in_memory
#print df_in_memory.A
#<==>
#print df_in_memory['A']
#print df_in_memory.B

#reading from a database
con = sqlite3.connect("db")
with con:
    sql = "SELECT * FROM data"
    df = psql.frame_query(sql,con)
    #print df
    #print df.shape

#reading from a csv
df = pd.read_csv("batting_yanks.csv")
#print df
#print df[['HR','Player']]
#creating a view
view = pd.DataFrame({'Player':df['Player'],'AVG':df['AVG']})
view =  view[['Player','AVG']]
#print view

#merging - joins, merges, unions

df = pd.DataFrame(np.random.randn(8,4), columns=['A','B','C','D'])
df1 = df.ix[1:, ['A','B']]
df2 = df.ix[:5, ['C','D']]

#print df
#print df1
#print df2
#merging - more general

#print pd.merge(df1,df2, left_index=True, right_index=True, how='outer')
#print pd.merge(df1,df2, left_index=True, right_index=True, how='inner')

#joining - for those folks used to SQL

#print df1.join(df2, how="outer") #includes missing values - union
#print df1.join(df2, how="inner") #ignores missing values - intersection

#cleaning - handling missing values, doing transformations

df_c = pd.DataFrame(np.random.randn(5,3), index=['a','c','e','f','h'], columns=['one','two','three'])

df_c['four'] = 'bar'
df_c['five'] = df_c['one'] > 0

df_2 = df_c.reindex(['a','b','c','d','e','f','g','h'])
df_3 = df_2.copy()
#print df_2
#print df_2['one']
#print pd.isnull(df_2['one'])

#pandas doesn't care about missing values
#print df_2['one'].sum()

#print df_2.mean(1) 

#print df_2.fillna(0) #fill everything
#print df_2['four'].fillna('missing') #fill a column
#print df_2.fillna(method='pad')#fill intermediate values only

#and now for something complete badass
df_3.interpolate()
#querying

#df.query('(A<B) & (B<C)')


