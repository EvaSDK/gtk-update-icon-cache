all:
	if [ -n "${VERSION}" ]; then \
		current_dir="$$(pwd)" ; cd ../gtk+ ; git checkout ${VERSION} ; git clean -fxd . ; \
		cd "$${current_dir}"; sed -e "2 s/, \[.*/, [${VERSION}],/" -i configure.ac ; \
	fi
	cp ../gtk+/docs/reference/gtk/gtk-update-icon-cache.xml ./docs/
	cp ../gtk+/gtk/updateiconcache.c ./gtk/
	cp ../gtk+/gtk/gtkiconcachevalidator.* ./gtk/
	for po in ../gtk+/po/*.po ; do \
		python utils/extract-po.py $${po} ./po/$$(basename $${po}); \
	done

