class CoWbUnitProcess(object):
    def simula_system_run(self):
        self._initialize()          # ! 和Ansys Workbench建立连接
        self._simula_sys_creat()    # ! 创建仿真系统
        self._mat_import()          # ! 创建材料
        self._geo_modeling()        # ! 创建几何
        self._simula_sys_cal()      # ! 开展模拟计算
        self.finalize()             # ! 项目退出