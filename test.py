#coding=utf-8
import time
import MySQLdb
import interfacedata
import qury_Sales_volume

# a = [2717396.5100000002,
# 2294896.22,
# 1832344.9100000004,
# 1775481.9500000004,
# 1640257.34,
# 1632793.2600000002,
# 1628018.19,
# 1623048.5899999999,
# 1536529.7700000003,
# 1354364.7400000002,
# 1353908.0399999998,
# 1213014.8900000001,
# 1021196.3699999999,
# 595759.1900000001]
# sum = 0
# for i in a:
#     sum += i
#
# print(sum)

b = [2717396.51,2294896.22,1021196.37,1628018.19,1536529.77,1354364.74,1632793.26,1353908.04,1832344.91,1775481.95,1213014.89,1640257.34,595759.19,1623048.59]

su1 = 0
for t in b:
    su1 += t

print(su1 == 22219009.97)