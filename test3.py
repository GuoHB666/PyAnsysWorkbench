### 创建材料容器，并导入数据
template_mat = GetTemplate(TemplateName="EngData")
system1 = GetSystem(Name="SYS")
system2 = template_mat.CreateSystem(
    Position="Right",
    RelativeTo=system1)