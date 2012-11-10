import ConfigParser


class iniFile:

    def __init__(self, fileName=''):
        self.fileName = ''
        if fileName != '':
            self.setFile(fileName)

    def setFile(self, fileName):
        self.fileName = fileName
        self.config = ConfigParser.SafeConfigParser(allow_no_value=True)

    def get(self, section, option):
        self.config.read(self.fileName)
        value = ""
        if self.config.has_option(section, option):
            value = self.config.get(section, option)
        return value

    def set(self, section, option, value):
        if not self.config.has_section(section):
            self.config.add_section('main')

        self.config.set(section, option, value)
        with open(self.fileName, 'w') as configfile:
            self.config.write(configfile)

    def getFilename(self):
        return self.fileName
