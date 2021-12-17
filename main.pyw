import tkinter
import webbrowser

version = '1.0'

def fakYe():
    while True:
        webbrowser.open('https://schoology.ytech.edu/login/ldap?&school=281446774')



def schoology():
    webbrowser.open('https://schoology.ytech.edu/login/ldap?&school=281446774')

def skyward():
    webbrowser.open('https://skyward.iscorp.com/YorkTechPAStuSTS')

def drive():
    webbrowser.open('https://accounts.google.com/ServiceLogin/webreauth?service=wise&passive=1209600&continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fmy-drive&followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fmy-drive&authuser=0&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

def nearpod():
    webbrowser.open('https://nearpod.com/')

def office():
    webbrowser.open('https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=637753449179190549.Mzc3MTRlMDgtOWE2My00YWM2LThhZGItZWM4OGE3MjNkMDU4ODBlYTZlY2EtMjI4Ni00MGExLWFlMmUtODNlZGM2ZmZhOWRj&ui_locales=en-US&mkt=en-US&client-request-id=339d0d6b-2cd4-4863-8847-b33211e25674&msafed=0&state=TaKabtFInR91iZHXc9VeDR8Uc9BVkwVS-EbEeSBJtI3pjv7psuHfvJbzcxx6XkUBVKum3rk_OXMvn3rH4bYmw1uAKRVAE4bUew04rhzUbuukhl5tOKk3LR4weB_fCEjldVCZdctRcqnnyTfhxvQqj-g5gqNOiMrRQKSk5jPJaYwXhaNGOmb2QDWrKrGRPwHizCbwYWc4mJwtEVLsUM3NoxMtrHpnUb2pw3oahw-lMSYkkPQl21a9cyvG8YJC0EzKKbMxBAEt4yXvWVuvRgZhApMpnD-p4rPQFR47mOxmErd6nmPxVi06jjgq28Qo2cXnQjOQPVMUBDUyLDOgZWUWSZg4LyrjWcaAtojLtHRQZqc&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.12.1.0')

window = tkinter.Tk()
window.title('Beta Version: ' + version)
window.geometry('500x500')

b1 = tkinter.Button(text='Schoology', command=fakYe, width=50)
b1.pack()

b2 = tkinter.Button(text='Skyward', command=skyward, width=50)
b2.pack()

b3 = tkinter.Button(text='Google Drive', command=drive, width=50)
b3.pack()

b4 = tkinter.Button(text='Nearpod', command=nearpod, width=50)
b4.pack()

b5 = tkinter.Button(text='Office 365', command=office, width=50)
b5.pack()

window.mainloop()
