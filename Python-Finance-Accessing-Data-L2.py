import pandas as pd
import requests
import matplotlib.pyplot as plt

# Series


print('==============================================================================================================')
print('# Series\n')
prices = [42.8, 102.03, 240.38, 80.9]
s = pd.Series(prices)
print("Dataframe\n")
print(s)
print("\nDescribe\n")
print(s.describe())

# DataFrame
print('==============================================================================================================')
print("# DataFrame\n")

data = {
    'date': ['2021-06-10', '2021-06-11', '2021-06-12', '2021-06-13'],
    'prices': [42.8, 102.03, 240.38, 80.9]
}
df = pd.DataFrame(data)
print(df)

# Web Scraping
print('==============================================================================================================')
print("\n# Web Scraping\n")
data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
print("All Tables as DataFrame\n")
print(data)
df = data[0]
print("\nAll Tables as DataFrame\n")
print(df)

# Web Scraping
print(
    '\n==============================================================================================================')
print("# Web Scraping 2")
df1 = df[['Symbol', 'Security']]
print(df1)
print(
    '\n==============================================================================================================')
df2 = df1[df['Security'] == 'Apple']
print(df2)
print(
    '\n==============================================================================================================')
print(df.info())
print(
    '\n==============================================================================================================')

# Yahoo Finance Tesla Profile
print(
    '\n==============================================================================================================')
print("# Yahoo Finance Tesla Profile\n")
url_link = 'https://finance.yahoo.com/quote/TSLA/profile'
r = requests.get(url_link, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
data = pd.read_html(r.text)
print(data)

# Yahoo Finance Tesla Analysis
print('\n==============================================================================================================')
print("# Yahoo Finance Tesla Analysis\n")
url_link = 'https://finance.yahoo.com/quote/TSLA/analysis?p=TSLA'
r = requests.get(url_link, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
data = pd.read_html(r.text)
data = data[0]
print(data)
data1 = data[data['Earnings Estimate'] == 'Avg. Estimate']
print(data1)
data1.plot(kind='bar')

plt.savefig('Tesla_Analysis.png')

# Yahoo Finance Tesla Analysis
print('\n==============================================================================================================')

