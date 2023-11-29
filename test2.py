import xml.etree.ElementTree as ET





# 解析xml文件
tree = ET.parse("D:\GuoHB\MyFiles\Code\PyAnsysWorkbench\my_mats2.0.xml")
root = tree.getroot()
# 获取单位并做相应设置
unit_elem = root.find("Unit")
unit = unit_elem.text
unitSystem = SetProjectUnitSystem(UnitSystemName=unit)
# 创建材料系统
template_mat = GetTemplate(TemplateName="EngData")
system_mat = GetSystem(Name="SYS")
system_mat = template_mat.CreateSystem()
engineeringData = system_mat.GetContainer(ComponentName="Engineering Data")
# 遍历材料元素
for mat_elem in root.findall("Material"):
    mat_name = mat_elem.get("name")
    # 创建材料
    mat = engineeringData.CreateMaterial(Name=mat_name)
    # 材料遍历赋值
    for property_elem in mat_elem.findall("property"):
        property_type = property_elem.get("type")
        temperatures_elem = property_elem.find("T")
        tr_elem = property_elem.find("tr")
        value_elem = property_elem.find("Value")
        # 先检查是否是弹性模量参数，再决定获取值的方法
        if property_type == "Elasticity":
            elastic_modulus_elem = value_elem.find("ElasticModulus")  # 提取弹性模量
            poisson_ratio_elem = value_elem.find("PoissonRatio")  # 提取泊松比
            elastic_modulus = elastic_modulus_elem.text
            poisson_ratio = poisson_ratio_elem.text
            if temperatures_elem is not None:
                temperatures = list(map(float, temperatures_elem.text.split(',')))
                elastic_modulus = elastic_modulus.split(',')
                poisson_ratio = poisson_ratio.split(',')
                # 转化为数字列表
                elastic_modulus = list(map(float, elastic_modulus))
                poisson_ratio = list(map(float, poisson_ratio))
                property_data1 = [temperatures, elastic_modulus]
                property_data2 = [temperatures, poisson_ratio]
                property_data = [temperatures, elastic_modulus,poisson_ratio]
            else:
                elastic_modulus = float(elastic_modulus)
                poisson_ratio = float(poisson_ratio)
                property_data = [elastic_modulus, poisson_ratio]
        else:
            values = value_elem.text
            if tr_elem is not None:
                tr_value = tr_elem.text
            if temperatures_elem is not None:
                temperatures = list(map(float, temperatures_elem.text.split(',')))
                values = list(map(float, values.split(',')))
                property_data = [temperatures,values]
            else:
                property_data = float(values)

        if temperatures_elem is None:
            if property_type == "Density":
                mat.CreateProperty(Name="Density").SetData(Variables=["Density"],
                                                           Values=property_data)
            elif property_type == "Thermal Conductivity":
                mat.CreateProperty(Name="Thermal Conductivity",
                                   Behavior="Isotropic").SetData(Variables=["Thermal Conductivity"],
                                                                 Values=property_data)
            elif property_type == "Specific Heat":
                mat.CreateProperty(Name="Specific Heat",
                                   Definition="Constant Pressure").SetData(Variables=["Specific Heat"],
                                                                   Values=property_data)
            elif property_type == "Coefficient of Thermal Expansion":
                thermalExpansionProp = mat.CreateProperty(Name="Coefficient of Thermal Expansion", Definition="Secant",
                                                          Behavior="Isotropic")
                thermalExpansionProp.SetData(SheetName="Coefficient of Thermal Expansion",
                                             Variables=["Temperature", "Coefficient of Thermal Expansion"],
                                             Values=property_data)
                thermalExpansionProp.SetData(SheetName="Zero-Thermal-Strain Reference Temperature",
                                             Variables=["Zero-Thermal-Strain Reference Temperature"],
                                             Values=tr_value)
            elif property_type == "Viscosity":
                mat.CreateProperty(Name="Viscosity").SetData(Variables=["Viscosity"],
                                                                   Values=property_data)
            elif property_type == "Elasticity":
                mat.CreateProperty(Name="Elasticity",
                                   Behavior="Isotropic").SetData(Variables=["Young's Modulus", "Poisson's Ratio"],
                                                                 Values=property_data)
            else:
                pass
        else:
            if property_type == "Density":
                mat.CreateProperty(Name="Density").SetData(Variables=["Temperature","Density"],
                                                           Values=property_data)
            elif property_type == "Thermal Conductivity":
                mat.CreateProperty(Name="Thermal Conductivity",
                                   Behavior="Isotropic").SetData(Variables=["Temperature","Thermal Conductivity"],
                                                                 Values=property_data)
            elif property_type == "Specific Heat":
                mat.CreateProperty(Name="Specific Heat",
                                   Definition="Constant Pressure").SetData(Variables=["Temperature","Specific Heat"],
                                                                   Values=property_data)
            elif property_type == "Coefficient of Thermal Expansion":
                thermalExpansionProp = mat.CreateProperty(Name="Coefficient of Thermal Expansion",Definition="Secant",
                                   Behavior="Isotropic")
                thermalExpansionProp.SetData(SheetName="Coefficient of Thermal Expansion",
                                                                 Variables=["Temperature","Coefficient of Thermal Expansion"],
                                                                 Values=property_data)
                thermalExpansionProp.SetData(SheetName="Zero-Thermal-Strain Reference Temperature",
                                   Variables=["Zero-Thermal-Strain Reference Temperature"],
                                   Values=tr_value)
            elif property_type == "Viscosity":
                mat.CreateProperty(Name="Viscosity").SetData(Variables=["Temperature","Viscosity"],
                                                                   Values=property_data)
            elif property_type == "Elasticity":
                mat.CreateProperty(Name="Elasticity",
                                   Behavior="Isotropic").SetData(Variables=["Temperature","Young's Modulus", "Poisson's Ratio"],
                                                                 Values=property_data)
            else:
                pass



