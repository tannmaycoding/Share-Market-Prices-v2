from nselib import capital_market
import streamlit as st
import pandas as pd

st.title("Stock Market Historical Prices")
name = st.text_input("Name Of The Share: ")

start, end = st.columns(2, vertical_alignment="top")

sdate = start.selectbox("Start Date", options=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
                                               "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",
                                               "25", "26", "27", "28", "29", "30", "31"])
smonth = start.selectbox("Start Month", options=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
syear = start.selectbox("Start Year", options=["2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016",
                                               "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007",
                                               "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998",
                                               "1997", "1996", "1995", "1994", "1993", "1992", "1991", "1990"])
edate = end.selectbox("End Date", options=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
                                           "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",
                                           "25", "26", "27", "28", "29", "30", "31"], index=1)
emonth = end.selectbox("End Month", options=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
eyear = end.selectbox("End Year", options=["2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016",
                                           "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007",
                                           "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998",
                                           "1997", "1996", "1995", "1994", "1993", "1992", "1991", "1990"])

# Define the start and end dates
start_date = f"{sdate}-{smonth}-{syear}"
end_date = f"{edate}-{emonth}-{eyear}"


# Function to fetch prices
@st.cache_data
def fetch_prices():
    try:
        # Fetch data from the library
        d = capital_market.price_volume_and_deliverable_position_data(name, start_date, end_date)
        return d
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None


# Function to convert DataFrame to CSV
@st.cache_data
def convert_df(dataframe: pd.DataFrame):
    return dataframe.to_csv().encode("utf-8")


# Get graph button
if st.button("Get Graph"):
    data = fetch_prices()
    if data is not None:
        df = data[["OpenPrice", "HighPrice", "LowPrice", "ClosePrice", "LastPrice", "AveragePrice"]]
        st.line_chart(df)

# Download prices button
if start_date != end_date:
    if st.button("Download Prices"):
        data = fetch_prices()
        if data is not None:
            csv_data = convert_df(data)
            st.success("Everything is done")
            st.download_button(
                label="Click here to download",
                data=csv_data,
                file_name=f"{name}.csv",
                mime="text/csv"
            )
          
