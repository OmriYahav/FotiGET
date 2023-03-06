import requests
import urllib3
import time
from json import JSONDecodeError


def get_fortigate_info(fortigate_ip, api_key):
    global system_ddns_JSON, system_interfaceJSON, system_globalJSON, monitor_virtual_wanJSON, SystemDDNSJson, SystemInterfaceJson, SystemGlobalJson

    # Define the API endpoints to access
    api_endpoint_address = "/api/v2/cmdb/firewall/address"
    api_endpoint_interface = "/api/v2/cmdb/system/interface/"
    api_endpoint_global = "/api/v2/cmdb/system/global/"
    api_endpoint_sla_log = "/api/v2/monitor/virtual-wan/sla-log"
    api_endpoint_ddns = "/api/v2/cmdb/system/ddns"

    # Define the headers to include the API key
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Define the URLs to access the API
    url_interface = f"https://{fortigate_ip}{api_endpoint_interface}"
    url_global = f"https://{fortigate_ip}{api_endpoint_global}"
    url_sla_log = f"https://{fortigate_ip}{api_endpoint_sla_log}"
    url_ddns = f"https://{fortigate_ip}{api_endpoint_ddns}"
    urllib3.disable_warnings()

    # Make a GET requests
    systemInterface_response = requests.get(url_interface, headers=headers,verify=False)
    systemGlobal_response = requests.get(url_global, headers=headers, verify=False)
    monitorVirtualWan_response = requests.get(url_sla_log, headers=headers, verify=False)
    systemDDNS_response = requests.get(url_ddns, headers=headers, verify=False)

    # Check if the requests were successful and extract the relevant information from the JSON responses:
    if systemInterface_response.status_code and systemGlobal_response.status_code and monitorVirtualWan_response.status_code and systemDDNS_response.status_code == 200:
        # Print the JSON response
        try:
            system_interfaceJSON = systemInterface_response.json()
            system_globalJSON = systemGlobal_response.json()
            monitor_virtual_wanJSON = monitorVirtualWan_response.json()
            system_ddns_JSON = systemDDNS_response.json()

        except JSONDecodeError as e:
            print(f"Error decoding JSON response from FortiGate {fortigate_ip}: {str(e)}")
            print(f"Error: {systemInterface_response.status_code} - {systemInterface_response.text}")

        SystemDDNSJson = {
            'DDNS': system_ddns_JSON['results'][0]['ddns-domain'],
        }

        SystemInterfaceJson = {
            'Http_method': system_interfaceJSON['http_method'],
            'Fortilink': system_interfaceJSON['results'][0]['fortilink'],
            'Wan1-IP': system_interfaceJSON['results'][14]['ip'],
            'Wan1-Username': system_interfaceJSON['results'][14]['username'],
            'Wan2-IP': system_interfaceJSON['results'][15]['ip'],
            'Path': system_interfaceJSON['path'],
            'Name': system_interfaceJSON['name'],
            'Status': system_interfaceJSON['status'],
            'Http_status': system_interfaceJSON['http_status'],
            'Serial': system_interfaceJSON['serial'],
            'Version': system_interfaceJSON['version'],
            'Build': system_interfaceJSON['build'],
            'Internal IP': system_interfaceJSON['results'][4]['ip'],
        }

        SystemGlobalJson = {
            'Hostname': system_globalJSON['results']['hostname'],
            'Administration HTTP Port': system_globalJSON['results']['admin-port'],
            'Administration HTTPS Port': system_globalJSON['results']['admin-sport'],
        }

    #check the length of the results list before trying to access
        if len(monitor_virtual_wanJSON['results']) >= 7:
               MonitorVirtualWanJson = {
               'Name': monitor_virtual_wanJSON['results'][6]['name'],
               'Interface': monitor_virtual_wanJSON['results'][6]['interface'],
               'Link': monitor_virtual_wanJSON['results'][6]['logs'][0]['link'],
               'Latency': monitor_virtual_wanJSON['results'][6]['logs'][0]['latency'],
               'Jitter': monitor_virtual_wanJSON['results'][6]['logs'][0]['jitter'],
               'Packet-loss': monitor_virtual_wanJSON['results'][6]['logs'][0]['packetloss'],
             }
        else:
         #If the results list is shorter than 7, the code sets default values for the MonitorVirtualWanJson dictionary
         MonitorVirtualWanJson = {
            'Name': 'N/A',
            'Interface': 'N/A',
            'Link': 'N/A',
            'Latency': 'N/A',
            'Jitter': 'N/A',
            'Packet-loss': 'N/A',
         }

        # create a list of dictionaries to iterate over
        dictionaries = [SystemDDNSJson, SystemInterfaceJson, MonitorVirtualWanJson, SystemGlobalJson]

        # loop over each dictionary in the list
        for dictionary in dictionaries:
            # print the name of the dictionary being displayed

          # loop over each key-value pair in the dictionary and display them
                for i, value in dictionary.items():
                    print(f"\t{i.upper()}: {value}")







