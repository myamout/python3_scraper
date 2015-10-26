#Scrapes A Certain Subreddit For Background Images
import urllib.request
import re

url = 'https://www.reddit.com/r/wallpapers'

response  = urllib.request.urlopen(url)
response_data = response.read()
links = re.findall("http://i.imgur.com/\w+.(?:jpg|gif|png)", str(response_data))

pictureParse = links
picture_names = []
for i in pictureParse:
	temp = i.split("/")
	picture_names.append(temp[3])
package = {links[i]: picture_names[i] for i in range (len(links))}

for link,file_name in package.items():
	urllib.request.urlretrieve(link, file_name)
print("[+] FILES DOWNLOADED")
