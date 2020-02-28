conf = {}
def read_config(name='allium.cfg'):
    with open(name) as fp:
        for line in fp:
            if line.startswith('#'):
                continue
            if not line.strip():
                continue
            #print(line)
            key, val = line.strip().split('=')
            #val=val[:-1]
            #print(val)
            if val[0]=="\"" and val[-1:]=="\"":
                #print(val)
                val=val[1:-1]
                conf[key] = val
def write_config(key,name='allium.cfg'):

    with open(name,"r") as config_file:
        config=config_file.readlines()
    new_config=[]
    for line in config:
        if key in line:
            import re
            line=re.sub(r'".*"','"'+conf[key]+'"',line)
        new_config.append(line)
    #print(new_config)
    with open(name,"w") as config_file:
        config_file.writelines(new_config)
def change_config(key,val,name='allium.cfg'):
    conf[key]=val
    write_config(key)
read_config()
#change_config('ALLIUM_TITLE','ZumShop')
#print(conf['ALLIUM_TITLE'])
#write_config('ALLIUM_TITLE')
import urwid

palette = [('palette', 'default,bold', 'default', 'bold'),]
allium_title_ask = urwid.Edit(('palette', u"ALLIUM_TITLE\n"),edit_text=conf['ALLIUM_TITLE'])
exit_button = urwid.Button(u'Exit')
div = urwid.Divider()
pile = urwid.Pile([allium_title_ask, div, exit_button])
top = urwid.Filler(pile, valign='top')


def on_exit_clicked(button):
    raise urwid.ExitMainLoop()


#urwid.connect_signal(allium_title_ask, 'change', on_ask_change)
urwid.connect_signal(exit_button, 'click', on_exit_clicked)

urwid.MainLoop(top, palette).run()