def Shutdown() :
    return (" ...Shutdown...")
YN = input(" Do you want to shut down? Y/N ")
if YN == "Y" :
    print (" Checking for activities before shutting down... ")
    print (" Saving unsaved work... ")
    print (" Making sure all applications are closed... ")
    print (" Making sure battery is full... ")
    print (" Checking for system updates... ")
    print (" Shutting down... ")
    print (" Bye bye... ")
    print (" See you later, alligator... ")
    print ( Shutdown(), )
elif YN == "N" :
    print (" Aborting shutdown... ")
    print ( Shutdown(), "aborted... ") 
else :
    print (" Sorry... ")
    print (" Not understandable ... ")