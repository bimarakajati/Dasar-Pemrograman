g_onoff = False

def NyalakanTV():
    g_onoff = True
    return g_onoff
    
def main():
    print("Status TV:",NyalakanTV(True))
    print(g_onoff)

if __name__ == '__main__':
    main()
