def simplify_path(path: str) -> str:
    stack = []

    for part in path.split('/'):
        if part == '' or part == '.':
            continue

        if part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return '/' + '/'.join(stack) if stack else '/'

if __name__ == "__main__":
    a = [
            "/home/",
            "/home//foo/",
            "/home/user/Documents/../Pictures",
            "/../",
            "/.../a/../b/c/../d/./"
        ]
    
    for i in a:
        print(i, "->", simplify_path(i))