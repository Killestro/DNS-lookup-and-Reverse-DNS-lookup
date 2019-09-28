import socket

while True:

    print('\n'*3,'-'*8,' DNS & Reverse DNS Lookup','-'*8)
    lookup = input("Lookup >> ")
    if lookup[0].isnumeric() == True :
        try :
            url = socket.gethostbyaddr(lookup)
            print('\n\n  IP Address: ',lookup,'\n  URL: ',url[0])
        except socket.error as error_msg :
            print(error_msg)
    else :
        try :
            IPv4 = socket.gethostbyname(lookup)
            url = socket.gethostbyaddr(IPv4)
            print('\n\n  URL: ',url[0],'\n  IP Address: ',IPv4)
        except socket.error as error_msg :
            print(error_msg)

