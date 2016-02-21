import datetime
import webbrowser

answer_format = '%m/%d'
link_format = '%b_%d'
link = 'http://en.wikipedia.org/wiki/{}'

while True:
    answer = input("What date would you like to know about? "
                   "Please enter a date in MM/DD format. Or type QUIT to quit ")

    if answer.upper() == 'QUIT':
        break

    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        open_web = webbrowser.open(output, new=0, autoraise=True)
        print(open_web)
    except ValueError:
        print("That's not a valid date. Please enter another date.")
