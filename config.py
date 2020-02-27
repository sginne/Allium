conf = {}
def read_config(name='allium.cfg'):
    with open(name) as fp:
        for line in fp:
            if line.startswith('#'):
                continue
            if not line.strip():
                continue

            key, val = line.strip().split('=')
            #val=val[:-1]
            #print(val)
            if val[0]=="\"" and val[-1:]=="\"":
                #print(val)
                val=val[1:-1]
                conf[key] = val
def write_config(key,name='allium.cfg'):
    import fileinput
    #print('here')
    for line in fileinput.input(name,inplace=True,backup='.bkp'):
        print (line)
        if key in line:
            print (line)
read_config()
#print(conf['ALLIUM_TITLE'])
write_config('ALLIUM_TITLE')