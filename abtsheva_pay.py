"""
This program will calculcate Bat-Sheva Pay 
As we discussed Per month for Morning hours she will get a constant of X Shekels
For Tzaharon hours which are alway 2 , 35 Shekels 

"""

MORNINGS_MONTHLY_PAY = 1800
TZAHARON_PAY_DAILY = 70

#input How many Tzaharon days did BS work
tzaharon_days = -1
for tzaharon_days < 0
    try:
        tzaharon_days = int(raw_input('Please insert how many Tzaharon days did BS worked:'))
        print "tzaharon_days inserted",worktzaharon_days_days
    except:
        word_days = -1 
        print "This is not a numbert please re-enter"

Total_monthly_pay = MORNINGS_MONTHLY_PAY + (TZAHARON_PAY_DAILY * tzaharon_days)
print "Bat Sheva Total monthly pay is:",Total_monthly_pay



