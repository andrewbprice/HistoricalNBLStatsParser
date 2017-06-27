# Historical NBL Boxscore Parser

Simple web scraper for grabbing all data from the SportsTG NBL data holdings. Currently exports to CSV files (one for each boxscore)

This script requires a URL from the SportsTG website currently used to hold all the NBL statistical data. An example URL (1997 data) is hard coded into the current repo can be modified to export different seasons.

The list of urls can be found on this page: http://websites.sportstg.com/comp_info.cgi?c=0-189-0-125723-0&a=REPORTS. Just change the season to the one required and click 'Fixture for the entire competition'

Resulting data can be found on https://www.spatialjam.com/nbl-historical-stats<br>
<i>While I didn't exclusively use this tool for grabbing the data for that online database above (just for cleaning up odds and ends), it should be a reasonably good place to start.</i>

# Requirements

Python 3.5 <br>
BeautifulSoup (pip install bs4) <br>
Pandas (pip install pandas) <br>

# To Do

Pandas is currently used to clean up duplicate records in boxscores - while this works fine, there will be a way to do this within the core Python library.

It's likely that a more usable format than individual CSV files for each game would be a single merged file. This functionaility can be built in the future

Date fields are currently a little hit and miss as the website seems to change it's format slightly from season to season. While the dates are still usable in the current format, it should be possible to create a smarter way of grabbing this than just trimming the string.
