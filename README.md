Repository moved
================

__This repository has been moved to https://gitlab.gnome.org/Community/gentoo/gtk-update-icon-cache and this one here is not updated anymore.__


General Information
===================

gtk-update-icon-cache is a tool from GTK+ to update icons and themes caches.

It is split from the GTK+ sources by the Gentoo Gnome team to help GTK+ 2 and 3
to co-exist better by extracting the single conflicting tool.

Official sources of this tool are located at:

    https://github.com/GNOME/gtk/blob/master/gtk/updateiconcache.c

Installation
============

gtk-update-icon-cache requires GLib >= 2.45 and gdk-pixbuf >= 2.30.

See the file 'INSTALL' for more detailed information.

Updating
========

* Clone gtk+ repository: `git clone git://git.gnome.org/gtk+`.
* Checkout the sources of gtk+ at the required version.
* Synchronize dependencies to glib and gdk-pixbuf, even if not strictly needed.
* Copy `gtkiconcachevalidator.c`, `gtkiconcachevalidator.h` and
  `updateiconcache.c` to the `gtk/` folder.
* Copy `docs/reference/gtk/gtk-update-icon-cache.xml` to `docs/`.
* Copy the locales from gtk+ `po/` directory to gtk-update-icon-cache `po/`
  directory and remove unneeded translation using the script
  `utils/extract-po.py`:

    $ for po in ../gtk+/po/*.po ; do \
        utils/extract-po.py ${po} ./po/$(basename ${po}; \
      done
* Compare and update po/LINGUAS if needed. If a language has been removed, remove
  the corresponding *.po file in addition to the LINGUAS entry.

Finally do a release using `make distcheck`.

How to report bugs
==================

Bugs should be reported to the Gentoo bug tracking system
(http://bugs.gentoo.org, product Gentoo Linux, component Current packages).
You will need to create an account for yourself.

In the bug report, please include:

* Information about your system. For instance:

   - What version of gtk-update-icon-cache
   - What operating system and version
   - What version of glib and gdk-pixbuf libraries

 And anything else you think is relevant.

* How to reproduce the bug.

* If the bug was crash, the exact text that was printed out when the
  crash occured.

* Further information such as stack traces may be useful, but is not
  necessary.

Please check the bugzilla pages for the list of known bugs.

Patches
=======

Patches should also be submitted to bugs.gentoo.org. If the patch
fixes an existing bug, add the patch as an attachment to that bug
report.

Otherwise, enter a new bug report that describes the problem the patch
fixes, and attach it to that bug report.

Patches should be created with the git format-patch command.


The Gentoo Gnome team.
