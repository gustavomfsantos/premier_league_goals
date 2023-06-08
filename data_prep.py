def transform_col(df):
    print("Remove dot from ranking columns")
    df['Ranking Season'] = df['Ranking Season'].str.rstrip('.')
    df['Goals'] = (df['Goals']).astype(int)
    #print("Change season format to single Year, choosing the latter")
    #df['Season'] = '20' + df.apply(lambda x: x['Season'][:2], axis = 1)

    return df

#def merge_season_club(df1, df2):
