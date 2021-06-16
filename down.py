from webdav3.client import Client
options = {
 'webdav_hostname': "https://b2drop.bsc.es/public.php/webdav/",
 'webdav_login':    "BIMCV-PadChest-FULL",
 'webdav_password': ""
}
client = Client(options)
#client.verify = False # To not check SSL certificates (Default = True)
#client.session.proxies(...) # To set proxy directly into the session (Optional)
#client.session.auth(...) # To set proxy auth directly into the session (Optional)

#client.copy(remote_path_from="", local_path="/home/ss2/data/padchest")
#client.execute_request("ls", '')
#client.pull(remote_directory='', local_directory='/home/ss2/data/padchest')

files = client.list()
files = files[1:]
total = len(files)
print('Total Files:', total)
i = 1
for file in files:
    print('Downloading File: {}/{}'.format(i,total))
    client.download_sync(remote_path=""+str(file), local_path="/home/ss2/data/padchest/" + str(file))
    i+=1