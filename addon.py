import util, urllib2

def playVideo(params):
    response = urllib2.urlopen(params['video'])
    if response and response.getcode() == 200:
        content = response.read()
        videoLink = util.extract(content, '<L>', '</L>')
        util.playMedia(params['title'], params['image'], videoLink, 'video')
    else:
        util.showError(ADDON_ID, 'La URL demande %s peut pas etre accede afin de creer le menu !' % (params['video']))

def buildMenu():
    url = WEB_PAGE_BASE
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        videos = util.extractAll(content, '<START>', '</END>')
        for video in videos:
            params={'play':1}
            params['title'] = util.extract(video, '<T>', '</T>')
            params['image'] = util.extract(video, '<I>', '</I>')
            params['video'] = util.extract(video, '<L>', '</L>')
            link = params['video']
            util.addMenuItem(params['title'], link, 'DefaultVideo.png',params['image'], False)
        util.endListing()
    else:
        util.showError(ADDON_ID, 'La URL demande %s peut pas etre accede afin de creer le menu !' % (url))

WEB_PAGE_BASE = 'http://pastebin.com/raw.php?i=BfJ4DCqa'
ADDON_ID = 'plugin.program.alexis'

parameters = util.parseParameters()
if 'play' in parameters:
    playVideo(parameters['play'])
else:
    buildMenu()