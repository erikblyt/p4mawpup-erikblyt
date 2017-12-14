import traceback
import requests
from bs4 import BeautifulSoup
import os
import time

def scrape():
	
	#twilio info
	 global account_sid = 'AC13813ad84a5313d922089ce95941b1b9';
	 global auth_token = 'd4958832fa5859c47d0cda932f9ce7a0';
	 global twilio_phone_number = '+15037555397';
	 global my_phone_number = '+15039154438';
	#beautifulsoup  requests and scraping setup
	url = "http://na.op.gg/champion/statistics";
	r = requests.get(url);
	r.content;
	soup = BeautifulSoup(r.content, 'html.parser');

	soup.prettify()
	item_info_list = soup.find_all("div", {"class":"champion-index-trend-champion__item"});


	for item in item_info_list:
		try:
			inner_item = item.select_one("a")

			rank_el = inner_item.select_one(".champion-trend-champion__rank")
			champion_el = inner_item.select_one(".champion-trend-champion__name")
			winrate_el = inner_item.select_one(".champion-trend-champion__value--winratio")
			pickrate_el = inner_item.select_one(".champion-trend-champion__value--pickratio")
			position_el = inner_item.select_one(".champion-trend-champion__position")

			rank = "Unknown"
			champion = "Unknown"
			winrate = "Unknown"
			pickrate = "Unknown"
			position = "Unknown"
			if rank_el is not None:
				rank = rank_el.text.strip()
			if champion_el is not None:
				champion = champion_el.text.strip()
			if winrate_el is not None:
				winrate = winrate_el.text.strip()
			if pickrate_el is not None:
				pickrate = pickrate_el.text.strip()
			if position_el is not None:
				position = position_el.text.strip().replace("\t", "").replace("\n", "").replace("\r", "")

			print("Rank: " + rank)
			print("Champion: " + champion)
			print("Win Rate: " + winrate)
			print("Pick Rate: " + pickrate)
			print("Position: " + position)

		except Exception as e:
			print("Error retrieving the information for:")
			print(item)
			print(e)
			traceback.print_exc()
			pass		
		
#setting up twilio





		
while True:
	os.system('cls')
	scrape()
	time.sleep(15)
