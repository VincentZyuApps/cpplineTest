import sys
import os

def generate_mega_cpp(filename="huge_code.cpp", target_lines=2_000_000):
    # C++ 头文件和初始部分
    header = [
        "#include <iostream>",
        "#include <vector>",
        "#include <string>",
        "",
        "namespace LargeCodebase {",
        ""
    ]
    
    # 结尾部分
    footer = [
        "}",
        "",
        "int main() {",
        '    std.cout << "This is a 1 million line C++ file." << std.endl;',
        "    return 0;",
        "}"
    ]

    # 计算中间需要生成的行数
    # target_lines - 头部行数 - 尾部行数
    body_lines_needed = target_lines - len(header) - len(footer)
    
    print(f"正在生成 {filename}，目标行数：{target_lines}...")

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # 写入头部
            f.write("\n".join(header) + "\n")
            
            # 循环生成中间代码 (每 4 行为一个逻辑块，增加语法多样性)
            for i in range(body_lines_needed // 4):
                # 生成一些类定义、变量赋值等
                block = [
                    f"    struct DataStructure_{i} {{ int id; double value; }};",
                    f"    int calculate_val_{i}(int input) {{ return input * 2 + {i % 100}; }}",
                    f"    static int global_var_{i} = {i};",
                    f"    // 行标记: {i * 4 + 10}" # 注释也算语法行
                ]
                f.write("\n".join(block) + "\n")
            
            # 补齐剩余的行数（如果有余数）
            current_lines = len(header) + (body_lines_needed // 4) * 4
            for i in range(target_lines - current_lines - len(footer)):
                f.write(f"    int padding_var_{i} = 0;\n")

            # 写入尾部
            f.write("\n".join(footer) + "\n")
            
        print(f"成功！文件已生成: {os.path.abspath(filename)}")
        # 统计实际行数
        os.system(f"wc -l {filename}")

    except IOError as e:
        print(f"写入文件时出错: {e}")

if __name__ == "__main__":
    generate_mega_cpp()
