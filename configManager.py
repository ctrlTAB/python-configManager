import ast
import os

class config():
    path = "config"
    def listConfig(self):
        files = os.listdir(self.path)
        configs = []
        for file in files:
            file_len = len(file)
            cnf_end = 4
            cnf_pos = file_len - cnf_end
            if(file[cnf_pos:] == ".cnf"):
                configs.append(file[:cnf_pos])
        return configs
    def getConfigOf(self, name):
        try:
            file = open(self.path+"/"+name+".cnf","r")
            config = ast.literal_eval(file.read())
            file.close()
            return config
        except(Exception):
            print(Exception)
    def makeConfig(self, name, varname, varvalue):
        try:
            file = open(self.path+"/"+name+".cnf","w+")
            text = {varname:varvalue}
            file.write(str(text))
            file.close()
        except(Exception):
            print(Exception)
    def setVariable(self, name, varname, varvalue):
        try:
            config = self.getConfigOf(name)
            config[varname]=varvalue
            file = open(self.path+"/"+name+".cnf","w+")
            file.write(str(config))
            file.close()
        except(Exception):
            print(Exception)
    
