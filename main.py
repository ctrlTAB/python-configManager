import configManager

cnfM = configManager.config()
configs = cnfM.listConfig()

for config in configs:
    cnfM.setVariable(config,"cognome","ridolfi")
    cnf = cnfM.getConfigOf(config)
    print(cnf)
    cnfM.setVariable(config,"cognome","Ridolfi")
    cnf = cnfM.getConfigOf(config)
    print(cnf)
    
