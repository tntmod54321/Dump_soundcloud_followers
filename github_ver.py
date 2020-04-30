import os, json, requests

global jsoncollection
global current_chunk
global f
current_chunk = None

#your soundcloud api key
api_key="YOUR_API_KEY"
#A users unique *NUMERICAL* id
user_id="TARGETTED_USER"

def dump_users():
	global jsoncollection
	global current_chunk
	itemlist=0
	for itemlist in range(len(jsoncollection)):
		collection_entry=jsoncollection[itemlist]
		user_url=collection_entry["permalink_url"]
		user_url=(user_url+"\n")
		f.write(user_url)
		itemlist+1
	if(current_chunk==None):
		current_chunk=1
	else:
		current_chunk=(current_chunk+1)
	print("Chunk ", current_chunk, " finished.")

f=open("follower_list.txt", "a+")
urlpart1="https://api-v2.soundcloud.com/users/"
urlpart2="/followers?limit=200&offset=0&linked_partitioning=1"
finalurl=(urlpart1+user_id+urlpart2+"&client_id="+api_key)
r=requests.get(finalurl)
r=r.json()
r=json.dumps(r)
fulljson=json.loads(r)
jsoncollection=fulljson["collection"]
dump_users()
next_url=fulljson["next_href"]
while(True):
	if(next_url==None):
		print("Done!")
		f.close()
		exit()
	next_url=(next_url + "&client_id=" + api_key)
	r=requests.get(next_url)
	r=r.json()
	r=json.dumps(r)
	fulljson=json.loads(r)
	jsoncollection=fulljson["collection"]
	dump_users()
	next_url=fulljson["next_href"]