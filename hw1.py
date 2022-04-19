# 1
import re

s = input()
pattern = r"((https)|(http)):\/\/\w+.\w+.([a-z]{2,4})"


res = re.search(pattern, s)

print(res.group(0))

# 2
import re

s = input()
pattern = r"(https?:\/\/\w+.\w+.[a-z]{2,4})"

res = re.findall(pattern, s)

print(res)

# 3
import re

s = input()
pattern = r" {2,}"

res = re.sub(pattern, '-', s)

print(res)

# 4
import re

s = input()
pattern = r"[;.] "

res = re.split(pattern, s)

print('\n'.join(res))