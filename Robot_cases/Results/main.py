import config
import pyautogui as pya  # for screenshots
import time  # for count seconds for approx. measuring
import subprocess
import win32com.client
from win32gui import GetWindowText, GetForegroundWindow


def saplogin():
    try:
        # 1.1. Connect to SAP
        subprocess.check_call([config.SAP_EXE,
                               '-user=%s' % config.SAP_USER,
                               '-pw=%s' % config.SAP_PASS,
                               '-system=%s' % config.SAP_SID,
                               '-client=%s' % config.SAP_MANDANT])

        time.sleep(10)  # need to ensure SAP created a session

        # Get session
        sap_gui_auto = win32com.client.GetObject('SAPGUI').GetScriptingEngine
        session = sap_gui_auto.findById(
            "con[0]/ses[0]")  # 1 - to run the second session comment this line and uncomment the next, with con[1] and so on; probably it may work with a param stored in config
        # session = sap_gui_auto.findById("con[1]/ses[0]")  # 2
        # session = sap_gui_auto.findById("con[2]/ses[0]")  # 3
        # session = sap_gui_auto.findById("con[3]/ses[0]")  # 4

        # 1.2. Check if dialog window appears
        if session.children.count > 1:
            try:
                # 1.2.1 License window (this code was written for different PCs with the same ses[0];
                # to run this code on the same machine it shoild be modified by adding a check for ses[1] and so on)
                # Open new session if the title equals to <your title>
                if (GetWindowText(GetForegroundWindow())) == "<Информация по лицензии при многократной регистрации>":
                    print("Title: %s" % session.children(
                        1).text)  # you may use this instead of GetWindowText in the line above

                    # Choose an option to create additional session
                    try:
                        session.findById("wnd[1]/usr/radMULTI_LOGON_OPT2").select()
                        session.findById("wnd[1]/usr/radMULTI_LOGON_OPT2").setFocus()
                        session.findById("wnd[0]").sendVKey(0)

                    except Exception as ex:
                        print("Cannot perform an operation (%s)" % ex)
                        pya.screenshot(config.SCR_ERR)
                        exit(1)

                time.sleep(1)  # for case if new dialog window appears

                try:
                    # Now we are about to be logged. Often at this moment the system message is shown
                    if session.children(1).text == "<Системные сообщения>":  # replace to your text
                        print("Title: %s" % session.children(1).text)
                        # in my case this window always has two lines of text; you may safely delete these two lines of code
                        print("%s | %s" % (session.findById("wnd[1]/usr/lbl[4,1]").text,
                                           session.findById("wnd[1]/usr/lbl[17,1]").text))
                        print("%s | %s" % (session.findById("wnd[1]/usr/lbl[4,3]").text,
                                           session.findById("wnd[1]/usr/lbl[17,3]").text))

                        print("The window is closed '%s', please wait..." % session.children(1).text)
                        session.findById("wnd[1]").sendVKey(0)
                    else:
                        # Exit if the window has unknown title
                        print("Title: %s. Exit." % session.children(1).text)
                        pya.screenshot(config.SCR_ERR)
                        exit(1)

                except Exception as ex:
                    # Exit for unknown window
                    print("Unknown window: %s. Exit (%s)" % (session.children(1).text, ex))
                    pya.screenshot(config.SCR_ERR)
                    exit(1)

            except Exception as ex:
                # Finally, exit for unknown reason
                print("Unknown error: %s. Exit (%s)" % (session.children(1).text, ex))
                pya.screenshot(config.SCR_ERR)
                exit(1)

        print("Logged to SAP.")
        return session

    except Exception as ex:
        print("Error. Cannot create session. Exit (%s)" % ex)
        pya.screenshot(config.SCR_ERR)
        exit(1)


def export_npp(session, params):
    # 2.1. Start counter (for those who cares about statistics and measuring)
    start = time.time()

    if config.ICONIFY:
        # minimize main window
        session.findById("wnd[0]").iconify()
    else:
        # or resize it
        session.findById("wnd[0]").resizeWorkingPane(84, 40, 0)

    # 2.2. Open transation
    session.findById("wnd[0]/tbar[0]/okcd").text = 'transaction'
    session.findById("wnd[0]").sendVKey(0)

    """
    startx = time.time()
    'doing some repeatable stuff'
    finish = time.time()
    total_time = finish - startx
    print("Time %02d seconds added to dict" % total_time)
    """
    total_finish = time.time()
    total_time = total_finish - start
    print("Total: %02d seconds" % total_time)


# Begin, start session
ses = saplogin()

# Use params of session to use it in transaction 'export_npp' and so on
npp = export_npp(ses, params)