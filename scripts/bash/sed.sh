#¡/bin/bash

myfile="file.txt"
new_string="line number 1\nline number 2\nline number 3"

if [ -f "$myfile" ]; then
    sed  -i.bak 's/string_to_replace/'"$new_string"'/g'  "$myfile"
    cat "$myfile"	
else
    echo " " > "$myfile"
    echo "file does not exist"
fi


