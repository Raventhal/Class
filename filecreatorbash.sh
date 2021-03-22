echo "This program creates 25 empty files."
read -n 1 -s -r -p "Press any key to continue." | pr -dT
clear 
#user input
read -p "Enter filename of: " name
#file check to see if file with user input exist. if not create the first one.
if [ -f "$name[0-9]".txt ]; then
    :
else
    touch $name"1".txt
fi
#calls directory with ls. grep finds files with name. egrep seperates the number from the file. sort arranges numbers. tail out put one value to the variable.
bub=$(ls | grep "$name[0-9]"*.txt | egrep -o '[0-9]+' | sort -n | tail -1)
#condition for needed because if there no files one is creates so ine less is needed.
if [[ $bub == 1 ]] ; then
    nub=23
elif [[ $bub > 1 ]] ; then
    nub=24
fi
#have to add one file and 23 or 24 to get the right out.
cut=$((bub + 1))
adder=$((cut + nub))
#printing files being created.
echo "Files ""$name""$cut"".txt to ""$name""$adder"".txt have been created."
read -n 1 -s -r -p "Press any key to continue." | pr -dT
clear
#loop to create the 25 files. Alternative since bash does not accept variables for range.
i=$cut
while [[ $i -le $adder ]]
do
    touch $name"$i".txt
    ((i = i + 1))
done

