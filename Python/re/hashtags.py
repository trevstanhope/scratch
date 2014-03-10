import re
text = '#sometag something else'
pattern = re.compile(r"#(\w+)")
tags = pattern.findall(text)
print tags
