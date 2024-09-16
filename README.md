# Share-Market-Prices-v2
This is a website from which you can get data of NSE shares. It is different from Share-Market-Prices-v1 as:
- It is not multipage
- Less Functionalities
- Is on Streamlit Community Cloud
  -This is because I wasn't able to upload Share-Market-Prices-v1 on Stremlit Community Cloud :disappointed:

[The Link For Website](https://share-market-prices.streamlit.app/)

The working:
1. Has input fields for share name, start date, start month, start year, end date, end month, end year

2. When you press Get Graph:
  - Takes data of the share
  - Removing some columns to not plot
  - Using streamlits st.line_chart to plot the dataframe

3. When you press Download Prices:
  - Takes the data
  - Make another button Click Here To Download after doing all the fetching
  - Clicking that button downloads the data

