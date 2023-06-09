import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.linear_model import Ridge as Ridge
from sklearn.linear_model import Lasso as Lasso
from sklearn.preprocessing import PolynomialFeatures as PF
from sklearn.preprocessing import StandardScaler as SS

from Dividing_Function_Loss import MonthLoss as ML

Subway = pd.read_excel('Data/Subway_Old_Final.xlsx', header=0, usecols=[3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 36])
Loss = ML

Subway = np.array(Subway).reshape(-1, 2)
Loss = np.array(Loss).reshape(-1, 1)

poly = PF(degree=3, include_bias=False)
poly.fit(Subway)
train_poly = poly.transform(Subway)

train_input, test_input, train_target, test_target = tts(train_poly, Loss, test_size=0.2, random_state=42)

lr = LR()
lr.fit(train_input, train_target)

print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))

ss = SS()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

ridge = Ridge()
lasso = Lasso()
ridge.fit(train_scaled, train_target)
print("_------------")
print(ridge.score(train_scaled, train_target))
print(ridge.score(test_scaled, test_target))

train_score = []
test_score = []

alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
  lasso = Lasso(alpha=alpha)
  lasso.fit(train_scaled, train_target)
  train_score.append(lasso.score(train_scaled, train_target))
  test_score.append(lasso.score(test_scaled, test_target))

plt.plot(np.log10(alpha_list), train_score)
plt.plot(np.log10(alpha_list), test_score)
plt.show()

coef = lr.coef_
intercept = lr.intercept_

predictValue = 25918000
predictValue2 = 3728315

sum = 0

for i in range(5):
  if i == 0:
    sum = sum + (coef[0][0] * predictValue)
  elif i == 1:
    sum = sum + (coef[0][1] * predictValue2)
  elif i == 2:
    sum = sum + (coef[0][2] * predictValue ** 2)
  elif i == 3:
    sum = sum + (coef[0][3] * predictValue * predictValue2)
  elif i == 4:
    sum = sum + (coef[0][4] * predictValue2 ** 2)
  elif i == 5:
    sum = sum + (coef[0][5] * predictValue ** 3)
  elif i == 6:
    sum = sum + (coef[0][6] * predictValue ** 2 * predictValue2)
  elif i == 7:
    sum = sum + (coef[0][7] * predictValue * predictValue2 ** 2)
  elif i == 8:
    sum = sum + (coef[0][8] * predictValue2 ** 3)

sum = sum + intercept[0]

print(sum)

print(5.33599202e+09)