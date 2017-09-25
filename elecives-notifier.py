import requests

f = open('/home/string/Documents/susihtml.txt', 'r')
html = f.read()

params = {
    '__VSTATE'          : 'eJz7z8ifws%2fKZWhsamBhYWBgYsmfIsaUhkKIMDHyizHJsYdlFmcm5aRmpDAxA%2fnyDEAGKz%2b%2fGIscv0d%2bUWZVfl5JYo5jTmZ6HreWZnBlcUlqrl54apJeqCeIcgZKF%2bXnFOuhqWWSY4lXDHZiamgQAFoHtAlkFUtIakVJakoKEzvIfHlGbm0WJnkmFDXyzCB5TgLy3ATkeWEe4SegUBCmUJgfykoBAMHgO5k%3d',
    '__VIEWSTATE'       : '',
    '__EVENTVALIDATION' : '/wEWBAL+raDpAgKl1bKzCQK1qbSRCwLCi9reAwK9c0s7bLCB8tBILUhZIPSBMlGK',
    'txtUserName'       : 'akaloferov',
    'txtPassword'       : '9710134400',
    'btnSubmit'         : ''
    }

with requests.Session() as s:
    s.post('https://susi.uni-sofia.bg/ISSU/forms/Login.aspx', data=params)
    open_page = s.get('https://susi.uni-sofia.bg/ISSU/forms/students/ElectiveDisciplinesSubscribe.aspx')

    susi = open_page.text.encode('utf-8').strip()
    if html == susi:
        print "No change"
    else:
        print "Changed"
        # f.close()
        # l = open('/home/string/Documents/susihtml.txt', 'w')
        # l.write(susi)

    