import re


def convert_vtt2txt(fpath, opath):
    print('Reading VTT')
    with open(fpath, 'r') as f:
        fullvtt = f.read()
    
    removal_re = [
            '<\d{2}:\d{2}:\d{2}.\d{3}>',
            '<c\.color.+>',
            '</?c>',
            'align:start position:\d+%',
            '\d{2}:\d{2}:\d{2}\.\d{3}',
            '::cue\(c\.color.+\) { color: rgb\(\d+,\d+,\d+\);',
            ' }',
            'Style:(\.*)?',
            'Kind: captions',
            '-->',
            '^\s*$',
            '^( +)?$'
            ]
    
    print('Substituting re')
    for regex in removal_re:
        fullvtt = re.sub(regex, '', fullvtt)
    
    print('Writing re sub output')
    with open(opath, 'w') as f:
        f.write(fullvtt)
    
    print('Removing empty line')
    out_lines = []
    with open(opath, 'r') as f:
        for line in f.readlines():
            if not re.match(r'^\s*$', line):
                out_lines.append(line)
    
    print('Removing duplicate lines')
    clineno = 0
    while clineno < len(out_lines) - 1:
        cline = out_lines[clineno].strip()
        nline = out_lines[clineno + 1].strip()
        if cline == nline:
            # check for same text
            del out_lines[clineno + 1]
        elif cline in nline:
            # check for current line is subset of next line
            del out_lines[clineno]
        elif nline in cline:
            # check for current line is subset of next line
            del out_lines[clineno + 1]
        else:
            clineno += 1
    
    print('Writing to txt')
    with open(opath, 'w') as f:
        for line in out_lines:
            f.write(line)
