# 🪐 Planet API 数据处理与 Flask 应用开发

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/RESTful_API-4479A1?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Score-30%2F30-brightgreen?style=for-the-badge" />
</p>

## 📝 项目背景
本项目是一个基于 **Flask** 框架开发的轻量级 Web 应用。系统通过对接外部 **Planets API** 获取行星原始数据，并利用后端 Python 逻辑进行高精度的二次换算与处理，为用户提供标准化的行星物理参数查询服务。

> **项目成果**：独立完成“开发-测试-部署”全流程，获课程评估 **30/30 满分**评价。

---

## ✨ 核心技术亮点

* **RESTful 接口设计**：设计并实现 `/radius` 等 3 个核心端点，使用 Python `requests` 库完成与外部 API 的高效对接，并统一处理了异构数据格式问题。
* **高精度数学建模**：借助 Python `math` 库，通过行星表面积反算半径等核心公式，将计算结果误差率严格控制在 **0.5% 以内**。
* **严谨的系统测试**：编写并执行了 10 余项接口测试用例，全面覆盖**参数异常**、**数据为空**及**边界值**等场景，保障了系统的健壮性。
* **云端生产部署**：项目已成功部署于 **PythonAnywhere** 平台，实测线上接口可访问率达到 **100%**。

---

## 🛠️ 目录结构说明
```text
.
├── app.py              # Flask 应用主入口，包含接口路由
├── logic.py            # 核心数学换算逻辑与 API 请求处理
├── requirements.txt    # 项目依赖清单
├── .gitignore          # 忽略非必要文件
└── README.md           # 项目文档
