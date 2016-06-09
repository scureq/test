import time
from selenium import webdriver

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/tmp')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

browser = webdriver.Firefox(profile)
pagenum = 46563
browser.get("http://ebuw.uw.edu.pl/Content/"+str(pagenum)+"/zip/")
#browser.get("http://ebuw.uw.edu.pl/dlibra/docmetadata?id="+str(pagenum))
#browser.find_element_by_link_text('Download').click()