import xml.etree.ElementTree as ET
def get_mat_property(property_elem):
    property_type = property_elem.get("type")
    temperatures_elem = property_elem.find("T")
    tr_elem = property_elem.find("Tr")
    value_elem = property_elem.find("Value")
    tr_value = None
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
            property_data = [temperatures, elastic_modulus, poisson_ratio]
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
            property_data = [temperatures, values]
        else:
            property_data = float(values)

    if temperatures_elem is None:
        temperature_variables = []
    else:
        temperature_variables = ["Temperature"]

    if property_type == "Elasticity":
        property_variables = ["Young's Modulus", "Poisson's Ratio"]
    else:
        property_variables = [property_type]
    mat_variables = temperature_variables+property_variables
    return tr_value,mat_variables,property_type,property_data
def mat_generations(mat_xml):
    # 解析xml文件
    tree = ET.parse(mat_xml)
    root = tree.getroot()
    # 获取单位并做相应设置
    unit_elem = root.find("Unit")
    unit = unit_elem.text
    SetProjectUnitSystem(UnitSystemName=unit)
    # 创建材料系统
    template_mat = GetTemplate(TemplateName="EngData")
    system_mat = template_mat.CreateSystem()
    engineeringData = system_mat.GetContainer(ComponentName="Engineering Data")
    # 遍历材料元素
    for mat_elem in root.findall("Material"):
        mat_name = mat_elem.get("name")
        # 创建材料
        mat = engineeringData.CreateMaterial(Name=mat_name)
        # 材料遍历赋值
        for property_elem in mat_elem.findall("property"):
            tr_value, mat_variables, property_type, property_data = get_mat_property(property_elem)
            # 材料赋值
            if property_type == "Specific Heat":
                mat.CreateProperty(Name=property_type, Definition="Constant Pressure").SetData(
                    Variables=mat_variables, Values=property_data)
            elif property_type == "Coefficient of Thermal Expansion":
                thermalExpansionProp = mat.CreateProperty(Name=property_type, Definition="Secant", Behavior="Isotropic")
                thermalExpansionProp.SetData(SheetName="Coefficient of Thermal Expansion",
                                             Variables=mat_variables, Values=property_data)
                thermalExpansionProp.SetData(SheetName="Zero-Thermal-Strain Reference Temperature",
                                             Variables=["Zero-Thermal-Strain Reference Temperature"], Values=tr_value)
            else:
                mat.CreateProperty(Name=property_type, Behavior="Isotropic").SetData(
                    Variables=mat_variables, Values=property_data)

if __name__ == '__main__':
    mat_xml = "D:\GuoHB\MyFiles\Code\PyAnsysWorkbench\my_mats2.0.xml"
    mat_generations(mat_xml)