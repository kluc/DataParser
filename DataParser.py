import urllib2
#1. Make call to API, check for return data

def urlCall():
	#url = raw_input("Please enter url: ")
	url = 'http://www.omdbapi.com/?t=The+Dark+Knight&y=&plot=short&r=json'
	response = urllib2.urlopen(url).read()
	print response



if __name__ == "__main__":
	urlCall()
	