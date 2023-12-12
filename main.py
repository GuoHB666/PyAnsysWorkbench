# -*- coding: utf-8 -*-
from PyWbUnit import CoWbUnitProcess

if __name__ == '__main__':
    coWbUnit = CoWbUnitProcess()
    coWbUnit.simula_system_run()

#
# # 尝试能否直接运行py脚本：
# '''
# systems_building_script = r"D:/GuoHB/MyFiles/Code/PyAnsysWorkbench/scripts/systems_building.py"
# mat_script = r"D:/GuoHB/MyFiles/Code/PyAnsysWorkbench/scripts/mat_creations.py"
# RunScript(FilePath=systems_creations_script)
# RunScript(FilePath=mat_script)
# '''
# script_path = r"D:\GuoHB\MyFiles\Code\PyAnsysWorkbench\software\scripts\example"
# systems_building_script = script_path + "\systems_building _structural.py"
# material_script = script_path + "\material_creation.py"
# geo_script = script_path + "\geo_creation.py"
#
# RunScript(FilePath=systems_building_script)
# RunScript(FilePath=material_script)
# RunScript(FilePath=geo_script)
