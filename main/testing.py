from sklearn.metrics import confusion_matrix

True_Positive = 5
True_Negative = 2
False_Positive = 2
False_Negative = 1

result_true = ['Loss', 'Loss', 'Win', 'Win', 'Loss', 'Win', 'Loss', 'Loss', 'Win', 'Win']
result_predicted = ['Win', 'Loss', 'Win', 'Loss', 'Win', 'Win', 'Loss', 'Loss', 'Loss', 'Loss']

conf = confusion_matrix(result_true, result_predicted)