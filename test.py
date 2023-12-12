# script_path = r"D:\GuoHB\MyFiles\Code\PyAnsysWorkbench\examples\scripts"
# calcu_scripts_path = ["\systems_building.py","\mat_creation.py","\geo_import.py","\calcu_launch.py"
#            ,"\calcu_run.py"]
#
# calcu_scripts = [script_path+calcu_scripts_path[i] for i in range(len(calcu_scripts_path))]
# for script in calcu_scripts:
#     RunScript(FilePath=script)
from pathlib import Path
_workDir = Path(".") # 当前py文件所在位置
_wbjpFolder = _workDir / "software"
script_foder = _wbjpFolder / "scripts"
script_names = ["systems_building.py", "mat_creation.py", "geo_import.py", "calcu_launch.py", "calcu_run.py"]
scripts = [str((script_foder / name).absolute()) for name in script_names]

print(scripts)