import os 
products = []
if os.path.isfile('product.csv'):
    print('yeah! 找到檔案了!')
    with open('product.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品, 價格' in line:
                continue  #直接反覆的概念
        name, price = line.strip().split(',')     #切成兩半後直接填入
        products.append([name, price])
    print(products)
else:
   print('找不到檔案!')




while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    int(price)
    products.append([name,price])
print(products)
for p in products:
   print(p[0], '的價格是', p[1])

with open('product.csv', 'w', encoding='utf-8') as f:
   f.write('商品, 價格\n')
   for p in products:
    f.write(p[0] + ',' + str(p[1]) + '\n') 
