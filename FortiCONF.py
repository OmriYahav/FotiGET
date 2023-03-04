import time
from datetime import datetime
import FortiGET

# Replace with your FortiGate's IP address:port and API key
Fortigates = dict(Client1='IP:PORT', Client2='IP:PORT')
Apikeys = dict(Client1='API_KEY', Client2='API_KEY')
now = datetime.now()
dt_string = now.strftime("Date : %d/%m/%Y \nTime: %H:%M:%S")


counter = 0
while True:
 for i in Fortigates:
        print(f'Client: {i.upper()}\n{dt_string}')
        if i in Apikeys:
            FortiGET.get_fortigate_info(fortigate_ip=Fortigates[i], api_key=Apikeys[i])
            counter += 1
            print(f'\nRequest Number:{counter}\n')

        else:
            print(FortiGET.JSONDecodeError)
            print('Check Client Name in Fortigate & Apikeys Dicts , [MUST BE SAME AT TWO OF THE DICTIONARY]')

