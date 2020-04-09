from redis import StrictRedis

if __name__ == '__main__':
    # 创建一个StrictRedis对象，与redsi服务器建立链接
    try:
        sr = StrictRedis()
        # 添加一个 key ,为name value Python
        res = sr.set("name","Python")
        print(res)
        # 修改name的值为 redis-Python
        res = sr.set("name","redis-Python")
        print(res)
        # 获取name的值
        res = sr.get("name")
        print(res)

        # 删除name及其对应的值
        res = sr.delete("name")
        print(res)

    except Exception as e:
        print(e)
