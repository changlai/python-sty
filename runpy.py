# -*- coding: utf-8 -*-

import sys

try:
    reload(sys).setdefaultencoding("UTF-8")
except:
    pass


filename = sys.argv[1]

with open(filename[:-3] + '.tex', "w") as fout:
    sys.stdout = fout
    with open(filename + '.err', "w") as ferr:
        with open(filename + '.rc', 'w') as frc:
            with open(filename) as f:
                try:
                    code = compile(f.read(), filename, 'exec')
                    exec(code, {'print': fout.write})
                    frc.write('0')
                except Exception as e:
                    frc.write('1')
                    import traceback
                    ferr.write(traceback.format_exc())
                    raise e
