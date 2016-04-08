import lz4f
import os
import sys
import tarfile

if sys.version_info.major >= 3:
    import builtins as __builtin__
    from .lz4lib import Lz4File
    from io import BytesIO as StringIO
else:
    import __builtin__
    from lz4lib import Lz4File
    from StringIO import StringIO

def compressDir(name, outname=None):
    """
    :type string: name   - the name of the dir to tar
    Generic compress method for creating .lz4r from a dir.
    """
    if not outname:
        outname = '.'.join([name.rstrip('/'), 'lz4r'])
    if not os.path.exists(name):
        print('Unable to locate the directory to compress.')
        return
    buff = StringIO()
    tarbuff = tarfile.open(fileobj=buff, mode='w')
    tarbuff.add(name)
    tarbuff.close()
    buff.seek(0)
    cCtx = lz4f.createCompContext()
    header = lz4f.compressBegin(cCtx)
    with __builtin__.open(outname, 'wb') as out:
        out.write(header)
        while True:
            decompData = buff.read((64*(1 << 10)))
            if not decompData:
                break
            compData = lz4f.compressUpdate(decompData, cCtx)
            out.write(compData)
        out.write(lz4f.compressEnd(cCtx))
        out.flush()
    lz4f.freeCompContext(cCtx)
    del tarbuff, buff

def decompressDir(name):
    """
    :type string: name      - name of dir to decompress
    Generic decompress method for a directory. Removes .lz4r to original file name
    for output.
    """
    tar_file = '.'.join(['tmp', 'tar'])
    infile = Lz4File.open(name)
    infile.decompress(tar_file)
    tar = tarfile.open(tar_file)
    tar.extractall()
    tar.close()
    os.remove(tar_file)
    
    
