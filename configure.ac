AC_PREREQ([2.69])
AC_INIT([gtk-update-icon-cache], [3.22.5],
        [http://bugzilla.gnome.org/enter_bug.cgi?product=gtk%2B])

AC_CONFIG_HEADERS([config.h])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_AUX_DIR([build-aux])

AM_INIT_AUTOMAKE([1.13 -Wall foreign no-dist-gzip dist-xz])
AM_MAINTAINER_MODE([enable])
AM_SILENT_RULES([yes])

m4_define([glib_required_version], [2.49.4])
m4_define([gdk_pixbuf_required_version], [2.30.0])

AC_CANONICAL_HOST

AC_MSG_CHECKING([for native Win32])
case "$host" in
    *-*-mingw*) os_win32=yes ;;
    *) os_win32=no ;;
esac
AC_MSG_RESULT([$os_win32])
AM_CONDITIONAL(OS_WIN32, test "$os_win32" = "yes")

# Initialize libtool
LT_PREREQ([2.2.6])
LT_INIT([disable-static win32-dll])
# Create libtool early, because it's used in configure
LT_OUTPUT

AM_GNU_GETTEXT([external])
AM_GNU_GETTEXT_VERSION([0.19.7])

GETTEXT_PACKAGE=gtk-update-icon-cache
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE",
                   [The prefix for our gettext translation domains.])

PKG_PROG_PKG_CONFIG

PKG_CHECK_MODULES(UPDATE_ICON_CACHE, [
    glib-2.0 >= glib_required_version
    gdk-pixbuf-2.0 >= gdk_pixbuf_required_version
])

AC_ARG_ENABLE([man],
              [AS_HELP_STRING([--enable-man],
                              [generate man pages @<:@default=auto@:>@])],
                              [],
                              [enable_man=auto])

AS_IF([test "$enable_man" != "no"],
      [AC_PATH_PROG([XSLTPROC], [xsltproc])
       AS_IF([test -z "$XSLTPROC" -a "$enable_man" = "yes"],
             AC_MSG_ERROR([xsltproc is required for --enable-man])
             enable_man=no)
      ])

AS_IF([test "$enable_man" != "no"],
      [JH_CHECK_XML_CATALOG([-//OASIS//DTD DocBook XML V4.3//EN],
                            [DocBook XML DTD V4.3], [have_docbook_dtd=yes], [have_docbook_dtd=no])
       AS_IF([test "$have_docbook_dtd" = "no" -a "$enable_man" = "yes"],
             AC_MSG_ERROR([Docbook DTD is required for --enable-man])
             enable_man=no)
      ])

AS_IF([test "$enable_man" != "no"],
      [JH_CHECK_XML_CATALOG([http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl],
                            [DocBook XSL Stylesheets], [have_docbook_style=yes], [have_docbook_style=no])
       AS_IF([test "${have_docbook_style}" = "no" -a "$enable_man" = "yes"],
             AC_MSG_ERROR([Docbook XSL Stylesheets are required for --enable-man])
             enable_man=no)
      ])

AM_CONDITIONAL(ENABLE_MAN, test "$enable_man" != "no")

AC_MSG_CHECKING([whether to generate man pages])
AS_IF([test "$enable_man" != "no"],
      [AC_MSG_RESULT([yes])],
      [AC_MSG_RESULT([no])])

AC_CONFIG_FILES([
    Makefile
    docs/Makefile
    po/Makefile.in
    gtk/Makefile
])

AC_OUTPUT
