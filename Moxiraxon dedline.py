import pandas as pd

data ={
    'Ism':['Moxira','Maftuna','Mavluda','Ayzirek','Zebo','Hurshida','Munavvar','Gulxayo','Gulchexra','Guljamol'],
    'Yoshi':[18,19,23,17,21,19,20,34,12,25],
    'Shahar':['Fargona','Andijon','Qoqon','Qashqadaryo','Samarqand','Xorazm','Fargona','Namangan','Andijon','Qashqadaryo']
 }
df = pd.DataFrame(data)

print(df)

young_people = df[df['Yoshi'] < 20]
print("20 yoshdan kichik talabalar:\n", young_people)

df['Yoshi'] += 1
print("Yangilangan DataFrame:\n", df)

from google.colab import drive
drive.mount('/content/drive')

