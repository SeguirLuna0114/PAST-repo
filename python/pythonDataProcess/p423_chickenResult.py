import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

chickenfile = 'chicken.csv'

colnames = ['지역', '브랜드', '매장수']
myframe = pd.read_csv(chickenfile, names=colnames, header=None) # header=None: pandas가 첫번째 행을 데이터로 처리하고 열 이름을 자동으로 할당하지 않도록 함 => 첫번째 행도 데이터로 포함되어 처리됨 ->이후에 사용자가 직접 열 이름을 지정하거나 열 이름 추가가 가능해짐
print(myframe)
#    지역   브랜드  매장수
# 0  서울  페리카나   10
# 1  서울   처가집   15
# 2  서울    굽네   20
# 3  부산  페리카나   25
# 4  부산   처가집   20
# 5  부산    굽네   30
print('-' * 40)

mygrouping = myframe.groupby('브랜드')['매장수']
sumSeries = mygrouping.sum()
sumSeries.index.name = '브랜드'
print(sumSeries)
# 브랜드
# 굽네      50
# 처가집     35
# 페리카나    35
# Name: 매장수, dtype: int64
print('-' * 40)

mycolor = ['red', 'green', 'blue']
mytitle = '브랜드별 매장 개수'
myylim = [0, sumSeries.max() + 5]
myalpha = 0.7

sumSeries.plot(kind='bar', color=mycolor, title=mytitle, legend=False, rot=15, ylim=myylim, grid=False, alpha=myalpha)

filename = 'xx_chick.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()

print(filename + 'finished.')