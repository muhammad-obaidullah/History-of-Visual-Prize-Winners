'''The Nobel Foundation has made a dataset available 
of all prize winners from the start of the prize, 
in 1901, to 2016. Let's load it in and take a look.'''

# IMPORTS
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# PRINT ALL COLUMNS OF DATAFRAME
pd.set_option("display.max_rows", None, "display.max_columns", None) 

# READ CSV FILE
df = pd.read_csv('E:/My Stuff/E-Course/VVI&C/DS Projects/A Visual History of Nobel Prize Winners/datasets/nobel.csv')

# PRINTING COLUMN INFO
print("-->Printing the Columns in DataFrame:\n",df.columns) 
print("-->Printing the total number of Columns:\n",len(df.columns))
print("-->Printing the DataFrame Info:\n",df.info())
print("-->Printing the Columns Datatypes:\n",df.dtypes)

# COUNT NULL VALUES IN EACH COLUMN
print("-->Printing the Null Values in each Column:\n",df.isnull().sum())


# QUERY1: COUNT NOBEL PRIZE AWARDED CATEGORY-WISE
print('\n===========>EXECUTING QUERY1: NOBEL PRIZE AWARDED CATEGORY-WISE')
print(df.category.value_counts())
print(df.category.unique())
# PLOTTING
ax = sns.countplot(x='category', data=df)
ax.set_title('Nobel Prizes Awarded per category')
for p in ax.patches:
        ax.annotate((p.get_height()), (p.get_x()+0.3, p.get_height()+0.3))
plt.show()


# QUERY2: COUNT NOBEL PRIZE AWARDED GENDER-WISE
print('\n===========>EXECUTING QUERY2: NOBEL PRIZE AWARDED GENDER-WISE')
print(df.sex.value_counts())
print(df.sex.unique())
# PLOTTING
ax = sns.countplot(x='sex', data=df)
ax.set_title('Nobel Prizes Awarded per Gender')
for p in ax.patches:
        ax.annotate((p.get_height()), (p.get_x()+0.38, p.get_height()+0.3))
plt.show()


# QUERY3: PERSONALITY AWARDED WITH THE MOST NOBEL PRIZE
print('\n===========>EXECUTING QUERY3: PERSONALITY AWARDED WITH THE MOST NOBEL PRIZE')
print(df.full_name.value_counts().head(1))
# IN WHICH CATEGORY THE PERSONALITY GOT THE AWARDS
most_prize_awarded = df.groupby(['full_name']).filter(lambda group: len(group) > 2)
print(most_prize_awarded['category'])


# QUERY4: PERSONALITIES WHO GOT MORE THAN ONE AWARD
print('\n===========>EXECUTING QUERY4: PERSONALITIES WHO GOT MORE THAN ONE AWARD')
most_prize_awarded = df.groupby(['full_name']).filter(lambda group: len(group) > 1)
print(most_prize_awarded[['full_name', 'category']].sort_values('full_name'))


# QUERY5: COUNT THE PRIZE AWARDED PER DECADE
print('\n===========>EXECUTING QUERY5: NOBEL PRIZES AWARDED PER DECADE')
# CREATING THE DECADE COLUMN
df['decade'] = (np.floor(df['year'] / 10) * 10).astype(int)
print(df['decade'].value_counts().sort_values())


# QUERY6: COUNT THE PRIZE AWARDED PER CATEGORY IN EACH DECADE
print('\n===========>EXECUTING QUERY6: NOBEL PRIZES AWARDED PER CATEGORY IN EACH DECADE')
print(df.groupby(['decade', 'category'])['category'].count())
# PLOTTING
ax = sns.countplot(x='decade', hue='category', data=df)
ax.set_title('Nobel Prize Awarded in each Category per decade (1901-2016)')
ax.set_xlabel('Decade')
ax.set_ylabel('Count')
plt.legend(loc='upper left')
for p in ax.patches:
    ax.annotate((p.get_height()).astype('int'), (p.get_x(), p.get_height()+0.3), size=6, weight='bold')
plt.show()


# QUERY7: CALCULATING THE AGE OF THE NOBEL PRIZE WINNERS
print('\n===========>EXECUTING QUERY7: PLOT THE AGE OF THE NOBEL PRIZE WINNERS')
# CONVERTING BIRTH_DATE FROM STRING TO DATETIME
df['birth_date'] = pd.to_datetime(df['birth_date'])
df['age'] = df['year'] - df['birth_date'].dt.year
# PLOTTING
ax = sns.lmplot(x='year', y='age', data=df, aspect=2, 
           lowess=True, line_kws={'color' : 'black'})
ax.fig.suptitle('Age of Nobel Prize Winners')
plt.show()


# QUERY8: CALCULATING THE PROPORTION OF FEMALE LAUREATES IN EACH CATEGORY PER DECADE
print('\n===========>EXECUTING QUERY8: PLOT THE PROPORTION OF FEMALE LAUREATES IN EACH CATEGORY PER DECADE')
df['female_winner'] = df['sex'] == 'Female'
prop_female_winners = df.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
# SETTING THEME AND SIZE
sns.set()
plt.rcParams['figure.figsize'] = [11, 7]
# PLOTTING 
ax = sns.lineplot(data=prop_female_winners, x='decade', y='female_winner', hue='category')
ax.set_title('Proportion of Female Laureates in each Category per Decade')
# ADDING %-FORMATTING TO Y-AXIS
PercentFormatter(1.0)
plt.show()


#----------------------------------------------------#
# EXTRAS
# ax.set_xticklabels(ax.get_xticklabels(), fontsize=7)
# plt.rcParams["figure.figsize"] = (8, 4)
# plt.rcParams["xtick.labelsize"] = 7
# plt.legend(loc='upper left')