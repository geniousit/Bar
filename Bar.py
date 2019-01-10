#this is a pro
import wx
import MySQLdb
import sys
import time
import wx.gizmos as gizmos



class DianaPub(wx.Frame):#Diana class


    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Diana Pub")
        panel = wx.Panel(self)
        
        self.ShowFullScreen(True)
        
        db_connect = MySQLdb.connect(host='localhost',user='root',passwd='mnyama')
        cursor = db_connect.cursor()
        
        cursor.execute('CREATE DATABASE IF NOT EXISTS employee')
        cursor.execute('GRANT ALL ON employee.*To henry@localhost IDENTIFIED BY "mnyama"')
        
       
       
       
        
        
        
        image_file ='diana10.jpg'
        bmp = wx.Image(image_file,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = wx.StaticBitmap(self,-1,bmp,(0,0))
        
        
        self.layout()#layout call
        #Onscreen Buttons
        #start
        #layout function
  
        #end of onScreen Button
        
        self.SetForegroundColour("yellow")
        self.SetBackgroundColour("red")
        text = wx.StaticText(self,-1,"BMS",size=(250,200),pos=(500,70))
        font = wx.Font(76,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        text.SetFont(font)
        
        menu1 = wx.Menu()
        menu2 = wx.Menu()
        menu3 = wx.Menu()
        menu4 = wx.Menu()
        menuBar = wx.MenuBar()
        submenu = wx.Menu()
        submenu1 = wx.Menu()
       
        
        soda1 = submenu.Append(-1,"Mauzo ya Soda za Chupa")
        self.Bind(wx.EVT_MENU,self.SodaMauzo,soda1)
        
        sodak = submenu.Append(-1,"Mauzo ya Soda za Kopo")
        self.Bind(wx.EVT_MENU,self.SodaKMauzo,sodak)
        
        vinywajiBrd = submenu.Append(-1,"Mauzo ya Vinywaji Baridi")
        self.Bind(wx.EVT_MENU,self.vinywajbard,vinywajiBrd)
        
        menu1.AppendMenu(-1,"Mauzo ya soda",submenu)
        
        
        
        
        item2 = menu1.Append(-1, "Mauzo ya bia")
        self.Bind(wx.EVT_MENU,self.OnItem2,item2)
        
        
        item3 = menu1.Append(-1, "Matumizi")
        self.Bind(wx.EVT_MENU,self.OnItem3,item3)
        
        
        
        item99 = menu1.Append(-1,"Mauzo")
        self.Bind(wx.EVT_MENU, self.Onitem99, item99)
        
        
        item4 = menu1.Append(-1, "Kiasi cha pesa kilichopo")
        self.Bind(wx.EVT_MENU, self.OnItem4, item4)
        
        manager = submenu1.Append(-1,"Futa mauzo")
        self.Bind(wx.EVT_MENU,self.FutaMauzo,manager)
        
        manager2 = submenu1.Append(-1,"Futa Number za simu")
        self.Bind(wx.EVT_MENU,self.FutaNumber,manager2)
        
        manager3 = submenu1.Append(-1,"Futa Matumizi")
        self.Bind(wx.EVT_MENU,self.FutaMatumizi,manager3)
        
        manager4 = submenu1.Append(-1,"Futa Mauzo ya Bia")
        self.Bind(wx.EVT_MENU,self.FutaBia,manager4)
        
        
        manager5 = submenu1.Append(-1,"Futa Soda Kopo")
        self.Bind(wx.EVT_MENU,self.FutaKopo,manager5)
        
        
        manager6 = submenu1.Append(-1,"Futa Soda Chupa")
        self.Bind(wx.EVT_MENU,self.FutaChupa,manager6)
        
        manager7 = submenu1.Append(-1,"Futa Vinywaji Baridi")
        self.Bind(wx.EVT_MENU,self.FutaBarid,manager7)
        
        manager8 = submenu1.Append(-1,"Futa Vinywaji Vipya")
        self.Bind(wx.EVT_MENU,self.FutaVipya,manager8)
        
        
        
        
        menu1.AppendMenu(-1,"Manager",submenu1)
        
        
        item5 = menu1.Append(wx.ID_EXIT,"Exit")
        self.Bind(wx.EVT_MENU,self.OnExit,item5)
        
        menu1.AppendSeparator()
        menuBar.Append(menu1,"Menu")
        
        
             
        
        menuBar.Append(menu4,"Mawasiliano")
        item1d = menu4.Append(-1,"Jaza mawasiliano")
        item2d = menu4.Append(-1,"Tazama Number")
        self.Bind(wx.EVT_MENU,self.OnJMawasiliano,item1d)
        self.Bind(wx.EVT_MENU,self.OnTMawasiliano,item2d)
        
        item1c = menu3.Append(-1, "OnAbout")
        menuBar.Append(menu3,"About")
        self.Bind(wx.EVT_MENU,self.OnAbout,item1c)
        
        
        self.SetMenuBar(menuBar)
  
        self.SetMenuBar(menuBar)
        
      
      
    def layout(self):
        
        self.button45 = wx.Button(self,-1,"Ingiza mauzo ya Soda\n\tKopo",pos=(30,450),size=(192,40))
        self.Bind(wx.EVT_BUTTON,self.SodaKopo,self.button45)
        self.button45.SetBackgroundColour("green")
         
        
       
        self.btn5 = wx.Button(self,-1,"Ingiza Mauzo ya Bia",pos=(30,150),size=(192,35))
        self.Bind(wx.EVT_BUTTON,self.OnIngizaM,self.btn5)
        self.btn5.SetBackgroundColour("red")
        

        self.btn6 = wx.Button(self,-1,"Ingiza Matumizi",pos=(30,200),size=(192,35))
        self.Bind(wx.EVT_BUTTON,self.OnIngizaMa,self.btn6)
        self.btn6.SetBackgroundColour("green")
                
     
        
        
        
        self.btn7 = wx.Button(self,-1,"vinywaji baridi",pos=(30,250),size=(192,35))
        self.Bind(wx.EVT_BUTTON,self.VinywajiBard,self.btn7)
        self.btn7.SetBackgroundColour("purple")
        
        self.btn8 = wx.Button(self,-1,"Vinywaji vipya",pos=(30,300),size=(192,35))
        self.Bind(wx.EVT_BUTTON,self.VinywajiV,self.btn8)
        self.btn8.SetBackgroundColour("orange")
                         
                         
        self.btn9 = wx.Button(self,-1,"Vinywaji Vilivyopo",pos=(30,350),size=(192,35))
        self.Bind(wx.EVT_BUTTON,self.VinywajiVi,self.btn9)
        self.btn9.SetBackgroundColour("blue")
        
        self.btn11 = wx.Button(self,-1," Ingiza Mauzo ya Soda\n\tChupa",pos=(30,400),size=(192,40))
        self.Bind(wx.EVT_BUTTON,self.Soda,self.btn11)
        self.btn11.SetBackgroundColour("brown")        
        
       
 
    #defining altibutes
    def FutaVipya(self,event):
        
        
        self.static = wx.StaticText(self,-1,"user name:",pos=(360,255))
        self.text = wx.TextCtrl(self,-1,"",pos=(450,250),size=(192,-1))
        self.static2 = wx.StaticText(self,-1,"Password:",pos=(365,295))
        self.text2 = wx.TextCtrl(self,-1,"",pos=(450,290),size=(192,-1))
        self.text.SetBackgroundColour("white")
        self.text.SetForegroundColour("black")
        self.text2.SetBackgroundColour("white")
        self.text2.SetForegroundColour("black")
        
        self.button = wx.Button(self,-1,"Login",pos=(570,330),size=(70,22))
        self.button.Bind(wx.EVT_BUTTON,self.loginFutaVinyw)
        self.button.SetBackgroundColour("green")
        
    def loginFutaVinyw(self,event):
    
        username = self.text.GetValue()
        passwdi = self.text2.GetValue()
        names = str(username)
        passs = str(passwdi)
        
                
        
        if names == "manager" and passs == "1967":
                    
                dlg = wx.MessageBox("Login sucessfull","login")
                
                self.text.Destroy()
                self.static.Destroy()
                self.button.Destroy()
                self.static2.Destroy()
                self.text2.Destroy()        
       
                try: 
        
                    db = MySQLdb.connect("localhost","henry","mnyama","employee")
                    self.dlg = wx.MessageDialog(self,"Do you want to clear \"Mauzo ya vinywaji \n\tza chupa\"","Option",wx.YES_NO | wx.ICON_QUESTION)
                    
                    reply = self.dlg.ShowModal()
                    if reply == wx.ID_YES:
                        try:
                    
                            cursor = db.cursor()
                        
                            sql = "DROP TABLE IF EXISTS vinywajiVipya"
               
                            cursor.execute(sql)
                        except:
                            wx.MessageBox("Tafadhali ingiza vinywaji Vipya","alert")
                            
               
                    else:
                        wx.MessageBox("Vinywaji vipya was not erased\n\tThank you!","Message")
                        
                except:
                    wx.MessageBox("Unable to connect to the Database\nPlease make sure the server is running")        
        
        else:
            wx.MessageBox("Try Again!","login")
        
        
    def FutaBarid(self,event):
        
        
        
        self.static = wx.StaticText(self,-1,"user name:",pos=(360,255))
        self.text = wx.TextCtrl(self,-1,"",pos=(450,250),size=(192,-1))
        self.static2 = wx.StaticText(self,-1,"Password:",pos=(365,295))
        self.text2 = wx.TextCtrl(self,-1,"",pos=(450,290),size=(192,-1))
        self.text.SetBackgroundColour("white")
        self.text.SetForegroundColour("black")
        self.text2.SetBackgroundColour("white")
        self.text2.SetForegroundColour("black")
        
        self.button = wx.Button(self,-1,"Login",pos=(570,330),size=(70,22))
        self.button.Bind(wx.EVT_BUTTON,self.loginFutabard)
        self.button.SetBackgroundColour("green")
        
    def loginFutabard(self,event):
    
        username = self.text.GetValue()
        passwdi = self.text2.GetValue()
        names = str(username)
        passs = str(passwdi)
        
                
        
        if names == "manager" and passs == "1967":
                    
                dlg = wx.MessageBox("Login sucessfull","login")
                
                self.text.Destroy()
                self.static.Destroy()
                self.button.Destroy()
                self.static2.Destroy()
                self.text2.Destroy()        
       
                try: 
        
                    db = MySQLdb.connect("localhost","henry","mnyama","employee")
                    self.dlg = wx.MessageDialog(self,"Do you want to clear \"Mauzo ya vinywaji Baridi\n\tza chupa\"","Option",wx.YES_NO | wx.ICON_QUESTION)
                    
                    reply = self.dlg.ShowModal()
                    if reply == wx.ID_YES:
                        try:
                    
                            cursor = db.cursor()
                        
                            sql = "DROP TABLE IF EXISTS vinywajiB"
               
                            cursor.execute(sql)
                        except:
                            wx.MessageBox("Tafadhali ingiza vinywaji Baridi","alert")
                            
               
                    else:
                        wx.MessageBox("Mauzo ya vinywaji Baridi was not erased\n\tThank you!","Message")
                        
                except:
                    wx.MessageBox("Unable to connect to the Database\nPlease make sure the server is running")        
        
        
        else:
            wx.MessageBox("Try Again!","login")
        
        
        
        
    def FutaChupa(self,event):
        
        self.static = wx.StaticText(self,-1,"user name:",pos=(360,255))
        self.text = wx.TextCtrl(self,-1,"",pos=(450,250),size=(192,-1))
        self.static2 = wx.StaticText(self,-1,"Password:",pos=(365,295))
        self.text2 = wx.TextCtrl(self,-1,"",pos=(450,290),size=(192,-1))
        self.text.SetBackgroundColour("white")
        self.text.SetForegroundColour("black")
        self.text2.SetBackgroundColour("white")
        self.text2.SetForegroundColour("black")
        
        self.button = wx.Button(self,-1,"Login",pos=(570,330),size=(70,22))
        self.button.Bind(wx.EVT_BUTTON,self.loginFutachupa)
        self.button.SetBackgroundColour("green")
        
    def loginFutachupa(self,event):
    
        username = self.text.GetValue()
        passwdi = self.text2.GetValue()
        names = str(username)
        passs = str(passwdi)
        
                
        
        if names == "manager" and passs == "1967":
                    
                dlg = wx.MessageBox("Login sucessfull","login")
                
                self.text.Destroy()
                self.static.Destroy()
                self.button.Destroy()
                self.static2.Destroy()
                self.text2.Destroy()        
       
                try: 
                    
                    db = MySQLdb.connect("localhost","henry","mnyama","employee")
                    self.dlg = wx.MessageDialog(self,"Do you want to clear \"Mauzo ya soda\n\tza chupa\"","Option",wx.YES_NO | wx.ICON_QUESTION)
                    
                    reply = self.dlg.ShowModal()
                    if reply == wx.ID_YES:
                        try:
                    
                            cursor = db.cursor()
                        
                            sql = "DROP TABLE IF EXISTS sodaC"
               
                            cursor.execute(sql)
                        except:
                            wx.MessageBox("Tafadhali ingiza soda za chupa","alert")
                            
               
                    else:
                        wx.MessageBox("Mauzo ya Soda za chupa was not erased\n\tThank you!","Message")
                        
                except:
                    wx.MessageBox("Unable to connect to the Database\nPlease make sure the server is running")        
        
        else:
            wx.MessageBox("Try Again!","login")
        
    
    def FutaKopo(self,event):
       
        self.static = wx.StaticText(self,-1,"user name:",pos=(360,255))
        self.text = wx.TextCtrl(self,-1,"",pos=(450,250),size=(192,-1))
        self.static2 = wx.StaticText(self,-1,"Password:",pos=(365,295))
        self.text2 = wx.TextCtrl(self,-1,"",pos=(450,290),size=(192,-1))
        self.text.SetBackgroundColour("white")
        self.text.SetForegroundColour("black")
        self.text2.SetBackgroundColour("white")
        self.text2.SetForegroundColour("black")
        
        self.button = wx.Button(self,-1,"Login",pos=(570,330),size=(70,22))
        self.button.Bind(wx.EVT_BUTTON,self.loginFutakopo)
        self.button.SetBackgroundColour("green")
        
    def loginFutakopo(self,event):
    
        username = self.text.GetValue()
        passwdi = self.text2.GetValue()
        names = str(username)
        passs = str(passwdi)
        
                
        
        if names == "manager" and passs == "1967":
                    
                dlg = wx.MessageBox("Login sucessfull","login")
                
                self.text.Destroy()
                self.static.Destroy()
                self.button.Destroy()
                self.static2.Destroy()
                self.text2.Destroy()        
       
                try: 
        
                    db = MySQLdb.connect("localhost","henry","mnyama","employee")
                    self.dlg = wx.MessageDialog(self,"Do you want to clear \"Mauzo ya Bia\"","Option",wx.YES_NO | wx.ICON_QUESTION)
                    
                    reply = self.dlg.ShowModal()
                    if reply == wx.ID_YES:
                        try:
                    
                            cursor = db.cursor()
                        
                            sql = "DROP TABLE IF EXISTS sodaK"
               
                            cursor.execute(sql)
                        except:
                            wx.MessageBox("Tafadhali ingiza soda za kopo","alert")
                            
               
                    else:
                        wx.MessageBox("Mauzo ya soda za kopo was not erased\n\tThank you!","Message")
                        
                except:
                    wx.MessageBox("Unable to connect to the Database\nPlease make sure the server is running")
                       
        else:
            wx.MessageBox("Try Again!","login")       
       
    
    def FutaBia(self,event):
        
        self.static = wx.StaticText(self,-1,"user name:",pos=(360,255))
        self.text = wx.TextCtrl(self,-1,"",pos=(450,250),size=(192,-1))
        self.static2 = wx.StaticText(self,-1,"Password:",pos=(365,295))
        self.text2 = wx.TextCtrl(self,-1,"",pos=(450,290),size=(192,-1))
        self.text.SetBackgroundColour("white")
        self.text.SetForegroundColour("black")
        self.text2.SetBackgroundColour("white")
        self.text2.SetForegroundColour("black")
        
        self.button = wx.Button(self,-1,"Login",pos=(570,330),size=(70,22))
        self.button.Bind(wx.EVT_BUTTON,self.loginFutaBia)
        self.button.SetBackgroundColour("green")
        
    def loginFutaBia(self,event):
    
        username = self.text.GetValue()
        passwdi = self.text2.GetValue()
        names = str(username)
        passs = str(passwdi)
        
                
        
        if names == "manager" and passs == "1967":
                    
                dlg = wx.MessageBox("Login sucessfull","login")
                
                self.text.Destroy()
                self.static.Destroy()
                self.button.Destroy()
                self.static2.Destroy()
                self.text2.Destroy()        
       
                try: 
        
                    db = MySQLdb.connect("localhost","henry","mnyama","employee")
                    self.dlg = wx.MessageDialog(self,"Do you want to clear \"Mauzo ya Bia\"","Option",wx.YES_NO | wx.ICON_QUESTION)
                    
                    reply = self.dlg.ShowModal()
                    if reply == wx.ID_YES:
                        
                        try:
                            cursor = db.cursor()
                            
                            sql = "DROP TABLE IF EXISTS bia"
                   
                            cursor.execute(sql)
                            
                        except:
                            wx.MessageBox("Tafadhali Ingiza Bia","alert")
               
                    else:
                        wx.MessageBox("Mauzo ya Bia was not erased\n\tThank you!","Message")
                        
                except:
                    wx.MessageBox("Unable to connect to the Database\nPlease make sure the server is running")
                
        else:
            wx.MessageBox("Try Again!","login")
                    
    
    
    def FutaMatumizi(self,event):
        
        self.static = wx.StaticText(self,-1,"user name:",pos=(360,255))
        self.text = wx.TextCtrl(self,-1,"",pos=(450,250),size=(192,-1))
        self.static2 = wx.StaticText(self,-1,"Password:",pos=(365,295))
        self.text2 = wx.TextCtrl(self,-1,"",pos=(450,290),size=(192,-1))
        self.text.SetBackgroundColour("white")
        self.text.SetForegroundColour("black")
        self.text2.SetBackgroundColour("white")
        self.text2.SetForegroundColour("black")
        
        self.button = wx.Button(self,-1,"Login",pos=(570,330),size=(70,22))
        self.button.Bind(wx.EVT_BUTTON,self.loginFutaMatumizi)
        self.button.SetBackgroundColour("green")
        
    def loginFutaMatumizi(self,event):
    
        username = self.text.GetValue()
        passwdi = self.text2.GetValue()
        names = str(username)
        passs = str(passwdi)
        
                
        
        if names == "manager" and passs == "1967":
                    
                dlg = wx.MessageBox("Login sucessfull","login")
                
                self.text.Destroy()
                self.static.Destroy()
                self.button.Destroy()
                self.static2.Destroy()
                self.text2.Destroy()        
       
                try: 
        
                    db = MySQLdb.connect("localhost","henry","mnyama","employee")
                    self.dlg = wx.MessageDialog(self,"Do you want to clear \"Matumizi\"","Option",wx.YES_NO | wx.ICON_QUESTION)
                    
                    reply = self.dlg.ShowModal()
                    if reply == wx.ID_YES:
                        try:
                    
                            cursor = db.cursor()
                            
                            sql = "DROP TABLE IF EXISTS matumizi"
                   
                            cursor.execute(sql)
                            
                        except:
                                wx.MessageBox("Tafadhali Ingiza matumizi","Alert")
                   
                    else:
                        wx.MessageBox("\"Matumizi\" was not erased\n\tThank you!","Message")
                        
                except:
                    wx.MessageBox("Unable to connect to the Database\nPlease make sure the server is running")
                    
        else:
            wx.MessageBox("Try Again!","login")
                    
    
    
    def FutaNumber(self,event):
        
        
        self.static = wx.StaticText(self,-1,"user name:",pos=(360,255))
        self.text = wx.TextCtrl(self,-1,"",pos=(450,250),size=(192,-1))
        self.static2 = wx.StaticText(self,-1,"Password:",pos=(365,295))
        self.text2 = wx.TextCtrl(self,-1,"",pos=(450,290),size=(192,-1))
        self.text.SetBackgroundColour("white")
        self.text.SetForegroundColour("black")
        self.text2.SetBackgroundColour("white")
        self.text2.SetForegroundColour("black")
        
        self.button = wx.Button(self,-1,"Login",pos=(570,330),size=(70,22))
        self.button.Bind(wx.EVT_BUTTON,self.loginFutanumber)
        self.button.SetBackgroundColour("green")
        
    def loginFutanumber(self,event):
    
        username = self.text.GetValue()
        passwdi = self.text2.GetValue()
        names = str(username)
        passs = str(passwdi)
        
                
        
        if names == "manager" and passs == "1967":
                    
                dlg = wx.MessageBox("Login sucessfull","login")
                
                self.text.Destroy()
                self.static.Destroy()
                self.button.Destroy()
                self.static2.Destroy()
                self.text2.Destroy()        
       
                try: 
        
                    db = MySQLdb.connect("localhost","henry","mnyama","employee")
                    self.dlg = wx.MessageDialog(self,"Do you want to clear \"Mawasiliano\"","Option",wx.YES_NO | wx.ICON_QUESTION)
                    
                    reply = self.dlg.ShowModal()
                    if reply == wx.ID_YES:
                        
                        try:
                            cursor = db.cursor()
                            
                            sql = "DROP TABLE IF EXISTS mawasiliano"
                   
                            cursor.execute(sql)
                        except:
                            wx.MessageBox("Tafadhali ingiza mawasiliano")
                            
                   
                    else:
                        wx.MessageBox("\"Mawasiliano\" was not erased\n\tThank you!","Message")
                        
                except:
                    wx.MessageBox("Unable to connect to the Database\nPlease make sure the server is running")       
       
        else:
            wx.MessageBox("Try Again!","login")       
    
    def FutaMauzo(self,event):
       
        self.static = wx.StaticText(self,-1,"user name:",pos=(360,255))
        self.text = wx.TextCtrl(self,-1,"",pos=(450,250),size=(192,-1))
        self.static2 = wx.StaticText(self,-1,"Password:",pos=(365,295))
        self.text2 = wx.TextCtrl(self,-1,"",pos=(450,290),size=(192,-1))
        self.text.SetBackgroundColour("white")
        self.text.SetForegroundColour("black")
        self.text2.SetBackgroundColour("white")
        self.text2.SetForegroundColour("black")
        
        self.button = wx.Button(self,-1,"Login",pos=(570,330),size=(70,22))
        self.button.Bind(wx.EVT_BUTTON,self.loginFutamauzo)
        self.button.SetBackgroundColour("green")
        
    def loginFutamauzo(self,event):
    
        username = self.text.GetValue()
        passwdi = self.text2.GetValue()
        names = str(username)
        passs = str(passwdi)
        
                
        
        if names == "manager" and passs == "1967":
                    
                dlg = wx.MessageBox("Login sucessfull","login")
                
                self.text.Destroy()
                self.static.Destroy()
                self.button.Destroy()
                self.static2.Destroy()
                self.text2.Destroy()        
       
                try: 
        
                    db = MySQLdb.connect("localhost","henry","mnyama","employee")
                    self.dlg = wx.MessageDialog(self,"Do you want to clear \"Mauzo\"","Option",wx.YES_NO | wx.ICON_QUESTION)
                    
                    reply = self.dlg.ShowModal()
                    if reply == wx.ID_YES:
                        
                        try:
                            cursor = db.cursor()
                            
                            sql = "DROP TABLE IF EXISTS mauzo"
                   
                            cursor.execute(sql)
                        except:
                            wx.MessageBox("Tafadhali Ingiza mauzo","Alert")
               
                        else:
                            wx.MessageBox("\"Mauzo\" was not erased\n\tThank you!","Message")
                        
                except:
                    wx.MessageBox("Unable to connect to the Database\nPlease make sure the server is running")       
       
        else:
            wx.MessageBox("Try Again!","login")
                      
    
    def OnExit(self,event):
        self.dlg = wx.MessageDialog(self,"Do you want to exit?","Exit",wx.YES_NO | wx.ICON_QUESTION)
        response = self.dlg.ShowModal()
        
        if response == wx.ID_YES:
            
            self.Close()
        
            
    
    def vinywajbard(self,event):#vinywaji Baridi
        try:
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            sql = "SELECT CONVERT(date2,CHAR(50)),(kinywaji),CONVERT(bei,CHAR(50)) FROM vinywajiB"
            
            cursor.execute(sql)
            
            vinywajbb = cursor.fetchall()
            
            self.lst = wx.ListCtrl(self,size=(700,500),pos=(120,50),style=wx.LC_REPORT)
            self.lst.InsertColumn(0,"Tarehe na muda",width=250)
            self.lst.InsertColumn(1,"Aina ya Kinywaji",width=250)
            self.lst.InsertColumn(2,"Bei",width=200)
            self.lst.SetBackgroundColour("white")
            self.lst.SetForegroundColour("black")
        except:
            wx.MessageBox("Unable to connect to the server\nplease make sure that the server is running")
            
        try:
            for row in vinywajbb:
                index = self.lst.InsertStringItem(sys.maxint,row[0])
                self.lst.SetStringItem(index,0,row[0])
                self.lst.SetStringItem(index,1,row[1])
                self.lst.SetStringItem(index,2,row[2])
                index += 1
                
                self.button = wx.Button(self,-1, "Home")
                self.button.Bind(wx.EVT_BUTTON,self.buttonx1)
                self.button.SetBackgroundColour("green")
                
                sizer = wx.BoxSizer(wx.VERTICAL)
                sizer.Add(self.button,1,wx.ALL|wx.EXPAND,5)
                sizer.Add(self.lst,0,wx.ALL|wx.CENTRE,5)
        except:
            wx.MessageBox("Hi, Tafadhali ingiza mauzo","alert")
            
    def buttonx1(self,event):
        try:
            
            self.lst.Destroy()
        except:
            wx.MessageBox("Hi, Welcome","Welcome")
        
    def SodaKMauzo(self,event):
        
        self.button45.Destroy()
        self.btn5.Destroy()
        self.btn6.Destroy()
        self.btn7.Destroy()
        self.btn8.Destroy()   
        self.btn9.Destroy()
        self.btn11.Destroy()         
        
        try:
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            sql2233 = "SELECT CONVERT(date1,CHAR(50)),CONVERT(idadik,CHAR(50)),CONVERT((idadik)*(1000),CHAR(50)) FROM sodaK"
            
            cursor.execute(sql2233)
            sodak = cursor.fetchall()
            
            self.lst = wx.ListCtrl(self,size=(1000,600),pos=(40,40),style=wx.LC_REPORT)
            
            self.lst.InsertColumn(1,"Tarehe na Muda",width=400)
            self.lst.InsertColumn(2,"Idadi",width=300)
            self.lst.InsertColumn(3,"Thamani(Tsh.)",width=300)
            self.lst.SetBackgroundColour("white")
            self.lst.SetForegroundColour("black")
            
            for row in sodak:
                
                index = self.lst.InsertStringItem(sys.maxint,row[0])
                self.lst.SetStringItem(index,0,row[0])
                self.lst.SetStringItem(index,1,row[1])
                self.lst.SetStringItem(index,2,row[2])
                index += 1
               
                
                self.button = wx.Button(self,-1,"Home")
                self.button.Bind(wx.EVT_BUTTON,self.OnbuttonK)
                self.button.SetBackgroundColour("green")
                
                sizer = wx.BoxSizer(wx.VERTICAL)
                sizer.Add(self.lst, 1, wx.ALL | wx.EXPAND,5)
                sizer.Add(self.button,0, wx.ALL | wx.CENTRE,5)
        except:
            wx.MessageBox("Hi, Tafadhali Ingiza mauzo ya soda","Welcome")
                
            
    def OnbuttonK(self,event):
        try:
            self.layout()
            self.lst.Destroy()
        except:
            wx.MessageBox("Hi, Welcome","Welcome")
    
    def SodaKopo(self,event):
        try:  
           
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            
            sql11 = ("""CREATE TABLE IF NOT EXISTS sodaK
            (
            
            date1 TIMESTAMP,
            idadik INT
            
            )
            """)
            cursor.execute(sql11)
            
                    
            sql2 = ("""CREATE TABLE IF NOT EXISTS mauzo
            (
            date TIMESTAMP,
            sodaC FLOAT,
            sodak FLOAT,
            vinywajiB FLOAT,
            bia FLOAT,
            matumizi FLOAT
            )
            """)
            cursor.execute(sql2)
            
            
            sqlsoda = ("""CREATE TABLE IF NOT EXISTS sodazte
            (
            sodaCin INT,
            sodaCut INT,
            sodaKin INT,
            sodaKout INT
            )
            """)
            cursor.execute(sqlsoda)
            
            
        except:
            wx.MessageBox("Unable to connect to the Database\nPlease make sure the server is running")
            
        
    
        
        dlg223 = wx.TextEntryDialog(self,"Ingiza idadi ya soda za kopo","Message")
        dlg223.ShowModal()
        response223 = dlg223.GetValue()
        
        try:    
            answ223 = int(response223)
        except:
            wx.MessageBox("Tafadhali Rudia")
            
        try:
        
            sql1 = "INSERT INTO sodaK (idadik) \
            VALUES ('%d')"%answ223
            sql3 = "INSERT INTO mauzo(sodak)\
            VALUES ('%d')"%answ223
            
            sqlsodazte = "INSERT INTO sodazte(sodaKout)\
            VALUES ('%d')"%answ223
            
            cursor.execute(sql1)
            cursor.execute(sql3)
            cursor.execute(sqlsodazte)
            
            db.commit()
            
        except:
            wx.MessageBox("Unable to feed data to the Database\nPlease make sure the server is running")
            
   
    def Onitem99(self,event):
        
        self.button45.Destroy()
        self.btn5.Destroy()
        self.btn6.Destroy()
        self.btn7.Destroy()
        self.btn8.Destroy()   
        self.btn9.Destroy()
        self.btn11.Destroy() 
        
        try:
            
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            sql = "SELECT CONVERT(SUM(sodaC),CHAR(50)),CONVERT(SUM((sodaC)*(700)),CHAR(50)),CONVERT(SUM(sodak),CHAR(50)),CONVERT(SUM((sodak)*(1000)),CHAR(50)),\
            CONVERT(SUM(vinywajiB),CHAR(50)),CONVERT(SUM(bia),CHAR(50)) FROM mauzo"
            
            cursor.execute(sql)
            
            sql44 = "SELECT SUM((sodaC)*(700))+SUM((sodak)*(1000))+SUM(vinywajiB)+SUM(bia) AS he from mauzo"
            
            
            
            
            cursor.execute(sql)
            
            mauzo = cursor.fetchall()
            
            
            self.lst33 = wx.ListCtrl(self,size=(1200,600),pos=(10,50),style=wx.LC_REPORT)
            self.lst33.InsertColumn(0,"Idadi Soda za Chupa",width=200)
            self.lst33.InsertColumn(1,"Mauzo soda za chupa",width=200)
            self.lst33.InsertColumn(2,"Idadi soda za kopo",width=200)
            self.lst33.InsertColumn(3,"Mauzo soda za kopo",width=200)
            self.lst33.InsertColumn(4,"Mauzo vinywaji Baridi",width=200)
            self.lst33.InsertColumn(5,"Mauzo Bia",width=200)
            self.lst33.SetBackgroundColour("white")
            self.lst33.SetForegroundColour("black")
            
            for row in mauzo:
                index = self.lst33.InsertStringItem(sys.maxint,row[0])
                self.lst33.SetStringItem(index,0,row[0])
                self.lst33.SetStringItem(index,1,row[1])
                self.lst33.SetStringItem(index,2,row[2])
                self.lst33.SetStringItem(index,3,row[3])
                self.lst33.SetStringItem(index,4,row[4])
                self.lst33.SetStringItem(index,5,row[5])
                
                index += 1
                
                
                cursor.execute(sql44)
                mauzot = cursor.fetchall()
                wx.MessageBox("Hi!\nKiasi cha Mauzo ni Tsh.%s"%mauzot,"Mauzo")
                
                self.button = wx.Button(self,-1,"Home")
                self.button.Bind(wx.EVT_BUTTON,self.mauzoFunga)
                
                self.button.SetBackgroundColour("green")
                
                
        except:
                wx.MessageBox("Hi,Tafadhali ingiza Mauzo")
            
    def mauzoFunga(self,event):
        try:
            self.layout()
            self.lst33.Destroy()
            self.button.Destroy()
          
        except:
            wx.MessageBox("Hi,Tafadhali ingiza Mauzo")
            
    def SodaMauzo(self,event):#defines kuonesha mauzo ya soda
       

        self.button45.Destroy()
        self.btn5.Destroy()
        self.btn6.Destroy()
        self.btn7.Destroy()
        self.btn8.Destroy()   
        self.btn9.Destroy()
        self.btn11.Destroy()          
       
       
        db = MySQLdb.connect("localhost","henry","mnyama","employee")
        cursor = db.cursor()
        
        sql24 = "SELECT CONVERT(date,CHAR(50)),CONVERT(soda,CHAR(50)),CONVERT((soda)*(700),CHAR(50)) FROM sodaC"
       
        cursor.execute(sql24)
        
        soda = cursor.fetchall()
        
       
            
        self.lst24 = wx.ListCtrl(self,size=(1200,600),pos=(30,30),style=wx.LC_REPORT)
        self.lst24.InsertColumn(0,"Tarehe na muda",width= 400)
        self.lst24.InsertColumn(1,"idadi ya soda",width=300)
        self.lst24.InsertColumn(2,"Thamani(TSH.)",width=300)
       
        
        self.lst24.SetBackgroundColour("white") 
        self.lst24.SetForegroundColour("black")
        
        for row in soda:
             
            index = self.lst24.InsertStringItem(sys.maxint,row[0])
            self.lst24.SetStringItem(index,0,row[0])
            self.lst24.SetStringItem(index,1,row[1])
            self.lst24.SetStringItem(index,2,row[2])
            
            index += 1
            
            self.button = wx.Button(self,-1,"Home")
            self.button.SetBackgroundColour("green")
            self.button.Bind(wx.EVT_BUTTON, self.fungaSodaMau)
            
            
            
    
    def fungaSodaMau(self,event):
        try:
            self.layout()
            self.lst24.Destroy()
            self.button.Destroy()
            
            
        except:
            wx.MessageBox("Hi, Welcome","Welcome")
            
    def Soda(self,event):#Defines uingizaji wa mauzo ya soda
        
        try:
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
    
            sql20 = ("""CREATE TABLE IF NOT EXISTS sodaC
            (
            date TIMESTAMP,
            soda INT
            
            )
            """)
            cursor.execute(sql20)
            
        
            sql2 = ("""CREATE TABLE IF NOT EXISTS mauzo
            (
            date TIMESTAMP,
            sodaC FLOAT,
            sodak FLOAT,
            vinywajiB FLOAT,
            bia FLOAT,
            matumizi FLOAT
            )
            """)
            cursor.execute(sql2)  
            
            sqlsoda = ("""CREATE TABLE IF NOT EXISTS sodazte
            (
            sodaCin INT,
            sodaCut INT,
            sodaKin INT,
            sodaKout INT
            )
            """)
            cursor.execute(sqlsoda)
                
            
        except:
            wx.MessageBox("Unable to connect to the Database\nPlease make sure that the server is running","alert")
                
        try:
            dlg22 = wx.TextEntryDialog(self,"Ingiza idadi ya soda za chupa zilizo uzwa","soda")
            dlg22.ShowModal()
            response22 = dlg22.GetValue()
            soda = int(response22)
        except:
            wx.MessageBox("Hi, Tafadhali rudia tena","alert")
                
        try:
            sql23 = "INSERT INTO sodaC (soda)\
            VALUES ('%d')"%soda
            
            sql3 = "INSERT INTO mauzo (sodaC)\
            VALUES ('%d')"%soda
            
            sqlsodazte = "INSERT INTO sodazte (sodaCut)\
            VALUES ('%d')"%soda
            
            cursor.execute(sql23)
            cursor.execute(sql3)
            cursor.execute(sqlsodazte)
            
            db.commit()
            
        except:
            wx.MessageBox("Tafadhali rudia tena","alert")
            
            
  
        
    def VinywajiV(self,event):
        try:
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            
            
            sqlsoda = ("""CREATE TABLE IF NOT EXISTS sodazte
            (
            sodaCin INT,
            sodaCut INT,
            sodaKin INT,
            sodaKout INT
            )
            """)
            cursor.execute(sqlsoda)
            
            
        except:
            wx.MessageBox("Unable to connect to the Database\nPlease make sure the server is running")
            
        
        try:       
            dlg25 = wx.TextEntryDialog(self,"Ingiza idadi ya soda Mpya Za Chupa\n\"0\" Kama hamna kilicho nunuliwa","Soda")
            dlg25.ShowModal()
            response25 = dlg25.GetValue()
            
            answ25 = int(response25)
            
            
           
            dlg27 = wx.TextEntryDialog(self,"Ingiza idadi ya Soda Mpya za kopo \n\"0\" Kama hamna kilicho nunuliwa","Vinywaji")
            dlg27.ShowModal()
            response27 = dlg27.GetValue()
            
                
            answ27 = int(response27)
        
        except:
            wx.MessageBox("Tafadhali ingiza\n\"0\" Kama hamna kilicho nunuliwa","Alert")
          
        try:
            sql26 = "INSERT INTO sodazte (sodaKin)\
            VALUES ('%d')"%answ27
            
            sqlsodazte = "INSERT INTO sodazte (sodaCin)\
            VALUES ('%d')"%answ25
            
            cursor.execute(sql26)
            cursor.execute(sqlsodazte)
            
            db.commit()
             
        except:
            wx.MessageBox("Hi!\nNo Data were inserted into the Database","DataInfo")
      
           
        
    def VinywajiVi(self,event):

        self.button45.Destroy()
        self.btn5.Destroy()
        self.btn6.Destroy()
        self.btn7.Destroy()
        self.btn8.Destroy()   
        self.btn9.Destroy()
        self.btn11.Destroy()           
        try:    
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            
            sqlsd = "SELECT CONVERT(SUM(sodaCin)-SUM(sodaCut),CHAR(500)),\
            CONVERT(SUM((sodaCin)*(700))-SUM((sodaCut)*(700)),CHAR(500)),\
            CONVERT(SUM(sodaKin)-SUM(sodaKout),CHAR(500)),\
            CONVERT(SUM((sodaKin)*(1000))-sum((sodaKout)*(1000)),CHAR(500)) from sodazte"
            
            
            sqlsd2 = "SELECT CONVERT(SUM((sodaCin)*(700))-SUM((sodaCut)*(700))\
            +SUM((sodaKin)*(1000))-SUM((sodaKout)*(1000)),CHAR(500)) from sodazte"
            
        
            
            cursor.execute(sqlsd)
            sodazte = cursor.fetchall()
            
        
        except:
            wx.MessageBox("Unable to connect to the server\nPlease make sure the server is running","Alert")
            
        try:
            self.lstsd = wx.ListCtrl(self,size=(1000,600),pos=(55,70),style=wx.LC_REPORT)
            self.lstsd.InsertColumn(0,"idadi ya Chupa",width=300)
            self.lstsd.InsertColumn(1,"Thamani ya SodaChupa",width=300)
            self.lstsd.InsertColumn(2,"Idadi ya Kopo",width=200)
            self.lstsd.InsertColumn(3,"Thamani ya SodaKopo",width=200)
            self.lstsd.SetBackgroundColour("white")
            self.lstsd.SetForegroundColour("black")
            
            
            
            for row in sodazte:
                
                
               
                index = self.lstsd.InsertStringItem(sys.maxint,row[0])
                
                self.lstsd.SetStringItem(index,0,row[0])
                self.lstsd.SetStringItem(index,1,row[1])
                self.lstsd.SetStringItem(index,2,row[2])
                self.lstsd.SetStringItem(index,3,row[3])
                index += 1
                
                cursor.execute(sqlsd2)
                sodazte2 = cursor.fetchall()
                
                msg = wx.MessageBox("Umebakiwa na soda zenye thamani ya\n\tTsh. %s"%sodazte2,"Salio Soda")
                 
                
                self.button = wx.Button(self,-1,"Home")
                self.button.Bind(wx.EVT_BUTTON,self.sodaztebtn)
                self.button.SetBackgroundColour("green")
                
                
        except:
            wx.MessageBox("Tafadhali Ingiza manunuzi ya vinywaji")
            
            
    def sodaztebtn(self,event):
        
        self.lstsd.Destroy()
        self.layout()
        self.button.Destroy()
                
        
        
        
        
    
    def VinywajiBard(self,event):
        
        try:
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            sql23 = ("""CREATE TABLE IF NOT EXISTS vinywajiB
            (
            date2 TIMESTAMP,
            kinywaji CHAR(60),
            bei FLOAT
            )
            """)
            cursor.execute(sql23)
            
        except:
            wx.MessageBox("Unable to connect to the Database\nPlease make sure that the server is running","alert")
            
        sql2 = ("""CREATE TABLE IF NOT EXISTS mauzo
        (
        date TIMESTAMP,
        sodaC FLOAT,
        sodak FLOAT,
        vinywajiB FLOAT,
        bia FLOAT
        )
        """)
        cursor.execute(sql2)
        
        sqlsoda = ("""CREATE TABLE IF NOT EXISTS sodazte
        (
        sodaCin INT,
        sodaCut INT,
        sodaKin INT,
        sodaKout INT
        )
        """)
        cursor.execute(sqlsoda)
        
        
        dlg23 = wx.TextEntryDialog(self,"Ingiza jina la kinywaji Baridi\neg. maji,juice,wine...","kinwaji Baridi")
        dlg23.ShowModal()
        response23 = dlg23.GetValue()
        
        dlg24 = wx.TextEntryDialog(self,"Ingiza Bei ya kinywaji","bei")
        dlg24.ShowModal()
        response24 = dlg24.GetValue()
        try:
            shop2 = float(response24)
        except ValueError:
            wx.MessageBox("Hi, Tafadhali Rudia","Alert")
            
        
       
    
        
        try:
            
            sql23 = "INSERT INTO vinywajiB (kinywaji,bei)\
                VALUES ('%s','%d')"%(response23,shop2)
            
            sql3 = "INSERT INTO mauzo (vinywajiB)\
            VALUES ('%d')"%shop2
            
            cursor.execute(sql23)
            cursor.execute(sql3)
            db.commit()
            
        except:
            wx.MessageBox("Unable to insert data into the Database\nPlease make sure that the server is running")
    
            
     
    
    
        
    
    def OnItem2(self,event):
      

        self.button45.Destroy()
        self.btn5.Destroy()
        self.btn6.Destroy()
        self.btn7.Destroy()
        self.btn8.Destroy()   
        self.btn9.Destroy()
        self.btn11.Destroy()        
        
       
        try:
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
        
            cursor = db.cursor()
            sql3 = "SELECT CONVERT(dt,CHAR(50)),(bidhaa),CONVERT(bei,CHAR(50)) from bia"
            
            cursor.execute(sql3)
            
            player = cursor.fetchall()
           
        except:
            wx.MessageBox("Unable to connect to the Database\nPlease make sure that the server is running","alert")
               
                   
        try:           
            
            
            self.lisit  = wx.ListCtrl(self,size=(1200,550),pos=(90,10),style=wx.LC_REPORT)
            self.lisit.InsertColumn(0,"Date and Time",width=400)  
            self.lisit.InsertColumn(1,"Bidhaa",width=300)
            self.lisit.InsertColumn(2,"Bei",width=300)
            self.lisit.SetBackgroundColour("white")
            self.lisit.SetForegroundColour("black")
           
            for row in player:
                
                
                    
                index =  self.lisit.InsertStringItem(sys.maxint,row[0])
                
                
                self.lisit.SetStringItem(index,0,row[0])
                self.lisit.SetStringItem(index,1,row[1])
                self.lisit.SetStringItem(index,2,row[2])
                index += 1
            
                         
                self.button = wx.Button(self,-1,"Home")
                self.button.Bind(wx.EVT_BUTTON,self.mauzoFungaz)
                
                self.button.SetBackgroundColour("green")
                
                
        except:
                wx.MessageBox("Hi,Tafadhali ingiza Mauzo")
            
    def mauzoFungaz(self,event):
        try:
            self.lisit.Destroy()
            self.button.Destroy()
            self.layout()
        except:
            wx.MessageBox("Hi,welcome","Alert")
        
   
        
        
    def OnItem3(self,event):

        self.button45.Destroy()
        self.btn5.Destroy()
        self.btn6.Destroy()
        self.btn7.Destroy()
        self.btn8.Destroy()   
        self.btn9.Destroy()
        self.btn11.Destroy()           
        
        
        try:
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            sql10 = "SELECT CONVERT(dt,CHAR(50)),(Amatumizi),CONVERT(Kiasi,CHAR(30)) FROM matumizi"
            cursor.execute(sql10)
            matumizi = cursor.fetchall()
            
        except:
            wx.MessageBox("unable to fetch data from the Database\nPlease make the server is running")
            
            
        try:
            self.lst3 = wx.ListCtrl(self,size=(1000,600),pos=(30,40),style=wx.LC_REPORT)
            self.lst3.InsertColumn(0,"Date and Time",width=300)
            self.lst3.InsertColumn(1,"Matumizi",width=300)
            self.lst3.InsertColumn(2,"Kiasi Kilichotumika",width=400)
            self.lst3.SetBackgroundColour("white")
            self.lst3.SetForegroundColour("black")
            
            
            for row2 in matumizi:
                index2 = self.lst3.InsertStringItem(sys.maxint,row2[0])
                self.lst3.SetStringItem(index2,0,row2[0])
                self.lst3.SetStringItem(index2,1,row2[1])
                self.lst3.SetStringItem(index2,2,row2[2])
                index2 += 1
                
                self.btn = wx.Button(self,-1,"Home")
                self.btn.Bind(wx.EVT_BUTTON,self.Click3)
                self.btn.SetBackgroundColour("green")
                
                
                sizer = wx.BoxSizer(wx.VERTICAL)
                sizer.Add(self.lst3,1,wx.ALL|wx.EXPAND,5)
                sizer.Add(self.btn,0,wx.ALL|wx.CENTER,5)
                
    
                
            
        except:
            wx.MessageBox("Tafadhali ingiza matumizi")
        
    
    def Click3(self,event):
        try:
            
            self.layout()
            self.lst3.Destroy()
            self.btn.Destroy()
        except:
            wx.MessageBox("Welcome","Welcome")
    
    def OnItem4(self,event):

        self.button45.Destroy()
        self.btn5.Destroy()
        self.btn6.Destroy()
        self.btn7.Destroy()
        self.btn8.Destroy()   
        self.btn9.Destroy()
        self.btn11.Destroy()   
        
        self.static = wx.StaticText(self,-1,"user name:",pos=(360,255))
        self.text = wx.TextCtrl(self,-1,"",pos=(450,250),size=(192,-1))
        self.static2 = wx.StaticText(self,-1,"Password:",pos=(365,295))
        self.text2 = wx.TextCtrl(self,-1,"",pos=(450,290),size=(192,-1))
        self.text.SetBackgroundColour("white")
        self.text.SetForegroundColour("black")
        self.text2.SetBackgroundColour("white")
        self.text2.SetForegroundColour("black")
        
        self.button = wx.Button(self,-1,"Login",pos=(570,330),size=(70,22))
        self.button.Bind(wx.EVT_BUTTON,self.login)
        self.button.SetBackgroundColour("green")
        
    def login(self,event):
    
        username = self.text.GetValue()
        passwdi = self.text2.GetValue()
        names = str(username)
        passs = str(passwdi)
        
                
        
        if names == "manager" and passs == "1967":
                    
                dlg = wx.MessageBox("Login sucessfull","login")
                
                self.text.Destroy()
                self.static.Destroy()
                self.button.Destroy()
                self.static2.Destroy()
                self.text2.Destroy() 
                
                db = MySQLdb.connect("localhost","henry","mnyama","employee")
                cursor = db.cursor()
                sql = "SELECT ((SUM((sodaC)*(700))+sum((sodak)*(1000))+SUM(vinywajiB)+SUM(bia))\
                -SUM(matumizi)) AS he FROM mauzo"
                
                cursor.execute(sql)
                
                kiasikilichopo = cursor.fetchall()
                
                wx.MessageBox("Kiasi kilichopo ni \nTsh.%s"%kiasikilichopo,"Kiasi")

        else:
            self.dlg2 = wx.MessageBox("Try Again!","login")
            self.text.Clear()
            self.text2.Clear()
            
        self.layout()
                
    def OnIngizaM(self,event):
        try:
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            sql = ( """
            CREATE TABLE IF NOT EXISTS bia
            (
            dt TIMESTAMP,
            bidhaa VARCHAR(30),
            bei FLOAT
            )
            """)
            
            cursor.execute(sql)
            
        except:
            wx.MessageBox("Unable to fetch data from the Database\nPlease make sure the server is running","alert")
        
        try:
            sql2 = ("""
            CREATE TABLE IF NOT EXISTS mauzo
            (
            date TIMESTAMP,
            sodaC FLOAT,
            sodak FLOAT,
            vinywajiB FLOAT,
            bia FLOAT,
            matumizi FLOAT
            )
            """)
            cursor.execute(sql2)
        except:
            wx.MessageBox("Unable to connect to the server\nPlease Make sure the server is runnng","alert")
            
        
        self.sext = wx.StaticText(self,-1,"Mauzo ya  Bia", pos=(390,225))
        font = wx.Font(36,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.sext.SetFont(font)            
            
        self.textz = wx.StaticText(self,-1,"Igiza jina la Bia 1:",pos=(200,300))
        self.bidh = wx.TextCtrl(self,pos=(320,300),size=(172,-1))
    
        self.textz1 = wx.StaticText(self,-1,"Igiza jina la Bia 2:",pos=(200,340))
        self.bidh11 = wx.TextCtrl(self,pos=(320,340),size=(172,-1))
        
        self.textz2 = wx.StaticText(self,-1,"Igiza jina la Bia 3:",pos=(200,380))
        self.bidh12 = wx.TextCtrl(self,pos=(320,380),size=(172,-1))
        
    
        self.textzq = wx.StaticText(self,-1,"Ingiza Bei ya Bia 1:",pos=(500,300))
        self.bei = wx.TextCtrl(self,pos=(625,300),size=(172,-1))


        self.textzq1 = wx.StaticText(self,-1,"Ingiza Bei ya Bia 1:",pos=(500,340))
        self.bei123 = wx.TextCtrl(self,pos=(625,340),size=(172,-1))
                

        self.textzq2 = wx.StaticText(self,-1,"Ingiza Bei ya Bia 1:",pos=(500,380))
        self.bei24 = wx.TextCtrl(self,pos=(625,380),size=(172,-1))
                
        
        self.buttonme = wx.Button(self,-1,"Submit",pos=(530,450),size=(90,-1))
        self.buttonme.Bind(wx.EVT_BUTTON,self.onBiaGet)
        self.buttonme.SetBackgroundColour("green")
        
        self.buttonmem = wx.Button(self,-1,"Cancel",pos=(640,450),size=(90,-1))
        self.buttonmem.Bind(wx.EVT_BUTTON,self.onBiaGetC)
        self.buttonmem.SetBackgroundColour("red")        
        
        #Destroying all activities
        
        self.button45.Destroy()
        self.btn5.Destroy()
        self.btn6.Destroy()
        self.btn7.Destroy()
        self.btn8.Destroy()   
        self.btn9.Destroy()
        self.btn11.Destroy()
        #end of destroy action
    def onBiaGetC(self,event):

        self.textzq1.Destroy()
        self.bidh.Destroy()
        self.bidh12.Destroy()
        self.bei.Destroy()
        self.textz2.Destroy()
        self.bei24.Destroy()
        self.bei123.Destroy()
        self.textz1.Destroy()
        self.bidh11.Destroy()
        self.buttonme.Destroy()
        self.buttonmem.Destroy()
        self.textz.Destroy()
        self.textzq.Destroy()  
        self.textzq2.Destroy()
        self.sext.Destroy()
        
        #calling back the layout
        self.layout()
                
        
    def OnIngizaMa(self,event):
        try:
            
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            sql8 = ("""
            CREATE TABLE IF NOT EXISTS matumizi
            (
            dt TIMESTAMP,
            Amatumizi CHAR(50),
            Kiasi INT
            )
            """)
            cursor.execute(sql8)
            
            sql11 = ("""
            CREATE TABLE IF NOT EXISTS mauzo
            (
            date TIMESTAMP,
            sodaC FLOAT,
            sodak FLOAT,
            vinywajiB FLOAT,
            bia FLOAT,
            matumizi FLOAT
            )
            """)
            cursor.execute(sql11)

        
        except:
            wx.MessageBox("Unable to connect to the Database\nPlease Make sure that the server is running","alert")
            
            
        dlg3 = wx.TextEntryDialog(self,"ingiza aina ya matumizi","matumizi")
        dlg4 = wx.TextEntryDialog(self,"Ingiza kiasi cha matumizi","kiasi")
        dlg3.ShowModal()
        dlg4.ShowModal()
        response3 = dlg3.GetValue()
        response4 = dlg4.GetValue()
        kiasi = int(response4)
        
        sql9 = "INSERT INTO matumizi(Amatumizi,Kiasi)\
        VALUES ('%s','%d')"%(response3,kiasi)
   
        
        sql12 = "INSERT INTO mauzo(matumizi)\
        VALUES ('%d')"%kiasi
        
        cursor.execute(sql9)
        
        cursor.execute(sql12)
        
        db.commit()
        
        
    def OnAbout(self, event):#henry Mwasulama
        wx.MessageBox("The Bar Management System (BMS) is meant for running a bar or night club or pub\nCoded in python language with MySQL\nFor support Dial 0756876592\n\tGeniousit332285@gmail.com\n\n\n\t@ Geniousit 2018","about")
        
    
    def OnTMawasiliano(self, event):
        db = MySQLdb.connect("localhost","henry","mnyama","employee")
        cursor = db.cursor()
        sql7 = "SELECT (jina),CONVERT(simu,CHAR(50)) FROM mawasiliano"
        
        cursor.execute(sql7)
        mawasiliano = cursor.fetchall()
        
        self.lst1 = wx.ListCtrl(self,size=(650,450),pos=(50,50),style=wx.LC_REPORT)
        
        self.lst1.InsertColumn(0,"Jina",width=220)
        
        self.lst1.InsertColumn(1,"Number za Simu",width=210)
        self.lst1.SetBackgroundColour("white")
        self.lst1.SetForegroundColour("black")
        
        
        for row1 in mawasiliano:
            
            index1 = self.lst1.InsertStringItem(sys.maxint,row1[0])
            self.lst1.SetStringItem(index1,0,row1[0])
            self.lst1.SetStringItem(index1,1,row1[1])
            index1 += 1
            
            self.button = wx.Button(self,-1,"Home")
            self.button.SetBackgroundColour("green")
            self.button.Bind(wx.EVT_BUTTON, self.OnClick1)
            
            
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self.lst1,1, wx.ALL|wx.EXPAND,5)
            sizer.Add(self.button,0,wx.ALL|wx.CENTER,5)
            
            
            self.SetSizer(sizer)
            
    
    def OnClick1(self,event):
        try:
            self.lst1.Destroy()
        except:
            wx.MessageBox("Hi, Welcome","Welcome")
            
            
            
    def onBiaGet(self,event):#price on Bia
      
                
        db = MySQLdb.connect("localhost","henry","mnyama","employee")
        cursor = db.cursor()     
        majibu = self.bidh.GetValue()
        resultz = self.bei.GetValue() 
        shop1 = int(resultz)
            
        sql1 = "INSERT INTO bia(bidhaa,bei)\
            VALUES ('%s','%d')"%(majibu,shop1)
        
        sql333 = "INSERT INTO mauzo(bia)\
        VALUES ('%d')"%shop1
        
        cursor.execute(sql1)
        cursor.execute(sql333)
        db.commit()
         

        majibuz = self.bidh12.GetValue()
        majib22 = self.bei24.GetValue()
        shop3 = int(majib22)
        
        sql13 = "INSERT INTO bia(bidhaa,bei)\
            VALUES ('%s','%d')"%(majibuz,shop3)

        sql322 = "INSERT INTO mauzo(bia)\
        VALUES ('%d')"%shop3
            
        cursor.execute(sql13)
        cursor.execute(sql322)
        db.commit()        
        
        majibuze = self.bidh11.GetValue()
        majib11 = self.bei123.GetValue()
        shop2 = int(majib11)

        sql14 = "INSERT INTO bia(bidhaa,bei)\
            VALUES ('%s','%d')"%(majibuze,shop2)
        
        
        sql355 = "INSERT INTO mauzo(bia)\
        VALUES ('%d')"%shop2        
        
        cursor.execute(sql14)
        cursor.execute(sql355)
        db.commit()        
        
        
        
        self.textzq1.Destroy()
        self.bidh.Destroy()
        self.bidh12.Destroy()
        self.bei.Destroy()
        self.textz2.Destroy()
        self.bei24.Destroy()
        self.bei123.Destroy()
        self.textz1.Destroy()
        self.bidh11.Destroy()
        self.buttonme.Destroy()     
        self.textz.Destroy()
        self.textzq.Destroy()  
        self.textzq2.Destroy()
        self.sext.Destroy()
        
        #calling back the layout
        self.layout()
        
            
            
            
    def OnJMawasiliano(self,event):
       
        try:
            
        
            db = MySQLdb.connect("localhost","henry","mnyama","employee")
            cursor = db.cursor()
            
            sql5 = ("""
            CREATE TABLE IF NOT EXISTS mawasiliano
            (
            jina CHAR(20),
            simu INT
            )
            """)
            
            cursor.execute(sql5)
        
        except:
            wx.MessageBox("Unable to connect to the Database\nPlease make sure that the server is running","alert")
        try:
            
            dlg = wx.TextEntryDialog(self,"jina kamili","mawasiliano")
            dlg1 = wx.TextEntryDialog(self, "Namba ya simu","mawasilino")
            dlg.ShowModal()
            dlg1.ShowModal()
                    
            response = dlg.GetValue()
            response2 = dlg1.GetValue()
            
            numberi = int(response2) 
        except:
            wx.MessageBox("Tafadhali Rudia","alert")
            
        try:
            
            sql6 = "INSERT INTO mawasiliano(jina,simu)\
                VALUES('%s','%d')"%(response,numberi)
            cursor.execute(sql6)
            db.commit()
            
        except:
            wx.MessageBox("Unable to connect to the Database\nPlease make sure that the server is running")
        
        
        
    #end of altibute difinition
        
        
   #run the program     
if __name__ == "__main__":
    
    app = wx.PySimpleApp()
    frame = DianaPub()
    
    frame.Show()
    app.MainLoop()
    
