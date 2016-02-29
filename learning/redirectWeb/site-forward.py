'''
Created on 2016年2月28日

@author: Calvin Wang
'''
"""
################################################################################
Create forward-link pages for relocating a web site.
Generates one page for every existing site html file; upload the generated
files to your old web site. See ftplib later in the book for ways to run
uploads in scripts either after or during page file creation.
################################################################################
"""

import os 

serverName = 'learning-python.com'
homeDir = 'books' 
siteFilesDir = r'C:\temp\public_html'
uploadDir = r'C:\temp\isp-forward'
templateName = 'template.html'

try:
    os.mkdir(uploadDir)
except OSError: pass

template = open(templateName).read()
siteFiles = os.listdir(siteFilesDir)  # filename, no directory prefix

count = 0
for file in siteFiles:
    if file.endswith('.html') or file.endswith('.htm'):
        fwdName = os.path.join(uploadDir,file)
        print('Creating',filename,' as ',fwdName)
        fileText = template.replace($server$,serverName)
        fileText = fileText.replace($home$,homeDir)
        fileText = fileText.replace($file$,file)
        open(fwdName,'w').write(fileText)
        count += 1
        
print('Last file =>\n',fileText,sep='')
print('Done: ',count,'forward files created.')