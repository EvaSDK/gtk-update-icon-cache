AM_CPPFLAGS =							\
	-I$(top_builddir)					\
	-DGTK_LOCALEDIR=\"$(localedir)\"	\
	$(UPDATE_ICON_CACHE_CFLAGS)

bin_PROGRAMS = gtk-update-icon-cache

if OS_WIN32

# Workaround for UAC silliness: programs with "update" in their name
# are believed to be installers and require elevated privileges to be
# used... Embed a manifest file into executable to tell Windows that
# gtk-update-icon-cache.exe doesn't require any special privileges.

GTK_UPDATE_ICON_CACHE_MANIFEST = gtk-update-icon-cache.exe.manifest
GTK_UPDATE_ICON_CACHE_RC = gtk-update-icon-cache.rc
GTK_UPDATE_ICON_CACHE_MANIFEST_OBJECT = gtk-update-icon-cache_manifest.o

$(GTK_UPDATE_ICON_CACHE_MANIFEST):
	(echo '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' ; \
	 echo '<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">' ; \
	 echo '  <assemblyIdentity version="1.0.0.0"' ; \
	 echo '     processorArchitecture="'$(EXE_MANIFEST_ARCHITECTURE)'"' ; \
	 echo '     name="gtk-update-icon-cache.exe"' ; \
	 echo '     type="win32"/>' ; \
	 echo '  <!-- Identify the application security requirements. -->' ; \
	 echo '  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">' ; \
	 echo '    <security>' ; \
	 echo '      <requestedPrivileges>' ; \
	 echo '        <requestedExecutionLevel' ; \
	 echo '          level="asInvoker"' ; \
	 echo '          uiAccess="false"/>' ; \
	 echo '        </requestedPrivileges>' ; \
	 echo '       </security>' ; \
	 echo '  </trustInfo>' ; \
	 echo '</assembly>' ) >$@

$(GTK_UPDATE_ICON_CACHE_RC):
	(echo 'CREATEPROCESS_MANIFEST_RESOURCE_ID RT_MANIFEST '$(GTK_UPDATE_ICON_CACHE_MANIFEST)) >$@

$(GTK_UPDATE_ICON_CACHE_MANIFEST_OBJECT): $(GTK_UPDATE_ICON_CACHE_RC) $(GTK_UPDATE_ICON_CACHE_MANIFEST)
	$(WINDRES) --input $< --output $@ --output-format=coff

endif

gtk_update_icon_cache_LDADD = $(UPDATE_ICON_CACHE_LIBS) $(GTK_UPDATE_ICON_CACHE_MANIFEST_OBJECT)
gtk_update_icon_cache_DEPENDENCIES = $(GTK_UPDATE_ICON_CACHE_MANIFEST_OBJECT)
gtk_update_icon_cache_SOURCES = updateiconcache.c

EXTRA_DIST = gtkiconcachevalidator.c gtkiconcachevalidator.h
