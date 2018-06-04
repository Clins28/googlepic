import fcrawl
import re

BASE_URL = "www.google.com"

class picsoup(dosoup):
    def getobject(self, html):
        soup = BeautifulSoup(html, "lxml")
        soup.find_all("a", href = re.compile(imgres?imgurl))



if __name__ == "__main__":
    dpicsoup = picsoup(BASE_URL)
    dpicsoup.getobject(self.html)