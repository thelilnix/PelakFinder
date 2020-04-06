#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# GNU Lesser General Public License (LGPL) v3.0 .
# The project has been developed by Saman Ebrahimnezhad .
# Created at Iran (IR) .
# Python 3 .

import sys
import json

from tkinter import *

class PelakFinder:
    def __init__(self):
        
        code = ""
        alphabet = ""

        if len(sys.argv) < 2:
            print("ERROR: Syntax : python3 PelakFinder.py CAR_TAG_CODE CAR_TAG_ALPHABET_(optional)")
            return
        elif len(sys.argv) == 2:
            code = sys.argv[1]
        else:
            code = sys.argv[1]
            alphabet = sys.argv[2]

        # JSON compilation and creation by Saman Ebrahimnezhad .
        # Online_RESTFUL_API : https://api.jsonbin.io/b/5a577a6d7cfd5a4dbc6b3b19/2
        
        jsonFile = open("Pelaks.json", mode = 'r')
        
        text = jsonFile.read()

        jsonFile.close()

        data = json.loads(text)

        labelText = "Not found"

        if alphabet != "":
            if alphabet in data[code][0].keys():
                labelText = data[code][0][alphabet]
            else:
                labelText = data[code][0][code]
        else:
            labelText = data[code][0][code]

        # ---------- Start GUI ----------

        root = Tk()
        root.title("PelakFinder")
        
        root.geometry("300x300")

        self.message = Message(root, text = labelText, justify = "center")
        self.message.config(font = ("times", 15, "bold"))

        self.closeBtn = Button(root, width = 10, text = "Close", command = root.destroy)
        
        self.message.pack()
        self.closeBtn.pack()

        root.mainloop()

def main():
    PelakFinder()

if __name__ == "__main__":
    main()
