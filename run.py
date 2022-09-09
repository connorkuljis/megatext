# Created 2021-08-07 by Connor Kuljis
# Purpose: rewrite of a previous java program 
# Last Modified: 2022-09-05
# Notes: unix readlink command to get working path of file

import os
import datetime

EDITOR = os.getenv('EDITOR')
TEMPLATE = ('/Users/connor/Journal/mega/template.txt') # TODO use os.path.realpath

def markdownTemplate(date):
    yearmonth = date.strftime("%Y-%b")
    month = date.strftime("%B")

    title = (f'% Monthly Running Megatext {yearmonth}\n')
    subheading = (f'# {month}\n')

    file = open(TEMPLATE, 'r')
    body = file.read()
    file.close()

    return title + subheading + body

def combine(directory, file):
    return directory + "/" + file

def createFile(date):
    month_number = date.strftime("%m").strip("0") # remove leading zeros from month eg: 08 -> 8
    filename = date.strftime("%Y-%b") + ".md" #2022-Aug

    # https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory
    project_dir         = os.path.dirname(os.path.realpath(__file__))  # ../mega
    parent_dir          = combine(project_dir, month_number)
    file_dir            = combine(parent_dir, filename)

    open_editor = str(EDITOR) + " " + file_dir # EDITOR defined by system environment eg: vim, vscode, subl

    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    if os.path.exists(file_dir):
        os.system(open_editor)
    else:
        f = open(file_dir, 'a')
        f.write(markdownTemplate(date))
        f.close()
        os.system(open_editor)

# main
createFile(datetime.datetime.now())
