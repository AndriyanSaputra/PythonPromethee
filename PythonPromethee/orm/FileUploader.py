import time
import os

def file_profile(instance, filename):
    ext = filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "%s.%s" % (str(milis), ext)
    return os.path.join('pekerja/profile', filename)


def file_pemilih(instance, filename):
    ext = filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "%s.%s" % (str(milis), ext)
    return os.path.join('pemilih/profile', filename)


def file_calon(instance, filename):
    ext = filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "%s.%s" % (str(milis), ext)
    return os.path.join('calon/profile', filename)

def file_calon2(instance, filename):
    ext = filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "%s.%s" % (str(milis), ext)
    return os.path.join('calon/profile', filename)