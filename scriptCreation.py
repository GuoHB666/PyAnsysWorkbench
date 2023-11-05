def rawScriptProcess(raw_script):
    # 分割字符串为行列表
    old_lines = raw_script.split('\n')[1:] # 将多行字符串按行分割，同时去除掉空行1
    # 计算开头制表符的数量
    nrof_space = len(old_lines[0]) - len(old_lines[0].lstrip())
    new_lines = [line[nrof_space:] for line in old_lines]
    # 重新拼接处理后的行
    new_strs = '\n'.join(new_lines)
    return new_strs


def scriptCreation(wbpj_path,setting=None):
    # 之后根据UI选项，将wbpj的保存路径融入到setting中
    material_script = r'''
    # 创建静结构分析流程
    # 获得Engineering Data数据容器
    engData = mechSys.GetContainer(ComponentName="Engineering Data")
    # 封装创建材料的方法
    def CreateMaterial(name, density, *elastic):
        mat = engData.CreateMaterial(Name=name)
        mat.CreateProperty(Name="Density").SetData(Variables=["Density"],
            Values=[["%s [kg m^-3]" % density]])
        elasticProp = mat.CreateProperty(Name="Elasticity", Behavior="Isotropic")
        elasticProp.SetData(Variables=["Young's Modulus"], Values=[["%s [MPa]" % elastic[0]]])
        elasticProp.SetData(Variables=["Poisson's Ratio"], Values=[["%s" % elastic[1]]])

    # 创建材料Steel，密度：7850kg/m3，杨氏模量：208e3MPa，泊松比：0.3
    CreateMaterial("Steel", 7850, 209.e3, 0.3)'''
    geo_script = r'''
    # Python Script, API Version = V18
    # 定义函数：通过坐标点选择面对象
    def GetFaceObjByPt(pt):
        for face in GetRootPart().GetDescendants[IDesignFace]():
            if face.Shape.ContainsPoint(pt): return face
    # 创建悬臂梁实体区域
    BlockBody.Create(Point.Origin, Point.Create(MM(200), MM(25), MM(20)))
    GetRootPart().SetName("Beam")
    # 选择beam实体，用于后续材料赋予
    Selection.Create(GetRootPart().Bodies).CreateAGroup("ns_beamBody")
    # 定义固定约束加载面并为其命名
    fixSupFace = GetFaceObjByPt(Point.Create(0, MM(12.5), MM(10)))
    Selection.Create(fixSupFace).CreateAGroup("ns_fixSup")
    # 定义压力载荷加载面并为其命名
    pressFace = GetFaceObjByPt(Point.Create(MM(50), MM(12.5), MM(20)))
    Selection.Create(pressFace).CreateAGroup("ns_press")
    '''
    mech_launch_script = r'''
    # 刷新Model Component数据
    modelComp = mechSys.GetComponent(Name="Model")
    modelComp.Refresh()
    # 获得Mechanical中Model的数据容器
    model = mechSys.GetContainer(ComponentName="Model")
    model.Edit(Hidden=True)
    '''
    mech_calcu_script = r'''
    # encoding: utf-8
    # 给定Named Selection名称获取子对象实例
    def GetLocByName(ns_name):
        for ns in Model.NamedSelections.Children:
            if ns.Name == ns_name: return ns
    # 指定材料
    matAss = Model.Materials.AddMaterialAssignment()
    matAss.Material = "Steel"
    matAss.Location = GetLocByName("ns_beamBody")
    # 划分网格
    mesh = Model.Mesh
    mesh.ElementSize = Quantity("10 [mm]")
    mesh.GenerateMesh()
    # 获得Analyses对象
    analysis = Model.Analyses[0]
    # 添加固定约束
    fixSup = analysis.AddFixedSupport()
    fixSup.Location= GetLocByName("ns_fixSup")
    # 加载压力载荷
    pressLoad = analysis.AddPressure()
    pressLoad.Location = GetLocByName("ns_press")
    pressLoad.Magnitude.Output.DiscreteValues = [Quantity("0.5 [MPa]")]
    Model.Solve()
    # 后处理操作
    solution = analysis.Solution
    misesResult = solution.AddEquivalentStress()
    misesResult.EvaluateAllResults()
    # 设置视角
    camera = ExtAPI.Graphics.Camera
    camera.UpVector = Vector3D(0,0,1)
    camera.SceneWidth = Quantity("150 [mm]")
    camera.SceneHeight = Quantity("120 [mm]")
    camera.FocalPoint = Point((0.08,0.0125,0), 'm')
    # 输出后处理云图
    misesResult.Activate()
    ExtAPI.Graphics.ExportImage("%s")''' % wbpj_path
    material_script = rawScriptProcess(material_script)
    geo_script = rawScriptProcess(geo_script)
    mech_launch_script = rawScriptProcess(mech_launch_script)
    mech_calcu_script = rawScriptProcess(mech_calcu_script)
    return geo_script, material_script, mech_launch_script, mech_calcu_script