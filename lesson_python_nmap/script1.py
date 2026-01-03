# устанавливаем nmap3
import nmap3
# создаем объект сканера
nm = nmap3.Nmap()
# сканируем хост
scan_result = nm.scan_top_ports("192.168.56.99")
# выводим результат сканирования
print(scan_result)
# сохраняем результат сканирования в файл
with open("scan_result.txt", "w") as f:
    f.write(str(scan_result))
# вывести какие службы работают на хосте
for host, info in scan_result.items():
    print(f"Host: {host}")
    if 'ports' in info:
        for port_info in info['ports']:
            port = port_info.get('portid', 'unknown')
            state = port_info.get('state', 'unknown')
            service = port_info.get('service', {}).get('name', 'unknown')
            print(f"Port: {port}, State: {state}, Service: {service}")
    else:
        print("No port information available.")
