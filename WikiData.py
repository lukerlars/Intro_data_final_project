import pageviewapi as wik
from datetime import date, datetime as dt, timedelta
import pandas as pd


def get_daily_wiki_data(TICKER, start='2017-01-01',
                        end=date.today().strftime(
                            "%Y-%m-%d")):  
    """Function that takes ticker, and name of firm as input and retrieves relevant data as pandas dataframe"""
    Name = TICKER
    out_df = pd.DataFrame()

    wikistart = start.replace('-', '')
    wikiend = end.replace("-", "")
    try:
        wikidata = wik.per_article('en.wikipedia', Name, wikistart, wikiend, access='all-access', agent='all-agents',
                                   granularity='daily')
        df_wiki = pd.DataFrame(wikidata['items'])
        df_wiki['Date'] = pd.to_datetime(df_wiki['timestamp'], format='%Y%m%d%H')
        df_wiki.set_index('Date', inplace=True)
        out_df['wikiviews'] = df_wiki['views']
    except:
        print('fungerte ikke')

    return out_df.dropna() 



