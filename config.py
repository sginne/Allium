conf = {}
def read_config(name='allium.cfg'):
    with open(name) as fp:
        for line in fp:
            if line.startswith('#'):
                continue
            if not line.strip():
                continue
            key, val = line.strip().split('=')
            if val[0]=="\"" and val[-1:]=="\"":
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
    with open(name,"w") as config_file:
        config_file.writelines(new_config)
def change_config(key,val,name='allium.cfg'):
    conf[key]=val
    write_config(key)

read_config()
import urwid
palette = [('palette', 'default,bold', 'default', 'bold'),]
div = urwid.Divider()

allium_title_ask = urwid.Edit(('palette', u"ALLIUM_TITLE: Short and precise, like MyShop\n"),edit_text=conf['ALLIUM_TITLE'])
allium_name_ask = urwid.Edit(('palette', u"ALLIUM_NAME: Addition to title, like \"Next day delivery!\"\n"),edit_text=conf['ALLIUM_NAME'])
allium_master_password_ask = urwid.Edit(('palette', u"MASTER_PASSWORD: VERY, EXTREMELY LONG STRING - No-one should be able to guess it. "),edit_text=conf['MASTER_PASSWORD'])
allium_ssl_ask = urwid.Edit(('palette', u"SSL_ENABLED: Darknet mode - disable SSL, Enabled for clearnet(/app/keys/*.crt & .key).  "),edit_text=conf['SSL_ENABLED'])
allium_port_ask = urwid.Edit(('palette', u"PORT: Port to serve flask on(80 for clearnet)"),edit_text=conf['PORT'])
allium_host_ask = urwid.Edit(('palette', u"HOST: Host to serve flask on(0.0.0.0 for all)"),edit_text=conf['HOST'])



exit_button = urwid.Button(u'Exit')
cancel_button = urwid.Button(u'Cancel')
revert_button = urwid.Button(u'Revert')

pile = urwid.Pile([allium_title_ask,allium_name_ask,allium_host_ask,allium_port_ask,allium_ssl_ask,allium_master_password_ask, div, exit_button,cancel_button])
top = urwid.Filler(pile, valign='top')


def on_exit_clicked(button):
    #change_config('ALLIUM_TITLE',allium_title_ask.get_text())
    change_config('ALLIUM_TITLE',conf['ALLIUM_TITLE'])
    change_config('ALLIUM_NAME',conf['ALLIUM_NAME'])
    change_config('MASTER_PASSWORD',conf['MASTER_PASSWORD'])
    change_config('SSL_ENABLED',conf['SSL_ENABLED'])
    change_config('PORT',conf['PORT'])
    change_config('HOST',conf['HOST'])


    raise urwid.ExitMainLoop()
def on_cancel_clicked(button):
    raise urwid.ExitMainLoop()
def on_revert_clicked(button):
    read_config()
urwid.connect_signal(exit_button, 'click', on_exit_clicked)
urwid.connect_signal(cancel_button, 'click', on_cancel_clicked)
urwid.connect_signal(revert_button, 'click', on_revert_clicked)

def on_title_change(edit,new_text):
    conf['ALLIUM_TITLE']=new_text
def on_name_change(edit,new_text):
    conf['ALLIUM_NAME']=new_text
def on_master_password_change(edit,new_text):
    conf['MASTER_PASSWORD']=new_text
def on_ssl_enable_change(edit,new_text):
    conf['SSL_ENABLED']=new_text
def on_port_change(edit,new_text):
    conf['PORT']=new_text
def on_host_change(edit,new_text):
    conf['HOST']=new_text
urwid.connect_signal(allium_title_ask, 'change', on_title_change)
urwid.connect_signal(allium_name_ask,'change',on_name_change)
urwid.connect_signal(allium_master_password_ask,'change',on_master_password_change)
urwid.connect_signal(allium_ssl_ask,'change',on_ssl_enable_change)
urwid.connect_signal(allium_port_ask,'change',on_port_change)

urwid.connect_signal(allium_host_ask,'change',on_host_change)


urwid.MainLoop(top, palette).run()