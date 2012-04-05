#!/usr/bin/python
import urllib2
import json

def timeline(query):
	limit = 20
	
	url = ''.join([
			'http://api.dp.la/dev/item/?search_type=keyword',
			'&query=%s' % query,
			'&limit=%s' % limit,
			])
	jsondata = urllib2.urlopen(url).read()
	pydata = json.loads(jsondata)
	
	datalist = []
	start = '2000'
	
	f = open('your_data.json', 'w')
	
	opening_data = '{"timeline":{"headline":"DPLA Search Timeline","type":"default","startDate":"%s","text":"Hello, World.","date":' % start
	f.write(opening_data)
	
	for item in pydata['docs']:
		if 'date' in item:
			startDate = item['date']
			if '>' in startDate:
			  startDate = "2013"
		else:
			startDate = ''
		if 'title' in item:
			headline = item['title'].replace('"','&quot;')
		else:
			headline = ''
		if 'description' in item:
			text = item['description'][0].replace('"','&quot;')
		else:
			text = ''
		if 'content_link' in item:
			media = item['content_link'][0]
		else:
			media = ''
		if 'data_source' in item:
			credit = item['data_source']
		else:
			credit = ''
	
		output = {}
		asset = {}
		output['startDate'] = startDate
		output['headline'] = headline
		output['text'] = text
		asset['media'] = media
		asset['credit'] = credit
		asset['caption'] = ''
		output['asset'] = asset
		
		datalist.append(output)
		
	datalist = json.dumps(datalist)
	f.write(datalist)
	f.write('}}')
	f.close()

if __name__=="__main__":
	timeline()