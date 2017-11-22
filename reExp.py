import re
image = "measure_line.jpg"

result = re.findall(r'[^a-zA-Z0-9]', image)
print result

print len(result)

smth = "measure_line.jpg"
print re.escape(smth)