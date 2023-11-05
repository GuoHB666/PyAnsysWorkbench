import subprocess
import os
def geoCreation(geo_script, geo_name="geo.scdoc", geo_pyname="modelScript.py"):
    # 初始化几何模型及其py文件的名称
    geo_folder = os.path.abspath('.\Geometry')
    geoPyFile = os.path.join(geo_folder, geo_pyname)
    geo_file = os.path.join(geo_folder, geo_name)
    geoScript2 = """# 保存文件\noptions = ExportOptions.Create()\nDocumentSave.Execute(r"%s", options)""" % (geo_file)
    geo_script = geo_script + geoScript2

    # ! 创建生成几何模型的py文件
    with open(geoPyFile, 'w', encoding="utf-8") as f:
        f.write(geo_script)
    # ! 启动SpaceClaim
    scdmPath = r"D:\Program Files\ANSYS2021R2\v212\scdm"
    modifierCommand = r" /Headless=True /Splash=False /Welcome=False /ExitAfterScript=True"
    #geoCreateCmd = "SpaceClaim.exe /RunScript=" + geoPyFile + modifierCommand
    geoCreateCmd = 'SpaceClaim.exe /RunScript=D:\\GuoHB\\MyFiles\\Code\\PyAnsysWorkbench\\geometry\\modelScript.py /Headless=True /Splash=False /Welcome=False /ExitAfterScript=True'
    subprocess.run(geoCreateCmd, shell=True, cwd=scdmPath, stdout=subprocess.DEVNULL)
    return geo_file
# 'SpaceClaim.exe /RunScript=D:\\GuoHB\\MyFiles\\Code\\PyAnsysWorkbench\\geometry\\modelScript.py /Headless=True /Splash=False /Welcome=False /ExitAfterScript=True'
# 'D:\Program Files\ANSYS2021R2\v212\scdm\SpaceClaim.exe/RunScript=D:\\GuoHB\\MyFiles\\Code\\PyAnsysWorkbench\\geometry\\geo.py /Headless=True /Splash=False /Welcome=False /ExitAfterScript=True'