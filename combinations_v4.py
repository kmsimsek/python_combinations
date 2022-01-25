def combinations(input_list,min_item=[],max_item=[],must_all=[],none_any=[],must_any=[],none_together=[],sum=[],multiply=[]):
    combination_list=[]
    if none_any!=[]:
        for item in none_any:
            count=int(input_list.count(item))
            for step in range(0,count):
                input_list.remove(item)
    if sum!=[] or multiply!=[]:
        for item in input_list:
            if isinstance(item,int)==False and isinstance(item,float)==False:
                input_list.remove(item)
    def combination_creator(list):
        check_failure=0
        check_stop_failure=0
        if min_item!=[]:
            if len(list)<min_item[0]:
                check_failure+=1
                check_stop_failure+=1
        if max_item!=[]:
            if len(list)>max_item[0]:
                check_failure+=1
        if must_all!=[]:
            must_all_count=len(must_all)
            for item in must_all:
                if list.count(item)>0:
                    must_all_count-=1
            if must_all_count!=0:
                check_failure+=1
                check_stop_failure+=1
        if must_any!=[]:
            counter=0
            for item in must_any:
                counter+=list.count(item)
            if counter==0:
                check_failure+=1
                check_stop_failure+=1
        if none_together!=[]:
            counter=0
            for item in none_together:
                if list.count(item)>0:
                    counter+=1
            if counter==len(none_together):
                check_failure+=1
        if sum!=[]:
            sum_check = 0
            positives = 0
            negatives = 0
            for item in list:
                if item > 0:
                    positives += item
                if item < 0:
                    negatives += item
            if len(sum)==1:
                if positives<sum[0]:
                    check_failure+=1
                    check_stop_failure+=1
                if negatives>sum[0]:
                    check_failure+=1
                    check_stop_failure+=1
                else:
                    for item in list:
                        sum_check+=item
                    if sum_check!=sum[0]:
                        check_failure+=1
            if len(sum)==2:
                if sum[0]=="=":
                    if positives < sum[1]:
                        check_failure += 1
                        check_stop_failure += 1
                    if negatives > sum[1]:
                        check_failure += 1
                        check_stop_failure += 1
                    else:
                        for item in list:
                            sum_check+=item
                        if sum_check!=sum[1]:
                            check_failure+=1
                if sum[0]==">=":
                    if positives < sum[1]:
                        check_failure += 1
                        check_stop_failure += 1
                    else:
                        for item in list:
                            sum_check+=item
                        if sum_check<sum[1]:
                            check_failure+=1
                if sum[0]==">":
                    if positives<sum[1]:
                        check_failure+=1
                        check_stop_failure+=1
                    else:
                        for item in list:
                            sum_check+=item
                        if sum_check<=sum[1]:
                            check_failure+=1
                if sum[0]=="<=":
                    if negatives-positives>sum[1]:
                        check_failure+=1
                        check_stop_failure+=1
                    else:
                        for item in list:
                            sum_check+=item
                        if sum_check>sum[1]:
                            check_failure+=1
                if sum[0]=="<":
                    if negatives-positives>=sum[1]:
                        check_failure+=1
                        check_stop_failure+=1
                    else:
                        for item in list:
                            sum_check+=item
                        if sum_check>=sum[1]:
                            check_failure+=1
        if multiply!=[]:
            multiply_check=1
            if len(multiply)==1:
                for item in list:
                    multiply_check*=item
                if multiply_check!=multiply[0]:
                    check_failure+=1
            if len(multiply)==2:
                if multiply[0]=="=":
                    for item in list:
                        multiply_check*=item
                    if multiply_check!=multiply[1]:
                        check_failure+=1
                if multiply[0]==">=":
                    for item in list:
                        multiply_check*=item
                    if multiply_check < multiply[1]:
                        check_failure+=1
                if multiply[0]==">":
                    for item in list:
                        multiply_check*=item
                    if multiply_check<=multiply[1]:
                        check_failure+=1
                if multiply[0]=="<=":
                    for item in list:
                        multiply_check*=item
                    if multiply_check>multiply[1]:
                        check_failure*=1
                if multiply[0]=="<":
                    for item in list:
                        multiply_check*=item
                    if multiply_check>=multiply[1]:
                        check_failure+=1
        if check_failure==0:
            combination_list.append(list)
        if check_stop_failure==0 and len(list)>1:
            for order in range(0,len(list)):
                temporary_remove =list[order]
                list.pop(order)
                new_combination=list.copy()
                list.insert(order,temporary_remove)
                if not new_combination in combination_list:
                    combination_creator(new_combination)
    if len(sum) == 4 or len(multiply) == 4:
        if len(sum) == 4 and len(multiply)!= 4:
            combination_candidate_list1=combinations(input_list, min_item=min_item, max_item=max_item, must_all=must_all, none_any=none_any,must_any=must_any, none_together=none_together, sum=sum[0:2], multiply=multiply)
            combination_candidate_list2=combinations(input_list, min_item=min_item, max_item=max_item, must_all=must_all, none_any=none_any, must_any=must_any,none_together=none_together, sum=sum[2:4], multiply=multiply)
            if len(combination_candidate_list1)>0 and len(combination_candidate_list2)>0:
                if len(combination_candidate_list1)<=len(combination_candidate_list2):
                    main_list=combination_candidate_list1
                    other_list=combination_candidate_list2
                else:
                    main_list=combination_candidate_list2
                    other_list=combination_candidate_list1
                combination_list=[]
                for item in main_list:
                    if item in other_list:
                        combination_list.append(item)
            else:
                return []
        elif len(sum)!=4 and len(multiply)==4:
            combination_candidate_list1=combinations(input_list, min_item=min_item, max_item=max_item, must_all=must_all, none_any=none_any,must_any=must_any, none_together=none_together, sum=sum, multiply=multiply[0:2])
            combination_candidate_list2=combinations(input_list, min_item=min_item, max_item=max_item, must_all=must_all, none_any=none_any, must_any=must_any,none_together=none_together, sum=sum, multiply=multiply[2:4])
            if len(combination_candidate_list1)>0 and len(combination_candidate_list2)>0:
                if len(combination_candidate_list1)<=len(combination_candidate_list2):
                    main_list=combination_candidate_list1
                    other_list=combination_candidate_list2
                else:
                    main_list=combination_candidate_list2
                    other_list=combination_candidate_list1
                combination_list=[]
                for item in main_list:
                    if other_list.count(item)>0:
                        combination_list.append(item)
            else:
                return []
        else:
            combination_candidate_list1=combinations(input_list, min_item=min_item, max_item=max_item, must_all=must_all, none_any=none_any,must_any=must_any, none_together=none_together, sum=sum[0:2], multiply=multiply[0:2])
            combination_candidate_list2=combinations(input_list,min_item=min_item, max_item=max_item, must_all=must_all, none_any=none_any, must_any=must_any,none_together=none_together, sum=sum[2:4], multiply=multiply[2:4])
            if len(combination_candidate_list1)>0 and len(combination_candidate_list2)>0:
                if len(combination_candidate_list1)<=len(combination_candidate_list2):
                    main_list=combination_candidate_list1
                    other_list=combination_candidate_list2
                else:
                    main_list=combination_candidate_list2
                    other_list=combination_candidate_list1
                combination_list=[]
                for item in main_list:
                    if other_list.count(item)>0:
                        combination_list.append(item)
            else:
                return []
    else:
        combination_creator(input_list)

    return combination_list