import json
import codecs
import re
from datetime import datetime
import time

CATEGORY_FALLBACK = 91
categoryMap = {u"뉴스": 1, u"Interview-한국어": 49, u"프리뷰": 20, u"리뷰": 7}
#id category title slogan content published created modified
SQL_FORMAT = "INSERT INTO `tc_Entries` VALUES (1,1,%d,0,3,0,%d,'%s','%s','%s','ttml','modern','/', 0, 0, NULL,1,1,%d,%d,%d,0,0,0);"

class TcArticle(object):
	def __init__(self, data):
		self.title = data["title"]
		self.title = self.title.replace("'", "\\'")
		
		self.content = data["description"]
		self.content = re.sub("<iframe.*</iframe>", "", self.content)
		self.content = re.sub("<script.*</script>", "", self.content)
		self.content = re.sub('<img src="http://feeds.feedburner.com/~r/.*/>', "", self.content)
		
		self.content = self.content.replace("\n", "")
		self.content = self.content.replace("'", "\\'")
		
		self.category = CATEGORY_FALLBACK
		
		for categoryKey, categoryValue in categoryMap.iteritems():
			if data["category"].find(categoryKey):
				self.category = categoryValue
		
		self.date = int(time.mktime(datetime.strptime(data["published"], "%Y-%m-%d %H:%M:%S").timetuple()))
		
		self.id = int(re.search(re.compile("http:\/\/pig-min.com\/tt\/([0-9]+)\#entry.*"), data["comments"]).group(1))
	
	def toSQL(self):
		return SQL_FORMAT % (self.id, self.category, self.title, self.title, self.content, self.date, self.date, self.date)

outFile = codecs.open("out.sql", "w", "utf-8")
		
def rescue(fileName):
	rescueData = open(fileName, "r")

	articles = json.loads(rescueData.read())

	for article in articles:
		outFile.write(TcArticle(article).toSQL())
		outFile.write("\n")
		
if __name__ == "__main__":
	rescue("rescue_data_1.json")
	rescue("rescue_data_2.json")