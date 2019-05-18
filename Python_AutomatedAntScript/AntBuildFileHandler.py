import xml.sax
class AntBuildFileHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.sfname =''
        self.sfpkgdir =''
        self.sfpkgname=''
        self.listoftarget =[]
        self.CurrentData=''
        self.type =''
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "target":
            self.sfname = attributes["name"]
            self.listoftarget.append(self.sfname)
        if tag == "sf:retrieve" and self.sfname == 'retrieveUnpackaged':
            self.sfpkgdir = attributes["unpackaged"]
        if tag == "sf:retrieve" and self.sfname == 'retrievePkg':
            self.sfpkgname = attributes["packageNames"]


    def endElement(self, tag):
        if self.CurrentData == "sf:deploy":
            print("Type:", self.CurrentData)
        if self.CurrentData == "sf:retrieve":
            print("Type:", self.CurrentData)
   # def characters(self, content):
    #    if self.CurrentData == "sf:retrieve":
     #        print(content)