import re

cmsc = open('cmsc.txt','r')

p = re.compile('^CMSC[0-9]+')
m = re.compile('^0[0-9]+')
t = re.compile('Seats \(Total: ([0-9]+), Open: ([0-9]+), Waitlist: ([0-9]+)\)')
d = re.compile('(M|Tu|W|Th|F)* (.*)$')
b = re.compile('(CSI|ITV|HBK|AVW|MTH|JMP)  ([0-9]*)$')
n = re.compile('.*')

info = ""
classname = ""
for line in cmsc:
    if p.match(line):
        classname = p.match(line).group()
    elif m.match(line):
        print info
        info = classname + ", " + m.match(line).group()
    elif t.match(line):
        matchgroup = t.match(line)
        info += ", " + matchgroup.group(1) + ", " + matchgroup.group(2) + ", " + matchgroup.group(3)
    elif d.match(line):
        matchgroup = d.match(line)
        info += ", " + matchgroup.group(1) + ", " + matchgroup.group(2)
    elif b.match(line):
        matchgroup = b.match(line)
        info += ", " + matchgroup.group(1) + ", " + matchgroup.group(2)
    
