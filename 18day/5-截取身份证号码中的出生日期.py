p1 = '你知道我的生日吗?'
print('小明说: ',p1)
p2 = '输入你的身份证号码.'
print('小刘说: ',p2)
idcard = '41072519890507541X'
print('小明说: ',idcard)
birthday = idcard[6:10] + '年' + idcard[10:12] + '月' + idcard[12:14] + '日'#截取生日
print('小刘说: ','你是' + birthday + '出生的,所以你的生日是' + birthday[5:])
