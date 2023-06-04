import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

page_count = 5
base_url = "https://www.example.com"
delay_seconds = 15

data = []

for page in range(1, page_count + 1):
    url = f"{base_url}/page/{page}"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    titles = soup.select(".title-class")
    descriptions = soup.select(".description-class")

    for title, description in zip(titles, descriptions):
        data.append({"Title": title.text, "Description": description.text})

    time.sleep(delay_seconds)

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("Data extraction completed and saved to data.csv")
