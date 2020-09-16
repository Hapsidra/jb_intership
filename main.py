import re
import pandas as pd

script1 = """X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1, max_depth = 5, alpha = 10, n_estimators = 10)
xg_reg.fit(X_train,y_train)"""
script2 = """X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.5, learning_rate = 0.0001, n_estimators = 10)
xg_reg.fit(X_train,y_train)"""
script3 = """X = [[0, 0], [2, 2]] y = [0.5, 2.5]
regr = svm.SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,coef0=1)
regr.fit(X, y)"""

models = [{'name': 'XGBRegressor', 'params': [
    'objective',
    'colsample_bytree',
    'learning_rate',
    'max_depth',
    'alpha',
    'n_estimators',
]}, {'name': 'SVR', 'params': ['kernel', 'C', 'gamma', 'degree', 'epsilon', 'coef0']}]

scripts = [script1, script2, script3]

xgb = []
svr = []

for script in scripts:
    for model in models:
        match = re.search(r"(?<=(" + model['name'] + ")\().+(?=\))", script)
        if match:
            args = script[match.start(): match.end()].replace(' ', '').split(',')
            dic = {}
            for param in model['params']:
                dic[param] = None
            for arg in args:
                name, value = arg.split('=')
                try:
                    dic[name] = float(value)
                except:
                    dic[name] = value
            if model['name'] == 'XGBRegressor':
                xgb += [dic]
            else:
                svr += [dic]

xgb_df = pd.DataFrame(xgb)
svr_df = pd.DataFrame(svr)

xgb_df.to_csv('xgb.csv', index=False)
svr_df.to_csv('svr.csv', index=False)

print(xgb_df.describe())
