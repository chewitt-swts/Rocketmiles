<b>Development Notes</b>

This test suite was developed in a Linux environment, running Chrome 78.0.3904.70. It was written using Python 3.6.8 in Pycharm Community Edition.

<b>System Requirements</b>

Python 3.6.8 or higher installed

Selenium Python bindings installed

Selenium Webdriver for Chrome downloaded and saved to a directory/folder of your choice

IDE of your choice installed

Chrome 78 or higher

<b>Installation Instructions</b>

<b>***Installing Python</b>

Download Python 3.6.8 or higher at https://www.python.org/downloads/

For installation help, visit this troubleshooting guide: https://realpython.com/installing-python/

***<b>Installing pip</b>

Pip should already be installed when you installed Python. If, for some reason, it is not, here are resources for installing pip:
Windows: https://pip.pypa.io/en/latest/installing/
Linux: https://www.tecmint.com/install-pip-in-linux/

<b>***Installing Selenium Bindings</b>

With pip installed, open your computer’s command line. Use the following command:
Pip install selenium

If you are on a Linux machine, you may need to use 
Sudo pip install selenium

Before proceeding, you will be prompted to log in with your administrator credentials.

<b>***Downloading Selenium Webdriver</b>

Once you’ve installed Selenium’s Python bindings, it’s time to download the Webdriver. Start by going here: https://selenium-python.readthedocs.io/installation.html#drivers

On that webpage, locate the link for Chrome’s drivers. Download the driver from the link. It will come as a zip file. Extract it to the directory/filepath of your choosing. For best results, store it in a simple path, such as /home/USERNAME/Drivers or C:\\Drivers. Save the filepath for reference.

<b>Running the Test Suite</b>

<b>***Test Script Manifest</b>

RocketMilesClass.py
This file contains methods to interact with each element on the website, as well as helper methods to navigate through any test preconditions. 
This file also contains all the Webdriver settings. You will need to update this file with your Webdriver’s local filepath. See the “Running the test cases” section.

SmokeTestAllModules.py

This file contains a test script to automate a smoke test all the way through the search, selection, and checkout process.

SmokeTestMainPageModule.py

This file contains a test script to automate a smoke test for the main search page only.

SmokeTestSearchResultsModule.py

This file contains a test script to automate a smoke test for the search results page only.

SmokeTestHotelDetailsModule.py

This file contains a test script to automate a smoke test for the hotel details page only.

SmokeTestCheckoutModule.py

This file contains a test script to automate a smoke test for the checkout page only.

<b>***Executing the Test Cases</b>

With all system requirements satisfied, it’s time to pull the test scripts from Github and open them in your IDE. Be sure they are all saved to the same directory.

Before running anything, you’ll need to open the RocketMilesClas.py file and change the Webdriver filepath to your local filepath, which you saved above. To do so, find: 

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('-incognito')
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument('--disable-notifications')
        self.chrome_options.add_argument('--disable-popup-blocking')
        self.driver = webdriver.Chrome(r'/home/helkirien/Drivers/chromedriver', options=self.chrome_options)

        self.logger = logging.basicConfig(filename='rocketmiles.log', level=logging.DEBUG)

You’ll want to find the line: 

        self.driver = webdriver.Chrome(r'/home/hugo/Drivers/chromedriver', options=self.chrome_options)

Keep everything the same except for the '/home/hugo/Drivers/chromedriver' string. Keep the ‘ ‘ but change everything inside the ‘ ‘ to your Webdriver’s filepath. 

Then, open any of the test script files in your IDE and use your IDE’s settings to run them. In Pycharm, you can right click anywhere in the file and select to run it, or use hotkey CTRL + SHIFT + F10. Other IDES may have different hotkeys or ways to run a file. 

Once you select to run the file, the test script should open a web browser and perform the actions of each test case. Exceptions and failures are written to a log.

Common failures are TimeOutExceptions and ClickIntercepts. Both can commonly be fixed by adding the time.sleep(5) command to the line before the failure. If that doesn’t solve the problem, more in-depth troubleshooting is required.

<b>***Logs</b>

Each test script is designed to write log files to the same directory that the test scripts are stored in. The script will create a folder titled “logs,” if one does not already exist, and create a subfolder for each test module. If these folders already exist, the script will proceed in creating the log file.

The log files are named with an acronym of the test module and timestamp. The acronyms are:

STAM (Smoke Test All Modules)
STMP (Smoke Test Main Page)
STSR (Smoke Test Search Results)
STHD (Smoke Test Hotel Details)
STC (Smoke Test Checkout)

The timestamp format is as follows:

YEAR_MONTH_DAY__HOURMINUTE_SECONDS

The full filename should read (as an example):

STC_log_2019_11_05__1504_50.log


