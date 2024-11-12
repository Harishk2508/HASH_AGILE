#!/bin/bash

# DEFINING A USER-DEFINED FUNCTION WITH ONE ARGUMENT AS LIST
secondlargest() {
  local arr=("$@")  # STORE ALL ELEMENTS PASSED AS ARGUMENT INTO AN ARRAY

  # CHECKS WHETHER THE LIST IS EMPTY OR HAVING LESS THAN TWO ELEMENTS
  if [ "${#arr[@]}" -lt 2 ]; then  
    echo "List needs elements"
    return
  fi

  max1=${arr[0]}  # INITIALISING THE LARGEST MAXIMUM ELEMENT AS THE FIRST ELEMENT OF LIST
  
  # ITERATING THROUGH ALL THE ELEMENTS IN THE LIST
  for num in "${arr[@]}"; do  
    # USING IF CONDITION FINDS THE LARGEST ELEMENT OF THE LIST
    if [ "$num" -gt "$max1" ]; then  
      max1=$num
    fi
  done

  seclgt=-999999  # INITIALISING THE SECOND LARGEST ELEMENT WITH A VERY LOW VALUE TO SIMULATE NEGATIVE INFINITY
  
  # AGAIN ITERATIONS IS PERFORMED THROUGHOUT THE LIST
  for num in "${arr[@]}"; do  
    # USING IF CONDITION THE SECOND LARGEST ELEMENT IS FOUND
    if [ "$num" -ne "$max1" ] && [ "$num" -gt "$seclgt" ]; then  
      seclgt=$num
    fi
  done

  # CHECKS WHETHER THE INITIALISED VALUE IS UPDATED OR NOT
  if [ "$seclgt" -eq -999999 ]; then  
    echo "There is no second element in the list and all the elements are equal"
  else
    # RETURNS THE SECOND LARGEST ELEMENT IN THE LIST
    echo "The second largest element in the list is $seclgt"  
  fi
}

# MAIN EXECUTION OF THE CODE
testcase=(25 7 6 21 18 28 2 31)  # SAMPLE TESTCASE 1
secondlargest "${testcase[@]}"  # PRINTING THE OUTPUT

