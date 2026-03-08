"""Scan all markdown frontmatter for broken single-quoted YAML values."""
import glob, re, os

content_dir = r'C:\Users\AmitKohli\Dropbox\My Projects\amitkohli.com\content'
files = glob.glob(content_dir + '/**/*.md', recursive=True)

broken = []
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not m:
        continue
    yaml_block = m.group(1)
    lines = yaml_block.split('\n')
    # Check single-quoted multiline YAML: starts with `key: '` and check for internal unescaped apostrophes
    in_single_quoted = False
    single_quoted_content = ''
    single_quoted_line = ''
    for line in lines:
        if not in_single_quoted:
            # Start of a single-quoted value?
            vm = re.match(r"^[\w_-]+:\s*'(.*)$", line)
            if vm:
                inner = vm.group(1)
                # Does it end with ' on the same line?
                if inner.endswith("'"):
                    # Single-line single-quoted - check for internal apostrophe
                    inner_content = inner[:-1]
                    if "'" in inner_content.replace("''", ''):
                        broken.append((os.path.relpath(fpath, content_dir), line.strip(), 'single-line'))
                else:
                    # Multiline - accumulate
                    in_single_quoted = True
                    single_quoted_content = inner
                    single_quoted_line = line
        else:
            # Continuation of multiline single-quoted
            stripped = line.strip()
            if stripped.endswith("'"):
                # End of multiline single-quoted
                all_content = single_quoted_content + ' ' + stripped[:-1]
                if "'" in all_content.replace("''", ''):
                    broken.append((os.path.relpath(fpath, content_dir), single_quoted_line.strip(), 'multiline'))
                in_single_quoted = False
                single_quoted_content = ''
            else:
                single_quoted_content += ' ' + stripped

print(f'Potentially broken YAML single-quoted values with apostrophes: {len(broken)}')
for f, line, kind in broken:
    print(f'  [{kind}] {f}')
    print(f'    {line[:140]}')
