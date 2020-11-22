# deepl-translate-scraper
A command line tool written in python that scrapes deepl.com and gives you the translation of the entered sentence into the entered language.
<br><br>
This was sort of an experiment but I ended up with a tool that works quite well. Currently it is a little slow since its scraping the website everytime. A better and faster command line utility is in the works.

# Setting up
1. Clone the repository and then navigate to it.
2. Make sure you have python3 and pip installed, check using:
``` python3 --version ``` then
``` pip --version ```
3. Install pipenv using: ``` pip install pipenv ```
4. Install the dependencies using ``` pipenv install ``` <br>
5. Make the script executable using ``` chmod +x path/to/scrapingDeepL2.py ``` <br>
You are good to go!

<br>

# Usage
<br>

Bash syntax for running this script: <br> 
`./scrapingDeepL2.py language_code The sentence to be translated`
<br>

*Note:* Make sure the language code is the ISO-639-1 code. 
