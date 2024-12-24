# Amazon-Seller-Central-Bot-to-Scrape-Sells

## Overview
The **Amazon Data Scraper** is a Python-based tool that automates the process of scraping data from Amazon Seller Central for weekly, monthly, and quarterly reports. The tool uses Selenium for web automation and Google BigQuery for data storage and analysis.

## Features
1. **Web Automation**:
   - Automates login and navigation through Amazon’s website.
   - Retrieves data based on weekly, monthly, or quarterly requirements.

2. **Data Cleaning**:
   - Cleans and formats scraped data for analysis.
   - Handles missing values and converts raw data into a structured CSV format.

3. **BigQuery Integration**:
   - Loads cleaned data into Google BigQuery tables.
   - Supports schemas for weekly, monthly, and quarterly datasets.

4. **Customizable Date Extraction**:
   - Extracts start and end dates from URLs for accurate data retrieval.

---

## Installation

### Prerequisites
1. **Python 3.8+**: Ensure Python is installed on your system.
2. **Google Cloud SDK**: Set up Google Cloud and authenticate with your service account.
3. **WebDriver**: Install the appropriate Selenium WebDriver (e.g., Edge).
4. **Python Libraries**:
   - Install required libraries using pip:
     ```bash
     pip install selenium pandas google-cloud-bigquery google-auth
     ```

5. **Service Account Key**:
   - Place your Google Cloud service account key JSON file (e.g., `Key.json`) in the root directory.

---

## File Structure
- `main.py`: Main script to scrape, clean, and upload data.
- `Key.json`: Google Cloud service account credentials.
- Output files:
  - Weekly: `Week<week_number>.csv`
  - Monthly: `Month-<month>-<year>.csv`
  - Quarterly: `Quarter-<quarter>-<year>.csv`
- Cleaned data:
  - `Week-Cleaned.csv`
  - `Monthly-Cleaned.csv`
  - `Quarterly-Cleaned.csv`

---

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. Select the option for data scraping:
   - `1`: Weekly Data
   - `2`: Monthly Data
   - `3`: Quarterly Data

3. Provide the required inputs:
   - Week number, Month, or Quarter.
   - Amazon URL for data extraction.

4. The script will:
   - Log in to Amazon.
   - Scrape the data.
   - Clean and save the data locally.
   - Upload the data to Google BigQuery.

---

## Functions and Modules

### Main Class: `Amazon`

#### Methods:
1. **`land_first_page(u)`**:
   - Navigates to the specified Amazon URL.

2. **`login_to_amazon()`**:
   - Logs in using pre-defined credentials.

3. **`choose_USA()`**:
   - Selects the USA marketplace.

4. **`get_body()`**:
   - Scrolls through the webpage to load all data.

5. **`get_data_weekly(w, sd, ed)`**:
   - Extracts weekly data for the specified week.

6. **`get_data_monthly(y, m)`**:
   - Extracts monthly data for the specified year and month.

7. **`get_data_quarterly(y, q)`**:
   - Extracts quarterly data for the specified year and quarter.

8. **`click_next_button(i)`**:
   - Automates pagination.

9. **`load_data_to_bigquery(file_path, table_id, schema)`**:
   - Uploads cleaned data to BigQuery.

10. **Data Cleaning Methods**:
    - `cleanDataWeekly(filePath, type)`
    - `cleanDataMonthly(filePath, type)`
    - `cleanDataQuarterly(filePath, type)`

---

### Utility Functions

1. **`extractDate(url)`**:
   - Extracts the date from a URL.

2. **`calcStartDate(end_date_str)`**:
   - Calculates the start date based on the end date.

3. **`extract_year_month(url)`**:
   - Extracts year and month from the URL.

4. **`extract_quarter_and_year(url)`**:
   - Extracts quarter and year from the URL.

---

## BigQuery Schema

### Weekly Data Schema
| Field                  | Type    |
|------------------------|---------|
| Filtered_Keyword       | STRING  |
| Week                   | STRING  |
| Year                   | DATE    |
| End_Date               | DATE    |
| Search_Term            | STRING  |
| Search_Term_Url        | STRING  |
| Search_Frequency_Rank  | INTEGER |
| Top_Clicked_Brands     | STRING  |
| Top_Clicked_Categories | STRING  |
| ASIN1                  | STRING  |
| Product_Title1         | STRING  |
| Click_Share1           | FLOAT   |
| Conversion_Share1      | STRING  |
| ASIN2                  | STRING  |
| Product_Title2         | STRING  |
| Click_Share2           | FLOAT   |
| Conversion_Share2      | STRING  |
| ASIN3                  | STRING  |
| Product_Title3         | STRING  |
| Click_Share3           | FLOAT   |
| Conversion_Share3      | STRING  |

### Monthly Data Schema
Similar to weekly but with `Year` and `Month` fields.

### Quarterly Data Schema
Similar to monthly but with `Year` and `Quarter` fields.

---

## Limitations
1. Requires Amazon account credentials.
2. Highly dependent on Amazon's website structure.
3. WebDriver compatibility issues may arise.
4. Rate limiting and CAPTCHA challenges may disrupt scraping.

---

## Future Enhancements
1. Add multi-threading for faster scraping.
2. Implement error handling for login and navigation.
3. Add support for additional data formats.

---

## Contributor
**Anwaar Mirza**

---

## Conclusion
The Amazon Data Scraper provides an efficient and automated way to collect, clean, and analyze data from Amazon's platform. With seamless integration into Google BigQuery, it supports large-scale data analysis for weekly, monthly, and quarterly periods. While there are limitations and potential improvements, this tool forms a solid foundation for data-driven decision-making in e-commerce analytics.

