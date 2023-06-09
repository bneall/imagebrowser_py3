#
# Conversion: Qt
#

def run(tp, size):

    from PySide2 import QtGui, QtCore

    QtImgReader = QtGui.QImageReader()
    qt_formats = [ f.data().decode().lower() for f in QtGui.QImageReader.supportedImageFormats()]
    QtImgReader.setFileName(tp.sourcePath)

    if QtImgReader.canRead() and tp.sourceExt.lower() in qt_formats:
        sourceImage = QtGui.QImage(tp.sourcePath)
        thumbImage = sourceImage.scaled(size, size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

        #Save out image file
        result = thumbImage.save(tp.thumbnailPath, str(tp.thumbnailExt), 75)
        if result:
            return True
        else:
            return False
    else:
        return False