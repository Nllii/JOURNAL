#!/bin/bash
#1. Create ProgressBar function
#//stackoverflow.com/questions/238073/how-to-add-a-progress-bar-to-a-shell-script
rightnow_date=$(date +"%m/%d/%Y "at" %H-%M")


progress-bar() {
  local duration=${1}

    already_done() { for ((done=0; done<$elapsed; done++)); do printf "▇"; done }
    remaining() { for ((remain=$elapsed; remain<$duration; remain++)); do printf " "; done }
    percentage() { printf "| %s%%" $(( (($elapsed)*100)/($duration)*100/100 )); }
    clean_line() { printf "\r"; }

  for (( elapsed=1; elapsed<=$duration; elapsed++ )); do
      already_done; remaining; percentage
      sleep 1
      clean_line
  done
  clean_line
}



progress-bar 1
if [[ -f "push.txt" ]]
then
    echo "PUSH.TXT ALREADY CREATED"
else
    echo "CREATING a push.txt"
    touch push.txt
    echo "DONE"
fi

checking_for_files() {
echo "IM LOOKING FOR: "
checking_for_files=`ls ./*.md ./*.txt`
for eachfile in $checking_for_files
do
   echo $eachfile "FOUND IT"
   echo "DONE"
   progress-bar 2

   done

}
progress-bar 3



git_push() {
echo "summary of today code:"
vim README.md
echo "# $rightnow_date" >> README.md
echo "debug" >> push.txt
progress-bar 4
if [[ -f "push.txt" ]]
then
    git add .
    git commit -am "okay" >> push.txt
    git push
    echo "UPLOADED FOR SAVE KEEPING!"
fi
}

checking_for_files
git_push
