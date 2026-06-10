#!/usr/bin/env python3
import os
import sys

def check_env_vars():
    access_key_id = os.environ.get('ALIYUN_ACCESS_KEY_ID')
    access_key_secret = os.environ.get('ALIYUN_ACCESS_KEY_SECRET')
    region_id = os.environ.get('ALIYUN_REGION_ID', 'cn-hangzhou')

    print("\n=== 环境变量信息 ===")
    print(f"AccessKey ID: {access_key_id}")
    print(f"AccessKey Secret: {'*' * len(access_key_secret) if access_key_secret else None}")  # 安全起见打星号
    print(f"Region ID: {region_id}")

    if not access_key_id or not access_key_secret:
        print("ERROR: 缺少必要环境变量！请设置：\n"
              "export ALIYUN_ACCESS_KEY_ID='your_key_id'\n"
              "export ALIYUN_ACCESS_KEY_SECRET='your_secret'")
        return False
    return True

if __name__ == '__main__':
    try:
        if check_env_vars():
            print("所有必要环境变量已就绪")
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"发生异常: {e}")
        sys.exit(1)
