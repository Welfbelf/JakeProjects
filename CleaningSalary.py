import ImportingData
import re
import pandas as pd
#
df = ImportingData.LoadAdjustedCSV()
#
# df['split'] = df['salary'].str.split('/')
#
# upper_pay = []
# lower_pay = []
#
# def append_blank():
#     str = ''
#     upper_pay.append(str)
#     lower_pay.append(str)
#
# def turn_to_float(str):
#     if str == '':
#         return ''
#     else:
#         flt = float(str)
#         return flt
#
#
# for x in df['split']:
#     if type(x) == list:
#         y = re.sub('401k', '', x[0])
#         y= re.sub ('401', '', x[0])
#         y = re.sub('[!@#$%^&*()_?:;"+$€,]', '' , y)
#         y = re.sub('[a-zA-Z]', '', y).strip()
#         y = re.sub('^\W', '', y).strip()
#
#         if re.match('-', y) == None and y != '':
#             y = y.split('-')
#             y[0] = re.sub('^\W','', y[0]).strip()
#
#
#
#         if type(y) == str:
#             lower_pay.append('')
#             upper_pay.append('')
#         elif len(y) == 1 and y[0] != '':
#             try:
#                 lower_pay.append(float(y[0]))
#                 upper_pay.append(float(y[0]))
#             except:
#                 lower_pay.append('')
#                 upper_pay.append('')
#         elif len(y) == 2:
#             lower_pay.append(float(y[0]))
#             if y[1] == '':
#                 upper_pay.append(float(y[0]))
#             else:
#                 upper_pay.append(float(y[1]))
#
#         else:
#             upper_pay.append('')
#             lower_pay.append('')
#     else:
#         upper_pay.append('')
#         lower_pay.append('')
#
#
# df['lower_pay'] = pd.Series(data = lower_pay, index = df.index)
# df['upper_pay'] = pd.Series(data = upper_pay, index = df.index)
#
#
#
#
# df = df.drop(columns = ['type_of_pay'])
# type_of_pay = []
# for x in df['upper_pay']:
#     if x == '':
#         type_of_pay.append('')
#     elif x <100:
#         type_of_pay.append('hour')
#     elif x > 100 and x < 14000:
#         type_of_pay.append('month')
#     elif x > 14000:
#         type_of_pay.append('year')
#     else:
#         type_of_pay.append('')
#
#
#
#
# df['type_of_pay'] = pd.Series(data=type_of_pay, index = df.index)
#
# ImportingData.SaveAdjustedCSV(df)

# pointer = 0
# upper_pay = []
# lower_pay = []
# type_of_pay = []
#
# for x in df['upper_pay']:
#     upper_pay.append(x)
#
# for y in df['lower_pay']:
#     if y == 0:
#         y = upper_pay[pointer]
#     lower_pay.append(y)
#
# for t in df['type_of_pay']:
#     if t == '':
#         type_of_pay.append('')
#     if t == 'year':
#         type_of_pay.append('year')
#     if t == 'month':
#         upper_pay[pointer] = upper_pay[pointer] * 12
#         lower_pay[pointer] = lower_pay[pointer] * 12
#         type_of_pay.append('year')
#     if t == 'hour':
#         upper_pay[pointer] = upper_pay[pointer] * 2080
#         lower_pay[pointer] = lower_pay[pointer] * 2080
#         type_of_pay.append('year')
#
#
#     pointer +=1
#
# df['upper_pay'] = pd.Series(data = upper_pay, index = df.index)
# df['lower_pay'] = pd.Series(data = lower_pay, index = df.index)
#
# pd.DataFrame.to_csv(df, 'adjusted_csv.csv')
#
#
