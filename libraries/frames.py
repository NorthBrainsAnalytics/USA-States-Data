import pandas as pd

inflation_rate = pd.read_excel(
    "~/Documents/USA-States-Data/libraries/data/expected_change_in_infaltion_rates.xlsx").rename \
    (columns={'DATE OF SURVEY': 'month_of_survey',
              'Unnamed: 1': 'year',
              'NEXT YEAR': 'next_year',
              'NEXT 5 YEARS': 'next_5_years'}, inplace=False)

consumer_index = pd.read_excel(
    "~/Documents/USA-States-Data/libraries/data/consumer_sentiment_index.xlsx").rename \
    (columns={'DATE OF SURVEY': 'month_of_survey',
              'Unnamed: 1': 'year',
              'INDEX OF CONSUMER SENTIMENT': 'consumer_sentiment_index'}, inplace=False)


class MeanFrames:
    """ Pick your method:
     👉🏼 single_frame(frame, year: int)
     or
     👉🏼 frames_total(frame, range1: int, range2: int)
     """

    def single_frame(self, frame, year: int) -> dict:
        """ Printing one chosen year from chosen frame:
          1. inflation_rate 👈🏼
          2. consumer_index 👈🏼
          """
        if frame == 'inflation_rate' and year in range(1998, 2023):
            mean_next_year = inflation_rate.loc[inflation_rate['year'] == year]['next_year'].mean()
            mean_next_5_years = inflation_rate.loc[inflation_rate['year'] == year]['next_5_years'].mean()
            d = {'Year': [year], 'NextYearMean': [mean_next_year], 'Next5YearsMean': [mean_next_5_years]}
            df = pd.DataFrame(data=d)
            return df.round(decimals=2)

        elif frame == 'consumer_index' and year in range(1998, 2023):
            c_index = consumer_index.loc[consumer_index['year'] == year]['consumer_sentiment_index'].mean()
            d2 = {'Year': [year], 'consumer_sentiment_index': [c_index]}
            df2 = pd.DataFrame(data=d2)
            return df2.round(decimals=2)

        else:
            print('Wrong table name or year 🙀')


    def frames_total(self, frame, range1: int, range2: int) -> dict:
        """ Printing entire table with indicated range of years """
        if frame == 'inflation_rate' and range1 in range(1998, 2023) and range2 != range1:
            mean_total = (inflation_rate[['year', 'next_year', 'next_5_years']]
                          .groupby('year').agg('mean').round(decimals=2))
            mean_total.reset_index(inplace=True)
            df = mean_total[(range1 <= mean_total.year) & (mean_total.year <= range2)].reset_index(drop=True)
            return df

        elif frame == 'consumer_index' and range1 in range(1998, 2023) and range2 != range1:
            mean_total2 = (consumer_index[['year', 'consumer_sentiment_index']]
                           .groupby('year').agg('mean').round(decimals=2))
            mean_total2.reset_index(inplace=True)
            df = mean_total2[(range1 <= mean_total2.year) & (mean_total2.year <= range2)].reset_index(drop=True)

            # adding column with percentage differences between years
            years = (consumer_index[['year', 'consumer_sentiment_index']]
                     .groupby('year').agg('mean').round(decimals=2))
            years.reset_index(inplace=True)

            y = years.loc[(years['year'] >= 1996) & (years['year'] < 2021)]
            y1 = y.reset_index(inplace=False).drop(columns='index')

            x = years.loc[(years['year'] >= 1997) & (years['year'] < 2022)]
            x1 = x.reset_index(inplace=False).drop(columns='index')

            #merging y1 + x1 to calculate percentage differences
            xy = pd.concat([x1, y1], axis=1, ignore_index=True)
            xy.columns = ['year_1', 'index1', 'year_2', 'index2']

            #building percentage_change_by_year with counted values
            for ind, row in xy.iterrows():
                xy.loc[ind, "percentage_change_by_previous_year"] = (row['index2'] - row['index1']) / row['index2'] * 100
                table = xy.drop(columns=['index1', 'year_2', 'index2']).rename(columns={'year_1':  'year'})

            #merging df with percentage_change_by_previous_year column
            final_table = pd.merge(df, table, on='year')

            return final_table

        else:
            print('Wrong table name or year 🙀')




# check for frames_total method
# x = MeanFrames()
# mean = x.frames_total('consumer_index', 1998, 2021)
# print(mean)

# check for single_frame method
# x = MeanFrames()
# mean2 = x.single_frame('consumer_index', 2021)
# print(mean2)

