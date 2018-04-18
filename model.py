import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []

def init():
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE
    now = datetime.now()
    # time_string = now.strftime("%b %d, %Y %-I:%M %p")
    time_string = str(now)
    try:
        with open(GUESTBOOK_ENTRIES_FILE,'r') as f:
            entries=json.load(f)
            max_id=-1
            for i in entries:
                if 'id' in i.keys():
                    if int(i['id']) > max_id:
                        max_id=int(i['id'])
            for j in entries:
                if len(entries) != 0:
                    if 'id' not in j.keys():
                        max_id+=1
                        j['id']=max_id
            next_id=max_id+1
            print(next_id)
    except:
        print('Error!')
    entry = {"author": name, "text": text, "timestamp": time_string,"id":str(next_id)}
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE
    try:
        with open(GUESTBOOK_ENTRIES_FILE,'r+') as f:
            entries=json.load(f)
            for i in entries:
                if id == int(i['id']):
                    entries.remove(i)
            f.seek(0)
            f.truncate()
            json.dump(entries, f)
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        # with open(GUESTBOOK_ENTRIES_FILE) as f:
        #     entries=json.load(f)
        #     print(entries)
        print('Deleted id:',id)
    except:
        print('Error!')

def modify_entry(id,text):
    global entries, GUESTBOOK_ENTRIES_FILE
    now = datetime.now()
    # time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    time_string = str(now)
    try:
        with open(GUESTBOOK_ENTRIES_FILE,'r+') as f:
            content=json.load(f)
            for i in content:
                if id == int(i['id']):
                    i['text']=text
                    i['timestamp']=time_string
            entries = content
            f.seek(0)
            f.truncate()
            json.dump(content, f)
        # with open(GUESTBOOK_ENTRIES_FILE) as f:
        #     content=json.load(f)
        #     print(content)
        print('Modified id:',id)
    except:
        print('Error!')
