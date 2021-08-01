import pandas as pd
import matplotlib.pyplot as plt
plt.figure(figsize=(15,5))
plt.title("India's Annual GDP Growth")
x = ['2016','2017','2018','2019','2020',"2021 forecast","2022 forecast"]
y = [8.3,6.8,6.5,4,-8,11,7]
plt.style.use("ggplot")
plt.xlabel("Years")
plt.ylabel("GDP growth in percentage %")
plt.grid()
plt.plot(x,y,'o-g')
plt.show()