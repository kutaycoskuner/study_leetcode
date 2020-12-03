def Main(): 
    try: 
        f = open("blah.txt","r")
        for line in f:
            print(line)
        f.close()
    except:
        print('the file either not found or unable to be read')    
    finally: # :: optional comes after exception
        # always do this
        print('exiting')

if __name__ == "__main__":
    Main()