import re
bong = [b'', b'CLEARDATA\r\n', b'LABEL,EMG\r\n', b'DATA,973\r\n', b'DATA,972\r\n', b'DATA,972\r\n', b'DATA,973\r\n', b'DATA,973\r\n', b'DATA,973\r\n', b'DATA,972\r\n', b'DATA,973\r\n', b'DATA,972\r\n', b'DATA,973\r\n', b'DATA,973\r\n', b'DATA,972\r\n', b'DATA,972\r\n', b'DATA,973\r\n', b'DATA,973\r\n', b'DATA,973\r\n', b'DATA,973\r\n',]
output = re.findall("\d{3}",str(bong))
print(output)

