import streamlit as st
import pandas as pd
import datetime

from revreports.params import MONTHS, ROOMCOUNT, CONDENSED_SEG, FULL_SEG
from revreports.dailyframes import create_pickup, create_day_view, create_month_view
from revreports.monthframes import seg_pickup
from revreports.fetch import get_data

TODAY = datetime.datetime.today()


def main():
    view = st.sidebar.selectbox("chose report", ["Monthly Segments", "Daily Pickup", "Matrix"])

    actuals, current_df, yesterday_df, past_df = get_data()


    if view == 'Daily Pickup':

        st.write('Current On The Books by Day')
        year = st.selectbox('Year', [2019, 2020, 2021], index=2)
        length = st.selectbox('Pickup Length', [1,7])

        if length == 1:
          pickup_df = create_pickup(current_df, yesterday_df)
        if length == 7:
          pickup_df = create_pickup(current_df, past_df)

        current_year = pickup_df[pickup_df.Date.dt.year == year]
        current_year = create_month_view(current_year, year)
        st.dataframe(current_year.astype('object'), width=800, height=500)

        month = MONTHS[st.selectbox('Month', list(MONTHS.keys()), index = TODAY.month - 6 )]

        day_df = pickup_df[(pickup_df.Date.dt.month == month) & (pickup_df.Date.dt.year == year)]

        day_df = create_day_view(day_df)

        st.dataframe(day_df, width=800, height=800)

        pop_data = [
            ['City', '2010 Population', '2000 Population'],
            ['New York City, NY', 8175000, 8008000],
            ['Los Angeles, CA', 3792000, 3694000],
            ['Chicago, IL', 2695000, 2896000],
            ['Houston, TX', 2099000, 1953000],
            ['Philadelphia, PA', 1526000, 1517000],
        ]


    if view == 'Monthly Segments':
        st.write('Current On The Books by Segment')
        year = st.selectbox('Year', [2019, 2020, 2021], index=2)
        month = MONTHS[st.selectbox('Month', list(MONTHS.keys()), index = TODAY.month - 6)]
        length = st.selectbox('Pickup Length', [1, 7])
        condensed = st.checkbox('Condensed Segment View')


        if length == 1:
          pickup_df = create_pickup(current_df, yesterday_df)
        if length == 7:
          pickup_df = create_pickup(current_df, past_df)

        current_month = pickup_df[(pickup_df.Date.dt.month == month) & (pickup_df.Date.dt.year == year)]

        if condensed:
            current_month['Code'] = current_month['Code'].map(CONDENSED_SEG)
        else:
            current_month['Code'] = current_month['Code'].map(FULL_SEG)

        st.dataframe(current_month)

    if view == 'Matrix':
        st.write('Work in Progress')
        year = st.selectbox('Year', [2019, 2020, 2021], index=2)
        month = MONTHS[st.selectbox('Month', list(MONTHS.keys()), index = TODAY.month - 6)]
        data = st.radio('Select View',
                             ('On The Books', '1 Day P/U', '7 Day P/U', 'Pace', 'Vs. Budget', 'Vs. Forecast'))
        condensed = st.checkbox('Condensed Segment View')

        if data == '7 Day P/U':
          pickup_df = create_pickup(current_df, past_df)
        else:
          pickup_df = create_pickup(current_df, yesterday_df)


        current_month = pickup_df[(pickup_df.Date.dt.month == month) & (pickup_df.Date.dt.year == year)]
        if condensed:
            current_month['Code'] = current_month['Code'].map(CONDENSED_SEG)
        else:
            current_month['Code'] = current_month['Code'].map(FULL_SEG)

        if data == 'On The Books':
            current_month = current_month.groupby(['Code', 'Date'])[['Res', 'Rev']].sum().unstack().swaplevel(0, 1, axis=1).sort_index(axis=1)
        else:
            current_month = current_month.groupby(['Code', 'Date'])[['Res p/u', 'Rev p/u']].sum().unstack().swaplevel(0, 1, axis=1).sort_index(axis=1)

        st.dataframe(current_month)


if __name__ == "__main__":
    main()
