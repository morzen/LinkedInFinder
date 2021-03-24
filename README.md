╔╗─╔╦═══╦╗──╔╗──╔═══╗╔╗
║║─║║╔══╣║──║║──║╔═╗║║║
║╚═╝║╚══╣║──║║──║║─║║║║
║╔═╗║╔══╣║─╔╣║─╔╣║─║║╚╝
║║─║║╚══╣╚═╝║╚═╝║╚═╝║╔╗
╚╝─╚╩═══╩═══╩═══╩═══╝╚╝

Welcome and thank you for choosing LInkedinFinder to stalk your mates.
We hope you will have a pleasant journey on the interweb with us.

This script uses:
-Selenium (might have to pip3 install that)

STEP1: enter your credential for linkedin User id and password  line 25 & 26
      (I suggest creating a fake account)

STEP2: Once all that is done put your list of URL linkedin profile in ListURL.txt
       the result will appear in a file called TempResult.txt

RUN the program with "python3 LinkedInFinder.py" whle being in the repository folder

extra-STEP 3: if a problem arrive due to the gecko driver look for a newer version

WORD OF WARNING
if the script fail at some point (probably due to and html page being slightly different than others)
do not panick all your results are stored in the TempResult.txt and the script is meant append anything to this file and not delete or overwrite
but i would recomment you look at what number the script faild and to modify the i=0 line 12 by the number at where it failed and  if it fail again to the next number.
like that you would avoid appenning result you already have.

