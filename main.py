import sys
import os

def generate_rich_cpp(filename="huge_code.cpp", target_lines=2_000_000):
    
    header = [
        "#include <iostream>",
        "#include <vector>",
        "#include <string>",
        "#include <map>",
        "",
        "namespace DevEngine {",
        ""
    ]
    
    footer = [
        "}",
        "",
        "int main() {",
        '    std::cout << "Large C++ codebase loaded." << std::endl;',
        "    return 0;",
        "}"
    ]
    
    def block_0(i):
        return [
            f"    template<typename T> class Container_{i} {{",
            f"    T val; public:",
            f"    void set(T v) {{ val = v; }}",
            f"    T get() const {{ return val; }} }};"
        ]

    def block_1(i):
        return [
            f"    int calc_{i}(int a, int b) {{",
            f"        int r = a ^ b;",
            f"        if (r > {i % 100}) return r;",
            f"        return a + b + {i % 10}; }}"
        ]

    def block_2(i):
        return [
            f"    struct Meta_{i} {{ int id; float score; }};",
            f"    static Meta_{i} get_meta_{i}(int id) {{",
            f"        Meta_{i} m = {{ id, {i}.5f }};",
            f"        return m; }}"
        ]

    def block_3(i):
        return [
            f"    auto lambda_{i} = [](int x) {{ return x * x; }};",
            f"    using Vec_{i} = std::vector<int>;",
            f"    void process_{i}(Vec_{i}& v) {{",
            f"        if (!v.empty()) v.pop_back(); }}"
        ]

    blocks = [block_0, block_1, block_2, block_3]
    body_lines_needed = target_lines - len(header) - len(footer)
    
    # 每个 block 产生 4 行
    iterations = body_lines_needed // 4

    print(f"正在生成丰富的 C++ 代码: {filename}")
    print(f"目标行数: {target_lines}")

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(header) + "\n")
            for i in range(iterations // len(blocks)):
                for b_func in blocks:
                    idx = i * len(blocks) + blocks.index(b_func)
                    f.write("\n".join(b_func(idx)) + "\n")
            
            current_total = len(header) + ((iterations // 4) * 4 * 4)
            remaining = target_lines - current_total - len(footer)
            for i in range(remaining):
                f.write(f"    int _p_{i} = {i};\n")

            f.write("\n".join(footer) + "\n")
            
        file_size_mb = os.path.getsize(filename) / (1024 * 1024)
        print(f"生成成功！")
        print(f"实际行数: ", end="")
        sys.stdout.flush()
        os.system(f"wc -l {filename}")
        print(f"文件大小: {file_size_mb:.2f} MB")

        if file_size_mb > 95:
            print("\n警告: 文件大小接近或超过 100MB，GitHub 可能会拒绝上传。")

    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    generate_rich_cpp(target_lines=2_000_000)
