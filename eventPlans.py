from datetime import datetime

TILL_JOBB= [
	[datetime(2018, 5, 3, 6, 30, 5), 'sendMsg', [['TEST'],['Amanda'],'Event started']],
	[datetime(2018, 5, 3, 6, 45, 5), 'goto', [['Christian'],[],'buss_bunkeflostrand_strandhem',datetime(2018, 5, 3, 6, 53, 0)]],
	[datetime(2018, 5, 3, 6, 55, 5), 'sendMsg', [['Christian'],[],'Ta buss 6 mot Toftanäs']],
	[datetime(2018, 5, 3, 7, 10, 5), 'sendMsg', [['Christian'],[],'Hoppa av i Hyllie']],
	[datetime(2018, 5, 3, 7, 12, 5), 'goto', [['Christian'],[],'train_hyllie',datetime(2018, 5, 3, 7, 24, 0)]],
	[datetime(2018, 5, 3, 7, 26, 5), 'sendMsg', [['Christian'],[],'Ta tåg mot Helsingborg']],
	[datetime(2018, 5, 3, 8, 18, 5), 'sendMsg', [['Christian'],[],'Hoppa av i Helsingborg']],
	[datetime(2018, 5, 3, 8, 20, 5), 'goto', [['Christian'],[],'jobb_ikea_hbg',datetime(2018, 5, 3, 8, 35, 0)]]
]


HKX= [
	[datetime(2018, 5, 5, 16, 46, 20), 'sendMsg', [['HKX2'],[],'Event started']],
	[datetime(2018, 5, 5, 16, 47, 0), 'goto', [['HKX2'],[],'Andy',datetime(2018, 5, 5, 16, 53, 0)]],
	[datetime(2018, 5, 5, 16, 47, 15), 'sendMsg', [['David'],[],'Ge Andy 2 klunkar']],
	[datetime(2018, 5, 5, 16, 47, 25), 'sendMsg', [['Andy'],[],'Drick dina 2 jävla klunkar']]
]


TEST= [
	[datetime(2018, 5, 2, 22, 29, 20), 'sendMsg', [['Christian'],[],'Event started']],
	[datetime(2018, 5, 2, 22, 31, 20), 'sendMsg', [['Christian'],[],'Event started']],
	[datetime(2018, 4, 21, 16, 8, 19), 'goto', [['TEST'],[],'Christian',datetime(2018, 4, 22, 19, 2, 39)]],
	[datetime(2018, 4, 21, 16, 8, 25), 'goto', [['TEST'],['Amanda'],'Christian',datetime(2018, 4, 20, 10, 2, 55)]]
]
