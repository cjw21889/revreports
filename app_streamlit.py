import streamlit as st
import pandas as pd
import datetime

from revreports.params import MONTHS, ROOMCOUNT
from revreports.frames import create_pickup, create_day_view, create_month_view
from revreports.fetch import get_data

TODAY = datetime.datetime.today()


def main():
    view = st.sidebar.selectbox("chose report", ["Daily Pickup", "Three Month"])

    actuals, current_df, yesterday_df, past_df = get_data()
    # pickup_df_one = create_pickup(current_df, yesterday_df)
    # pickup_df_sev = create_pickup(current_df, past_df)

    if view == 'Daily Pickup':

        st.write('Current On The Books by Day')
        year = st.selectbox('Year', [2019, 2020, 2021], index=1)
        length = st.selectbox('Pickup Length', [1,7])

        if length == 1:
          pickup_df = create_pickup(current_df, yesterday_df)
          # pickup_df = pickup_df_one.copy()
        if length == 7:
          pickup_df = create_pickup(current_df, past_df)
          # pickup_df = pickup_df_sev.copy()

        current_year = pickup_df[pickup_df.Date.dt.year == year]
        current_year = create_month_view(current_year)
        st.dataframe(current_year.astype('object'), width=800, height=500)
        # st.table(current_year.astype('object'))

        month = MONTHS[st.selectbox('Month', list(MONTHS.keys()), index = TODAY.month - 1 )]

        day_df = pickup_df[(pickup_df.Date.dt.month == month) & (pickup_df.Date.dt.year == year)]

        day_df = create_day_view(day_df)

        st.dataframe(day_df, width=800, height=800)
        # st.table(day_df)


    if view == 'Three Month':
        st.write('Month')


        three_month = create_pickup(current_df, yesterday_df)
        three_month = three_month.set_index(['Date','Code']).unstack().swaplevel(0,1,axis=1).sort_index(axis=1)
        # st.dataframe(three_month.astype('object'))
        st.write(three_month.astype('object'))


if __name__ == "__main__":
    #df = read_data()
    main()
