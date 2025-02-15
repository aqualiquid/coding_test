import pandas as pd


def time_spent_by_region(month, df_feature_usage_data, df_user_data):
    """
    :param month: Always present
    :param type: str - structured as YYYY-MM, e.g. "2022-07"

    :param df_feature_usage_data: Always present
    :param type: Dataframe

    :param df_user_data: Always present
    :param type: Dataframe

    :return: a dataframe containing all the regions and their Roadmap
    feature time spent in the last year (last 12 months). For the timespent
    not attributed to a region, put this in a row with "No-Region" as the label.

    For example: If "2022-07" is given, use 2021-08-01 to 2022-07-31 as a range

    Example Output Data Frame:
      Region     Total_Time_Spent
     US-West           4659
     US-East           4595
     US-Central        4528
     No-Region         1009

    Remember to `return` your dataframe output!

    Note: It is important for the tests that your output data frame columns and rows match the example output dataframe
    """

    # import csv files
    df_feature_usage_data = pd.read_csv('../data/usage_data.csv')
    df_user_data = pd.read_csv('../data/user_data.csv')

    # covert to datetime format
    df_feature_usage_data['date'] = pd.to_datetime(df_feature_usage_data['date'])

    start_month = pd.to_datetime(month, format='%Y-%m') - pd.DateOffset(months=11)
    end_month = pd.to_datetime(month, format='%Y-%m')

    # preprocess the features within the date range
    needs_to_filtered = (df_feature_usage_data['date'].dt.to_period('M').between(start_month.to_period('M'), \
                                                                                 end_month.to_period('M')) & (df_feature_usage_data['feature'] == 'Roadmap'))
    filtered_usage = df_feature_usage_data.loc[needs_to_filtered]

    # merge usage and user data
    merged_data = filtered_usage.merge(df_user_data[['Username', 'Region']], \
                                       left_on='username', right_on='Username',how='left')

    # cumulating total_time_spent, followed by sorting
    cumulated_TTS = merged_data.groupby('Region')['time spent'].sum().reset_index(name='Total_Time_Spent')
    cumulated_TTS = cumulated_TTS.sort_values(by='Total_Time_Spent', ascending=False).reset_index(drop=True)

    return cumulated_TTS