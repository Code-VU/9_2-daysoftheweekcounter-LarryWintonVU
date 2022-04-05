
def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")    
    # categorize mail messages by which day of the week the commit was done
    commitsByDayOfWeekHistogram = dict()
    try:
        file_handle = open(file_name, mode='r', encoding='utf-8')
        for line in file_handle :
            line = line.strip()
            if line == '' :
                continue
            wordsInThisLine = line.split()
            if len(wordsInThisLine) < 2 :
                continue
            if wordsInThisLine[0] == 'From' :
                commitsByDayOfWeekHistogram[wordsInThisLine[2]] = commitsByDayOfWeekHistogram.get(wordsInThisLine[2], 0) + 1
        print(commitsByDayOfWeekHistogram)     
    except:
        print('File cannot be opened:', file_name)
        quit()
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countDayOfTheWeek()