import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from google.cloud import bigquery
from google.oauth2 import service_account
import re
from datetime import datetime, timedelta

schemaWeekly = [
    bigquery.SchemaField("Filtered_Keyword", "STRING"),
    bigquery.SchemaField("Week", "STRING"),
    bigquery.SchemaField("Year", "DATE"),
    bigquery.SchemaField("End_Date", "DATE"),
    bigquery.SchemaField("Search_Term", "STRING"),
    bigquery.SchemaField("Search_Term_Url", "STRING"),
    bigquery.SchemaField("Search_Frequency_Rank", "INTEGER"),
    bigquery.SchemaField("Top_Clicked_Brands", "STRING"),
    bigquery.SchemaField("Top_Clicked_Categories", "STRING"),
    bigquery.SchemaField("ASIN1", "STRING"),
    bigquery.SchemaField("Product_Title1", "STRING"),
    bigquery.SchemaField("Click_Share1", "FLOAT"),
    bigquery.SchemaField("Conversion_Share1", "STRING"),
    bigquery.SchemaField("ASIN2", "STRING"),
    bigquery.SchemaField("Product_Title2", "STRING"),
    bigquery.SchemaField("Click_Share2", "FLOAT"),
    bigquery.SchemaField("Conversion_Share2", "STRING"),
    bigquery.SchemaField("ASIN3", "STRING"),
    bigquery.SchemaField("Product_Title3", "STRING"),
    bigquery.SchemaField("Click_Share3", "FLOAT"),
    bigquery.SchemaField("Conversion_Share3", "STRING"),
]


schemaMonthly = [
    bigquery.SchemaField("Filtered_Keyword", "STRING"),
    bigquery.SchemaField("Year", "INTEGER"),
    bigquery.SchemaField("Month", "STRING"),
    bigquery.SchemaField("Search_Term", "STRING"),
    bigquery.SchemaField("Search_Term_Url", "STRING"),
    bigquery.SchemaField("Search_Frequency_Rank", "INTEGER"),
    bigquery.SchemaField("Top_Clicked_Brands", "STRING"),
    bigquery.SchemaField("Top_Clicked_Categories", "STRING"),
    bigquery.SchemaField("ASIN1", "STRING"),
    bigquery.SchemaField("Product_Title1", "STRING"),
    bigquery.SchemaField("Click_Share1", "FLOAT"),
    bigquery.SchemaField("Conversion_Share1", "STRING"),
    bigquery.SchemaField("ASIN2", "STRING"),
    bigquery.SchemaField("Product_Title2", "STRING"),
    bigquery.SchemaField("Click_Share2", "FLOAT"),
    bigquery.SchemaField("Conversion_Share2", "STRING"),
    bigquery.SchemaField("ASIN3", "STRING"),
    bigquery.SchemaField("Product_Title3", "STRING"),
    bigquery.SchemaField("Click_Share3", "FLOAT"),
    bigquery.SchemaField("Conversion_Share3", "STRING"),
]

schemaQuarterly = [
    bigquery.SchemaField("Filtered_Keyword", "STRING"),
    bigquery.SchemaField("Year", "INTEGER"),
    bigquery.SchemaField("Quarter", "INTEGER"),
    bigquery.SchemaField("Search_Term", "STRING"),
    bigquery.SchemaField("Search_Term_Url", "STRING"),
    bigquery.SchemaField("Search_Frequency_Rank", "INTEGER"),
    bigquery.SchemaField("Top_Clicked_Brands", "STRING"),
    bigquery.SchemaField("Top_Clicked_Categories", "STRING"),
    bigquery.SchemaField("ASIN1", "STRING"),
    bigquery.SchemaField("Product_Title1", "STRING"),
    bigquery.SchemaField("Click_Share1", "FLOAT"),
    bigquery.SchemaField("Conversion_Share1", "STRING"),
    bigquery.SchemaField("ASIN2", "STRING"),
    bigquery.SchemaField("Product_Title2", "STRING"),
    bigquery.SchemaField("Click_Share2", "STRING"),
    bigquery.SchemaField("Conversion_Share2", "STRING"),
    bigquery.SchemaField("ASIN3", "STRING"),
    bigquery.SchemaField("Product_Title3", "STRING"),
    bigquery.SchemaField("Click_Share3", "STRING"),
    bigquery.SchemaField("Conversion_Share3", "STRING"),
]


class Amazon:
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def land_first_page(self, u):
        self.driver.get(u)
        self.driver.implicitly_wait(10)

    def login_to_amazon(self):
        mail = self.driver.find_element(By.ID, 'ap_email')
        self.driver.implicitly_wait(5)
        mail.send_keys('Email')
        password = self.driver.find_element(By.ID, 'ap_password')
        self.driver.implicitly_wait(5)
        password.send_keys('Password')
        time.sleep(2)
        signin = self.driver.find_element(By.ID, 'signInSubmit')
        self.driver.implicitly_wait(5)
        signin.click()
        time.sleep(20)

    def choose_USA(self):
        choose = self.driver.find_element(By.XPATH, '//div[@id="picker-container"]/div/div[2]/div/div[3]/div/div[5]')
        self.driver.implicitly_wait(15)
        choose.click()
        self.driver.implicitly_wait(15)
        ok_btn = self.driver.find_element(By.XPATH, '//button[@class="picker-switch-accounts-button"]')
        self.driver.implicitly_wait(5)
        ok_btn.click()
        self.driver.implicitly_wait(5)
        time.sleep(5)

    def get_body(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        self.driver.implicitly_wait(5)
        for _ in range(0, 10):
            body.send_keys(Keys.PAGE_DOWN)
        time.sleep(9)

    def get_data_weekly(self, w, sd, ed):
        week_info = self.driver.find_element(By.XPATH, '//kat-dropdown[@id="weekly-week"]').text
        self.driver.implicitly_wait(15)
        print(week_info)

        a0 = []
        a0_5 = []
        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []
        a6 = []
        a7 = []
        a8 = []
        a9 = []
        a10 = []
        a11 = []
        a12 = []
        a13 = []
        a14 = []
        a15 = []

        try:
            cross = self.driver.find_element(By.XPATH, '//div[@id="hmd2f-exit"]')
            self.driver.implicitly_wait(15)
            cross.click()
            time.sleep(2)
        except:
            print("\n")

        zero = self.driver.find_elements(By.XPATH, '//kat-link[@class="css-iz47zr"]/strong')
        self.driver.implicitly_wait(10)
        print(len(zero))
        zeropfive = self.driver.find_elements(By.XPATH, '//kat-link[@class="css-iz47zr"]')
        self.driver.implicitly_wait(10)
        print(len(zeropfive))
        one = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[2]')
        self.driver.implicitly_wait(10)
        print(len(one))
        two = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[3]')
        self.driver.implicitly_wait(10)
        print(len(two))
        three = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[4]')
        self.driver.implicitly_wait(10)
        print(len(three))
        four = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[5]')
        self.driver.implicitly_wait(7)
        print(len(four))
        five = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[6]')
        self.driver.implicitly_wait(7)
        print(len(five))
        six = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[7]')
        self.driver.implicitly_wait(7)
        print(len(six))
        seven = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[8]')
        self.driver.implicitly_wait(7)
        print(len(seven))
        eight = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[9]')
        self.driver.implicitly_wait(7)
        print(len(eight))
        nine = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[10]')
        self.driver.implicitly_wait(7)
        print(len(nine))
        ten = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[11]')
        self.driver.implicitly_wait(7)
        print(len(ten))
        eleven = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[12]')
        self.driver.implicitly_wait(7)
        print(len(eleven))
        twelve = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[13]')
        self.driver.implicitly_wait(7)
        print(len(twelve))
        thirteen = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[14]')
        self.driver.implicitly_wait(7)
        print(len(thirteen))
        fourteen = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[15]')
        self.driver.implicitly_wait(7)
        print(len(fourteen))
        fifteen = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[16]')
        self.driver.implicitly_wait(7)
        print(len(fifteen))
        for z in zero:
            a0.append(z.text)
        for zp in zeropfive:
            a0_5.append(zp.get_attribute('href'))
        for o in one:
            a1.append(o.text)
        for t in two:
            a2.append(t.text)
        for t in three:
            a3.append(t.text)
        for f in four:
            a4.append(f.text)
        for f in five:
            a5.append(f.text)
        for s in six:
            a6.append(s.text)
        for s in seven:
            a7.append(s.text)
        for e in eight:
            a8.append(e.text)
        for n in nine:
            a9.append(n.text)
        for t in ten:
            a10.append(t.text)
        for e in eleven:
            a11.append(e.text)
        for t in twelve:
            a12.append(t.text)
        for t in thirteen:
            a13.append(t.text)
        for f in fourteen:
            a14.append(f.text)
        for f in fifteen:
            a15.append(f.text)

        data = {
            'Filtered Keyword': '',
            'Week': f'Week {w}',
            'Start Date': f'{sd}',
            'End Date': f'{ed}',
            'Search Term': a0,
            'Search Term Url': a0_5,
            'Search Frequency Rank': a1,
            'Top Clicked Brands': a2,
            'Top Clicked Categories': a3,
            'ASIN1': a4,
            'Product Title1': a5,
            'Click Share1': a6,
            'Conversion Share1': a7,
            'ASIN2': a8,
            'Product Title2': a9,
            'Click Share2': a10,
            'Conversion Share2': a11,
            'ASIN3': a12,
            'Product Title3': a13,
            'Click Share3': a14,
            'Conversion Share3': a15
        }
        df = pd.DataFrame(data)
        df.to_csv(f"Week{w}.csv", mode='a', index=False)

        a0.clear()
        a0_5.clear()
        a1.clear()
        a2.clear()
        a3.clear()
        a4.clear()
        a5.clear()
        a6.clear()
        a7.clear()
        a8.clear()
        a9.clear()
        a10.clear()
        a11.clear()
        a12.clear()
        a13.clear()
        a14.clear()
        a15.clear()
        print('OK Done! Click Next....................')

    ## Monthly

    def get_data_Monthly(self, y, m):
        # week_info = self.driver.find_element(By.XPATH, '//kat-dropdown[@id="weekly-week"]').text
        self.driver.implicitly_wait(15)
        # print(week_info)

        a0 = []
        a0_5 = []
        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []
        a6 = []
        a7 = []
        a8 = []
        a9 = []
        a10 = []
        a11 = []
        a12 = []
        a13 = []
        a14 = []
        a15 = []

        try:
            cross = self.driver.find_element(By.XPATH, '//div[@id="hmd2f-exit"]')
            self.driver.implicitly_wait(15)
            cross.click()
            time.sleep(2)
        except:
            print("\n")

        zero = self.driver.find_elements(By.XPATH, '//kat-link[@class="css-iz47zr"]/strong')
        self.driver.implicitly_wait(10)
        print(len(zero))
        zeropfive = self.driver.find_elements(By.XPATH, '//kat-link[@class="css-iz47zr"]')
        self.driver.implicitly_wait(10)
        print(len(zeropfive))
        one = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[2]')
        self.driver.implicitly_wait(10)
        print(len(one))
        two = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[3]')
        self.driver.implicitly_wait(10)
        print(len(two))
        three = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[4]')
        self.driver.implicitly_wait(10)
        print(len(three))
        four = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[5]')
        self.driver.implicitly_wait(7)
        print(len(four))
        five = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[6]')
        self.driver.implicitly_wait(7)
        print(len(five))
        six = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[7]')
        self.driver.implicitly_wait(7)
        print(len(six))
        seven = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[8]')
        self.driver.implicitly_wait(7)
        print(len(seven))
        eight = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[9]')
        self.driver.implicitly_wait(7)
        print(len(eight))
        nine = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[10]')
        self.driver.implicitly_wait(7)
        print(len(nine))
        ten = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[11]')
        self.driver.implicitly_wait(7)
        print(len(ten))
        eleven = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[12]')
        self.driver.implicitly_wait(7)
        print(len(eleven))
        twelve = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[13]')
        self.driver.implicitly_wait(7)
        print(len(twelve))
        thirteen = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[14]')
        self.driver.implicitly_wait(7)
        print(len(thirteen))
        fourteen = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[15]')
        self.driver.implicitly_wait(7)
        print(len(fourteen))
        fifteen = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[16]')
        self.driver.implicitly_wait(7)
        print(len(fifteen))
        for z in zero:
            a0.append(z.text)
        for zp in zeropfive:
            a0_5.append(zp.get_attribute('href'))
        for o in one:
            a1.append(o.text)
        for t in two:
            a2.append(t.text)
        for t in three:
            a3.append(t.text)
        for f in four:
            a4.append(f.text)
        for f in five:
            a5.append(f.text)
        for s in six:
            a6.append(s.text)
        for s in seven:
            a7.append(s.text)
        for e in eight:
            a8.append(e.text)
        for n in nine:
            a9.append(n.text)
        for t in ten:
            a10.append(t.text)
        for e in eleven:
            a11.append(e.text)
        for t in twelve:
            a12.append(t.text)
        for t in thirteen:
            a13.append(t.text)
        for f in fourteen:
            a14.append(f.text)
        for f in fifteen:
            a15.append(f.text)

        data = {
            'Filtered Keyword': '',
            'Year': f'{y}',
            'Month': f'{m}',
            'Search Term': a0,
            'Search Term Url': a0_5,
            'Search Frequency Rank': a1,
            'Top Clicked Brands': a2,
            'Top Clicked Categories': a3,
            'ASIN1': a4,
            'Product Title1': a5,
            'Click Share1': a6,
            'Conversion Share1': a7,
            'ASIN2': a8,
            'Product Title2': a9,
            'Click Share2': a10,
            'Conversion Share2': a11,
            'ASIN3': a12,
            'Product Title3': a13,
            'Click Share3': a14,
            'Conversion Share3': a15
        }
        df = pd.DataFrame(data)
        df.to_csv(f"Month-{m}-{y}.csv", mode='a', index=False)

        a0.clear()
        a0_5.clear()
        a1.clear()
        a2.clear()
        a3.clear()
        a4.clear()
        a5.clear()
        a6.clear()
        a7.clear()
        a8.clear()
        a9.clear()
        a10.clear()
        a11.clear()
        a12.clear()
        a13.clear()
        a14.clear()
        a15.clear()
        print('OK Done! Click Next....................')

    # Quarterly
    def get_data_Quarterly(self, y, q):
        # week_info = self.driver.find_element(By.XPATH, '//kat-dropdown[@id="weekly-week"]').text
        self.driver.implicitly_wait(15)
        # print(week_info)

        a0 = []
        a0_5 = []
        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []
        a6 = []
        a7 = []
        a8 = []
        a9 = []
        a10 = []
        a11 = []
        a12 = []
        a13 = []
        a14 = []
        a15 = []

        try:
            cross = self.driver.find_element(By.XPATH, '//div[@id="hmd2f-exit"]')
            self.driver.implicitly_wait(15)
            cross.click()
            time.sleep(2)
        except:
            print("\n")

        zero = self.driver.find_elements(By.XPATH, '//kat-link[@class="css-iz47zr"]/strong')
        self.driver.implicitly_wait(10)
        print(len(zero))
        zeropfive = self.driver.find_elements(By.XPATH, '//kat-link[@class="css-iz47zr"]')
        self.driver.implicitly_wait(10)
        print(len(zeropfive))
        one = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[2]')
        self.driver.implicitly_wait(10)
        print(len(one))
        two = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[3]')
        self.driver.implicitly_wait(10)
        print(len(two))
        three = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[4]')
        self.driver.implicitly_wait(10)
        print(len(three))
        four = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[5]')
        self.driver.implicitly_wait(7)
        print(len(four))
        five = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[6]')
        self.driver.implicitly_wait(7)
        print(len(five))
        six = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[7]')
        self.driver.implicitly_wait(7)
        print(len(six))
        seven = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[8]')
        self.driver.implicitly_wait(7)
        print(len(seven))
        eight = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[9]')
        self.driver.implicitly_wait(7)
        print(len(eight))
        nine = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[10]')
        self.driver.implicitly_wait(7)
        print(len(nine))
        ten = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[11]')
        self.driver.implicitly_wait(7)
        print(len(ten))
        eleven = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[12]')
        self.driver.implicitly_wait(7)
        print(len(eleven))
        twelve = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[13]')
        self.driver.implicitly_wait(7)
        print(len(twelve))
        thirteen = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[14]')
        self.driver.implicitly_wait(7)
        print(len(thirteen))
        fourteen = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[15]')
        self.driver.implicitly_wait(7)
        print(len(fourteen))
        fifteen = self.driver.find_elements(By.XPATH, '//div[@class="body css-0"]/div/div[16]')
        self.driver.implicitly_wait(7)
        print(len(fifteen))
        for z in zero:
            a0.append(z.text)
        for zp in zeropfive:
            a0_5.append(zp.get_attribute('href'))
        for o in one:
            a1.append(o.text)
        for t in two:
            a2.append(t.text)
        for t in three:
            a3.append(t.text)
        for f in four:
            a4.append(f.text)
        for f in five:
            a5.append(f.text)
        for s in six:
            a6.append(s.text)
        for s in seven:
            a7.append(s.text)
        for e in eight:
            a8.append(e.text)
        for n in nine:
            a9.append(n.text)
        for t in ten:
            a10.append(t.text)
        for e in eleven:
            a11.append(e.text)
        for t in twelve:
            a12.append(t.text)
        for t in thirteen:
            a13.append(t.text)
        for f in fourteen:
            a14.append(f.text)
        for f in fifteen:
            a15.append(f.text)

        data = {
            'Filtered Keyword': '',
            'Year': f'{y}',
            'Quarter': f'{q}',
            'Search Term': a0,
            'Search Term Url': a0_5,
            'Search Frequency Rank': a1,
            'Top Clicked Brands': a2,
            'Top Clicked Categories': a3,
            'ASIN1': a4,
            'Product Title1': a5,
            'Click Share1': a6,
            'Conversion Share1': a7,
            'ASIN2': a8,
            'Product Title2': a9,
            'Click Share2': a10,
            'Conversion Share2': a11,
            'ASIN3': a12,
            'Product Title3': a13,
            'Click Share3': a14,
            'Conversion Share3': a15
        }
        df = pd.DataFrame(data)
        df.to_csv(f"Quarter-{q}-{y}.csv", mode='a', index=False)

        a0.clear()
        a0_5.clear()
        a1.clear()
        a2.clear()
        a3.clear()
        a4.clear()
        a5.clear()
        a6.clear()
        a7.clear()
        a8.clear()
        a9.clear()
        a10.clear()
        a11.clear()
        a12.clear()
        a13.clear()
        a14.clear()
        a15.clear()
        print('OK Done! Click Next....................')

    # The method to click the next button
    def click_next_button(self, i):
        btn = self.driver.find_element(By.XPATH, '//div[@class="css-1v8yaar"]/kat-input[@class="css-x6gsl5"]')
        self.driver.implicitly_wait(25)
        btn.send_keys(Keys.BACKSPACE)
        btn.send_keys(Keys.BACKSPACE, Keys.BACKSPACE)
        btn.send_keys(i)
        btn.send_keys(Keys.ENTER)
        time.sleep(3)

    # The method to load data to BigQuery
    def load_data_to_bigquery(self, file_path, table_id, schema):
        service_account_path = 'Key.json'  # Replace with your actual service account file path
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_path
        credentials = service_account.Credentials.from_service_account_file(service_account_path)
        client = bigquery.Client(credentials=credentials, project=credentials.project_id)

        job_config = bigquery.LoadJobConfig(
            schema=schema,
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            write_disposition="WRITE_APPEND",
        )

        try:
            with open(file_path, "rb") as source_file:
                job = client.load_table_from_file(source_file, table_id, job_config=job_config)
            job.result()  # Wait for the job to complete
            table = client.get_table(table_id)  # Make an API request
            print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")
        except Exception as e:
            print(f"Error occurred: {e}")

    def cleanDataWeekly(self, filePath, type):
        df = pd.read_csv(filePath)
        dropRow = df.apply(lambda row: all(row == df.columns), axis=1)
        df = df[~dropRow]
        df['Filtered Keyword'] = df['Filtered Keyword'].fillna('').astype(str)
        df['Week'] = df['Week'].astype(str)
        df['Start Date'] = pd.to_datetime(df['Start Date']).dt.date
        df['End Date'] = pd.to_datetime(df['End Date']).dt.date
        df['Search Frequency Rank'] = df['Search Frequency Rank'].str.replace(',', '')  # Remove commas
        df['Search Frequency Rank'] = pd.to_numeric(df['Search Frequency Rank'], errors='coerce')  # Convert to numeric
        df['Search Frequency Rank'] = df['Search Frequency Rank'].astype(int)
        for column in ['Click Share1', 'Click Share2', 'Click Share3']:
            if df[column].dtype == object:
                df[column] = df[column].str.replace('%', '').astype(float) / 100
                df[column] = df[column].round(2)
        df['Start Date'] = pd.to_datetime(df['Start Date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
        df['End Date'] = pd.to_datetime(df['End Date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
        df.to_csv(f"{type}-Cleaned.csv", index=False)

    def cleanDataMonthly(self, filePath, type):
        df = pd.read_csv(filePath)
        dropRow = df.apply(lambda row: all(row == df.columns), axis=1)
        df = df[~dropRow]
        df['Filtered Keyword'] = df['Filtered Keyword'].fillna('').astype(str)
        df['Month'] = df['Month'].astype(str)
        df['Search Frequency Rank'] = df['Search Frequency Rank'].str.replace(',', '')  # Remove commas
        df['Search Frequency Rank'] = pd.to_numeric(df['Search Frequency Rank'], errors='coerce')  # Convert to numeric
        df['Search Frequency Rank'] = df['Search Frequency Rank'].astype(int)

        for column in ['Click Share1', 'Click Share2', 'Click Share3']:
            if df[column].dtype == object:
                df[column] = df[column].str.replace('%', '').astype(float) / 100
                df[column] = df[column].round(2)

        df.to_csv(f"{type}-Cleaned.csv", index=False)

    def cleanDataQuarterly(self, filePath, type):
        df = pd.read_csv(filePath)
        dropRow = df.apply(lambda row: all(row == df.columns), axis=1)
        df = df[~dropRow]
        df['Filtered Keyword'] = df['Filtered Keyword'].fillna('').astype(str)
        df['Month'] = df['Month'].astype(str)
        df['Search Frequency Rank'] = df['Search Frequency Rank'].str.replace(',', '')
        df['Search Frequency Rank'] = pd.to_numeric(df['Search Frequency Rank'], errors='coerce')
        df['Search Frequency Rank'] = df['Search Frequency Rank'].astype(int)

        for column in ['Click Share1', 'Click Share2', 'Click Share3']:
            if df[column].dtype == object:
                df[column] = df[column].str.replace('%', '').astype(float) / 100
                df[column] = df[column].round(2)

        df.to_csv(f"{type}-Cleaned.csv", index=False)

def extractDate(url):
    match = re.search(r'\d{4}-\d{2}-\d{2}', url)
    if match:
        return match.group(0)
    else:
        raise ValueError("No valid date found in the URL")

def calcStartDate(end_date_str):
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    start_date = end_date - timedelta(days=6)
    return start_date.strftime('%Y-%m-%d')

def extract_year_month(url: str):
    year_match = re.search(r'year=(\d{4})', url)
    month_match = re.search(r'month=(\d{4})-(\d{2})-\d{2}', url)
    year = year_match.group(1) if year_match else None
    month = month_match.group(2) if month_match else None
    month_name = None
    if month:
        month_names = ["January", "February", "March", "April", "May", "June", "July",
                       "August", "September", "October", "November", "December"]
        month_name = month_names[int(month) - 1]
    return year, month_name

def extract_quarter_and_year(url):
    # Regular expression pattern to match the quarter and year in the URL
    pattern = r'quarterly-year=(\d+)&.*?quarter=(\d+)-(\d+)-\d+'

    # Search the URL for the pattern
    match = re.search(pattern, url)

    # Extract the year and quarter number if a match is found
    if match:
        year = match.group(1)
        month = int(match.group(3))  # Extract the month from the date
        # Calculate the quarter based on the month
        if 1 <= month <= 3:
            quarter = 1
        elif 4 <= month <= 6:
            quarter = 2
        elif 7 <= month <= 9:
            quarter = 3
        else:
            quarter = 4
        return (year, quarter)
    else:
        pass
    return None

print("Please select from of of the Following")
print("1. Weekly Data \n2. Monthly Data \n3. Quaterly Data")
Option = input("Select Your Option: ")

if (Option == "1"):
    type = "Week"
    week = input("Enter Week Number: ")
    URL = input("Enter the URL: ")
    try:
        endDate = extractDate(URL)
        print(f"End Date: {endDate}")
        startDate = calcStartDate(endDate)
        print(f"Start Date: {startDate}")
    except ValueError as e:
        print(e)
    filePathClean = f"Week{week}.csv"
    filePath = f"{type}-Cleaned.csv"
    bigQueryTableID = 'amazon-analysis-409513.amazon_weekly_data.Amazon-Weekly-Table'
    # Instantiate the Amazon bot
    bot = Amazon()
    bot.land_first_page(URL)
    bot.login_to_amazon()
    bot.choose_USA()
    bot.get_body()
    i = 1
    while i <= 100:
        i = i + 1
        if i == 2:
            bot.get_data_weekly(week, startDate, endDate)
            bot.click_next_button(i)
        else:
            bot.get_data_weekly(week, startDate, endDate)
            bot.click_next_button(i)
    bot.cleanDataWeekly(filePathClean, type)
    bot.load_data_to_bigquery(filePath, bigQueryTableID, schemaWeekly)
    bot.driver.quit()
###############################

elif (Option == "2"):
    # Yet to CHange Not Final
    type = "Monthly"
    URL = input("Enter the URL: ")
    Year, Month = extract_year_month(URL)
    print(f"Month: {Month}\nYear: {Year}")
    filePathClean = f"Month-{Month}-{Year}.csv"
    filePath = f"{type}-Cleaned.csv"
    bigQueryTableID = 'amazon-analysis-409513.month_ds_1.Amazon-Monthly-Data'
    # Instantiate the Amazon bot
    bot = Amazon()
    bot.land_first_page(URL)
    bot.login_to_amazon()
    bot.choose_USA()
    bot.get_body()
    i = 1
    while i <= 100:
        i = i + 1
        if i == 2:
            bot.get_data_Monthly(Year, Month)
            bot.click_next_button(i)
        else:
            bot.get_data_Monthly(Year, Month)
            bot.click_next_button(i)
    bot.cleanDataMonthly(filePathClean, type)
    bot.load_data_to_bigquery(filePath, bigQueryTableID, schemaMonthly)
    bot.driver.quit()

elif (Option == "3"):
    # Yet to CHange Not Final
    type = "Quarterly"
    URL = input("Enter the URL: ")
    Year, Quarter = extract_quarter_and_year(URL)
    print(f"Year: {Year}, Quarter: {Quarter}")
    filePathClean = f"Quarter-{Quarter}-{Year}.csv"
    filePath = f"{type}-Cleaned.csv"
    bigQueryTableID = 'amazon-analysis-409513.amazon_quarterly_1.Amazon-Quarterly-Data'
    # Instantiate the Amazon bot
    bot = Amazon()
    bot.land_first_page(URL)
    bot.login_to_amazon()
    bot.choose_USA()
    bot.get_body()
    i = 1
    while i <= 100:
        i = i + 1
        if i == 2:
            bot.get_data_Quarterly(Year, Quarter)
            bot.click_next_button(i)
        else:
            bot.get_data_Quarterly(Year, Quarter)
            bot.click_next_button(i)
    bot.cleanDataQuarterly(filePathClean, type)
    bot.load_data_to_bigquery(filePath, bigQueryTableID, schemaQuarterly)
    bot.driver.quit()
else:
    print("Sorry: You have not selected Correct Option")