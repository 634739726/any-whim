# -*- coding: cp936 -*-
from tkinter import *
from win32service import *

class MyServiceInstaller:
    def __init__(self):
        self.master = Tk()
        self.master.resizable(False,False)
        self.master.title(u'��������')
        self.label = Label(self.master,text="welcome")
        self.entry = Entry(self.master)
        self.width = 60    
        self.label.pack(fill=X)
        self.entry.pack(fill=X)
        self.tk_install   = Button(self.master,command=self.install      ,text = u"��װ")
        self.tk_starts    = Button(self.master,command=self.starts       ,text = u"����")
        self.tk_stops     = Button(self.master,command=self.stops        ,text = u"ֹͣ")
        self.tk_uninstall = Button(self.master,command=self.uninstall    ,text = u"ж��")
        self.tk_close     = Button(self.master,command=self.master.quit  ,text = u"�ر�")
        self.tk_install.pack  (side=LEFT)
        self.tk_starts.pack   (side=LEFT)
        self.tk_stops.pack    (side=LEFT)
        self.tk_uninstall.pack(side=LEFT)
        self.tk_close.pack    (side=LEFT)
        self.label['width']          = self.width
        self.entry['width']          = self.width
        self.tk_install['width']     = self.width/5
        self.tk_starts['width']      = self.width/5
        self.tk_stops['width']       = self.width/5
        self.tk_uninstall['width']   = self.width/5
        self.tk_close['width']       = self.width/5
        self.scm = OpenSCManager(None,None,SC_MANAGER_ALL_ACCESS)
        self.service_handle = None
        mainloop()

    def fullpathname(self):
        return self.entry.get()
    def name(self):
        if self.fullpathname().strip()=='':return ''
        else:return self.fullpathname().rsplit('\\',1)[1].rsplit('.')[0]
    

    def install(self):
        name = self.name()
        fullpathname = self.fullpathname()
        try:
            self.service_handle = CreateService( self.scm,
                                  name, #�����������ע����е�����    
                                  name, # ע������������ DisplayName ֵ    
                                  SERVICE_ALL_ACCESS, # ������������ķ���Ȩ��    
                                  SERVICE_KERNEL_DRIVER,# ��ʾ���صķ�������������    
                                  SERVICE_DEMAND_START, # ע������������ Start ֵ    
                                  SERVICE_ERROR_IGNORE, # ע������������ ErrorControl ֵ    
                                  fullpathname, # *****ע������������ ImagePath ֵ*****
                                  None,    
                                  0,    
                                  None,    
                                  None,    
                                  None)
            self.label['text'] = 'install ok'
        except:
            try:
                self.service_handle = OpenService(self.scm,name,SERVICE_ALL_ACCESS)
                self.label['text'] = 'install ok'
            except:
                self.service_handle = None
                self.label['text'] = 'install failed, pls check filepath'

    def starts(self):
        if self.service_handle != None:
            try:
                StartService(self.service_handle,None)
                self.label['text'] = 'starts ok'
            except:
                self.label['text'] = 'start failed, maybe it already start.'
        else:
            self.label['text'] = 'None service handle.'

    def stops(self):
        if self.service_handle != None:
            try:
                ControlService(self.service_handle,SERVICE_CONTROL_STOP)
                self.label['text'] = 'stops ok'
            except:
                self.label['text'] = 'stop failed, maybe it already stop.'
        else:
            self.label['text'] = 'None service handle.'
        
    def uninstall(self):
        if self.service_handle != None:
            try:
                DeleteService(self.service_handle)
                CloseServiceHandle(self.service_handle)
                self.service_handle = None
                self.label['text'] = 'uninstall ok'
            except:
                self.label['text'] = 'uninstall failed, maybe it already uninstall.'
        else:
            self.label['text'] = 'None service handle.'
        

if __name__ == '__main__':
    MyServiceInstaller()
    
    
