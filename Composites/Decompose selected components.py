g = CurrentGlyph()
n = 0

g.prepareUndo('Decompose selected components')
for c in g.components:
    if c.selected == True:
        c.decompose()
        n = n+1
        print "Decomposing component " + str(c.baseGlyph)
        
if n == 0:
    print 'No components were selected / decomposed.'
g.performUndo()
g.update()    
