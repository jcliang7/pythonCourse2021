running = True
day28 = ['february', '2']
day30 = ['april', 'june', 'september', 'november',
        '4', '6', '9', '11']
day31 = ['january', 'march', 'may', 'july', 'august', 'october', 'december', 
          '1', '3', '5', '7', '8', '10', '12']
exitList = ['exit', 'quit', 'leave', 'end', 'done', 'q']
while running:
    user_month = input('Please input a month name:\n(Enter \"exit\" to end.)\n')
    # 轉小寫
    user_month = user_month.lower()
    if user_month in day28:
        print('28/29 days.\n')
    elif user_month in day30:
        print('30 days.\n')
    elif user_month in day31:
        print('31 days\n')
    elif user_month in exitList:
        running = False
        print("Bye!")
    else:
        print('Wrong month name.\n')