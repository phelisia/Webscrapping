
from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup
import re
# url = "http://olympus.realpython.org/profiles/aphrodite"
# page = urlopen(url)
# # print(page)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# # print(html)
# title_index = html.find("<title>")
# # print(title_index)
# start_index = title_index + len("<title>")
# # print(start_index)
# end_index = html.find("</title>")
# # print(end_index)
# title = html[start_index:end_index]
# print(title)
# url = "http://olympus.realpython.org/profiles/poseidon"
# page = urlopen(url)
# # print(page)
# html_bytes=page.read()
# html=html_bytes.decode("utf-8")
# # print(html)
# # print(re.findall("ab*c", "ac"))
# # print(re.findall("ab*c", "abdc"))
# print(re.findall("ab*c", "ABC", re.IGNORECASE))

# another Example
# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")

# pattern = "<title.*?>.*?</title.*?>"
# match_results = re.search(pattern, html, re.IGNORECASE)
# title = match_results.group()
# title = re.sub("<.*?>", "", title) # Remove HTML tags

# print(title)
# a link to webscrapp if you forget https://realpython.com/python-web-scraping-practical-introduction/

# Use an HTML Parser for Web Scraping in Python

# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")
# print(soup.get_text())
# print(soup.find_all("img"))
# image1, image2 = soup.find_all("img")
# print( image1.name)
# print(image1["src"])

# print(soup.title)

# mechanical soup
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)
print(page)
type(page.soup)
print(page.soup)
login_page = browser.get(url)
login_html = login_page.soup
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"
profiles_page = browser.submit(form, login_page.url)
print(profiles_page)

# https://realpython.com/python-web-scraping-practical-introduction/ link to webscrapping python