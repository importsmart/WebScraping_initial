import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.text')

#res is response object
#res.status_code - check status
#res.text
#res.raise_for_status - raises error if download doesnt work

playfile = open ('Romeoandjuliet.txt','wb')
#wb - write binary

#write in binary files by taking chunks, 100000 is chunk size
for chunk in res.iter_content(100000):
    playfile.write(chunk)

playfile.close()