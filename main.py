# -*- coding: utf-8 -*-
from PyWbUnit import CoWbUnitProcess
import time


if __name__ == '__main__':
    init_time = time.time()
    end_time = time.time()
    # ! 创建Workbench模拟计算对象，并进行初始化
    start_time = end_time
    coWbUnit = CoWbUnitProcess()
    coWbUnit.initialize()
    # ! 创建仿真系统
    coWbUnit.simula_sys_creat()
    # ! 创建材料
    coWbUnit.mat_import()
    # ! 创建几何
    coWbUnit.geo_modeling()
    # # ! 开展模拟计算
    # coWbUnit.simula_sys_cal()
    # ! 项目退出
    coWbUnit.finalize()

    end_time = time.time()
    print("项目保存完成！其中：保存项目用时%.2f秒，总运行%.2f秒\n" % (end_time - start_time, end_time - init_time))

