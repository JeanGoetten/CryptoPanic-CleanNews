from urllib.request import urlopen
import datetime
import json
import pandas as pd 
from tabulate import tabulate

date_moment = datetime.datetime.today()
fmt_clean = date_moment.strftime('%y %m %d  %H %M %S')


token_add = "" '''insert your token from CryptoPanic'''
URL = token_add
Get_Data_URL = urlopen(URL)

data_work = json.load(Get_Data_URL)

results = data_work['results']

with open('timestamp orderer ' + fmt_clean + '.json' , 'a') as outfile:
    json.dump(results, outfile)
outfile.close()

result_len = len(results)

range_data = 0

cluster_title = []
cluster_vote_positive = []
cluster_vote_negative = []
cluster_vote_important = []
cluster_published_at = []

while range_data < result_len:

	results_pos = results[range_data]

	title = results_pos['title']
	votes = results_pos['votes']
	positive = votes['positive']
	negative = votes['negative']
	important = votes['important']
	published_at = results_pos['published_at']
	published_at_fmt = published_at.replace('T', " ")
	published_at_new = published_at_fmt[:-11]
	
	title_list = [title]
	cluster_title.append(title_list)

	range_data = range_data + 1
		
	s = []

	for i in cluster_title:
		if cluster_title not in s:
			s.append(cluster_title)

	cluster_vote_positive.append(positive)

	for i in cluster_vote_positive:
		if cluster_vote_positive not in s:
			s.append(cluster_vote_positive)

	cluster_vote_negative.append(negative)

	for i in cluster_vote_negative:
		if cluster_vote_negative not in s:
			s.append(cluster_vote_negative)

	cluster_vote_important.append(important)

	for i in cluster_vote_important:
		if cluster_vote_important not in s:
			s.append(cluster_vote_important)

	cluster_published_at.append(published_at_new)

	for i in cluster_published_at:
		if cluster_published_at not in s:
			s.append(cluster_published_at)


data = pd.DataFrame({'1) New' : (cluster_title), 
					 '2) Date' : cluster_published_at,
					 '3) +' : cluster_vote_positive,
					 '4) -' : cluster_vote_negative,
					 '5) Important' : cluster_vote_important,						
						})

print(tabulate(data, headers='keys', tablefmt='fancy_grid'))

input("Press Enter to Finish")
