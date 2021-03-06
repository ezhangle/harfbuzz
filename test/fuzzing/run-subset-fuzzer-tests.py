#!/usr/bin/env python

from __future__ import print_function
import sys, os, subprocess

srcdir = os.environ.get ("srcdir", ".")
EXEEXT = os.environ.get ("EXEEXT", "")
top_builddir = os.environ.get ("top_builddir", ".")
hb_subset_fuzzer = os.path.join (top_builddir, "hb-subset-fuzzer" + EXEEXT)

if not os.path.exists (hb_subset_fuzzer):
        if len (sys.argv) == 1 or not os.path.exists (sys.argv[1]):
                print ("""Failed to find hb-subset-fuzzer binary automatically,
please provide it as the first argument to the tool""")
                sys.exit (1)

        hb_subset_fuzzer = sys.argv[1]

print ('hb_subset_fuzzer:', hb_subset_fuzzer)
fails = 0

parent_path = os.path.join (srcdir, "..", "subset", "data", "fonts")
print ("running subset fuzzer against fonts in %s" % parent_path)
for file in os.listdir (parent_path):
        path = os.path.join(parent_path, file)
        print ("running subset fuzzer against %s" % path)
        p = subprocess.Popen ([hb_subset_fuzzer, path])

        if p.wait () != 0:
                print ("failed for %s" % path)
                fails = fails + 1

if fails:
        print ("%i subset fuzzer related tests failed." % fails)
        sys.exit (1)
