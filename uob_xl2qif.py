from BeautifulSoup import *
 
def getdate(datetd):
# reads a date <td>, returns the date as a unicode
    return unicode(datetd.contents[1].contents[0]).strip()
 
def getdescription(dscrtd):
# reads a description <td>, returns the description as a unicode
# with /n replaced by spaces
    utxt = dscrtd.contents[1].contents[1].contents
    dscr = ''
    for i in range(0,len(utxt)):
        if i % 2 == 0:
            dscr = dscr + unicode(utxt[i])
        else:
            dscr = dscr + ' '
    return dscr
 
def getamount(amnttd):
# reads an amount (Withdrawals/Deposits) <td>, returns
# the amount as a unicode
    utxt = amnttd.contents[1].contents[1].contents
    return unicode(utxt[0]) + unicode(utxt[1].contents[0])
 
from BeautifulSoup import *
import datetime
 
fhandle = open("Jan2016.xls")
soup = BeautifulSoup(fhandle)
trtags = soup('tr','text-md')
 
print '!Type:Bank'
 
for trtag in trtags:
# for each <tr> in the table
    for i in range(0,8):
#   for all the <td> in the <tr> (except the last <td>,
#   which is just a \n):
        if i == 1:
#           *Date* (2nd index, i=1)
            thedate = getdate(trtag.contents[i])
            d = datetime.datetime.strptime(thedate, '%d %b %Y')
            print 'D' + d.strftime('%d/%m/%Y')
        elif i == 3:
#           *Description* (4th index, i=3)
            thedescription = getdescription(trtag.contents[i])
            print 'P' + thedescription
        elif i == 5:
#           *Amount*
#           (6th index i=5 for Withdrawals, 8th index i=7 for Deposits)
#           Check if it is a "-" to identify Withdrawal vs Deposit
            utxt = trtag.contents[i].contents[1].contents[1].contents
            if unicode(utxt[0]) == "-":
                theamount = getamount(trtag.contents[i+2])
            else: 
#               add -ve sign for withdrawals
                theamount = '-' + getamount(trtag.contents[i])
            print 'T' + theamount
    print '^'
