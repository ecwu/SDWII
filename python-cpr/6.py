# Zhenghao Wu l630003054

MONTHS = 12

if __name__ == '__main__':
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    user_month, user_day, accumulate = (0, 0, 0)

    while user_month > MONTHS or user_month <= 0:
        user_month = int(input("Enter the month: "))
    
    while user_day > days_in_month[user_month - 1] or user_day <= 0:
        user_day = int(input("Enter the day: "))

    for i in range(user_month - 1):
        accumulate += days_in_month[i]
    accumulate += user_day

    print("%d/%d is the day number %d in the year" % (user_day, user_month, accumulate))
