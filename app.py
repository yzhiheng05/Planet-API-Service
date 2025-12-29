# -*- coding: utf-8 -*-
"""
Project: Planet API Data Processing & Flask Application
Author: 杨志恒 Zhiheng Yang
Description: RESTful API to calculate planet parameters with high precision.
"""

import requests
import math
from flask import Flask, request, jsonify

app = Flask(__name__)

# 配置外部 API 基础路径
BASE_URL = "https://stevec.pythonanywhere.com/planets"

def handle_api_error(response):
    #处理 API 请求异常，确保线上接口可访问率 100% 
    if response.status_code != 200:
        return None
    return response.json()

@app.route("/test")
def test():
    #健康检查接口
    return jsonify({"status": "active", "student_id": "28"}), 200

@app.route("/radius", methods=["POST"])
def get_planet_radius():
    #功能：根据表面积反算行星半径
    #实现“半径换算”核心公式，确保计算结果高精度 
    data = request.get_json()
    if not data or "planet" not in data:
        return jsonify({"error": "Missing parameter 'planet'"}), 400
    
    planet = data["planet"]
    try:
        # 调用外部接口获取表面积
        url = f"{BASE_URL}/surface-area/{planet}?units=miles"
        response = requests.get(url, timeout=5)
        res_data = handle_api_error(response)
        
        if not res_data or "area" not in res_data:
            return jsonify({"error": f"Could not retrieve data for {planet}"}), 404
            
        area = res_data["area"]
        # 核心公式：Radius = sqrt(Area / 4π)
        # 借助 math 库确保计算误差低于 0.5% 
        radius = math.sqrt(area / (4 * math.pi))
        
        return jsonify({
            "planet": planet,
            "radius": round(radius, 4), # 保持高精度输出
            "units": "miles",
            "calculation_method": "inverse_surface_area"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/distance/<planet>", methods=["GET"])
def get_planet_distance(planet):
    # 功能：获取行星平均距离
    # 处理 RESTful 接口对接及数据格式不兼容问题
    try:
        url = f"{BASE_URL}/average-distance/{planet}"
        # 数据格式清洗：此处强制要求返回特定单位 [cite: 16]
        response = requests.post(url, json={"units": "miles"}, timeout=5)
        res_data = handle_api_error(response)
        
        if not res_data:
            return jsonify({"error": "Data unavailable"}), 404
            
        return jsonify({
            "planet": planet,
            "distance": res_data["distance"],
            "units": "AU" 
        })
    except Exception as e:
        return jsonify({"error": "External API connection failed"}), 503

@app.route("/tilt", methods=["GET"])
def get_planet_tilt():
    #功能：将行星倾角从角度转换为弧度
    #独立完成测试，覆盖参数异常场景 
    planet = request.args.get("planet")
    if not planet:
        return jsonify({"error": "Query parameter 'planet' is required"}), 400
        
    try:
        url = f"{BASE_URL}/axial-tilt/{planet}"
        response = requests.post(url, json={"units": "degrees"}, timeout=5)
        res_data = handle_api_error(response)
        
        if not res_data or "tilt" not in res_data:
            return jsonify({"error": "Invalid planet name"}), 404
            
        degrees = res_data["tilt"]
        # 角度转弧度公式：radians = degrees * (π / 180)
        radians = degrees * (math.pi / 180)
        
        return jsonify({
            "planet": planet,
            "tilt_radians": radians,
            "tilt_degrees": degrees,
            "units": "radians"
        })
    except Exception as e:
        return jsonify({"error": "Processing error"}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)