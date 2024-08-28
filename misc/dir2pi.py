#!/usr/bin/python3
# Refactored from pip2pi <https://github.com/wolever/pip2pi>.

import os
import re
import shutil
try:
    from html import escape
except ImportError:
    from cgi import escape as _escape
    escape = lambda s: _escape(s, quote = True)

def safe_name(name):
    return re.sub("[^A-Za-z0-9.]+", "-", name)

def normalize_pep503(pkg_name):
    return re.sub(r"[-_.]+", "-", pkg_name).lower()

def file_to_package(file_name):
    file_name = os.path.basename(file_name)
    file_ext = os.path.splitext(file_name)[1].lower()
    assert file_ext != ".egg"
    split = re.search(r"(.*?)-(\d+.*)", file_name).groups()
    assert split[1]
    return (safe_name(split[0]), safe_name(split[1]))

def make_simple(pkgdir, simple):
    processed = {}
    for file_name in os.listdir(pkgdir):
        pkg_filepath = os.path.join(pkgdir, file_name)
        if not os.path.isfile(pkg_filepath):
            continue
        pkg_basename = os.path.basename(file_name)
        if pkg_basename.startswith("."):
            continue
        pkg_name, pkg_rest = file_to_package(pkg_basename)
        norm_name = normalize_pep503(pkg_name)
        dir_name = os.path.join(simple, norm_name)
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        symlink_target = os.path.join(dir_name, pkg_basename)
        symlink_source = os.path.join("../../", pkg_basename)
        os.symlink(symlink_source, symlink_target)
        if norm_name not in processed:
            processed[norm_name] = [pkg_name, dir_name]
        processed[norm_name].append(escape(pkg_basename))
    return processed

def make_index(simple, processed):
    pkg_index = ("<html><head><title>Simple Index</title>"
                 '<meta name="api-version" value="2" /></head><body>\n')
    for norm_name, pkg_info in sorted(processed.items()):
        pkg_index += '<a href="%s/">%s</a><br />\n' % (
            escape(norm_name), escape(pkg_info[0]),
        )
        for esc_basename in sorted(pkg_info[2:]):
            with open(os.path.join(pkg_info[1], "index.html"), "a") as fp:
                fp.write('<a href="%s">%s</a><br />\n' % (
                    esc_basename, esc_basename
                ))
    pkg_index += "</body></html>\n"
    with open(os.path.join(simple, "index.html"), "w") as fp:
        fp.write(pkg_index)

def dir2pi(pkgdir):
    assert os.path.isdir(pkgdir)
    simple = os.path.join(pkgdir, "simple")
    shutil.rmtree(simple, ignore_errors = True)
    os.mkdir(simple)
    processed = make_simple(pkgdir, simple)
    make_index(simple, processed)

if __name__ == "__main__":
    import sys
    assert len(sys.argv) == 2
    dir2pi(sys.argv[1])

