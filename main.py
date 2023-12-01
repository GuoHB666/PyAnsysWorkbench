# -*- coding: utf-8 -*-
from PyWbUnit import CoWbUnitProcess

if __name__ == '__main__':
    coWbUnit = CoWbUnitProcess()
    coWbUnit.simula_system_run()


# 尝试能否直接运行py脚本：
'''
systems_building_script = r"D:/GuoHB/MyFiles/Code/PyAnsysWorkbench/scripts/systems_building.py"
mat_script = r"D:/GuoHB/MyFiles/Code/PyAnsysWorkbench/scripts/mat_creations.py"
RunScript(FilePath=systems_creations_script)
RunScript(FilePath=mat_script)
'''
