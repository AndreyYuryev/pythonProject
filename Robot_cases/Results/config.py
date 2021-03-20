import os  # for path join

SAP_SID = 'SID'
SAP_MANDANT = '1000'
SAP_USER = 'login'
SAP_PASS = 'secret'
SAP_EXE = "C:\Program Files (x86)\SAP\FrontEnd\SAPgui\sapshcut.exe"

# minimize SAP window, enable it after debugging is completed; unfortunately small windows still appear with this setting
ICONIFY = False

# screenshots for debug and visual logging
SCR_ERR = os.path.join('path', 'err_screen.png')