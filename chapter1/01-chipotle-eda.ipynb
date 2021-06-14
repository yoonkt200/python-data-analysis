{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Copyright (c) 2019 [윤기태]\n",
    "\n",
    "https://github.com/yoonkt200/python-data-analysis\n",
    "\n",
    "[MIT License](https://github.com/yoonkt200/python-data-analysis/blob/master/LICENSE.txt)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# (가제) 파이썬 데이터 분석"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.2) 멕시코풍 프랜차이즈 Chipotle의 주문 데이터 분석하기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 바로가기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- [<Step1. 탐색> : 데이터의 기초 정보 살펴보기](#<Step1.-탐색>-:-데이터의-기초-정보-살펴보기)\n",
    "    - [Chipotle 데이터셋의 기본 정보]\n",
    "    - [Chipotle 데이터셋의 행과 열, 데이터]\n",
    "    - [Chipotle 데이터셋의 수치적 특징 파악]\n",
    "- [<Step2. 인사이트의 발견> : 탐색과 시각화](#<Step2.-인사이트의-발견>-:-탐색과-시각화)\n",
    "    - [가장 많이 주문한 item]\n",
    "    - [item당 주문 개수와 총량 구하기]\n",
    "    - [시각화로 분석 결과 살펴보기]\n",
    "- [<Step3. 데이터 전처리> : 나만의 조력자를 정의하자](#<Step3.-데이터-전처리>-:-나만의-조력자를-정의하자)\n",
    "    - [apply와 lambda 함수를 이용한 데이터 전처리]\n",
    "- [<Step4. 탐색적 분석> : 스무고개로 분석하는 개념적 탐색](#<Step4.-탐색적-분석>-:-스무고개로-분석하는-개념적-탐색)\n",
    "    - [주문당 평균 계산금액 출력하기]\n",
    "    - [한 주문에 10달러 이상 사용한 주문 번호(id) 출력하기]\n",
    "    - [각 아이템의 가격 구하기]\n",
    "    - [가장 비싼 주문에서 item이 총 몇개 팔렸는지 구하기]\n",
    "    - [“Veggie Salad Bowl”이 몇 번 주문되었는지 구하기]\n",
    "    - [“Chicken Bowl”을 2개 이상 주문한 주문 횟수 구하기]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <Step1. 탐색> : 데이터의 기초 정보 살펴보기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [Chipotle 데이터셋의 기본 정보]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "# read_csv 함수로 데이터를 Dataframe 형태로 불러옵니다.\n",
    "file_path = '../data/chipotle.tsv'\n",
    "chipo = pd.read_csv(file_path, sep = '\\t')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4622, 5)\n",
      "------------------------------------\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 4622 entries, 0 to 4621\n",
      "Data columns (total 5 columns):\n",
      " #   Column              Non-Null Count  Dtype \n",
      "---  ------              --------------  ----- \n",
      " 0   order_id            4622 non-null   int64 \n",
      " 1   quantity            4622 non-null   int64 \n",
      " 2   item_name           4622 non-null   object\n",
      " 3   choice_description  3376 non-null   object\n",
      " 4   item_price          4622 non-null   object\n",
      "dtypes: int64(2), object(3)\n",
      "memory usage: 180.7+ KB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(chipo.shape)\n",
    "print(\"------------------------------------\")\n",
    "print(chipo.info())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [Chipotle 데이터셋의 행과 열, 데이터]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>quantity</th>\n",
       "      <th>item_name</th>\n",
       "      <th>choice_description</th>\n",
       "      <th>item_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Chips and Fresh Tomato Salsa</td>\n",
       "      <td>NaN</td>\n",
       "      <td>$2.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Izze</td>\n",
       "      <td>[Clementine]</td>\n",
       "      <td>$3.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Nantucket Nectar</td>\n",
       "      <td>[Apple]</td>\n",
       "      <td>$3.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Chips and Tomatillo-Green Chili Salsa</td>\n",
       "      <td>NaN</td>\n",
       "      <td>$2.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>Chicken Bowl</td>\n",
       "      <td>[Tomatillo-Red Chili Salsa (Hot), [Black Beans...</td>\n",
       "      <td>$16.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>Chicken Bowl</td>\n",
       "      <td>[Fresh Tomato Salsa (Mild), [Rice, Cheese, Sou...</td>\n",
       "      <td>$10.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>Side of Chips</td>\n",
       "      <td>NaN</td>\n",
       "      <td>$1.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>Steak Burrito</td>\n",
       "      <td>[Tomatillo Red Chili Salsa, [Fajita Vegetables...</td>\n",
       "      <td>$11.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>Steak Soft Tacos</td>\n",
       "      <td>[Tomatillo Green Chili Salsa, [Pinto Beans, Ch...</td>\n",
       "      <td>$9.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>Steak Burrito</td>\n",
       "      <td>[Fresh Tomato Salsa, [Rice, Black Beans, Pinto...</td>\n",
       "      <td>$9.25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   order_id  quantity                              item_name  \\\n",
       "0         1         1           Chips and Fresh Tomato Salsa   \n",
       "1         1         1                                   Izze   \n",
       "2         1         1                       Nantucket Nectar   \n",
       "3         1         1  Chips and Tomatillo-Green Chili Salsa   \n",
       "4         2         2                           Chicken Bowl   \n",
       "5         3         1                           Chicken Bowl   \n",
       "6         3         1                          Side of Chips   \n",
       "7         4         1                          Steak Burrito   \n",
       "8         4         1                       Steak Soft Tacos   \n",
       "9         5         1                          Steak Burrito   \n",
       "\n",
       "                                  choice_description item_price  \n",
       "0                                                NaN     $2.39   \n",
       "1                                       [Clementine]     $3.39   \n",
       "2                                            [Apple]     $3.39   \n",
       "3                                                NaN     $2.39   \n",
       "4  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98   \n",
       "5  [Fresh Tomato Salsa (Mild), [Rice, Cheese, Sou...    $10.98   \n",
       "6                                                NaN     $1.69   \n",
       "7  [Tomatillo Red Chili Salsa, [Fajita Vegetables...    $11.75   \n",
       "8  [Tomatillo Green Chili Salsa, [Pinto Beans, Ch...     $9.25   \n",
       "9  [Fresh Tomato Salsa, [Rice, Black Beans, Pinto...     $9.25   "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# chipo 라는 Dataframe에서 순서대로 10개의 row 데이터를 보여줍니다.\n",
    "chipo.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['order_id', 'quantity', 'item_name', 'choice_description',\n",
      "       'item_price'],\n",
      "      dtype='object')\n",
      "------------------------------------\n",
      "RangeIndex(start=0, stop=4622, step=1)\n"
     ]
    }
   ],
   "source": [
    "print(chipo.columns)\n",
    "print(\"------------------------------------\")\n",
    "print(chipo.index)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### 이제 데이터의 수치적 특징 탐색을 위한 간단한 질문들을 정의합니다.\n",
    "\n",
    "- quantity와 item_price의 요약 통계\n",
    "- order_id와 item_name의 개수"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [Chipotle 데이터셋의 수치적 특징 파악]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### describe 함수로 요약 통계량 출력하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "chipo['order_id'] = chipo['order_id'].astype(str) # order_id는 숫자의 의미를 가지지 않기 때문에 str으로 변환합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          quantity\n",
      "count  4622.000000\n",
      "mean      1.075725\n",
      "std       0.410186\n",
      "min       1.000000\n",
      "25%       1.000000\n",
      "50%       1.000000\n",
      "75%       1.000000\n",
      "max      15.000000\n"
     ]
    }
   ],
   "source": [
    "print(chipo.describe()) # chipo dataframe에서 수치형 피처들의 요약 통계량을 확인합니다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### unique 함수로 범주형 피처의 개수 출력하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1834\n",
      "50\n"
     ]
    }
   ],
   "source": [
    "print(len(chipo['order_id'].unique())) # order_id의 개수를 출력합니다.\n",
    "print(len(chipo['item_name'].unique())) # item_name의 개수를 출력합니다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <Step2. 인사이트의 발견> : 탐색과 시각화"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----\n",
    "##### 다음으로, 인사이트를 발견할 수 있을만한 개념적 질문들을 정의합니다.\n",
    "\n",
    "- 가장 많이 주문한 item은 무엇인지\n",
    "- item당 주문의 총량은 얼마인지"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [가장 많이 주문한 item]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Top 1 : Chicken Bowl 726\n",
      "Top 2 : Chicken Burrito 553\n",
      "Top 3 : Chips and Guacamole 479\n",
      "Top 4 : Steak Burrito 368\n",
      "Top 5 : Canned Soft Drink 301\n",
      "Top 6 : Steak Bowl 211\n",
      "Top 7 : Chips 211\n",
      "Top 8 : Bottled Water 162\n",
      "Top 9 : Chicken Soft Tacos 115\n",
      "Top 10 : Chicken Salad Bowl 110\n"
     ]
    }
   ],
   "source": [
    "# 가장 많이 주문한 item : top 10을 출력합니다.\n",
    "item_count = chipo['item_name'].value_counts()[:10]\n",
    "for idx, (val, cnt) in enumerate(item_count.iteritems(), 1):\n",
    "    print(\"Top\", idx, \":\", val, cnt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Chicken Bowl'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "chipo['item_name'].value_counts().index.tolist()[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [item당 주문 개수와 총량 구하기]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "item_name\n",
       "6 Pack Soft Drink         54\n",
       "Barbacoa Bowl             66\n",
       "Barbacoa Burrito          91\n",
       "Barbacoa Crispy Tacos     11\n",
       "Barbacoa Salad Bowl       10\n",
       "Barbacoa Soft Tacos       25\n",
       "Bottled Water            162\n",
       "Bowl                       2\n",
       "Burrito                    6\n",
       "Canned Soda              104\n",
       "Name: order_id, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# item당 주문 개수를 출력합니다.\n",
    "order_count = chipo.groupby('item_name')['order_id'].count()\n",
    "order_count[:10] # item당 주문 개수를 출력합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "item_name\n",
       "6 Pack Soft Drink         55\n",
       "Barbacoa Bowl             66\n",
       "Barbacoa Burrito          91\n",
       "Barbacoa Crispy Tacos     12\n",
       "Barbacoa Salad Bowl       10\n",
       "Barbacoa Soft Tacos       25\n",
       "Bottled Water            211\n",
       "Bowl                       4\n",
       "Burrito                    6\n",
       "Canned Soda              126\n",
       "Name: quantity, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# item당 주문 총량을 출력합니다.\n",
    "item_quantity = chipo.groupby('item_name')['quantity'].sum()\n",
    "item_quantity[:10] # item당 주문 총량을 출력합니다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [시각화로 분석 결과 살펴보기]\n",
    "- 지금까지의 분석 결과를 간단한 시각화로 표현"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "item_name_list = item_quantity.index.tolist()\n",
    "x_pos = np.arange(len(item_name_list))\n",
    "order_cnt = item_quantity.values.tolist()\n",
    " \n",
    "plt.bar(x_pos, order_cnt, align='center')\n",
    "plt.ylabel('ordered_item_count')\n",
    "plt.title('Distribution of all orderd item')\n",
    " \n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### `[미니 퀴즈 - 1.1]`\n",
    "- `pandas에서 유용하게 사용되는 함수 value_counts()와 unique()의 차이점은 무엇일까요?` \n",
    "    - 각 함수는 어떤 데이터 타입에 적용이 되는지, 어떤 기능을 가지고 있는지, 정확히 어떤 결과값을 반환하는지 실행해봅시다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chicken Bowl           726\n",
      "Chicken Burrito        553\n",
      "Chips and Guacamole    479\n",
      "Steak Burrito          368\n",
      "Canned Soft Drink      301\n",
      "Steak Bowl             211\n",
      "Chips                  211\n",
      "Bottled Water          162\n",
      "Chicken Soft Tacos     115\n",
      "Chicken Salad Bowl     110\n",
      "Name: item_name, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(chipo['item_name'].value_counts()[:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.series.Series'>\n"
     ]
    }
   ],
   "source": [
    "print(type(chipo['item_name'].value_counts()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Chips and Fresh Tomato Salsa' 'Izze' 'Nantucket Nectar'\n",
      " 'Chips and Tomatillo-Green Chili Salsa' 'Chicken Bowl' 'Side of Chips'\n",
      " 'Steak Burrito' 'Steak Soft Tacos' 'Chips and Guacamole'\n",
      " 'Chicken Crispy Tacos']\n"
     ]
    }
   ],
   "source": [
    "print(chipo['item_name'].unique()[:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "print(type(chipo['item_name'].unique()))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <Step3. 데이터 전처리> : 나만의 조력자를 정의하자"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [apply와 lambda 함수를 이용한 데이터 전처리]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 4622 entries, 0 to 4621\n",
      "Data columns (total 5 columns):\n",
      " #   Column              Non-Null Count  Dtype \n",
      "---  ------              --------------  ----- \n",
      " 0   order_id            4622 non-null   object\n",
      " 1   quantity            4622 non-null   int64 \n",
      " 2   item_name           4622 non-null   object\n",
      " 3   choice_description  3376 non-null   object\n",
      " 4   item_price          4622 non-null   object\n",
      "dtypes: int64(1), object(4)\n",
      "memory usage: 180.7+ KB\n",
      "None\n",
      "-------------\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0     $2.39 \n",
       "1     $3.39 \n",
       "2     $3.39 \n",
       "3     $2.39 \n",
       "4    $16.98 \n",
       "Name: item_price, dtype: object"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(chipo.info())\n",
    "print('-------------')\n",
    "chipo['item_price'].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>quantity</th>\n",
       "      <th>item_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>4622.000000</td>\n",
       "      <td>4622.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1.075725</td>\n",
       "      <td>7.464336</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.410186</td>\n",
       "      <td>4.245557</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.090000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.390000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>8.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>9.250000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>44.250000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          quantity   item_price\n",
       "count  4622.000000  4622.000000\n",
       "mean      1.075725     7.464336\n",
       "std       0.410186     4.245557\n",
       "min       1.000000     1.090000\n",
       "25%       1.000000     3.390000\n",
       "50%       1.000000     8.750000\n",
       "75%       1.000000     9.250000\n",
       "max      15.000000    44.250000"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# column 단위 데이터에 apply 함수로 전처리를 적용합니다.\n",
    "chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))\n",
    "chipo.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     2.39\n",
       "1     3.39\n",
       "2     3.39\n",
       "3     2.39\n",
       "4    16.98\n",
       "Name: item_price, dtype: float64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "chipo['item_price'].head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <Step4. 탐색적 분석> : 스무고개로 분석하는 개념적 탐색\n",
    "\n",
    "##### 데이터를 이해하기 위한 조금 더 복잡한 질문들로 탐색적 데이터 분석 연습하기\n",
    "\n",
    "\n",
    "- 주문당 평균 계산금액 출력하기\n",
    "- 한 주문에 10달러 이상 사용한 주문의 id들 출력하기\n",
    "- 각 아이템의 가격 구하기\n",
    "- 가장 비싼 주문에서 item이 몇개 팔렸는지 구하기\n",
    "- “Veggie Salad Bowl”이 몇 번 주문되었는지 구하기\n",
    "- “Chicken Bowl”을 2개 이상 주문한 주문 횟수 구하기\n",
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [주문당 평균 계산금액 출력하기]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18.811428571428568"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 주문당 평균 계산금액을 출력합니다.\n",
    "chipo.groupby('order_id')['item_price'].sum().mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    1834.000000\n",
       "mean       18.811429\n",
       "std        11.652512\n",
       "min        10.080000\n",
       "25%        12.572500\n",
       "50%        16.200000\n",
       "75%        21.960000\n",
       "max       205.250000\n",
       "Name: item_price, dtype: float64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "chipo.groupby('order_id')['item_price'].sum().describe()[:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [한 주문에 10달러 이상 사용한 주문 번호(id) 출력하기]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          quantity  item_price\n",
      "order_id                      \n",
      "1                4       11.56\n",
      "10               2       13.20\n",
      "100              2       10.08\n",
      "1000             2       20.50\n",
      "1001             2       10.08\n",
      "1002             2       10.68\n",
      "1003             2       13.00\n",
      "1004             2       21.96\n",
      "1005             3       12.15\n",
      "1006             8       71.40\n",
      "['1' '10' '100' ... '997' '998' '999']\n"
     ]
    }
   ],
   "source": [
    "# 한 주문에 10달러 이상 사용한 id를 출력합니다.\n",
    "chipo_orderid_group = chipo.groupby('order_id').sum()\n",
    "results = chipo_orderid_group[chipo_orderid_group.item_price >= 10]\n",
    "\n",
    "print(results[:10])\n",
    "print(results.index.values)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [각 아이템의 가격 구하기]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>quantity</th>\n",
       "      <th>choice_description</th>\n",
       "      <th>item_price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>item_name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Steak Salad Bowl</th>\n",
       "      <td>1032</td>\n",
       "      <td>1</td>\n",
       "      <td>[Fresh Tomato Salsa, Lettuce]</td>\n",
       "      <td>9.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Barbacoa Salad Bowl</th>\n",
       "      <td>1283</td>\n",
       "      <td>1</td>\n",
       "      <td>[Fresh Tomato Salsa, Guacamole]</td>\n",
       "      <td>9.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Carnitas Salad Bowl</th>\n",
       "      <td>1035</td>\n",
       "      <td>1</td>\n",
       "      <td>[Fresh Tomato Salsa, [Rice, Black Beans, Chees...</td>\n",
       "      <td>9.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Carnitas Soft Tacos</th>\n",
       "      <td>1011</td>\n",
       "      <td>1</td>\n",
       "      <td>[Fresh Tomato Salsa (Mild), [Black Beans, Rice...</td>\n",
       "      <td>8.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Carnitas Crispy Tacos</th>\n",
       "      <td>1774</td>\n",
       "      <td>1</td>\n",
       "      <td>[Fresh Tomato Salsa, [Fajita Vegetables, Rice,...</td>\n",
       "      <td>8.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Steak Soft Tacos</th>\n",
       "      <td>1054</td>\n",
       "      <td>1</td>\n",
       "      <td>[Fresh Tomato Salsa (Mild), [Cheese, Sour Cream]]</td>\n",
       "      <td>8.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Carnitas Salad</th>\n",
       "      <td>1500</td>\n",
       "      <td>1</td>\n",
       "      <td>[[Fresh Tomato Salsa (Mild), Roasted Chili Cor...</td>\n",
       "      <td>8.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Carnitas Bowl</th>\n",
       "      <td>1007</td>\n",
       "      <td>1</td>\n",
       "      <td>[Fresh Tomato (Mild), [Guacamole, Lettuce, Ric...</td>\n",
       "      <td>8.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Barbacoa Soft Tacos</th>\n",
       "      <td>1103</td>\n",
       "      <td>1</td>\n",
       "      <td>[Fresh Tomato Salsa, [Black Beans, Cheese, Let...</td>\n",
       "      <td>8.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Barbacoa Crispy Tacos</th>\n",
       "      <td>110</td>\n",
       "      <td>1</td>\n",
       "      <td>[Fresh Tomato Salsa, Guacamole]</td>\n",
       "      <td>8.99</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      order_id  quantity  \\\n",
       "item_name                                  \n",
       "Steak Salad Bowl          1032         1   \n",
       "Barbacoa Salad Bowl       1283         1   \n",
       "Carnitas Salad Bowl       1035         1   \n",
       "Carnitas Soft Tacos       1011         1   \n",
       "Carnitas Crispy Tacos     1774         1   \n",
       "Steak Soft Tacos          1054         1   \n",
       "Carnitas Salad            1500         1   \n",
       "Carnitas Bowl             1007         1   \n",
       "Barbacoa Soft Tacos       1103         1   \n",
       "Barbacoa Crispy Tacos      110         1   \n",
       "\n",
       "                                                      choice_description  \\\n",
       "item_name                                                                  \n",
       "Steak Salad Bowl                           [Fresh Tomato Salsa, Lettuce]   \n",
       "Barbacoa Salad Bowl                      [Fresh Tomato Salsa, Guacamole]   \n",
       "Carnitas Salad Bowl    [Fresh Tomato Salsa, [Rice, Black Beans, Chees...   \n",
       "Carnitas Soft Tacos    [Fresh Tomato Salsa (Mild), [Black Beans, Rice...   \n",
       "Carnitas Crispy Tacos  [Fresh Tomato Salsa, [Fajita Vegetables, Rice,...   \n",
       "Steak Soft Tacos       [Fresh Tomato Salsa (Mild), [Cheese, Sour Cream]]   \n",
       "Carnitas Salad         [[Fresh Tomato Salsa (Mild), Roasted Chili Cor...   \n",
       "Carnitas Bowl          [Fresh Tomato (Mild), [Guacamole, Lettuce, Ric...   \n",
       "Barbacoa Soft Tacos    [Fresh Tomato Salsa, [Black Beans, Cheese, Let...   \n",
       "Barbacoa Crispy Tacos                    [Fresh Tomato Salsa, Guacamole]   \n",
       "\n",
       "                       item_price  \n",
       "item_name                          \n",
       "Steak Salad Bowl             9.39  \n",
       "Barbacoa Salad Bowl          9.39  \n",
       "Carnitas Salad Bowl          9.39  \n",
       "Carnitas Soft Tacos          8.99  \n",
       "Carnitas Crispy Tacos        8.99  \n",
       "Steak Soft Tacos             8.99  \n",
       "Carnitas Salad               8.99  \n",
       "Carnitas Bowl                8.99  \n",
       "Barbacoa Soft Tacos          8.99  \n",
       "Barbacoa Crispy Tacos        8.99  "
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 각 아이템의 가격을 계산합니다.\n",
    "chipo_one_item = chipo[chipo.quantity == 1]\n",
    "price_per_item = chipo_one_item.groupby('item_name').min()\n",
    "price_per_item.sort_values(by = \"item_price\", ascending = False)[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 아이템 가격 분포 그래프를 출력합니다.\n",
    "item_name_list = price_per_item.index.tolist()\n",
    "x_pos = np.arange(len(item_name_list))\n",
    "item_price = price_per_item['item_price'].tolist()\n",
    " \n",
    "plt.bar(x_pos, item_price, align='center')\n",
    "plt.ylabel('item price($)')\n",
    "plt.title('Distribution of item price')\n",
    " \n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 아이템 가격 히스토그램을 출력합니다.\n",
    "plt.hist(item_price)\n",
    "plt.ylabel('counts')\n",
    "plt.title('Histogram of item price')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [가장 비싼 주문에서 item이 총 몇개 팔렸는지 구하기]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>quantity</th>\n",
       "      <th>item_price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>order_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>926</th>\n",
       "      <td>23</td>\n",
       "      <td>205.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1443</th>\n",
       "      <td>35</td>\n",
       "      <td>160.74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1483</th>\n",
       "      <td>14</td>\n",
       "      <td>139.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>691</th>\n",
       "      <td>11</td>\n",
       "      <td>118.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1786</th>\n",
       "      <td>20</td>\n",
       "      <td>114.30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          quantity  item_price\n",
       "order_id                      \n",
       "926             23      205.25\n",
       "1443            35      160.74\n",
       "1483            14      139.00\n",
       "691             11      118.25\n",
       "1786            20      114.30"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 가장 비싼 주문에서 item이 총 몇개 팔렸는지를 계산합니다.\n",
    "chipo.groupby('order_id').sum().sort_values(by='item_price', ascending=False)[:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [“Veggie Salad Bowl”이 몇 번 주문되었는지 구하기]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "18\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>quantity</th>\n",
       "      <th>item_name</th>\n",
       "      <th>choice_description</th>\n",
       "      <th>item_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>186</th>\n",
       "      <td>83</td>\n",
       "      <td>1</td>\n",
       "      <td>Veggie Salad Bowl</td>\n",
       "      <td>[Fresh Tomato Salsa, [Fajita Vegetables, Rice,...</td>\n",
       "      <td>11.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>295</th>\n",
       "      <td>128</td>\n",
       "      <td>1</td>\n",
       "      <td>Veggie Salad Bowl</td>\n",
       "      <td>[Fresh Tomato Salsa, [Fajita Vegetables, Lettu...</td>\n",
       "      <td>11.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>455</th>\n",
       "      <td>195</td>\n",
       "      <td>1</td>\n",
       "      <td>Veggie Salad Bowl</td>\n",
       "      <td>[Fresh Tomato Salsa, [Fajita Vegetables, Rice,...</td>\n",
       "      <td>11.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>496</th>\n",
       "      <td>207</td>\n",
       "      <td>1</td>\n",
       "      <td>Veggie Salad Bowl</td>\n",
       "      <td>[Fresh Tomato Salsa, [Rice, Lettuce, Guacamole...</td>\n",
       "      <td>11.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>960</th>\n",
       "      <td>394</td>\n",
       "      <td>1</td>\n",
       "      <td>Veggie Salad Bowl</td>\n",
       "      <td>[Fresh Tomato Salsa, [Fajita Vegetables, Lettu...</td>\n",
       "      <td>8.75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    order_id  quantity          item_name  \\\n",
       "186       83         1  Veggie Salad Bowl   \n",
       "295      128         1  Veggie Salad Bowl   \n",
       "455      195         1  Veggie Salad Bowl   \n",
       "496      207         1  Veggie Salad Bowl   \n",
       "960      394         1  Veggie Salad Bowl   \n",
       "\n",
       "                                    choice_description  item_price  \n",
       "186  [Fresh Tomato Salsa, [Fajita Vegetables, Rice,...       11.25  \n",
       "295  [Fresh Tomato Salsa, [Fajita Vegetables, Lettu...       11.25  \n",
       "455  [Fresh Tomato Salsa, [Fajita Vegetables, Rice,...       11.25  \n",
       "496  [Fresh Tomato Salsa, [Rice, Lettuce, Guacamole...       11.25  \n",
       "960  [Fresh Tomato Salsa, [Fajita Vegetables, Lettu...        8.75  "
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# “Veggie Salad Bowl”이 몇 번 주문되었는지를 계산합니다.\n",
    "chipo_salad = chipo[chipo['item_name'] == \"Veggie Salad Bowl\"]\n",
    "chipo_salad = chipo_salad.drop_duplicates(['item_name', 'order_id']) # 한 주문 내에서 중복 집계된 item_name을 제거합니다.\n",
    "\n",
    "print(len(chipo_salad))\n",
    "chipo_salad.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [“Chicken Bowl”을 2개 이상 주문한 주문 횟수 구하기]\n",
    "#### 공지사항\n",
    "- `'Chicken Bowl'을 2개 이상 주문한 주문 횟수 구하기` 문제의 출제 의도 오류가 있었습니다. 원래의 의도는 `'Chicken Bowl'을 2개 이상 주문한 고객들의 \"Chicken Bowl\" 메뉴에 대한 총 주문 수량`에 대한 문제였습니다. 이슈를 제기해주신 장기식님께 감사드립니다.\n",
    "- 따라서, 현재 문제의 의도대로 코드를 변경하였습니다. 기존의 출제 의도`“Chicken Bowl”을 2개 이상 주문한 고객들의 \"Chicken Bowl\" 메뉴에 대한 총 주문 수량`에 대한 코드는 아래에 추가해두었습니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "33\n"
     ]
    }
   ],
   "source": [
    "# “Chicken Bowl”을 2개 이상 주문한 주문 횟수를 구합니다.\n",
    "chipo_chicken = chipo[chipo['item_name'] == \"Chicken Bowl\"]\n",
    "chipo_chicken_result = chipo_chicken[chipo_chicken['quantity'] >= 2]\n",
    "print(chipo_chicken_result.shape[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "114\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "order_id\n",
       "1004    2\n",
       "1023    2\n",
       "1072    2\n",
       "1078    2\n",
       "1091    2\n",
       "Name: quantity, dtype: int64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# “Chicken Bowl”을 2개 이상 주문한 고객들의 \"Chicken Bowl\" 메뉴의 총 주문 수량을 구합니다.\n",
    "chipo_chicken = chipo[chipo['item_name'] == \"Chicken Bowl\"]\n",
    "chipo_chicken_ordersum = chipo_chicken.groupby('order_id').sum()['quantity']\n",
    "chipo_chicken_result = chipo_chicken_ordersum[chipo_chicken_ordersum >= 2]\n",
    "\n",
    "print(len(chipo_chicken_result))\n",
    "chipo_chicken_result.head(5)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
