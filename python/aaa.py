import os
from send2trash import send2trash


def delete_files_containing_text(root_path, target_text):
    """
    递归删除指定路径下所有文件名包含目标文本的文件（移动到废纸篓）

    参数:
        root_path: 要清理的根目录路径
        target_text: 文件名需要包含的文本
    """
    deleted_count = 0
    error_count = 0

    # 遍历目录及其所有子目录[1](@ref)
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # 检查文件名是否包含目标文本[6](@ref)
            if target_text in file:
                file_path = os.path.join(root, file)
                try:
                    # 使用send2trash安全删除文件[4](@ref)
                    send2trash(file_path)
                    print(f"✅ 已移到废纸篓: {file_path}")
                    deleted_count += 1
                except Exception as e:
                    print(f"❌ 删除失败 {file_path}: {e}")
                    error_count += 1

    print(f"\n处理完成! 共删除 {deleted_count} 个文件, 失败 {error_count} 个.")


if __name__ == "__main__":
    target_path = "/Volumes/ST4000VX/albums"
    keyword = "桔钓沙-2"

    # 检查路径是否存在[3](@ref)
    if not os.path.exists(target_path):
        print(f"❌ 错误: 路径 '{target_path}' 不存在")
    else:
        # 确认操作
        confirm = input(
            f"将删除路径下所有包含 '{keyword}' 的文件。确认执行? (输入 'yes' 继续): "
        )
        if confirm.lower() == "yes":
            delete_files_containing_text(target_path, keyword)
            print("💡 提示: 所有删除的文件可在废纸篓中恢复")
        else:
            print("操作已取消")
