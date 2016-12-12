#http://www.pythonchallenge.com/pc/def/map.html

# K -> M
# O -> Q
# E -> G

txt = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """
r = [chr((ord(i)+2)) for i in txt]
result = ''.join(r)
print result

r2 = [chr((ord(i)+2)) for i in "map"]
result2 = ''.join(r2)
print result2