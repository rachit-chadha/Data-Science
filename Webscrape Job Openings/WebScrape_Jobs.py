import pandas as pd
from bs4 import BeautifulSoup
from requests import get



#list to store job metrics
title = []
company_name = []
location = []


# variables used for modifying url parameters
query = ["data analyst","data engineer", "business analyst","data architect"]
locations=['baltimore','washington dc']


#header
headers = {"Accept-Language": "en-US, en;q=0.5"}

#looping through locations
for loc in locations:
    #looping through jobs
    for q in query:

        #making a get request
        response=get("https://www.indeed.com/jobs?q=" + q + "&l=" + loc, headers = headers )

        # Parse the content of the request with BeautifulSoup
        bs = BeautifulSoup(response.text, 'html.parser')

        #Creating container for job listings
        job_container = bs.find_all('div', {'class':{'jobsearch-SerpJobCard'}})

        for container in job_container:

            #extracting job title
            position = container.find('a',{'class':'jobtitle turnstileLink '}).text
            title.append(position)

            #extracting company name
            name=container.find('span',{'class':'company'}).text
            company_name.append(name)


            #extracting location
            place=container.find(['span','div'],{'class':{'location accessible-contrast-color-location'}})
            location.append(place.get_text())

#Creating dataframes for to store scraped data
jobs_data = pd.DataFrame({'Title': title,
'Company Name': company_name,
'Location': location,
})

print(jobs_data.info())
jobs_data
jobs_data.to_csv("/Users/Rachit/Desktop/jobs_data.csv")
