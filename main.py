# -*- coding: utf-8 -*-
from PyWbUnit import CoWbUnitProcess
from geoCreation import geoCreation
from scriptCreation import scriptCreation
import time
from filesInit import filesInit


if __name__ == '__main__':
 #   wbpj_path = filesInit()
  #  geo_script, material_script, mech_launch_script, mech_calcu_script = scriptCreation(wbpj_path)
    init_time = time.time()
    print("******************** 几何模型创建中.... ********************")
    # ! 创建几何模型
 #   start_time = init_time
#    geoFile = geoCreation(geo_script)
    # geoFile = r"D:\GuoHB\MyFiles\Code\PyAnsysWorkbench\Geometry\geo.scdoc"
    end_time = time.time()
    #print("几何模型创建完成！其中：建模用时%.2f秒，当前已运行%.2f秒\n" % (end_time - start_time, end_time - init_time))

    print("******************** 仿真流程创建中... ********************")
    # ! 创建workbench对象，并以批处理方式启动workbench
    start_time = end_time
    coWbUnit = CoWbUnitProcess()
    coWbUnit.initialize()

    """
     end_time = time.time()
    print("1. 仿真初始化创建完成！其中：初始化用时%.2f秒，当前已运行%.2f秒\n" % (end_time - start_time, end_time - init_time))

    # ! 创建分析流程：即生成静力学分析模块
    start_time = end_time
    command = 'mechSys = GetTemplate(TemplateName="Static Structural", Solver="ANSYS").CreateSystem()'
    coWbUnit.execWbCommand(command)
    coWbUnit.execWbCommand('systems=GetAllSystems()')
    end_time = time.time()
    print("2. 静力学分析系统创建完成！其中：静力学分析系统创建用时%.2f秒，当前已运行%.2f秒\n" % (end_time - start_time, end_time - init_time))

    print("******************** 材料属性创建中... ********************")
    start_time = end_time
    # ! 创建材料
    coWbUnit.execWbCommand(material_script)
    end_time = time.time()
    print("材料属性创建完成！其中：材料属性创建用时%.2f秒，当前已运行%.2f秒\n" % (end_time - start_time, end_time - init_time))

    print("******************** 导入几何模型中... ********************")
    start_time = end_time
    # ! 创建几何
    coWbUnit.execWbCommand('geo=mechSys.GetContainer("Geometry")')
    coWbUnit.execWbCommand('geo.SetFile(FilePath="%s")' % geoFile)
    end_time = time.time()
    print("几何模型导入成功！其中：导入模型用时%.2f秒，当前已运行%.2f秒\n" % (end_time - start_time, end_time - init_time))
    print("******************** 开展静力学计算... ********************")
    start_time = end_time
    # ! 进行静力学分析：启动、前处理、求解、后处理、关闭
    coWbUnit.execWbCommand(mech_launch_script)
    coWbUnit.execWbCommand(f'model.SendCommand(Language="Python", Command={mech_calcu_script!r})')
    coWbUnit.execWbCommand('model.Exit()')
    end_time = time.time()
    print("静力学计算完成！其中：计算用时%.2f秒，当前已运行%.2f秒\n" % (end_time - start_time, end_time - init_time))
    print("******************** 项目保存并退出 ********************")
    start_time = end_time
    # ! 项目保存及退出
    #coWbUnit.saveProject(wbpj_path)
      
   """
    coWbUnit.finalize()
    end_time = time.time()
    print("项目保存完成！其中：保存项目用时%.2f秒，总运行%.2f秒\n" % (end_time - start_time, end_time - init_time))

