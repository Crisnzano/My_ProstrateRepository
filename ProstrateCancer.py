# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 21:48:11 2022

@author: Crisp
"""

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing multiple library to read,analysed and visualized the dataset\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sbn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Loading the dataset\n",
    "Cancer_data = pd.read_csv(r\"C:\\Users\\SERA NDAMBARI\\OneDrive\\Documents\\_Strathmore\\AI\\Prostate_Cancer.csv\")"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
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
       "      <th>id</th>\n",
       "      <th>diagnosis_result</th>\n",
       "      <th>radius</th>\n",
       "      <th>texture</th>\n",
       "      <th>perimeter</th>\n",
       "      <th>area</th>\n",
       "      <th>smoothness</th>\n",
       "      <th>compactness</th>\n",
       "      <th>symmetry</th>\n",
       "      <th>fractal_dimension</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>M</td>\n",
       "      <td>23</td>\n",
       "      <td>12</td>\n",
       "      <td>151</td>\n",
       "      <td>954</td>\n",
       "      <td>0.143</td>\n",
       "      <td>0.278</td>\n",
       "      <td>0.242</td>\n",
       "      <td>0.079</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>B</td>\n",
       "      <td>9</td>\n",
       "      <td>13</td>\n",
       "      <td>133</td>\n",
       "      <td>1326</td>\n",
       "      <td>0.143</td>\n",
       "      <td>0.079</td>\n",
       "      <td>0.181</td>\n",
       "      <td>0.057</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>M</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>130</td>\n",
       "      <td>1203</td>\n",
       "      <td>0.125</td>\n",
       "      <td>0.160</td>\n",
       "      <td>0.207</td>\n",
       "      <td>0.060</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>M</td>\n",
       "      <td>14</td>\n",
       "      <td>16</td>\n",
       "      <td>78</td>\n",
       "      <td>386</td>\n",
       "      <td>0.070</td>\n",
       "      <td>0.284</td>\n",
       "      <td>0.260</td>\n",
       "      <td>0.097</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>M</td>\n",
       "      <td>9</td>\n",
       "      <td>19</td>\n",
       "      <td>135</td>\n",
       "      <td>1297</td>\n",
       "      <td>0.141</td>\n",
       "      <td>0.133</td>\n",
       "      <td>0.181</td>\n",
       "      <td>0.059</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>B</td>\n",
       "      <td>25</td>\n",
       "      <td>25</td>\n",
       "      <td>83</td>\n",
       "      <td>477</td>\n",
       "      <td>0.128</td>\n",
       "      <td>0.170</td>\n",
       "      <td>0.209</td>\n",
       "      <td>0.076</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>M</td>\n",
       "      <td>16</td>\n",
       "      <td>26</td>\n",
       "      <td>120</td>\n",
       "      <td>1040</td>\n",
       "      <td>0.095</td>\n",
       "      <td>0.109</td>\n",
       "      <td>0.179</td>\n",
       "      <td>0.057</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>M</td>\n",
       "      <td>15</td>\n",
       "      <td>18</td>\n",
       "      <td>90</td>\n",
       "      <td>578</td>\n",
       "      <td>0.119</td>\n",
       "      <td>0.165</td>\n",
       "      <td>0.220</td>\n",
       "      <td>0.075</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>M</td>\n",
       "      <td>19</td>\n",
       "      <td>24</td>\n",
       "      <td>88</td>\n",
       "      <td>520</td>\n",
       "      <td>0.127</td>\n",
       "      <td>0.193</td>\n",
       "      <td>0.235</td>\n",
       "      <td>0.074</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>M</td>\n",
       "      <td>25</td>\n",
       "      <td>11</td>\n",
       "      <td>84</td>\n",
       "      <td>476</td>\n",
       "      <td>0.119</td>\n",
       "      <td>0.240</td>\n",
       "      <td>0.203</td>\n",
       "      <td>0.082</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id diagnosis_result  radius  texture  perimeter  area  smoothness  \\\n",
       "0   1                M      23       12        151   954       0.143   \n",
       "1   2                B       9       13        133  1326       0.143   \n",
       "2   3                M      21       27        130  1203       0.125   \n",
       "3   4                M      14       16         78   386       0.070   \n",
       "4   5                M       9       19        135  1297       0.141   \n",
       "5   6                B      25       25         83   477       0.128   \n",
       "6   7                M      16       26        120  1040       0.095   \n",
       "7   8                M      15       18         90   578       0.119   \n",
       "8   9                M      19       24         88   520       0.127   \n",
       "9  10                M      25       11         84   476       0.119   \n",
       "\n",
       "   compactness  symmetry  fractal_dimension  \n",
       "0        0.278     0.242              0.079  \n",
       "1        0.079     0.181              0.057  \n",
       "2        0.160     0.207              0.060  \n",
       "3        0.284     0.260              0.097  \n",
       "4        0.133     0.181              0.059  \n",
       "5        0.170     0.209              0.076  \n",
       "6        0.109     0.179              0.057  \n",
       "7        0.165     0.220              0.075  \n",
       "8        0.193     0.235              0.074  \n",
       "9        0.240     0.203              0.082  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Checking top 10 records of Dataset..\n",
    "Cancer_data.head(10)"
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
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 100 entries, 0 to 99\n",
      "Data columns (total 10 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   id                 100 non-null    int64  \n",
      " 1   diagnosis_result   100 non-null    object \n",
      " 2   radius             100 non-null    int64  \n",
      " 3   texture            100 non-null    int64  \n",
      " 4   perimeter          100 non-null    int64  \n",
      " 5   area               100 non-null    int64  \n",
      " 6   smoothness         100 non-null    float64\n",
      " 7   compactness        100 non-null    float64\n",
      " 8   symmetry           100 non-null    float64\n",
      " 9   fractal_dimension  100 non-null    float64\n",
      "dtypes: float64(4), int64(5), object(1)\n",
      "memory usage: 7.9+ KB\n"
     ]
    }
   ],
   "source": [
    "#Basic Information regarding data\n",
    "Cancer_data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "M    62\n",
       "B    38\n",
       "Name: diagnosis_result, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Data points count value for each class labels..\n",
    "Cancer_data.diagnosis_result.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
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
    "#Visualizing the dataset features to find pattern to solve our task\n",
    "plt.scatter(Cancer_data['radius'],Cancer_data['texture'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Building Classification Model\n",
    "#Imporing few library for create Decision tree classifier and visualizing the tree structure'''\n",
    "from sklearn import tree\n",
    "import graphviz\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.model_selection import train_test_split, cross_val_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "#separating dependent and independent variables\n",
    "feature_columns = ['radius', 'texture', 'perimeter','area', 'smoothness', 'compactness', 'symmetry', 'fractal_dimension']\n",
    "X = Cancer_data[feature_columns].values\n",
    "y = Cancer_data['diagnosis_result'].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Data Splitting\n",
    "Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.30, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#spliting data into validation train and validation test\n",
    "Xt, Xcv, Yt, Ycv = train_test_split(Xtrain, Ytrain, test_size=0.10, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Text(0.4444444444444444, 0.9166666666666666, 'X[2] <= 87.5\\ngini = 0.485\\nsamples = 63\\nvalue = [26, 37]'),\n",
       " Text(0.2222222222222222, 0.75, 'X[5] <= 0.109\\ngini = 0.278\\nsamples = 30\\nvalue = [25, 5]'),\n",
       " Text(0.1111111111111111, 0.5833333333333334, 'gini = 0.0\\nsamples = 20\\nvalue = [20, 0]'),\n",
       " Text(0.3333333333333333, 0.5833333333333334, 'X[5] <= 0.127\\ngini = 0.5\\nsamples = 10\\nvalue = [5, 5]'),\n",
       " Text(0.2222222222222222, 0.4166666666666667, 'gini = 0.0\\nsamples = 3\\nvalue = [0, 3]'),\n",
       " Text(0.4444444444444444, 0.4166666666666667, 'X[0] <= 15.5\\ngini = 0.408\\nsamples = 7\\nvalue = [5, 2]'),\n",
       " Text(0.3333333333333333, 0.25, 'X[2] <= 68.5\\ngini = 0.444\\nsamples = 3\\nvalue = [1, 2]'),\n",
       " Text(0.2222222222222222, 0.08333333333333333, 'gini = 0.0\\nsamples = 1\\nvalue = [1, 0]'),\n",
       " Text(0.4444444444444444, 0.08333333333333333, 'gini = 0.0\\nsamples = 2\\nvalue = [0, 2]'),\n",
       " Text(0.5555555555555556, 0.25, 'gini = 0.0\\nsamples = 4\\nvalue = [4, 0]'),\n",
       " Text(0.6666666666666666, 0.75, 'X[6] <= 0.211\\ngini = 0.059\\nsamples = 33\\nvalue = [1, 32]'),\n",
       " Text(0.5555555555555556, 0.5833333333333334, 'gini = 0.0\\nsamples = 26\\nvalue = [0, 26]'),\n",
       " Text(0.7777777777777778, 0.5833333333333334, 'X[6] <= 0.212\\ngini = 0.245\\nsamples = 7\\nvalue = [1, 6]'),\n",
       " Text(0.6666666666666666, 0.4166666666666667, 'gini = 0.0\\nsamples = 1\\nvalue = [1, 0]'),\n",
       " Text(0.8888888888888888, 0.4166666666666667, 'gini = 0.0\\nsamples = 6\\nvalue = [0, 6]')]"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
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
    "#Creating the decsion tree\n",
    "Cancer_clf = DecisionTreeClassifier(criterion='gini',min_samples_split=2)\n",
    "Cancer_clf.fit(Xt, Yt)\n",
    "#Visualized the Tree which is formed on train dataset\n",
    "tree.plot_tree(Cancer_clf)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Visualizing Decision Tree using graphviz library\n",
    "#dot_data = tree.export_graphviz(Cancer_clf, out_file=None)\n",
    "#graph = graphviz.Source(dot_data)\n",
    "#graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy score is: 0.8412698412698413\n"
     ]
    }
   ],
   "source": [
    "#Accuracy\n",
    "print('Accuracy score is:',cross_val_score(Cancer_clf, Xt, Yt, cv=3, scoring='accuracy').mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Checking validation test data on our trained model and getting performance metrices\n",
    "from sklearn.metrics import multilabel_confusion_matrix, accuracy_score\n",
    "Y_hat = Cancer_clf.predict(Xcv)"
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
      "Accuracy score for validation test data is: 0.8571428571428571\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[[3, 0],\n",
       "        [1, 3]],\n",
       "\n",
       "       [[3, 1],\n",
       "        [0, 3]]], dtype=int64)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print('Accuracy score for validation test data is:',accuracy_score(Ycv, Y_hat))\n",
    "multilabel_confusion_matrix(Ycv , Y_hat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['M', 'M', 'M', 'M', 'B', 'M', 'M', 'B', 'M', 'M', 'M', 'M', 'M',\n",
       "       'M', 'M', 'M', 'M', 'M', 'M', 'B', 'B', 'B', 'M', 'M', 'B', 'M',\n",
       "       'B', 'B', 'B', 'M'], dtype=object)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Checking our model performance on actual unseen test data.. \n",
    "YT_hat = Cancer_clf.predict(Xtest)\n",
    "YT_hat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model Accuracy Score on totally unseen data(Xtest) is: 76.66666666666667 %\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[[18,  4],\n",
       "        [ 3,  5]],\n",
       "\n",
       "       [[ 5,  3],\n",
       "        [ 4, 18]]], dtype=int64)"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print('Model Accuracy Score on totally unseen data(Xtest) is:',accuracy_score(Ytest, YT_hat)*100,'%')\n",
    "multilabel_confusion_matrix(Ytest , YT_hat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Text(0.5, 0.9166666666666666, 'X[2] <= 87.5\\ngini = 0.49\\nsamples = 70\\nvalue = [30, 40]'),\n",
       " Text(0.16666666666666666, 0.75, 'X[5] <= 0.109\\ngini = 0.257\\nsamples = 33\\nvalue = [28, 5]'),\n",
       " Text(0.08333333333333333, 0.5833333333333334, 'gini = 0.0\\nsamples = 23\\nvalue = [23, 0]'),\n",
       " Text(0.25, 0.5833333333333334, 'X[5] <= 0.127\\ngini = 0.5\\nsamples = 10\\nvalue = [5, 5]'),\n",
       " Text(0.16666666666666666, 0.4166666666666667, 'gini = 0.0\\nsamples = 3\\nvalue = [0, 3]'),\n",
       " Text(0.3333333333333333, 0.4166666666666667, 'X[0] <= 15.5\\ngini = 0.408\\nsamples = 7\\nvalue = [5, 2]'),\n",
       " Text(0.25, 0.25, 'X[3] <= 315.0\\ngini = 0.444\\nsamples = 3\\nvalue = [1, 2]'),\n",
       " Text(0.16666666666666666, 0.08333333333333333, 'gini = 0.0\\nsamples = 1\\nvalue = [1, 0]'),\n",
       " Text(0.3333333333333333, 0.08333333333333333, 'gini = 0.0\\nsamples = 2\\nvalue = [0, 2]'),\n",
       " Text(0.4166666666666667, 0.25, 'gini = 0.0\\nsamples = 4\\nvalue = [4, 0]'),\n",
       " Text(0.8333333333333334, 0.75, 'X[4] <= 0.136\\ngini = 0.102\\nsamples = 37\\nvalue = [2, 35]'),\n",
       " Text(0.75, 0.5833333333333334, 'X[3] <= 654.5\\ngini = 0.054\\nsamples = 36\\nvalue = [1, 35]'),\n",
       " Text(0.6666666666666666, 0.4166666666666667, 'X[3] <= 650.0\\ngini = 0.219\\nsamples = 8\\nvalue = [1, 7]'),\n",
       " Text(0.5833333333333334, 0.25, 'gini = 0.0\\nsamples = 7\\nvalue = [0, 7]'),\n",
       " Text(0.75, 0.25, 'gini = 0.0\\nsamples = 1\\nvalue = [1, 0]'),\n",
       " Text(0.8333333333333334, 0.4166666666666667, 'gini = 0.0\\nsamples = 28\\nvalue = [0, 28]'),\n",
       " Text(0.9166666666666666, 0.5833333333333334, 'gini = 0.0\\nsamples = 1\\nvalue = [1, 0]')]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    },
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
    "#Training model on Actual train data... '''\n",
    "Cancer_Fclf = DecisionTreeClassifier(criterion='gini',min_samples_split=2)\n",
    "Cancer_Fclf.fit(Xtrain, Ytrain)\n",
    "#Visualize tree structure..\n",
    "tree.plot_tree(Cancer_Fclf)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Final Decision tree build for deploying in real world cases....\n",
    "#dot_data = tree.export_graphviz(Cancer_Fclf, out_file=None)\n",
    "#graph = graphviz.Source(dot_data)\n",
    "#graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model Accuracy Score on totally unseen data(Xtest) is: 70.0 %\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[[16,  6],\n",
       "        [ 3,  5]],\n",
       "\n",
       "       [[ 5,  3],\n",
       "        [ 6, 16]]], dtype=int64)"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Checking the performance of model on Actual Test data...\n",
    "YT_Fhat = Cancer_Fclf.predict(Xtest)\n",
    "YT_Fhat\n",
    "print('Model Accuracy Score on totally unseen data(Xtest) is:',accuracy_score(Ytest, YT_Fhat)*100,'%')\n",
    "multilabel_confusion_matrix(Ytest , YT_Fhat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Testing for New points except from Dataset\n",
    "#Test_point = [[5.4,3.0,4.5,1.5],\n",
    "             #[6.5,2.8,4.6,1.5],\n",
    "             #[5.1,2.5,3.0,1.1,-0.5,1.4],\n",
    "             #[5.1,3.3,1.7,0.5,1.6,2.8]]\n",
    "#print(Cancer_Fclf.predict(Test_point))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
