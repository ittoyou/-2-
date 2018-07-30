
verse = "welcome to our school"
'''
byte = verse.encode('GBK')#采用GBK编码转换为二进制数据，不处理异常
print('原字符串:',verse)#输出原字符串

print('转换后:',byte)#输出转换后的二进制数据 



verse = "接天莲叶无穷碧，映日荷花别样红"
'''
byte = verse.encode('UTF-8')#采用UTF-8编码转换为二进制数据，不处理异常
print('原字符串:',verse)#输出原字符串
print('转换后:',byte)#输出转换后的二进制数据


'''
print('解码后:',byte.decode('GBK'))

'''
print('解码后:',byte.decode('UTF-8'))

