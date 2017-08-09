from zope import interface

from sparc.file import ISparcUnicodeFile, ISparcUnicodeFileContent

class ISparcLogEntry(ISparcUnicodeFileContent):
    """A unique log entry"""

class ISparcLocatableLogEntry(ISparcLogEntry):
    """A locatable log entry"""
    

class ISparcUnicodeLogReader(ISparcUnicodeFile):
    """An append-only log file that can be truncated"""

class ISparcDatetimeOrderedLogReader(ISparcUnicodeLogReader):
    """An append-only log file whose entries are datetime ordered"""