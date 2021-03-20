# Importing the Libraries
import win32com.client
import sys
import subprocess
import time


# This function will Login to SAP from the SAP Logon window

def saplogin():

    try:

        #subprocess.check_call(
        #    ['C:\Program Files (x86)\SAP\FrontEnd\SAPgui\\sapshcut.exe', '-system=XPL', '-client=200',
        #     '-user=USERNAME', '-pw=PASSWORD'])

        path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        subprocess.Popen(path)
        time.sleep(10)


        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        if not type(SapGuiAuto) == win32com.client.CDispatch:
            return

        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
            return

        connection = application.Children(0)
        if not type(connection) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
            return

        session = connection.Children(1)
        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return

        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = "USER"
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "PASS"
        session.findById("wnd[0]").sendVKey(0)

    except:
        print(sys.exc_info()[0])

    finally:
        session = None
        connection = None
        application = None
        SapGuiAuto = None


saplogin()

