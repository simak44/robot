from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP
http = HTTP()


@task
def genrate_reply_from_Chatgpt():
    browser.configure(
        slowmo=1000,
    )
    # open_facebook()
    open_the_intranet_website()
    # download_traffic_data()
def open_facebook():
    browser.goto('https://www.facebook.com/')
    page= browser.page()
    page.click("a[data-testid='open-registration-form-button']")

def open_the_intranet_website():
    """Navigates to the given URL"""
    browser.goto("https://chatgpt.com/")
    page = browser.page()
    page.fill("#prompt-textarea", "define computer")
    page.click("button[data-testid='send-button']")

def download_traffic_data():
    http.download(
        url="https://www.ppsc.gop.pk/(S(kwf5wkc0f1lr4jed5ompfkbg))/Adds/Corrigendum%20of%20Advertisement%20No%2003-2024.pdf",
        target_file="output/traffic.pdf",
        overwrite=True,
    )

# @task
# def robot_spare_bin_python():
#     """Insert the sales data for the week and export it as a PDF"""
#     browser.configure(
#         slowmo=3000,
#     )

#     open_the_intranet_website()
#     login()
#     open_the_next_page()
#     open_cart()
#     fill_shipping()

# def open_the_intranet_website():
#     """Navigates to the given URL"""
#     browser.goto("http://127.0.0.1:8000/accounts/login/")
# def login():
#     """Fills in the login form and clicks the 'Log in' button"""
#     page = browser.page()
#     page.fill("#id_username", "admin")
#     page.fill("#id_password", "admin")
#     page.click("button[name='submit']")

# def open_the_next_page():
#     browser.goto("http://127.0.0.1:8000/showcart/")

# def button():
#     page=browser.page()
#     page.click("button[name='checkout']")

# def open_cart():
#     browser.goto("http://127.0.0.1:8000/checkoutinfo/")


# def open_address():
#     browser.goto("http://127.0.0.1:8000/checkoutinfo/")

# def fill_shipping():
#     page=browser.page()
#     page.fill("#id_fname", "Muhammad")
#     page.fill("#id_lname", "Ahmad")
#     page.fill("#id_areacode", "63100")
#     page.fill("#id_phone", "03088803944")
#     page.fill("#id_address", "Enigmatix")
#     page.fill("#id_zipcode", "12345")
#     page.click("button[type='submit']")

# def payment():
#     browser.goto('http://127.0.0.1:8000/c')


# from robocorp import browser
# from robocorp.tasks import task
# from RPA.Excel.Files import Files as Excel

# from pathlib import Path
# import os
# import requests

# FILE_NAME = "challenge.xlsx"
# OUTPUT_DIR = Path(os.environ.get('ROBOT_ARTIFACTS'))
# EXCEL_URL = f"https://rpachallenge.com/assets/downloadFiles/{FILE_NAME}"


# @task
# def solve_challenge():
#     """
#     Solve the RPA challenge
    
#     Downloads the source data excel and uses Playwright to solve rpachallenge.com from challenge
#     """
#     browser.configure(
#         browser_engine="chromium",
#         screenshot="only-on-failure",
#         headless=True,
#     )
#     try:
#         excel_file = download_file(EXCEL_URL, OUTPUT_DIR, FILE_NAME)
#         excel = Excel()
#         excel.open_workbook(excel_file)
#         rows = excel.read_worksheet_as_table("Sheet1", header=True)

#         page = browser.goto("https://rpachallenge.com/")
#         page.click("button:text('Start')")
#         for row in rows:
#             fill_and_submit_form(row)
#         element = page.locator("css=div.congratulations")
#         browser.screenshot(element)

#     finally:
#         # Place for teardown and cleanups
#         # Playwright handles browser closing
#         print('Done')


# def download_file(url: str, target_dir: Path, target_filename:str) -> str:
#     """ 
#     Downloads a file from the given url into the given folder with given filename. 
#     """
#     target_dir.mkdir(exist_ok=True)
#     response = requests.get(url)
#     response.raise_for_status()  # This will raise an exception if the request fails
#     local_filename = Path(target_dir, target_filename)
#     with open(local_filename, 'wb') as f:
#         f.write(response.content)  # Write the content of the response to a file
#     return local_filename


# def fill_and_submit_form(row):
#     """
#     Fills a single form with the information of a single row in the Excel
#     """
#     page = browser.page()
#     page.fill("//input[@ng-reflect-name='labelFirstName']", str(row["First Name"]))
#     page.fill("//input[@ng-reflect-name='labelLastName']", str(row["Last Name"]))
#     page.fill("//input[@ng-reflect-name='labelCompanyName']", str(row["Company Name"]))
#     page.fill("//input[@ng-reflect-name='labelRole']", str(row["Role in Company"]))
#     page.fill("//input[@ng-reflect-name='labelAddress']", str(row["Address"]))
#     page.fill("//input[@ng-reflect-name='labelEmail']", str(row["Email"]))
#     page.fill("//input[@ng-reflect-name='labelPhone']", str(row["Phone Number"]))
#     page.click("input:text('Submit')")

from robocorp.tasks import task
from robocorp import browser

from RPA.HTTP import HTTP
from RPA.Excel.Files import Files

@task
def robot_spare_bin_python():
    """Insert the sales data for the week and export it as a PDF"""
    browser.configure(
        slowmo=3000,
    )
    open_the_intranet_website()
    log_in()
    download_excel_file()
    fill_form_with_excel_data()

def open_the_intranet_website():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/")

def log_in():
    """Fills in the login form and clicks the 'Log in' button"""
    page = browser.page()
    page.fill("#username", "maria")
    page.fill("#password", "thoushallnotpass")
    page.click("button:text('Log in')")

def fill_and_submit_sales_form():
    """Fills in the sales data and click the 'Submit' button"""
    page = browser.page()

    page.fill("#firstname", "John")
    page.fill("#lastname", "Smith")
    page.fill("#salesresult", "123")
    page.select_option("#salestarget", "10000")
    page.click("text=Submit")

def download_excel_file():
    """Downloads excel file from the given URL"""
    http = HTTP()
    http.download(url="https://robotsparebinindustries.com/SalesData.xlsx", overwrite=True)


def fill_form_with_excel_data():
    """Read data from excel and fill in the sales form"""
    excel = Files()
    excel.open_workbook("SalesData.xlsx")
    worksheet = excel.read_worksheet_as_table("data", header=True)
    excel.close_workbook()