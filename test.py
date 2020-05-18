import os
url = ["google.com", "africanallianceplc.com", "livescores.com"]
for ip in url:
    reply = os.popen(f"ping {ip}").read()
    if "Received = 4" in reply:
        print(f"UP {ip}. The link is up and running")
    else:
        print(f"DOWN {ip}. The link is down. contact your network administrator")
