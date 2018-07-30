import os

import re

 

class Finder:

 

    matches = []

 

    def __init__(self, type = None, path = '/', caseIns = False):

        self.type = type

        self.path = path

        self.caseIns = caseIns

 

    def __list(self):

        for wPath in os.walk(self.path):

            yield wPath

 

    def __listFolders(self):

        for basepath, dirs, files in self.__list():

            for name in dirs:

                yield os.path.join(basepath, name)

 

    def __listFiles(self):

        for basepath, dirs, files in self.__list():

            for name in files:

                yield os.path.join(basepath, name)

 

    def __find(self, generator, regex):

        if regex:

            flag = 0

            if self.caseIns:

                flag = re.IGNORECASE

            for path in generator:

                if re.search(r'' + self.needle, path, flag):

                    self.matches.append(path)

        else:

            if (self.caseIns):

                for path in generator:

                    temppath = path.lower()

                    if temppath.endswith(self.needle.lower()):

                        self.matches.append(path)

            else:

                for path in generator:

                    if path.endswith(self.needle):

                        self.matches.append(path)

 

    def find(self, needle, regex = False):

        if self.type == None:

            raise Exception("Debes especificar un tipo de archivo a buscar")

        print ("Buscando........ ")

        try:

            self.needle = needle

            if self.type.upper() == 'FOLDER':

                self.__find(self.__listFolders(), regex)

            elif self.type.upper() == 'FILE':

                self.__find(self.__listFiles(), regex)

        except KeyboardInterrupt:

            return self

        return self

 

    def showAll(self):

        if len(self.matches) > 0:

            matches = lambda: [(yield num, match) for num, match in enumerate(self.matches)]

            print("Coincidencias: %s" % len(self.matches))

            for num, match in matches():

                print("[%d] - '%s'" % (num, match))

        else:

            print("No se encontraron coincidencias")

 

    def show(self, option):

        if len(self.matches) > 0:

            pathOrFile = self.matches[option]

            line = "-" * 150

            if os.path.isdir(pathOrFile):

                content = [os.path.relpath(content) for content in os.listdir(pathOrFile)]

                print("\n-> %d archivos en el directorio seleccionado '%s'\n-> Mostrando el contenido:\n" % (len(content), pathOrFile))

                print ("%s\n" % "\n".join(content))

            elif os.path.isfile(pathOrFile):

                print("\nMostrando contenido del archivo '%s':\n" % pathOrFile)

                print(line)

                with open(pathOrFile, 'r') as file:

                    print file.read()

                print(line)

                print("\nFin de archivo")

        else:

            print("No se encontraron coincidencias")