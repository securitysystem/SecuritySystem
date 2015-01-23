##import requests
##response = requests.get('http://www.omnibean.weebly.com')
###print(response.text)
from html.parser import HTMLParser
##
class XMHParser(HTMLParser):
    recorda = False
    curval = ''
    tagid = ''
    def digest(self, elemID):
        self.tagid = elemID
    
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag==self.tagid:
            self.recorda = True
##        if tag == "a":
##           # Check the list of defined attributes.
##           for name, value in attrs:
##               # If href is defined, print it.
##               if name == "href":
##                   #print (name, "=", value)
##                   self.curval=value
    def handle_endtag(self, tag):
        if tag ==self.tagid:
            self.recorda = False
            #self.curval = ''
##        if tag=="a":
##            #print('End <a> tag')
##            pass
    def handle_data(self, data):
        if self.recorda==True:
            self.curval = data
            #print(data)
            #print(data,'=',self.curval)
        #print('Data:',data)
    def get_data(self):
        return self.curval


##parser = XMHParser()
##parser.feed(response.text)

class XDocument:
    def __init__(self, document_location):
        doc_loc = document_location
        self.location = doc_loc
        xdoc = open(self.location)
        self.docText = xdoc.read()
        xdoc.close()
    def getElement(self,elemN):
        self.parser = XMHParser()
        self.parser.digest(elemN)
        self.parser.feed(self.docText)
        return self.parser.get_data()
