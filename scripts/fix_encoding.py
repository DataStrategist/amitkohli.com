import glob, os

content_dir = r'C:\Users\AmitKohli\Dropbox\My Projects\amitkohli.com\content'
files = glob.glob(content_dir + '/**/*.md', recursive=True)

# Replace all problematic Unicode typographic chars with plain ASCII equivalents
# Key: UTF-8 bytes of the Unicode char, Value: plain ASCII replacement bytes
bad_sequences = [
    (b'\xe2\x80\x98', b"'"),    # U+2018 left single quote -> '
    (b'\xe2\x80\x99', b"'"),    # U+2019 right single quote -> '
    (b'\xe2\x80\x9a', b"'"),    # U+201A single low-9 quote -> '
    (b'\xe2\x80\x9b', b"'"),    # U+201B single high-9 quote -> '
    (b'\xe2\x80\x9c', b'"'),    # U+201C left double quote -> "
    (b'\xe2\x80\x9d', b'"'),    # U+201D right double quote -> "
    (b'\xe2\x80\x9e', b'"'),    # U+201E double low-9 quote -> "
    (b'\xe2\x80\x9f', b'"'),    # U+201F double high-9 quote -> "
    (b'\xe2\x80\x93', b'-'),    # U+2013 en dash -> -
    (b'\xe2\x80\x94', b'-'),    # U+2014 em dash -> -
    (b'\xe2\x80\x95', b'-'),    # U+2015 horizontal bar -> -
    (b'\xe2\x80\xa6', b'...'),  # U+2026 ellipsis -> ...
    (b'\xc2\xa0', b' '),        # U+00A0 non-breaking space -> space
    (b'\xc2\xad', b''),         # U+00AD soft hyphen -> nothing
    (b'\xc2\xab', b'"'),        # U+00AB left angle quote -> "
    (b'\xc2\xbb', b'"'),        # U+00BB right angle quote -> "
    (b'\xc2\xae', b'(R)'),      # U+00AE registered -> (R)
    (b'\xc2\xa9', b'(C)'),      # U+00A9 copyright -> (C)
    (b'\xe2\x84\xa2', b'(TM)'), # U+2122 trademark -> (TM)
    (b'\xe2\x80\x8b', b''),     # U+200B zero-width space -> nothing
    (b'\xef\xbb\xbf', b''),     # UTF-8 BOM -> nothing
]

total_fixes = 0
fixed_files = []

for fpath in files:
    with open(fpath, 'rb') as f:
        raw = f.read()
    
    fixed = raw
    file_changes = 0
    for bad_bytes, replacement in bad_sequences:
        count = fixed.count(bad_bytes)
        if count:
            fixed = fixed.replace(bad_bytes, replacement)
            file_changes += count
    
    if file_changes > 0:
        with open(fpath, 'wb') as f:
            f.write(fixed)
        total_fixes += file_changes
        fixed_files.append((os.path.relpath(fpath, content_dir), file_changes))

if fixed_files:
    print(f'Fixed {total_fixes} sequences across {len(fixed_files)} files:')
    for fname, n in fixed_files:
        print(f'  {fname}: {n}')
else:
    print('All files already clean.')
