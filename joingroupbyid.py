from telethon import TelegramClient
import telegram
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

#đọc file
with open('ids.txt', 'r') as ids:
    id = ids.readline()

with open('privateids.txt', 'r') as prids:
    prid = prids.readline()

with open('anothertoken.txt', 'r') as f:
    TOKEN = f.read()

with open('api.txt', 'r') as api:
    api_id = api.read()

with open('api-hash.txt', 'r') as apih:
    api_hash = apih.read()

client = TelegramClient('user', api_id, api_hash)
client.start() #bắt đầu kết nối với telegram và đăng nhập nếu cần

def main():
    #yêu cầu vào các nhóm public trong file
    for itms1 in id: 
        client(JoinChannelRequest(itms1))
        for message in client.iter_messages():
            print(message.sender_id, ':', message.text)


    #yêu cầu vào các nhóm private trong file
    for itm2 in prid:
        updates = client(ImportChatInviteRequest(itm2))
        for message in client.iter_messages():
            print(message.sender_id, ':', message.text)

with client:
    client.loop.run_until_complete(main())
