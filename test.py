import xml.etree.ElementTree as ET

# 解析xml文件
tree = ET.parse("my_mats2.0.xml")
root = tree.getroot()

# 获取单位
unit_elem = root.find("Unit")
unit = unit_elem.text
print("Unit:", unit)

# 遍历材料元素
for mat_elem in root.findall("Material"):
    mat_name = mat_elem.get("name")
    print("Material:", mat_name)
    # 遍历属性元素
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
                property_data = [property_data1,property_data2]
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
        print("property_type: ", property_type)
        print("property_data: ", property_data)

        # 创建材料


        # if temperatures_elem is None:
        #     if property_type == "Density":



        # if temperatures_elem is not None:
        #     mat.CreateProperty(Name="Density").SetData(Variables=["Density"],
        #                                                Values=[["%s [kg m^-3]" % density]])



