import sqlite3
import os
import pdb

DEBUG = True

def DebugPrint(string):
  if DEBUG:
    print string

Columns = {'Title' : 'c00',
           'Year' : 'c07',
           'FilePath' : 'c22'}
CollIndexes = {}

class BddColumns:
  def __init__(self, name, bddColumnName):
    self.Name = name
    self.BddColumn = bddColumnName

class BddDecriptor:
  def __init__(

class BddTools :
  def __init__(self, bddFile) :
    self.bddFile = bddFile

  def ExecuteRequest(self, request) :
    connection = sqlite3.connect(self.bddFile)
    cursor = connection.cursor()
    cursor.execute(request)
    for row in cursor.fetchall():
      yield row


def CreateRequest(table, columns) :

  request = ''
  for idx in range(len(columns)) :
    # save in use columns indexes
    CollIndexes[columns[idx]] = idx
    if len(request) != 0 :
      request += ', '
    request += Columns[columns[idx]]

  request = 'SELECT ' + request + ' FROM ' + table
  return request

class XbmcFilm:
  Title = ''
  OriginalTitle = ''
  Year = ''
  DbPath = ''
  Files = ''

  def __init__(self, row):
    pdb.set_trace()
    self.Title = row[0]
    self.Year = row[1]
    self.OriginalTitle= row[2]
    self.DbPath = row[3]
    self.GetFileNames()
    
  def __repr__(self):
    return """Titre : {0}
Annee : {1}
Titre Original : {2}
Chemin (DB) : {3}
Chemins : {4}""".format(self.Title, self.Year, self.OriginalTitle, self.DbPath, self.Files)

  def GetContainingFolder(self):
    return ''

  def GetNormalizedFolder(self):
    return self.Title + ' - ' + self.Year



  # return list of filepath if element is a stack return separates file names
  def GetFileNames(self):
    pdb.set_trace()
    if self.DbPath[:5] == 'stack' :
      DebugPrint( self.Title + ' is a stack')
      filenames = self.DbPath[8:].split(' , ')
      self.Files = filenames
    else:
      DebugPrint(  self.Title + ' is NOT a stack')
      self.Files = self.DbPath

def MoveFiles(fileList):
  for file in fileList:
    return

def main():
  bdd = BddTools('/home/atohmic/.xbmc/userdata/Database/MyVideos60.db')
  film = []
  req = CreateRequest('movie', ['Title', 'Year', 'FilePath'])
  DebugPrint(req)
  for row in bdd.ExecuteRequest(req):
    film.append(XbmcFilm(row))
  DebugPrint(film)
    
    
  
  
  
  
  
  
  DebugPrint( '')

main()
