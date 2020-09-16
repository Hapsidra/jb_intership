# Data-driven hyper-optimization

This script parses scripts and extracts model parameters from there and saves them to csv table. 
Regular expressions are used for development speed, but for more general tasks it will be possible to use parsers such as a parser, 
ast or tokenizer or something else.

## Tables
- [XGBRegresser](https://github.com/Hapsidra/jb_intership/blob/master/xgb.csv)
- [SVR](https://github.com/Hapsidra/jb_intership/blob/master/svr.csv)
## XGBRegressor statistics
|       | colsample_bytree | learning_rate | max_depth | alpha | n_estimators |
|-------|------------------|---------------|-----------|-------|--------------|
| count | 2.000000         | 2.000000      | 1.0       | 1.0   | 2.0          |
| mean  | 0.400000         | 0.050050      | 5.0       | 10.0  | 10.0         |
| std   | 0.141421         | 0.070640      | NaN       | NaN   | 0.0          |
| min   | 0.300000         | 0.000100      | 5.0       | 10.0  | 10.0         |
| 25%   | 0.350000         | 0.025075      | 5.0       | 10.0  | 10.0         |
| 50%   | 0.400000         | 0.050050      | 5.0       | 10.0  | 10.0         |
| 75%   | 0.450000         | 0.075025      | 5.0       | 10.0  | 10.0         |
| max   | 0.500000         | 0.100000      | 5.0       | 10.0  | 10.0         |
