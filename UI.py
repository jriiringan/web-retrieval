#!/usr/bin/env python2.7
import webbrowser
import time
import trigram
import contraction
import tkMessageBox
from Tkinter import *
from search import Search
from word_graph import Graph
from htmlparser import htmlParser
from nltk.tokenize import sent_tokenize
from ScrolledText import ScrolledText

class gui:

    def __init__(self):
        self.master = Tk()
        self.master.geometry("800x600+100+10")
        self.master.title("WIReS - Web Information Retrieval System")
        self.master.configure(background='white')
        self.master.resizable(width=FALSE, height=FALSE)

    ########################################################################################################
    def guimain(self):

        global query
        query = StringVar(None)

        def devs():
            tkMessageBox.showinfo("DEVELOPERS", '''BS COMPUTER SCIENCE 302
CAVITE STATE UNIVERSITY - ROSARIO CAMPUS

Lamberto A. Bruno. Jr.
Jomari R. Iringan
            ''')

        def help():
            tkMessageBox.showinfo("HELP", '''CONTACT US:
Bruno ( 0905-511-9881 )
Joms ( 0906-870-2976 )

EMAIL US:
wiressupport@gmail.com
            ''')

        def priv():
            tkMessageBox.showinfo("PRIVACY", '''For privacy terms and policies please see
https://www.google.com/policies/privacy/
            ''')

        def clearBtn():
            self.searchEntry.delete(0,END)
            self.searchEntry.focus_set()
            return



        self.label1 = Label(self.master, text="WIReS", font=('Impact',70),bg='white')
        self.label2 = Label(self.master, text="   SEARCH ENGINE", bg ='#008080', fg='white', font=('arial',7))
        self.lineLabel = Label(self.master,text="____________________________",fg='red',bg='red', font =('arial',7))
        self.helpBtn = Button(self.master, text="HELP", font=('Courier',10),command = help)
        self.privBtn = Button(self.master, text="PRIVACY", font=('Courier',10),command = priv)
        self.devsBtn = Button(self.master, text="DEVS", font=('Courier',10),command = devs)
        self.searchEntry = Entry(self.master, width='50', relief='groove', borderwidth='5', font=('Calibri',15), textvariable=query)
        self.searchButton = Button(self.master, text="SEARCH!", width='30')
        self.clearButton = Button(self.master, text="CLEAR FIELD", command = clearBtn)
        #locs
        self.label1.place(x=300,y=150)
        self.label2.place(x=455,y=250)
        self.lineLabel.place(x=310,y=250)
        self.searchEntry.place(x=180,y=320)
        self.searchButton.place(x=400,y=400)
        self.clearButton.place(x=250, y=400)
        self.devsBtn.place(x=690,y=570)
        self.helpBtn.place(x=738,y=570)
        self.privBtn.place(x=618, y=570)

        self.searchEntry.focus_set()

        self.searchButton.bind("<Button-1>",self.searchBtn)
        self.searchEntry.bind("<Return>", self.searchBtn)


    def searchBtn(self, event):
        try:
            global xTime
            global query
            xTime = StringVar()
            query = StringVar(None)
            search_ = Search()
            query = self.searchEntry.get()
            if query not in (None, '', ' '):
                start_time = time.time()
                global title_url
                title_url = [None]
                raw = search_.fetch_url(query)
                title_url = search_.process_url(raw)
                self.master.withdraw()
                xTime = (time.time() - start_time)
                self.guiresults()
            else:
                tkMessageBox.showinfo('Info', 'You must put a keyword')
        except Exception as e:
                tkMessageBox.showinfo('Info', 'No Internet Connection Try Again Later')
                exit()

####################

    def guiresults(self):

        global q_String
        q_String = StringVar()
        graph = Graph()
        html_parse = htmlParser()
        

        def showGraph():        
            raws = StringVar()
            raws = self.result_label.get(1.0, END)
            
            graph.plot_word(raws)

        def showPos():
            raws = StringVar()
            raws = self.result_label.get(1.0, END)
            graph.plot_pos(raws)


        def clearBtn1():
            self.searchEntry1.delete(0,END)
            self.searchEntry1.focus_set()
            return
        start_time = time.time()
        self.masters = Tk()
        self.masters.geometry("1100x700+100+10")
        self.masters.title("WIReS - Web Information Retrieval System")
        self.masters.configure(background='white')
        self.masters.resizable(width=FALSE, height=FALSE)

        self.searchEntry1 = Entry(self.masters, width='50', relief='groove', borderwidth='5', font=('Calibri',15))
        self.searchButton = Button(self.masters, text="SEARCH!", width='25')
        self.clearButton1 = Button(self.masters, text="CLEAR FIELD", width='25',command = clearBtn1)
        self.labelss = Label(self.masters, text="SEARCH RESULTS:", bg ='#008080', fg='white', font=('arial',10))
        self.timeLabel = Label(self.masters, text="SEARCH COMPLETED AT ", font=('arial',8))
        self.resultframe = LabelFrame(self.masters,text="PAGE RESULT",height=520, width=990,relief = "groove", bg ="white")
        self.resultframe1 = LabelFrame(self.masters,height=540, width=990,relief = "groove", bg ="white")
        self.result_label = ScrolledText(self.resultframe,width = 120, height = 32,bg = 'white', undo = True)
        self.graphButton = Button(self.masters, text="WORD OCCURENCE(GRAPH)", width='25',command = showGraph)
        self.posButton = Button(self.masters, text="PART OF SPEECH(GRAPH)", width='25', command = showPos)

        #URL
        self.labelres1 = Label(self.resultframe1, text = title_url[0][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres1= Label(self.resultframe1, text = title_url[0][1], fg="blue", cursor="hand2", bg="white")
        self.labelres2 = Label(self.resultframe1, text = title_url[1][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres2 = Label(self.resultframe1, text = title_url[1][1], fg="blue", cursor="hand2", bg="white")
        self.labelres3 = Label(self.resultframe1, text = title_url[2][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres3 = Label(self.resultframe1, text = title_url[2][1], fg="blue", cursor="hand2", bg="white")
        self.labelres4 = Label(self.resultframe1, text = title_url[3][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres4 = Label(self.resultframe1, text = title_url[3][1], fg="blue", cursor="hand2", bg="white")
        self.labelres5 = Label(self.resultframe1, text = title_url[4][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres5 = Label(self.resultframe1, text = title_url[4][1], fg="blue", cursor="hand2", bg="white")
        self.labelres6 = Label(self.resultframe1, text = title_url[5][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres6 = Label(self.resultframe1, text = title_url[5][1], fg="blue", cursor="hand2", bg="white")
        self.labelres7 = Label(self.resultframe1, text = title_url[6][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres7 = Label(self.resultframe1, text = title_url[6][1], fg="blue", cursor="hand2", bg="white")
        self.labelres8 = Label(self.resultframe1, text = title_url[7][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres8 = Label(self.resultframe1, text = title_url[7][1], fg="blue", cursor="hand2", bg="white")

        #gui2 loc
        self.resultframe1.place(x=15,y=80)
        self.searchEntry1.place(x=15,y=15)
        self.searchButton.place(x=550,y=18)
        self.labelss.place(x=15,y=60)
        self.timeLabel.place(x=15,y=630)


        self.labelres1.place(x=1,y=30)
        self.linkres1.place(x=5,y=60)
        self.labelres2.place(x=1,y=90)
        self.linkres2.place(x=5,y=120)
        self.labelres3.place(x=1,y=150)
        self.linkres3.place(x=5,y=180)
        self.labelres4.place(x=1,y=210)
        self.linkres4.place(x=5,y=240)
        self.labelres5.place(x=1,y=270)
        self.linkres5.place(x=5,y=300)
        self.labelres6.place(x=1,y=330)
        self.linkres6.place(x=5,y=360)
        self.labelres7.place(x=1,y=390)
        self.linkres7.place(x=5,y=420)
        self.labelres8.place(x=1,y=450)
        self.linkres8.place(x=5,y=480)
        self.clearButton1.place(x=800,y=18)


        self.searchEntry1.insert(END,query)

        self.timeLabelres = Label(self.masters, text="--- %s seconds ---" % (xTime), font=('arial',8))
        self.timeLabelres.place(x=150,y=630)

        def graphloc():
            self.graphButton.place(x = 550, y=50)
            self.posButton.place(x = 800, y=50)








        #eventfunc
        def callback1(event):
            start_time = time.time()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[0][1]))
            self.resultframe1.destroy()
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')
            self.timeLabelres = Label(self.masters, text="--- %s seconds ---" % (time.time() - start_time), font=('arial',8))
            self.timeLabelres.place(x=150,y=630)
            graphloc()


        def callback2(event):
            start_time = time.time()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[1][1]))
            self.resultframe1.destroy()
            self.timeLabelres = Label(self.masters, text="--- %s seconds ---" % (time.time() - start_time), font=('arial',8))
            self.timeLabelres.place(x=150,y=630)
            graphloc()


        def callback3(event):
            start_time = time.time()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[2][1]))
            self.resultframe1.destroy()
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')
            self.timeLabelres = Label(self.masters, text="--- %s seconds ---" % (time.time() - start_time), font=('arial',8))
            self.timeLabelres.place(x=150,y=630)
            graphloc()

        def callback4(event):
            start_time = time.time()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[3][1]))
            self.resultframe1.destroy()
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')
            self.timeLabelres = Label(self.masters, text="--- %s seconds ---" % (time.time() - start_time), font=('arial',8))
            self.timeLabelres.place(x=150,y=630)
            graphloc()

        def callback5(event):
            start_time = time.time()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[4][1]))
            self.resultframe1.destroy()
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')
            self.timeLabelres = Label(self.masters, text="--- %s seconds ---" % (time.time() - start_time), font=('arial',8))
            self.timeLabelres.place(x=150,y=630)
            graphloc()


        def callback6(event):
            start_time = time.time()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[5][1]))
            self.resultframe1.destroy()
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')
            self.timeLabelres = Label(self.masters, text="--- %s seconds ---" % (time.time() - start_time), font=('arial',8))
            self.timeLabelres.place(x=150,y=630)
            graphloc()


        def callback7(event):
            start_time = time.time()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[6][1]))
            self.resultframe1.destroy()
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')
            self.timeLabelres = Label(self.masters, text="--- %s seconds ---" % (time.time() - start_time), font=('arial',8))
            self.timeLabelres.place(x=150,y=630)
            graphloc()



        def callback8(event):
            start_time = time.time()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[7][1]))
            self.resultframe1.destroy()
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')
            self.timeLabelres = Label(self.masters, text="--- %s seconds ---" % (time.time() - start_time), font=('arial',8))
            self.timeLabelres.place(x=150,y=630)
            graphloc()


       

        def searchAction(event):
            try:
                global query
                global mTime
                mTime = StringVar(None)
                query = StringVar(None)
                search_ = Search()
                query = self.searchEntry1.get()

                if query not in (None, '', ' '):
                    start_time = time.time()
                    global title_url
                    title_url = [None]
                    raw = search_.fetch_url(query)
                    title_url = search_.process_url(raw)
                    self.masters.withdraw()
                    mTime = (time.time() - start_time)
                    self.guiresults()
                    self.timeLabelres = Label(self.masters, text="--- %s seconds ---" % (mTime), font=('arial',8))
                    self.timeLabelres.place(x=150,y=630)
                    
                else:
                    tkMessageBox.showinfo('Info', 'You must put a keyword')
            except Exception as e:
                    tkMessageBox.showinfo('Info', 'No Internet Connection Try Again Later')
                    exit()

        #eventlink

        self.searchButton.bind("<Button-1>",searchAction)
        self.searchEntry1.bind("<Return>",searchAction)
        self.linkres1.bind("<Button-1>", callback1)
        self.linkres2.bind("<Button-1>", callback2)
        self.linkres3.bind("<Button-1>", callback3)
        self.linkres4.bind("<Button-1>", callback4)
        self.linkres5.bind("<Button-1>", callback5)
        self.linkres6.bind("<Button-1>", callback6)
        self.linkres7.bind("<Button-1>", callback7)
        self.linkres8.bind("<Button-1>", callback8)
        self.labelres1.bind("<Button-1>", callback1)
        self.labelres2.bind("<Button-1>", callback2)
        self.labelres3.bind("<Button-1>", callback3)
        self.labelres4.bind("<Button-1>", callback4)
        self.labelres5.bind("<Button-1>", callback5)
        self.labelres6.bind("<Button-1>", callback6)
        self.labelres7.bind("<Button-1>", callback7)
        self.labelres8.bind("<Button-1>", callback8)
        self.searchEntry1.insert(END,'')



def main():
    master1 = gui()
    master1.guimain()
    master1.master.mainloop()

if __name__=='__main__':
    main()
