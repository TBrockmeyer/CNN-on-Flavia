import libarchive
 
for state in libarchive.pour('test.7z'):
    if state.pathname == 'dont/write/me':
        state.set_selected(False)
        continue
 
    # (The state evaluates to a filename.)
    print("Writing: %s" % (state))