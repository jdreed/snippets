from reportlab.platypus.flowables import HRFlowable

class SignatureLine(HRFlowable):
    """
    Draw a "signature" line on documents, with a hint/title
    below the line.
    """
    def __init__(self, *args, **kwargs):
        self.sig_title = kwargs.pop('title', '(signature)')
        self.font = kwargs.pop('font', ('Helvetica-Oblique', 10))
        # reportlab is still old-style classes
        HRFlowable.__init__(self, **kwargs)
    
    def draw(self):
        HRFlowable.draw(self)
        canv = self.canv
        canv.saveState()
        canv.setFont(*self.font)
        canv.setFillColor(self.color)
        # Move up by the font height plus half the linewidth, back down by 1
        canv.drawString(0, -1 * (self.font[1] + (self.lineWidth // 2) - 1),
                        self.sig_title)
        canv.restoreState()
