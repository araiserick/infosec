### Решение задания 

настраиваем виртуальное окружение скриптом

[script.sh](./venv.sh)

Пишем скрипт nmap3

[script.py](./script1.py)

Запускаем скрипт и смотрим результат

```
python3 ././script1.py
{'192.168.56.99': {'osmatch': {}, 'ports': [{'protocol': 'tcp', 'portid': '21', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'ftp', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '22', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'ssh', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '23', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'telnet', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '25', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'smtp', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '80', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'http', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '110', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'pop3', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '139', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'netbios-ssn', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '443', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'https', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '445', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'microsoft-ds', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '3389', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'ms-wbt-server', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}], 'hostname': [], 'macaddress': None, 'state': {'state': 'up', 'reason': 'syn-ack', 'reason_ttl': '0'}}, 'runtime': {'time': '1767459046', 'timestr': 'Sat Jan  3 19:50:46 2026', 'summary': 'Nmap done at Sat Jan  3 19:50:46 2026; 1 IP address (1 host up) scanned in 0.13 seconds', 'elapsed': '0.13', 'exit': 'success'}, 'stats': {'scanner': 'nmap', 'args': '/usr/bin/nmap -v -oX - --top-ports 10 192.168.56.99', 'start': '1767459046', 'startstr': 'Sat Jan  3 19:50:46 2026', 'version': '7.94SVN', 'xmloutputversion': '1.05'}, 'task_results': [{'task': 'Ping Scan', 'time': '1767459046', 'extrainfo': '1 total hosts'}, {'task': 'Parallel DNS resolution of 1 host.', 'time': '1767459046'}, {'task': 'Connect Scan', 'time': '1767459046', 'extrainfo': '10 total ports'}]}
Host: 192.168.56.99
Port: 21, State: open, Service: ftp
Port: 22, State: open, Service: ssh
Port: 23, State: open, Service: telnet
Port: 25, State: open, Service: smtp
Port: 80, State: open, Service: http
Port: 110, State: open, Service: pop3
Port: 139, State: open, Service: netbios-ssn
Port: 443, State: open, Service: https
Port: 445, State: open, Service: microsoft-ds
Port: 3389, State: open, Service: ms-wbt-server
Host: runtime
No port information available.
Host: stats
No port information available.
Host: task_results
No port information available.
```