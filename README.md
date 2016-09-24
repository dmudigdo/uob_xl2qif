# uob_xl2qif

Python program that converts UOB (United Overseas Bank) Singapore transaction export file from Excel to QIF format

##Background

Since 2008, I have been storing my bank transactions on clearcheckbook.com, which accepts QIF files. UOB Singapore does not export QIF files, so on clearcheckbook.com, I had to tediously enter each transaction by hand. Until I did a [Coursera course on Python](https://www.coursera.org/learn/python), and subsequently wrote this little Python program, which uses [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/).

Months later, I read Automate the Boring Stuff with Python and learnt about [openpyxl](https://openpyxl.readthedocs.io/en/default/) which is presumably a better way to do it than Beautiful Soup. One day I'll play around with doing the same task using openpyxl instead.

##Usage
Make sure Beautiful Soup is good and running in the same directory, then `python uob_xl2qif >> blah.qif`.


