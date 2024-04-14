# 获取当前脚本文件的绝对路径
SCRIPT=$(readlink -f "$0")

# 获取当前脚本文件所在的目录
SCRIPT_DIR=$(dirname "$SCRIPT")

echo "当前脚本文件所在的目录是：$SCRIPT_DIR"

# 切换到根目录
project_dir="$SCRIPT_DIR/.."

# 删除旧的解释器
rm -rf dist
rm -rf venv

# 执行编译命令
cd "$project_dir/Python-3.11.7" && ./configure  --prefix="$project_dir/dist" && make -j install

# 创建新的虚拟环境
cd $project_dir && ./dist/bin/python3 -m venv venv && source venv/bin/activate 