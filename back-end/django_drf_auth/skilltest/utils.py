import os
from datetime import datetime


def user_directory_path(instance, filename):
    #sessionSavedTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    session = instance.session_id
    sessionSplit = str(session).split(",")      #uploaded file is 'InMemoryUploadedFile' object, need to convert to string data type to use split function
    sessionId = sessionSplit[0].strip()
    #directory_path = 'sessionScreeningVideos/session_{}/{}'.format(sessionId,sessionSavedTime)
    directory_path = 'sessionScreeningVideos/session_{}/'.format(sessionId)
    return os.path.join(directory_path, filename)


def getObject(modelname):
    getObjectModel = modelname.objects
    return getObjectModel