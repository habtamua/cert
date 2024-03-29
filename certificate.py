#!/usr/bin/python
"""
File certificate.py: a Python 2.x and 3.x script,
Generate a bare-bones class completion certificate: printed, and
saved in text and html files displayed in a web browser.
"""

from __future__ import print_function       # 2.x compatibility
import time, sys, webbrowser

if sys.version_info[0] == 2:                # 2.x compatibility
    input = input()
    import cgi
    htmlscape = cgi.escape
else:
    import html
    htmlscape = html.escape

maxline = 60                                # For seperator lines
browser = True                              # Display in a browser
saveto = 'Certificate.txt'                  # Output filenames
template = """
%s

===> Official Certificate <===

Date: %s

This certifies that:

\t%s

has survived the massive tome:

\t%s

and is now entitled to all privileges thereof, including the right to proceed
on to learning how to develop Web sites, Desktop GUIs, Scientific Models, and
Assorted Apps, with the possible assistance of follow-up applications books
such as Programming Python (shameless plug intended).

--Joseph Aeron Schilz, Instructor

(Note: certificate void where obtained by skipping ahead.)

%s
"""

# Interact, setup
for c in 'Congratulations!'.upper():
    print(c, end=' ')
    sys.stdout.flush()                      # Else some shells wait for \n
    time.sleep(0.25)
print()

date = time.asctime()
name = input('Enter your name: ').strip() or 'An unknown reader'
sept = '*' * maxline
book = 'certificate program in Python programming'

# Make text file version
file = open(saveto, 'w')
text = template % (sept, date, name, book, sept)
print(text, file=file)
file.close()

# Make html file version
htmlto = saveto.replace('.txt', '.html')
file = open(htmlto, 'w')

tags = text.replace(sept, '<hr>')           # Insert a few tags
tags = tags.replace('===>', '<h1 align=center>')
tags = tags.replace('<===', '</h1>')

tags = tags.split('\n')                     # Line-by-line mods
tags = ['<p>' if line == ''
            else line for line in tags]
tags = ['<i>%s</i>' % htmlscape(line) if line[:1] == '\t'
            else line for line in tags]
tags = '\n'.join(tags)

link = '<i><a href="https://www.pce.uw.edu/certificates/python-programming">CERTIFICATE IN PYTHON PROGRAMMING</a></i>\n'
foot = '<table>\n<td><img src="ora-lp_3_15.jpg" hspace=5>\n<td>%s</table>\n' % link
tags = '<html><body bgcolor=beige>' + tags + foot + '</body></html>'

print(tags, file=file)
file.close()

# Display results
print('[File: %s]' % saveto, end='')
print('\n' * 2, open(saveto).read())

if browser:
    webbrowser.open(saveto, new=True)
    webbrowser.open(htmlto, new=False)

if sys.platform.startswith('win'):
    input('[Press Enter]') # Keep window open if clicked on Windows
