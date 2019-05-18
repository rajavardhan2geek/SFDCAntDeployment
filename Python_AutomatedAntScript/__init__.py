import os
import subprocess
import re
import xml.sax
import AutomateDeployment.AntBuildFileHandler as xmlantparser

def __init__():
    path =input('Enter path to build file and package xml')
    os.chdir(path)
    print(' build file prsent in ',path)
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # override the default ContextHandler
    Handler = xmlantparser.AntBuildFileHandler()
    parser.setContentHandler(Handler)
    parser.parse(".//build.xml")
    index=0;
    for targetname in Handler.listoftarget:
            print('{} . {}'.format(index,targetname))
            index+=1
    print('\n unpackaged dir name',Handler.sfpkgdir)
    print(' \n package name',Handler.sfpkgname)
    sfcommand = input('Enter Salesforce Command to retrieve or deploy from above list')
    cmd ='ant '+sfcommand
    print(subprocess.call(cmd,shell=True))
    #buildfile =open('.\\build.xml','r')
    #for line in buildfile.readlines():
    #    print(line)

__init__()
