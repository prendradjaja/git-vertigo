kinda like [vim-vertigo](https://github.com/prendradjaja/vim-vertigo)

not in any sort of stable state; use at your own peril

## Usage

```
$ git show AOEUIDHTNS_  # note the underscore at the end
 - AOEUIDHTNS_ -> 1234567890
fatal: ambiguous argument '1234567890': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'

$ git show OTDbETf_
 - OTDbETf_ -> 286b38f
commit 286b38f9ec54d015bfb6201e585829de6d69e719
Author: Pandu Rendradjaja
Date:   Tue Aug 29 02:19:19 2017 +0000

    init

diff --git a/README b/README
new file mode 100644
index 0000000..1333ed7
--- /dev/null
+++ b/README
@@ -0,0 +1 @@
+TODO
```

## Installation

clone to some directory

`alias git="INSTALL_DIR/wrapper.py"`
