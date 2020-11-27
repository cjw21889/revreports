import streamlit as st
import pandas as pd



def main():
    view = st.sidebar.selectbox("chose report", ["Daily Pickup", "Three Month"])

    if view == 'Daily Pickup':
        st.write('Current On The Books')
        current_df = pd.read_csv('otb-11-27.csv')
        yesterday_df = pd.read_csv('otb-11-26.csv')
        actuals = pd.read_csv('actuals.csv')
        current_df.Date = pd.to_datetime(current_df.Date)
        # current_df = current_df.set_index(['Date'])
        act = current_df.groupby('Date', as_index=True)['Res', 'Rev'].sum()
        act['ADR'] = round(act.Rev / act.Res)
        act = act[['Res', 'ADR', 'Rev']]
        # month = current_df.groupby(current_df.Date.dt.month)['Res', 'Rev'].sum()
        st.table(act)

    if view == 'Three Month':
        st.write('Month')


if __name__ == "__main__":
    #df = read_data()
    main()
