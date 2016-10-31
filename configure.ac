AC_PREREQ([2.69])
AC_INIT([gtk-update-icon-cache], [3.22.0],
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

AC_CONFIG_FILES([
    Makefile
    po/Makefile.in
    gtk/Makefile
])

AC_OUTPUT
