
import pandas as pd
import numpy as np

df = pd.read_csv("employee_data.csv")
print(df)

random_array = np.random.rand(3,2)
print(random_array)

print(df.head())
print(df.describe())

# 부서별로 그룹화하여 나이의 평균 계산
grouped_df = df.groupby('부서')['나이'].mean()
print(grouped_df)

print(df.isnull().sum())

# 나이 기준으로 정렬
sorted_df = df.sort_values(by='나이')
print(sorted_df.head())

# 등록날짜 기준으로 내림차순 정렬
sorted_df_desc = df.sort_values(by='등록날짜', ascending=False)
print(sorted_df_desc.head())

# 결측치 확인
print(df.isnull().sum());

# 결측치 채우기 fillna 함수 이용(예: 나이의 결측치를 평균 나이로 채우기)
df['나이'].fillna(df['나이'].mean(), inplace=True)

import matplotlib.pyplot as plt

print(df.head())

df_1 = df.loc[['사원번호','나이']]

plt.scatter(df_1)
plt.title('나이 분포')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()