def VerifyPlayStore():
    pass

def VerifyKey():
    pass

def AllowedFile(filename):
    ALLOWED_EXTENSIONS = set(['sh', 'SH', 'png', 'PNG'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS