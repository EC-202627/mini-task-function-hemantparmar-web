#test name = T4
#ID = t4
def calculate_fine(book_title, days_overdue, daily_rate, max_fine=150.0):
    fine = days_overdue * daily_rate

    if fine > max_fine:
        fine = max_fine
        print("You have accumulated the maximum fine of INR: 150.0")

    return fine   
book_title = input()
days_overdue = int(input())
daily_rate = int(input())

